#include "data_generator.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint32_t prng_next(uint32_t *state) {
    *state = (*state * 1664525u + 1013904223u);
    return *state;
}

static const char *sample_payloads[] = {
    "GET /index.php?id=1 UNION SELECT null, username, password FROM users--",
    "POST /api/v1/auth/login user=admin' OR 1=1-- HTTP/1.1",
    "Failed SSH login for root from 192.168.1.50 port 44222 ssh2",
    "System event: suspicious process powershell.exe -enc JABzACAAPQAgAE4AZQB3... launched",
    "Kernel audit: execution of /bin/sh by user apache from /tmp/exploit.bin",
    "DNS tunnel detection: query d34db33f.data-exfil.c2-network.net TXT",
    "Firewall drop: outbound TCP SYN to port 4444 on IP 185.220.101.5",
    "SMB brute force attempt on ADMIN$ share with Kerberos ticket replay",
    "Ransomware canary file modified in C:\\Corporate\\Shares\\Accounting\\readme.txt",
    "Lateral movement attempt via PsExec on 10.0.4.12 using stolen NTLM hash"
};

void generate_event_logs(EventLog *dest, size_t count, uint32_t seed) {
    if (!dest || count == 0) return;
    uint32_t state = (seed != 0) ? seed : 987654321;
    uint64_t base_time = 1710000000ULL;

    size_t num_samples = sizeof(sample_payloads) / sizeof(sample_payloads[0]);

    for (size_t i = 0; i < count; i++) {
        dest[i].log_id = (uint32_t)(i + 1);
        /* Pseudo-random time progression */
        base_time += (prng_next(&state) % 15) + 1;
        dest[i].timestamp = base_time;

        uint32_t s3 = (prng_next(&state) % 254) + 1;
        uint32_t s4 = (prng_next(&state) % 254) + 1;
        uint32_t d3 = (prng_next(&state) % 254) + 1;
        uint32_t d4 = (prng_next(&state) % 254) + 1;

        snprintf(dest[i].src_ip, sizeof(dest[i].src_ip), "192.168.%u.%u", s3, s4);
        snprintf(dest[i].dst_ip, sizeof(dest[i].dst_ip), "10.0.%u.%u", d3, d4);

        dest[i].severity = (int)((prng_next(&state) % 10) + 1);

        /* Default background anomaly fluctuation: -20 to +15 */
        dest[i].anomaly_delta = (int)((prng_next(&state) % 36) - 20);

        /* Inject concentrated attack bursts in the middle of log sequence */
        if (count >= 10 && i >= count / 3 && i <= (count / 3 + count / 5)) {
            dest[i].anomaly_delta = (int)((prng_next(&state) % 40) + 15); /* +15 to +54 */
            dest[i].severity = 8 + (int)(prng_next(&state) % 3);
        }

        dest[i].event_code = (char)('A' + (prng_next(&state) % 26));

        size_t sample_idx = prng_next(&state) % num_samples;
        snprintf(dest[i].payload, sizeof(dest[i].payload), "%s", sample_payloads[sample_idx]);
    }
}

void generate_adversarial_sorted_logs(EventLog *dest, size_t count) {
    generate_event_logs(dest, count, 42);
    /* Ensure strictly increasing timestamps */
    for (size_t i = 1; i < count; i++) {
        if (dest[i].timestamp <= dest[i - 1].timestamp) {
            dest[i].timestamp = dest[i - 1].timestamp + 10;
        }
    }
}

void generate_adversarial_reversed_logs(EventLog *dest, size_t count) {
    generate_event_logs(dest, count, 42);
    /* Reverse array in place */
    for (size_t i = 0; i < count / 2; i++) {
        EventLog tmp = dest[i];
        dest[i] = dest[count - 1 - i];
        dest[count - 1 - i] = tmp;
    }
}

void generate_adversarial_identical_logs(EventLog *dest, size_t count) {
    generate_event_logs(dest, count, 42);
    uint64_t fixed_time = 1710005000ULL;
    for (size_t i = 0; i < count; i++) {
        dest[i].timestamp = fixed_time;
        dest[i].severity = 5;
    }
}

void generate_adversarial_string(char *dest, size_t len, const char *pattern) {
    if (!dest || len == 0) return;
    size_t pat_len = pattern ? strlen(pattern) : 0;
    if (pat_len == 0 || pat_len >= len) {
        memset(dest, 'A', len - 1);
        dest[len - 1] = '\0';
        return;
    }

    /* Fill with 'A' except pattern or near-match at the very end */
    for (size_t i = 0; i < len - 1; i++) {
        dest[i] = 'A';
    }
    /* Embed near-miss or target at end */
    size_t start = len - 1 - pat_len;
    for (size_t i = 0; i < pat_len; i++) {
        dest[start + i] = pattern[i];
    }
    dest[len - 1] = '\0';
}

