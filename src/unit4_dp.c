#include "unit4_dp.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 1. 0/1 Knapsack DP */
Knapsack01Result knapsack_01_dp(const ContainmentAction *actions, size_t n, int budget, MetricsTracker *m) {
    Knapsack01Result res;
    res.max_risk_mitigated = 0;
    res.total_cost = 0;
    res.num_selected = 0;
    if (!actions || n == 0 || budget <= 0) return res;

    int count = (int)((n > MAX_HOSTS) ? MAX_HOSTS : n);

    /* Allocate DP table: (count + 1) x (budget + 1) */
    size_t rows = (size_t)count + 1;
    size_t cols = (size_t)budget + 1;
    int **dp = (int **)tracked_malloc(rows * sizeof(int *), m);
    if (!dp) return res;

    for (size_t i = 0; i < rows; i++) {
        dp[i] = (int *)tracked_malloc(cols * sizeof(int), m);
        if (!dp[i]) {
            for (size_t k = 0; k < i; k++) free(dp[k]);
            free(dp);
            return res;
        }
        for (size_t w = 0; w < cols; w++) dp[i][w] = 0;
    }

    for (int i = 1; i <= count; i++) {
        int cost = actions[i - 1].disruption_cost;
        int val = actions[i - 1].risk_mitigated;

        for (int w = 0; w <= budget; w++) {
            if (m) m->comparisons++;
            if (cost <= w) {
                int take = dp[i - 1][w - cost] + val;
                int skip = dp[i - 1][w];
                if (m) m->comparisons++;
                dp[i][w] = (take > skip) ? take : skip;
            } else {
                dp[i][w] = dp[i - 1][w];
            }
            if (m) m->swaps_or_writes++;
        }
    }

    res.max_risk_mitigated = dp[count][budget];

    /* Backtrack to reconstruct chosen playbooks */
    int w = budget;
    for (int i = count; i > 0 && w > 0; i--) {
        if (m) m->comparisons++;
        if (dp[i][w] != dp[i - 1][w]) {
            res.selected_ids[res.num_selected++] = actions[i - 1].action_id;
            res.total_cost += actions[i - 1].disruption_cost;
            w -= actions[i - 1].disruption_cost;
            if (m) m->swaps_or_writes++;
        }
    }

    for (size_t i = 0; i < rows; i++) free(dp[i]);
    free(dp);

    return res;
}

/* 2. Matrix Chain Multiplication DP */
static void build_parens_string(int i, int j, int s[MAX_HOSTS][MAX_HOSTS], char *buf, size_t *pos, size_t max_len) {
    if (i == j) {
        if (*pos + 4 < max_len) {
            *pos += (size_t)snprintf(buf + *pos, max_len - *pos, "A%d", i + 1);
        }
        return;
    }
    if (*pos + 1 < max_len) buf[(*pos)++] = '(';
    build_parens_string(i, s[i][j], s, buf, pos, max_len);
    if (*pos + 3 < max_len) {
        *pos += (size_t)snprintf(buf + *pos, max_len - *pos, " x ");
    }
    build_parens_string(s[i][j] + 1, j, s, buf, pos, max_len);
    if (*pos + 1 < max_len) buf[(*pos)++] = ')';
}

MatrixChainResult matrix_chain_order_dp(const int *dims, int n, MetricsTracker *m) {
    MatrixChainResult res;
    res.min_scalar_multiplications = 0;
    res.optimal_parens[0] = '\0';
    if (!dims || n <= 1 || n > MAX_HOSTS) return res;

    int num_matrices = n - 1;
    int m_table[MAX_HOSTS][MAX_HOSTS] = {0};
    int s_table[MAX_HOSTS][MAX_HOSTS] = {0};

    for (int len = 2; len <= num_matrices; len++) {
        for (int i = 0; i <= num_matrices - len; i++) {
            int j = i + len - 1;
            m_table[i][j] = INF_COST;

            for (int k = i; k < j; k++) {
                int cost = m_table[i][k] + m_table[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1];
                if (m) m->comparisons++;
                if (cost < m_table[i][j]) {
                    m_table[i][j] = cost;
                    s_table[i][j] = k;
                    if (m) m->swaps_or_writes++;
                }
            }
        }
    }

    res.min_scalar_multiplications = m_table[0][num_matrices - 1];

    size_t pos = 0;
    build_parens_string(0, num_matrices - 1, s_table, res.optimal_parens, &pos, sizeof(res.optimal_parens));
    res.optimal_parens[pos] = '\0';

    return res;
}

