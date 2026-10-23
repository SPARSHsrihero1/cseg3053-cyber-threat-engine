#include "unit6_flow_string_crt.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 1. Ford-Fulkerson / Edmonds-Karp Maximum Flow & Min-Cut */
static int bfs_augmenting_path(int n, int r_cap[MAX_HOSTS][MAX_HOSTS], int s, int t, int *parent, MetricsTracker *m) {
    int visited[MAX_HOSTS] = {0};
    int queue[MAX_HOSTS];
    int head = 0, tail = 0;

    queue[tail++] = s;
    visited[s] = 1;
    parent[s] = -1;

    while (head < tail) {
        int u = queue[head++];

        for (int v = 0; v < n; v++) {
            if (!visited[v] && r_cap[u][v] > 0) {
                if (m) m->comparisons++;
                queue[tail++] = v;
                parent[v] = u;
                visited[v] = 1;
                if (v == t) return 1;
            }
        }
    }
    return 0;
}

FlowResult ford_fulkerson_max_flow(const AttackGraph *graph, int source, int sink, MetricsTracker *m) {
    FlowResult res;
    res.max_flow = 0;
    res.num_mincut_edges = 0;
    if (!graph || source < 0 || sink < 0 || source >= graph->num_hosts || sink >= graph->num_hosts) return res;

    int n = graph->num_hosts;
    int r_cap[MAX_HOSTS][MAX_HOSTS];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            r_cap[i][j] = graph->adj_capacity[i][j];
        }
    }

    int parent[MAX_HOSTS];

    /* Augment flow using shortest paths (Edmonds-Karp) */
    while (bfs_augmenting_path(n, r_cap, source, sink, parent, m)) {
        int path_flow = INF_COST;

        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            if (m) m->comparisons++;
            if (r_cap[u][v] < path_flow) {
                path_flow = r_cap[u][v];
            }
        }

        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            r_cap[u][v] -= path_flow;
            r_cap[v][u] += path_flow;
            if (m) {
                m->graph_relaxations++;
                m->swaps_or_writes += 2;
            }
        }

        res.max_flow += path_flow;
    }

    /* Extract Min-Cut edges: BFS in residual graph from source */
    int visited[MAX_HOSTS] = {0};
    int queue[MAX_HOSTS];
    int head = 0, tail = 0;

    queue[tail++] = source;
    visited[source] = 1;

    while (head < tail) {
        int u = queue[head++];
        for (int v = 0; v < n; v++) {
            if (!visited[v] && r_cap[u][v] > 0) {
                visited[v] = 1;
                queue[tail++] = v;
            }
        }
    }

    /* Cut edges are original edges from visited to unvisited */
    for (int u = 0; u < n; u++) {
        if (visited[u]) {
            for (int v = 0; v < n; v++) {
                if (!visited[v] && graph->adj_capacity[u][v] > 0) {
                    if (res.num_mincut_edges < MAX_HOSTS * MAX_HOSTS) {
                        res.mincut_edges[res.num_mincut_edges++] = (NetworkEdge){
                            u, v, graph->adj_weight[u][v], graph->adj_capacity[u][v]
                        };
                    }
                }
            }
        }
    }

    return res;
}

/* 2. Maximum Bipartite Matching */
static int bpm_dfs(int u, int num_analysts, const int adj[MAX_HOSTS][MAX_HOSTS], int *visited, int *match, MetricsTracker *m) {
    if (m) m->recursive_calls++;

    for (int v = 0; v < num_analysts; v++) {
        if (adj[u][v] && !visited[v]) {
            visited[v] = 1;
            if (m) m->comparisons++;

            if (match[v] < 0 || bpm_dfs(match[v], num_analysts, adj, visited, match, m)) {
                match[v] = u;
                if (m) m->swaps_or_writes++;
                return 1;
            }
        }
    }
    return 0;
}