static const struct {
    const char *pattern;
    int risk;
    double weight;
} default_sigs[] = {
    { "UNION SELECT", 95, 0.22 },
    { "OR 1=1", 85, 0.18 },
    { "powershell.exe", 90, 0.15 },
    { "/bin/sh", 88, 0.12 },
    { "ADMIN$", 70, 0.10 },
    { "c2-network", 98, 0.08 },
    { "readme.txt", 92, 0.06 },
    { "4444", 75, 0.05 },
    { "audit", 40, 0.02 },
    { "passwd", 80, 0.02 }
};

void generate_threat_signatures(ThreatSignature *dest, size_t count) {
    if (!dest || count == 0) return;
    size_t num_defaults = sizeof(default_sigs) / sizeof(default_sigs[0]);
    double total_prob = 0.0;

    for (size_t i = 0; i < count; i++) {
        dest[i].sig_id = (int)(i + 1);
        size_t idx = i % num_defaults;
        snprintf(dest[i].pattern, sizeof(dest[i].pattern), "%s", default_sigs[idx].pattern);
        dest[i].risk_score = default_sigs[idx].risk;
        dest[i].hit_probability = default_sigs[idx].weight;
        total_prob += dest[i].hit_probability;
    }

    /* Normalize hit probabilities */
    if (total_prob > 0.0) {
        for (size_t i = 0; i < count; i++) {
            dest[i].hit_probability /= total_prob;
        }
    }
}

static const struct {
    const char *name;
    int cost;
    int value;
    int start;
    int end;
} default_actions[] = {
    { "Isolate Perimeter Subnet 10.0.1.0/24", 25, 80, 1, 4 },
    { "Null-Route C2 External IP Range", 10, 90, 2, 5 },
    { "Revoke Compromised Kerberos TGT", 15, 75, 3, 7 },
    { "Suspend Ingress Port 445 SMB", 30, 85, 4, 8 },
    { "Deploy Endpoint EDR Deep Scan", 40, 60, 5, 9 },
    { "Flush Active DNS Cache", 5, 40, 6, 10 },
    { "Snapshot Forensic Disk Memory", 50, 70, 7, 12 },
    { "Rotate Privileged Service Keys", 20, 65, 8, 11 },
    { "Quarantine Infection Jump-Box", 35, 95, 9, 13 },
    { "Sever Data Exfiltration Tunnel", 12, 88, 10, 14 },
    { "Re-image Infected Web Server", 60, 50, 11, 15 },
    { "Trigger Honeytoken Alarm", 8, 45, 12, 16 }
};

void generate_containment_actions(ContainmentAction *dest, size_t count) {
    if (!dest || count == 0) return;
    size_t num_defaults = sizeof(default_actions) / sizeof(default_actions[0]);

    for (size_t i = 0; i < count; i++) {
        dest[i].action_id = (int)(i + 1);
        size_t idx = i % num_defaults;
        snprintf(dest[i].name, sizeof(dest[i].name), "%.36s #%u", default_actions[idx].name, (unsigned)(i + 1));
        dest[i].disruption_cost = default_actions[idx].cost + (int)(i % 5);
        dest[i].risk_mitigated = default_actions[idx].value + (int)(i % 7);
        dest[i].start_time = default_actions[idx].start + (int)(i * 2);
        dest[i].end_time = dest[i].start_time + (default_actions[idx].end - default_actions[idx].start);
    }
}

void generate_attack_graph(AttackGraph *graph, int num_hosts, double edge_density, uint32_t seed) {
    if (!graph || num_hosts <= 0 || num_hosts > MAX_HOSTS) return;
    uint32_t state = (seed != 0) ? seed : 5551212;

    graph->num_hosts = num_hosts;
    graph->num_edges = 0;

    for (int i = 0; i < num_hosts; i++) {
        for (int j = 0; j < num_hosts; j++) {
            graph->adj_weight[i][j] = (i == j) ? 0 : INF_COST;
            graph->adj_capacity[i][j] = 0;
            graph->comm_matrix[i][j] = 0;
        }
    }

    for (int i = 0; i < num_hosts; i++) {
        for (int j = 0; j < num_hosts; j++) {
            if (i == j) continue;
            double r = (double)(prng_next(&state) % 1000) / 1000.0;
            if (r < edge_density) {
                int w = (int)((prng_next(&state) % 50) + 1);
                int cap = (int)((prng_next(&state) % 100) + 10);

                graph->adj_weight[i][j] = w;
                graph->adj_capacity[i][j] = cap;
                graph->comm_matrix[i][j] = 1;

                if (graph->num_edges < MAX_HOSTS * MAX_HOSTS) {
                    graph->edges[graph->num_edges].u = i;
                    graph->edges[graph->num_edges].v = j;
                    graph->edges[graph->num_edges].exploit_weight = w;
                    graph->edges[graph->num_edges].bandwidth_capacity = cap;
                    graph->num_edges++;
                }
            }
        }
    }
}