/* 3. LCS Attack Correlation */
LCSResult lcs_attack_correlation(const char *observed_events, const char *killchain_pattern, MetricsTracker *m) {
    LCSResult res;
    res.lcs_length = 0;
    res.matched_sequence[0] = '\0';
    if (!observed_events || !killchain_pattern) return res;

    int n = (int)strlen(observed_events);
    int p = (int)strlen(killchain_pattern);
    if (n == 0 || p == 0) return res;

    if (n >= MAX_PAYLOAD_LEN) n = MAX_PAYLOAD_LEN - 1;
    if (p >= MAX_PAYLOAD_LEN) p = MAX_PAYLOAD_LEN - 1;

    int dp[MAX_PAYLOAD_LEN][MAX_PAYLOAD_LEN] = {0};

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= p; j++) {
            if (m) m->comparisons++;
            if (observed_events[i - 1] == killchain_pattern[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                int up = dp[i - 1][j];
                int left = dp[i][j - 1];
                dp[i][j] = (up > left) ? up : left;
            }
            if (m) m->swaps_or_writes++;
        }
    }

    res.lcs_length = dp[n][p];

    /* Backtrack to reconstruct matching sequence */
    int idx = res.lcs_length;
    res.matched_sequence[idx] = '\0';

    int i = n, j = p;
    while (i > 0 && j > 0) {
        if (m) m->comparisons++;
        if (observed_events[i - 1] == killchain_pattern[j - 1]) {
            res.matched_sequence[--idx] = observed_events[i - 1];
            i--;
            j--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
        if (m) m->swaps_or_writes++;
    }

    return res;
}

/* 4. Optimal Binary Search Tree (OBST) */
OBSTResult obst_signature_index(const ThreatSignature *sigs, int n, MetricsTracker *m) {
    OBSTResult res;
    res.min_expected_cost = 0.0;
    memset(res.root_table, 0, sizeof(res.root_table));
    if (!sigs || n <= 0 || n >= MAX_HOSTS) return res;

    double e[MAX_HOSTS + 1][MAX_HOSTS + 1] = {{0.0}};
    double w[MAX_HOSTS + 1][MAX_HOSTS + 1] = {{0.0}};

    /* Base cases: e[i][i-1] = 0, w[i][i-1] = 0 */
    for (int i = 1; i <= n + 1; i++) {
        e[i][i - 1] = 0.0;
        w[i][i - 1] = 0.0;
    }

    for (int len = 1; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            e[i][j] = 1e9;
            w[i][j] = w[i][j - 1] + sigs[j - 1].hit_probability;

            for (int r = i; r <= j; r++) {
                double t = e[i][r - 1] + e[r + 1][j] + w[i][j];
                if (m) m->comparisons++;
                if (t < e[i][j]) {
                    e[i][j] = t;
                    res.root_table[i][j] = r;
                    if (m) m->swaps_or_writes++;
                }
            }
        }
    }

    res.min_expected_cost = e[1][n];
    return res;
}

/* 5. Bellman-Ford Shortest Path */
BellmanFordResult bellman_ford_escalation(const AttackGraph *graph, int source, MetricsTracker *m) {
    BellmanFordResult res;
    res.has_negative_cycle = 0;
    if (!graph || source < 0 || source >= graph->num_hosts) return res;

    int n = graph->num_hosts;
    for (int i = 0; i < n; i++) {
        res.dist[i] = INF_COST;
        res.parent[i] = -1;
    }
    res.dist[source] = 0;

    /* Relax all edges |V| - 1 times */
    for (int i = 1; i <= n - 1; i++) {
        for (int j = 0; j < graph->num_edges; j++) {
            int u = graph->edges[j].u;
            int v = graph->edges[j].v;
            int w = graph->edges[j].exploit_weight;

            if (res.dist[u] < INF_COST) {
                if (m) m->comparisons++;
                if (res.dist[u] + w < res.dist[v]) {
                    res.dist[v] = res.dist[u] + w;
                    res.parent[v] = u;
                    if (m) {
                        m->graph_relaxations++;
                        m->swaps_or_writes++;
                    }
                }
            }
        }
    }

    /* Check for negative-weight cycles */
    for (int j = 0; j < graph->num_edges; j++) {
        int u = graph->edges[j].u;
        int v = graph->edges[j].v;
        int w = graph->edges[j].exploit_weight;

        if (res.dist[u] < INF_COST && res.dist[u] + w < res.dist[v]) {
            res.has_negative_cycle = 1;
            break;
        }
    }

    return res;
}