BipartiteMatchingResult max_bipartite_matching_soc(int num_incidents, int num_analysts, const int adj[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m) {
    BipartiteMatchingResult res;
    res.max_matches = 0;
    for (int i = 0; i < MAX_HOSTS; i++) res.incident_assigned_to[i] = -1;
    if (num_incidents <= 0 || num_analysts <= 0 || !adj) return res;

    int match[MAX_HOSTS];
    for (int i = 0; i < MAX_HOSTS; i++) match[i] = -1;

    for (int u = 0; u < num_incidents; u++) {
        int visited[MAX_HOSTS] = {0};
        if (bpm_dfs(u, num_analysts, adj, visited, match, m)) {
            res.max_matches++;
        }
    }

    for (int v = 0; v < num_analysts; v++) {
        if (match[v] >= 0) {
            res.incident_assigned_to[match[v]] = v;
        }
    }

    return res;
}

/* 3. Chinese Remainder Theorem (CRT) Telemetry Reconstruction */
int64_t extended_gcd(int64_t a, int64_t b, int64_t *x, int64_t *y) {
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }
    int64_t x1, y1;
    int64_t gcd = extended_gcd(b, a % b, &x1, &y1);
    *x = y1;
    *y = x1 - (a / b) * y1;
    return gcd;
}

int64_t mod_inverse(int64_t a, int64_t m) {
    int64_t x, y;
    int64_t g = extended_gcd(a, m, &x, &y);
    if (g != 1) return -1;
    return (x % m + m) % m;
}

CRTResult crt_reconstruct_telemetry(int num_sensors, const int64_t *remainders, const int64_t *moduli, MetricsTracker *m) {
    CRTResult res;
    res.reconstructed_counter = 0;
    res.total_modulus = 1;
    res.success = 0;
    if (!remainders || !moduli || num_sensors <= 0) return res;

    for (int i = 0; i < num_sensors; i++) {
        res.total_modulus *= moduli[i];
    }

    __int128 total = 0;
    __int128 M = res.total_modulus;

    for (int i = 0; i < num_sensors; i++) {
        int64_t mi = moduli[i];
        int64_t Mi = (int64_t)(M / mi);
        int64_t yi = mod_inverse(Mi % mi, mi);

        if (m) m->comparisons++;
        if (yi == -1) {
            res.success = 0;
            return res;
        }

        __int128 term = ((__int128)remainders[i] * (__int128)Mi * (__int128)yi) % M;
        total = (total + term) % M;
        if (m) m->swaps_or_writes++;
    }

    res.reconstructed_counter = (int64_t)((total % M + M) % M);
    res.success = 1;
    return res;
}

/* 4. String-Matching Engines */

/* Naive String Matching */
StringMatchResult strmatch_naive(const char *text, const char *pattern, MetricsTracker *m) {
    StringMatchResult res;
    res.match_count = 0;
    res.first_match_index = -1;
    res.spurious_hits = 0;
    if (!text || !pattern) return res;

    int n = (int)strlen(text);
    int p = (int)strlen(pattern);
    if (p == 0 || n < p) return res;

    for (int i = 0; i <= n - p; i++) {
        int match = 1;
        for (int j = 0; j < p; j++) {
            if (m) m->comparisons++;
            if (text[i + j] != pattern[j]) {
                match = 0;
                break;
            }
        }
        if (match) {
            if (res.first_match_index == -1) res.first_match_index = i;
            res.match_count++;
            if (m) m->swaps_or_writes++;
        }
    }
    return res;
}