void generate_flow_network(AttackGraph *graph, int num_hosts, int source, int sink) {
    if (!graph || num_hosts <= 2 || num_hosts > MAX_HOSTS) return;
    (void)source;
    (void)sink;
    generate_attack_graph(graph, num_hosts, 0.45, 88812);

    /* Guarantee forward connectivity from source to intermediate layers, and intermediate to sink */
    for (int i = 1; i < num_hosts - 1; i++) {
        if (graph->adj_capacity[0][i] == 0) {
            int cap = 20 + (i * 7) % 50;
            graph->adj_capacity[0][i] = cap;
            graph->adj_weight[0][i] = 10;
            graph->edges[graph->num_edges++] = (NetworkEdge){0, i, 10, cap};
        }
        if (graph->adj_capacity[i][num_hosts - 1] == 0) {
            int cap = 15 + (i * 11) % 60;
            graph->adj_capacity[i][num_hosts - 1] = cap;
            graph->adj_weight[i][num_hosts - 1] = 10;
            graph->edges[graph->num_edges++] = (NetworkEdge){i, num_hosts - 1, 10, cap};
        }
    }
}

void generate_negative_weight_graph(AttackGraph *graph, int num_hosts, int insert_negative_cycle) {
    if (!graph || num_hosts <= 0 || num_hosts > MAX_HOSTS) return;
    generate_attack_graph(graph, num_hosts, 0.35, 99933);

    /* Inject negative weights modeling privilege escalation advantages */
    if (num_hosts >= 3) {
        graph->adj_weight[0][1] = 5;
        graph->adj_weight[1][2] = -3; /* Advantage: gained root tokens */

        if (insert_negative_cycle && num_hosts >= 4) {
            graph->adj_weight[2][3] = 2;
            graph->adj_weight[3][1] = -10; /* Cycle 1->2->3->1 sum = -3 + 2 - 10 = -11 */
        }
    }

    /* Re-sync edge list */
    graph->num_edges = 0;
    for (int i = 0; i < num_hosts; i++) {
        for (int j = 0; j < num_hosts; j++) {
            if (i != j && graph->adj_weight[i][j] < INF_COST) {
                graph->edges[graph->num_edges++] = (NetworkEdge){
                    i, j, graph->adj_weight[i][j], graph->adj_capacity[i][j]
                };
            }
        }
    }
}

void generate_c2_celebrity_graph(AttackGraph *graph, int num_hosts, int c2_node) {
    if (!graph || num_hosts <= 0 || num_hosts > MAX_HOSTS) return;
    if (c2_node < 0 || c2_node >= num_hosts) c2_node = 0;

    graph->num_hosts = num_hosts;
    uint32_t state = 442211;

    for (int i = 0; i < num_hosts; i++) {
        for (int j = 0; j < num_hosts; j++) {
            if (i == j) {
                graph->comm_matrix[i][j] = 0;
            } else {
                /* Random noise for ordinary communications */
                graph->comm_matrix[i][j] = (prng_next(&state) % 100 < 30) ? 1 : 0;
            }
        }
    }

    /* Enforce Celebrity (C2 Sinkhole) Properties:
       1. All other nodes beacon to c2_node (comm_matrix[i][c2_node] = 1 for all i != c2_node)
       2. c2_node initiates zero outbound connections (comm_matrix[c2_node][j] = 0 for all j) */
    for (int i = 0; i < num_hosts; i++) {
        if (i != c2_node) {
            graph->comm_matrix[i][c2_node] = 1;
        }
    }
    for (int j = 0; j < num_hosts; j++) {
        graph->comm_matrix[c2_node][j] = 0;
    }
}

void generate_soc_bipartite_graph(int num_incidents, int num_analysts, int adj[MAX_HOSTS][MAX_HOSTS], double match_prob, uint32_t seed) {
    if (!adj || num_incidents > MAX_HOSTS || num_analysts > MAX_HOSTS) return;
    uint32_t state = (seed != 0) ? seed : 77123;

    for (int i = 0; i < num_incidents; i++) {
        int has_match = 0;
        for (int j = 0; j < num_analysts; j++) {
            double r = (double)(prng_next(&state) % 1000) / 1000.0;
            if (r < match_prob) {
                adj[i][j] = 1;
                has_match = 1;
            } else {
                adj[i][j] = 0;
            }
        }
        /* Ensure each incident has at least one qualified analyst */
        if (!has_match && num_analysts > 0) {
            int pick = (int)(prng_next(&state) % (uint32_t)num_analysts);
            adj[i][pick] = 1;
        }
    }
}

void generate_crt_telemetry_system(int num_sensors, uint64_t true_counter, int64_t *remainders, int64_t *moduli) {
    if (!remainders || !moduli || num_sensors <= 0) return;
    /* Pairwise coprime prime moduli */
    static const int64_t primes[] = {
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
        151, 157, 163, 167, 173, 179, 181, 191, 193, 197
    };
    int max_primes = sizeof(primes) / sizeof(primes[0]);

    for (int i = 0; i < num_sensors; i++) {
        moduli[i] = (i < max_primes) ? primes[i] : (primes[max_primes - 1] + (i * 2 + 1));
        remainders[i] = (int64_t)(true_counter % (uint64_t)moduli[i]);
    }
}