/* 6. Floyd-Warshall All-Pairs Exposure Matrix */
FloydWarshallResult floyd_warshall_exposure(const AttackGraph *graph, MetricsTracker *m) {
    FloydWarshallResult res;
    if (!graph || graph->num_hosts <= 0) return res;

    int n = graph->num_hosts;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            res.dist[i][j] = graph->adj_weight[i][j];
            if (i != j && graph->adj_weight[i][j] < INF_COST) {
                res.next_hop[i][j] = j;
            } else {
                res.next_hop[i][j] = -1;
            }
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (res.dist[i][k] < INF_COST && res.dist[k][j] < INF_COST) {
                    if (m) m->comparisons++;
                    if (res.dist[i][k] + res.dist[k][j] < res.dist[i][j]) {
                        res.dist[i][j] = res.dist[i][k] + res.dist[k][j];
                        res.next_hop[i][j] = res.next_hop[i][k];
                        if (m) {
                            m->graph_relaxations++;
                            m->swaps_or_writes++;
                        }
                    }
                }
            }
        }
    }

    return res;
}

/* 7. TSP Held-Karp Bitmask DP */
TSPResult tsp_held_karp_dp(const AttackGraph *graph, int n, MetricsTracker *m) {
    TSPResult res;
    res.min_tour_cost = INF_COST;
    res.tour_length = 0;
    if (!graph || n <= 1 || n > 16) return res;

    int num_states = 1 << n;

    /* Allocate memo table: num_states x n */
    int **dp = (int **)tracked_malloc(num_states * sizeof(int *), m);
    int **parent = (int **)tracked_malloc(num_states * sizeof(int *), m);

    for (int i = 0; i < num_states; i++) {
        dp[i] = (int *)tracked_malloc(n * sizeof(int), m);
        parent[i] = (int *)tracked_malloc(n * sizeof(int), m);
        for (int j = 0; j < n; j++) {
            dp[i][j] = INF_COST;
            parent[i][j] = -1;
        }
    }

    /* Start at jump-box host 0 */
    dp[1][0] = 0;

    for (int mask = 1; mask < num_states; mask++) {
        for (int u = 0; u < n; u++) {
            if (!(mask & (1 << u))) continue;
            if (dp[mask][u] == INF_COST) continue;

            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int w = graph->adj_weight[u][v];
                if (w >= INF_COST) continue;

                int next_mask = mask | (1 << v);
                int cost = dp[mask][u] + w;

                if (m) m->comparisons++;
                if (cost < dp[next_mask][v]) {
                    dp[next_mask][v] = cost;
                    parent[next_mask][v] = u;
                    if (m) m->swaps_or_writes++;
                }
            }
        }
    }

    /* Return to jump-box 0 */
    int full_mask = (1 << n) - 1;
    int best_last = -1;

    for (int u = 1; u < n; u++) {
        int w = graph->adj_weight[u][0];
        if (dp[full_mask][u] < INF_COST && w < INF_COST) {
            int total = dp[full_mask][u] + w;
            if (m) m->comparisons++;
            if (total < res.min_tour_cost) {
                res.min_tour_cost = total;
                best_last = u;
            }
        }
    }

    /* Tour reconstruction */
    if (best_last != -1) {
        int curr_mask = full_mask;
        int curr_node = best_last;
        int route[MAX_HOSTS];
        int r_len = 0;

        while (curr_node != -1 && curr_mask > 0) {
            route[r_len++] = curr_node;
            int prev = parent[curr_mask][curr_node];
            curr_mask ^= (1 << curr_node);
            curr_node = prev;
        }

        res.tour_nodes[0] = 0;
        for (int i = 0; i < r_len; i++) {
            res.tour_nodes[i + 1] = route[r_len - 1 - i];
        }
        res.tour_nodes[r_len + 1] = 0;
        res.tour_length = r_len + 2;
    }

    for (int i = 0; i < num_states; i++) {
        free(dp[i]);
        free(parent[i]);
    }
    free(dp);
    free(parent);

    return res;
}