/* Rabin-Karp String Matching */
StringMatchResult strmatch_rabin_karp(const char *text, const char *pattern, MetricsTracker *m) {
    StringMatchResult res;
    res.match_count = 0;
    res.first_match_index = -1;
    res.spurious_hits = 0;
    if (!text || !pattern) return res;

    int n = (int)strlen(text);
    int p = (int)strlen(pattern);
    if (p == 0 || n < p) return res;

    const uint64_t d = 256;
    const uint64_t q = 1000000007ULL;

    uint64_t h = 1;
    for (int i = 0; i < p - 1; i++) {
        h = (h * d) % q;
    }

    uint64_t p_hash = 0;
    uint64_t t_hash = 0;

    for (int i = 0; i < p; i++) {
        p_hash = (d * p_hash + (unsigned char)pattern[i]) % q;
        t_hash = (d * t_hash + (unsigned char)text[i]) % q;
    }

    for (int i = 0; i <= n - p; i++) {
        if (m) m->comparisons++;
        if (p_hash == t_hash) {
            /* Hash match - verify character sequence */
            int full_match = 1;
            for (int j = 0; j < p; j++) {
                if (m) m->comparisons++;
                if (text[i + j] != pattern[j]) {
                    full_match = 0;
                    break;
                }
            }
            if (full_match) {
                if (res.first_match_index == -1) res.first_match_index = i;
                res.match_count++;
                if (m) m->swaps_or_writes++;
            } else {
                res.spurious_hits++;
            }
        }

        if (i < n - p) {
            /* Roll hash */
            int64_t next_t = (int64_t)d * ((int64_t)t_hash - (int64_t)((unsigned char)text[i] * h)) + (unsigned char)text[i + p];
            next_t = next_t % (int64_t)q;
            if (next_t < 0) next_t += q;
            t_hash = (uint64_t)next_t;
            if (m) m->swaps_or_writes++;
        }
    }

    return res;
}

/* Finite Automaton String Matching */
static int get_next_state(const char *pat, int m_len, int state, int x) {
    if (state < m_len && x == (unsigned char)pat[state]) {
        return state + 1;
    }
    for (int next = state; next > 0; next--) {
        if ((unsigned char)pat[next - 1] == x) {
            int match = 1;
            for (int i = 0; i < next - 1; i++) {
                if (pat[i] != pat[state - next + 1 + i]) {
                    match = 0;
                    break;
                }
            }
            if (match) return next;
        }
    }
    return 0;
}

StringMatchResult strmatch_finite_automaton(const char *text, const char *pattern, MetricsTracker *m) {
    StringMatchResult res;
    res.match_count = 0;
    res.first_match_index = -1;
    res.spurious_hits = 0;
    if (!text || !pattern) return res;

    int n = (int)strlen(text);
    int p = (int)strlen(pattern);
    if (p == 0 || n < p || p >= MAX_PATTERN_LEN) return res;

    /* Build transition table: delta[state][char] */
    int delta[MAX_PATTERN_LEN + 1][256];
    for (int state = 0; state <= p; state++) {
        for (int c = 0; c < 256; c++) {
            delta[state][c] = get_next_state(pattern, p, state, c);
            if (m) m->swaps_or_writes++;
        }
    }

    int state = 0;
    for (int i = 0; i < n; i++) {
        state = delta[state][(unsigned char)text[i]];
        if (m) {
            m->comparisons++;
            m->swaps_or_writes++;
        }
        if (state == p) {
            int match_start = i - p + 1;
            if (res.first_match_index == -1) res.first_match_index = match_start;
            res.match_count++;
        }
    }

    return res;
}

/* Knuth-Morris-Pratt (KMP) String Matching */
static void compute_lps_array(const char *pat, int p, int *lps, MetricsTracker *m) {
    int len = 0;
    lps[0] = 0;
    int i = 1;

    while (i < p) {
        if (m) m->comparisons++;
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
            if (m) m->swaps_or_writes++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
                if (m) m->swaps_or_writes++;
            }
        }
    }
}

StringMatchResult strmatch_kmp(const char *text, const char *pattern, MetricsTracker *m) {
    StringMatchResult res;
    res.match_count = 0;
    res.first_match_index = -1;
    res.spurious_hits = 0;
    if (!text || !pattern) return res;

    int n = (int)strlen(text);
    int p = (int)strlen(pattern);
    if (p == 0 || n < p) return res;

    int *lps = (int *)tracked_malloc(p * sizeof(int), m);
    if (!lps) return res;

    compute_lps_array(pattern, p, lps, m);

    int i = 0; /* Index for text */
    int j = 0; /* Index for pattern */

    while (i < n) {
        if (m) m->comparisons++;
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }

        if (j == p) {
            int match_start = i - j;
            if (res.first_match_index == -1) res.first_match_index = match_start;
            res.match_count++;
            j = lps[j - 1];
            if (m) m->swaps_or_writes++;
        } else if (i < n && pattern[j] != text[i]) {
            if (m) m->comparisons++;
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    free(lps);
    return res;
}
