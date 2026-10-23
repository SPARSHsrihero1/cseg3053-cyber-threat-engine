#include "domain.h"
#include "metrics.h"
#include "data_generator.h"
#include "unit2_divide_conquer.h"
#include "unit3_greedy.h"
#include "unit4_dp.h"
#include "unit5_backtracking_bb.h"
#include "unit6_flow_string_crt.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

static int tests_passed = 0;
static int tests_total = 0;

#define TEST_ASSERT(cond, msg) do { \
    tests_total++; \
    if (cond) { \
        tests_passed++; \
        printf("  [PASS] %s\n", msg); \
    } else { \
        printf("  [FAIL] %s (Line %d)\n", msg, __LINE__); \
        assert(cond); \
    } \
} while(0)

/* ========================================================================= */
/* UNIT II TESTS: DIVIDE AND CONQUER                                         */
/* ========================================================================= */
void test_unit2_divide_conquer(void) {
    printf("\n=== Running Unit II Tests: Divide and Conquer ===\n");
    MetricsTracker m;
    metrics_init(&m, "Test_Unit2", "Divide & Conquer", 100);

    /* 1. Merge Sort & Binary Search */
    EventLog logs[20];
    generate_event_logs(logs, 20, 101);

    merge_sort(logs, 20, &m);
    int is_sorted = 1;
    for (int i = 1; i < 20; i++) {
        if (logs[i].timestamp < logs[i - 1].timestamp) {
            is_sorted = 0;
            break;
        }
    }
    TEST_ASSERT(is_sorted, "Merge Sort produces monotonically sorted timestamps");

    uint64_t target_ts = logs[7].timestamp;
    int idx_iter = binary_search_iterative(logs, 20, target_ts, &m);
    int idx_rec = binary_search_recursive(logs, 0, 19, target_ts, &m);
    TEST_ASSERT(idx_iter == 7 && idx_rec == 7, "Iterative and Recursive Binary Search locate exact target");

    int idx_missing = binary_search_iterative(logs, 20, 999999999999ULL, &m);
    TEST_ASSERT(idx_missing == -1, "Binary Search returns -1 on absent timestamp");

    /* BST Signature Lookup */
    BSTNode *bst_root = NULL;
    ThreatSignature sigs[5];
    generate_threat_signatures(sigs, 5);
    for (int i = 0; i < 5; i++) {
        bst_root = bst_insert(bst_root, sigs[i], &m);
    }
    BSTNode *found_iter = bst_search_iterative(bst_root, sigs[2].sig_id, &m);
    BSTNode *found_rec = bst_search_recursive(bst_root, sigs[2].sig_id, &m);
    TEST_ASSERT(found_iter != NULL && found_rec != NULL && found_iter->key == sigs[2].sig_id,
                "BST Iterative and Recursive search locate threat signature");
    bst_free(bst_root);

    /* 2. Quick Sort (Deterministic & Randomized) */
    EventLog qlogs1[20], qlogs2[20];
    generate_event_logs(qlogs1, 20, 202);
    generate_event_logs(qlogs2, 20, 202);

    quick_sort_deterministic(qlogs1, 0, 19, &m);
    quick_sort_randomized(qlogs2, 0, 19, &m);

    int q1_sorted = 1, q2_sorted = 1;
    for (int i = 1; i < 20; i++) {
        if (qlogs1[i].timestamp < qlogs1[i - 1].timestamp) q1_sorted = 0;
        if (qlogs2[i].timestamp < qlogs2[i - 1].timestamp) q2_sorted = 0;
    }
    TEST_ASSERT(q1_sorted && q2_sorted, "Deterministic and Randomized Quick Sort sort correctly");

    /* 3. Maximum Subarray (DC vs. Kadane) */
    EventLog burst_logs[10];
    int deltas[10] = { 2, -4, 5, -1, 6, -3, 8, -10, 4, 1 };
    for (int i = 0; i < 10; i++) {
        burst_logs[i].anomaly_delta = deltas[i];
    }
    SubarrayResult res_dc = max_subarray_dc(burst_logs, 0, 9, &m);
    SubarrayResult res_kadane = max_subarray_kadane(burst_logs, 10, &m);
    TEST_ASSERT(res_dc.max_sum == 15 && res_kadane.max_sum == 15,
                "Maximum Subarray: Divide-and-Conquer and Kadane yield identical optimal burst (sum=15)");

    /* 4. Fast Power Modular Exponentiation */
    uint64_t pow_rec = fast_power_mod_recursive(7, 13, 1000, &m);
    uint64_t pow_iter = fast_power_mod_iterative(7, 13, 1000, &m);
    TEST_ASSERT(pow_rec == 407 && pow_iter == 407,
                "Fast Exponentiation: 7^13 mod 1000 == 407 for both recursive and iterative");

    /* 5. Celebrity C2 Sinkhole */
    AttackGraph c2_graph;
    generate_c2_celebrity_graph(&c2_graph, 8, 3);
    int c2_found = find_celebrity_c2(8, c2_graph.comm_matrix, &m);
    TEST_ASSERT(c2_found == 3, "Celebrity Problem: O(N) detection identifies hidden C2 node 3");

    /* 6. Classical vs. Strassen Matrix Multiplication */
    int A[MAX_HOSTS][MAX_HOSTS] = {{1, 2}, {3, 4}};
    int B[MAX_HOSTS][MAX_HOSTS] = {{5, 6}, {7, 8}};
    int C_classic[MAX_HOSTS][MAX_HOSTS] = {{0}};
    int C_strassen[MAX_HOSTS][MAX_HOSTS] = {{0}};

    matrix_mult_classical(2, A, B, C_classic, &m);
    matrix_mult_strassen(2, A, B, C_strassen, &m);
    int mat_match = (C_classic[0][0] == 19 && C_classic[0][1] == 22 &&
                     C_classic[1][0] == 43 && C_classic[1][1] == 50 &&
                     C_classic[0][0] == C_strassen[0][0] && C_classic[1][1] == C_strassen[1][1]);
    TEST_ASSERT(mat_match, "Matrix Multiplication: Classical and Strassen match expected product");
}

/* ========================================================================= */
/* UNIT III TESTS: GREEDY METHOD                                             */
/* ========================================================================= */
void test_unit3_greedy(void) {
    printf("\n=== Running Unit III Tests: Greedy Method ===\n");
    MetricsTracker m;
    metrics_init(&m, "Test_Unit3", "Greedy", 100);

    /* 1. Activity Selection */
    ContainmentAction actions[6] = {
        {1, "Scan A", 10, 20, 1, 3},
        {2, "Scan B", 10, 20, 2, 5},
        {3, "Scan C", 10, 20, 4, 7},
        {4, "Scan D", 10, 20, 1, 8},
        {5, "Scan E", 10, 20, 6, 9},
        {6, "Scan F", 10, 20, 8, 10}
    };
    ActivityResult act_res = activity_selection_scans(actions, 6, &m);
    TEST_ASSERT(act_res.count == 3, "Activity Selection: Max non-overlapping scans selected == 3");

    /* 2. Interval Partitioning */
    PartitionResult part_res = interval_partition_sandboxes(actions, 6, &m);
    TEST_ASSERT(part_res.total_sandboxes >= 2, "Interval Partitioning: Min parallel sandboxes determined");

    /* 3. Fractional Knapsack */
    ContainmentAction dpi_items[3] = {
        {1, "DPI Stream 1", 10, 60, 0, 0}, /* Ratio 6.0 */
        {2, "DPI Stream 2", 20, 100, 0, 0},/* Ratio 5.0 */
        {3, "DPI Stream 3", 30, 120, 0, 0} /* Ratio 4.0 */
    };
    FractionalKnapsackResult fk_res = fractional_knapsack_dpi(dpi_items, 3, 50.0, &m);
    TEST_ASSERT(fk_res.total_risk_mitigated == 240.0, "Fractional Knapsack: Optimal fractional value == 240.0");

    /* 4. Huffman Coding */
    const char *syslog_sample = "CRITICAL_LOG_ALERT: EXPLOIT DETECTED ON PORT 445";
    HuffmanResult huff = huffman_compress_logs(syslog_sample, &m);
    char decompressed[256] = {0};
    huffman_decompress_logs(&huff, decompressed, sizeof(decompressed), &m);
    TEST_ASSERT(strcmp(syslog_sample, decompressed) == 0,
                "Huffman Coding: 100% Lossless log payload compression and decompression");
    huffman_free_tree(huff.root);

    /* 5. Dijkstra's Algorithm */
    AttackGraph g;
    g.num_hosts = 4;
    g.num_edges = 4;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) g.adj_weight[i][j] = INF_COST;
    g.adj_weight[0][1] = 1;
    g.adj_weight[1][2] = 2;
    g.adj_weight[0][2] = 5;
    g.adj_weight[2][3] = 1;
    DijkstraResult dij = dijkstra_attack_path(&g, 0, 3, &m);
    TEST_ASSERT(dij.dist[3] == 4, "Dijkstra: Single-source shortest path cost to target == 4");

    /* 6. Prim vs. Kruskal MST */
    AttackGraph mst_g;
    mst_g.num_hosts = 4;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) mst_g.adj_weight[i][j] = INF_COST;
    mst_g.adj_weight[0][1] = mst_g.adj_weight[1][0] = 1;
    mst_g.adj_weight[1][2] = mst_g.adj_weight[2][1] = 2;
    mst_g.adj_weight[2][3] = mst_g.adj_weight[3][2] = 3;
    mst_g.adj_weight[0][3] = mst_g.adj_weight[3][0] = 10;
    mst_g.adj_weight[0][2] = mst_g.adj_weight[2][0] = 4;

    MSTResult prim = prim_quarantine_mst(&mst_g, &m);
    MSTResult kruskal = kruskal_quarantine_mst(&mst_g, &m);
    TEST_ASSERT(prim.total_weight == 6 && kruskal.total_weight == 6,
                "Prim and Kruskal MST yield identical minimum spanning weight == 6");
}

/* ========================================================================= */
/* UNIT IV TESTS: DYNAMIC PROGRAMMING                                        */
/* ========================================================================= */
void test_unit4_dp(void) {
    printf("\n=== Running Unit IV Tests: Dynamic Programming ===\n");
    MetricsTracker m;
    metrics_init(&m, "Test_Unit4", "Dynamic Programming", 100);

    /* 1. 0/1 Knapsack DP */
    ContainmentAction playbooks[4] = {
        {1, "PB1", 2, 3, 0, 0},
        {2, "PB2", 3, 4, 0, 0},
        {3, "PB3", 4, 5, 0, 0},
        {4, "PB4", 5, 6, 0, 0}
    };
    Knapsack01Result kp_res = knapsack_01_dp(playbooks, 4, 5, &m);
    TEST_ASSERT(kp_res.max_risk_mitigated == 7, "0/1 Knapsack DP: Max value under budget == 7");

    /* 2. Matrix Chain Multiplication DP */
    int dims[5] = {10, 20, 30, 40, 30};
    MatrixChainResult mcm = matrix_chain_order_dp(dims, 5, &m);
    TEST_ASSERT(mcm.min_scalar_multiplications == 30000, "Matrix Chain Order DP: Correct minimum multiplications == 30000");

    /* 3. LCS Attack Correlation */
    const char *obs = "ABCBDAB";
    const char *pattern = "BDCABA";
    LCSResult lcs = lcs_attack_correlation(obs, pattern, &m);
    TEST_ASSERT(lcs.lcs_length == 4, "LCS Attack Correlation: Kill-chain subsequence length == 4");

    /* 4. Optimal BST */
    ThreatSignature sigs[3] = {
        {1, "P1", 10, 0.5},
        {2, "P2", 20, 0.3},
        {3, "P3", 30, 0.2}
    };
    OBSTResult obst = obst_signature_index(sigs, 3, &m);
    TEST_ASSERT(obst.min_expected_cost > 0.0, "Optimal BST computes non-zero expected lookup cost");

    /* 5. Bellman-Ford Shortest Path */
    AttackGraph bg;
    bg.num_hosts = 4;
    bg.num_edges = 4;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) bg.adj_weight[i][j] = INF_COST;
    bg.edges[0] = (NetworkEdge){0, 1, 5, 0};
    bg.edges[1] = (NetworkEdge){1, 2, -2, 0}; /* Negative edge */
    bg.edges[2] = (NetworkEdge){2, 3, 3, 0};
    bg.edges[3] = (NetworkEdge){0, 3, 10, 0};
    BellmanFordResult bf = bellman_ford_escalation(&bg, 0, &m);
    TEST_ASSERT(bf.dist[3] == 6 && !bf.has_negative_cycle,
                "Bellman-Ford: Correctly relaxes negative edges without cycle (dist=6)");

    /* 6. Floyd-Warshall All-Pairs */
    AttackGraph fg;
    fg.num_hosts = 3;
    for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) fg.adj_weight[i][j] = (i == j) ? 0 : INF_COST;
    fg.adj_weight[0][1] = 4;
    fg.adj_weight[1][2] = 3;
    fg.adj_weight[0][2] = 10;
    FloydWarshallResult fw = floyd_warshall_exposure(&fg, &m);
    TEST_ASSERT(fw.dist[0][2] == 7, "Floyd-Warshall: All-pairs distance dist[0][2] == 7");

    /* 7. TSP Held-Karp DP */
    AttackGraph tg;
    tg.num_hosts = 4;
    int dists[4][4] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) tg.adj_weight[i][j] = dists[i][j];
    TSPResult tsp_dp = tsp_held_karp_dp(&tg, 4, &m);
    TEST_ASSERT(tsp_dp.min_tour_cost == 80, "TSP Held-Karp Bitmask DP: Optimal tour cost == 80");
}

/* ========================================================================= */
/* UNIT V TESTS: BACKTRACKING & BRANCH AND BOUND                             */
/* ========================================================================= */
void test_unit5_backtracking_bb(void) {
    printf("\n=== Running Unit V Tests: Backtracking & Branch and Bound ===\n");
    MetricsTracker m;
    metrics_init(&m, "Test_Unit5", "Backtracking & BB", 100);

    /* 1. N-Queens Honeypots */
    NQueensResult nq4 = n_queens_honeypots(4, &m);
    TEST_ASSERT(nq4.total_solutions == 2, "N-Queens Backtracking: 4-Queens total solutions == 2");

    NQueensResult nq8 = n_queens_honeypots(8, &m);
    TEST_ASSERT(nq8.total_solutions == 92, "N-Queens Backtracking: 8-Queens total solutions == 92");

    /* 2. Sum of Subsets */
    int alerts[5] = {10, 15, 20, 25, 35};
    SumOfSubsetsResult ss = sum_of_subsets_alerts(alerts, 5, 45, &m);
    TEST_ASSERT(ss.total_subsets_found >= 2, "Sum of Subsets: Identified valid risk escalation combinations");

    /* 3. 0/1 Knapsack: Backtracking vs FIFO, LIFO, LC Branch & Bound */
    ContainmentAction actions[4] = {
        {1, "A1", 2, 40, 0, 0},
        {2, "A2", 3, 50, 0, 0},
        {3, "A3", 4, 100, 0, 0},
        {4, "A4", 5, 95, 0, 0}
    };
    int cap = 7;
    Knapsack01Result dp_gold = knapsack_01_dp(actions, 4, cap, &m);
    KnapsackBacktrackResult bt_res = knapsack_01_backtrack(actions, 4, cap, &m);
    KnapsackBBResult bb_fifo = knapsack_bb_fifo(actions, 4, cap, &m);
    KnapsackBBResult bb_lifo = knapsack_bb_lifo(actions, 4, cap, &m);
    KnapsackBBResult bb_lc = knapsack_bb_lc(actions, 4, cap, &m);

    TEST_ASSERT(bt_res.max_value == dp_gold.max_risk_mitigated &&
                bb_fifo.max_value == dp_gold.max_risk_mitigated &&
                bb_lifo.max_value == dp_gold.max_risk_mitigated &&
                bb_lc.max_value == dp_gold.max_risk_mitigated,
                "0/1 Knapsack: Backtracking and FIFO/LIFO/LC Branch & Bound match DP gold standard (val=140)");

    /* 4. TSP Least-Cost Branch & Bound */
    AttackGraph tg;
    tg.num_hosts = 4;
    int dists[4][4] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) tg.adj_weight[i][j] = dists[i][j];
    TSPBBResult tsp_bb = tsp_bb_lc(&tg, 4, &m);
    TEST_ASSERT(tsp_bb.min_tour_cost == 80, "TSP Least-Cost Branch & Bound matches Held-Karp DP tour cost == 80");
}

/* ========================================================================= */
/* UNIT VI TESTS: FLOW, STRING-MATCHING, CRT                                 */
/* ========================================================================= */
void test_unit6_flow_string_crt(void) {
    printf("\n=== Running Unit VI Tests: Flow, String Matching, CRT ===\n");
    MetricsTracker m;
    metrics_init(&m, "Test_Unit6", "Flow & Strings", 100);

    /* 1. Ford-Fulkerson Max Flow & Min Cut */
    AttackGraph flow_g;
    flow_g.num_hosts = 4;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) flow_g.adj_capacity[i][j] = 0;
    flow_g.adj_capacity[0][1] = 10;
    flow_g.adj_capacity[0][2] = 5;
    flow_g.adj_capacity[1][2] = 15;
    flow_g.adj_capacity[1][3] = 10;
    flow_g.adj_capacity[2][3] = 10;
    FlowResult flow_res = ford_fulkerson_max_flow(&flow_g, 0, 3, &m);
    TEST_ASSERT(flow_res.max_flow == 15, "Ford-Fulkerson / Edmonds-Karp Max Flow == 15");
    TEST_ASSERT(flow_res.num_mincut_edges > 0, "Minimum s-t cut edges extracted successfully");

    /* 2. Maximum Bipartite Matching for SOC Analysts */
    int adj[MAX_HOSTS][MAX_HOSTS] = {{0}};
    adj[0][0] = 1; adj[0][1] = 1;
    adj[1][0] = 1;
    adj[2][2] = 1;
    BipartiteMatchingResult bpm = max_bipartite_matching_soc(3, 3, adj, &m);
    TEST_ASSERT(bpm.max_matches == 3, "Maximum Bipartite Matching assigns 3 incidents to 3 analysts");

    /* 3. Chinese Remainder Theorem */
    int64_t rems[3] = {2, 3, 2};
    int64_t mods[3] = {3, 5, 7};
    CRTResult crt = crt_reconstruct_telemetry(3, rems, mods, &m);
    TEST_ASSERT(crt.success && (crt.reconstructed_counter % 3 == 2) &&
                (crt.reconstructed_counter % 5 == 3) && (crt.reconstructed_counter % 7 == 2) &&
                crt.reconstructed_counter == 23,
                "Chinese Remainder Theorem reconstructs exact packet counter (23 mod 105)");

    /* 4. String-Matching Engines (4 implementations) */
    const char *haystack = "AABAACAADAABAABA";
    const char *needle = "AABA";
    StringMatchResult sm_naive = strmatch_naive(haystack, needle, &m);
    StringMatchResult sm_rk = strmatch_rabin_karp(haystack, needle, &m);
    StringMatchResult sm_fa = strmatch_finite_automaton(haystack, needle, &m);
    StringMatchResult sm_kmp = strmatch_kmp(haystack, needle, &m);

    TEST_ASSERT(sm_naive.match_count == 3 &&
                sm_rk.match_count == 3 &&
                sm_fa.match_count == 3 &&
                sm_kmp.match_count == 3,
                "All 4 String-Matching Engines identify identical match count (count=3)");
    TEST_ASSERT(sm_naive.first_match_index == 0 &&
                sm_rk.first_match_index == 0 &&
                sm_fa.first_match_index == 0 &&
                sm_kmp.first_match_index == 0,
                "All 4 String-Matching Engines identify identical first match index (0)");
}

int main(void) {
    printf("===============================================================\n");
    printf("   CSEG3053 DAA PBL: CYBERSECURITY THREAT ENGINE TEST SUITE    \n");
    printf("===============================================================\n");

    test_unit2_divide_conquer();
    test_unit3_greedy();
    test_unit4_dp();
    test_unit5_backtracking_bb();
    test_unit6_flow_string_crt();

    printf("\n===============================================================\n");
    printf("TEST SUMMARY: %d / %d PASSED (100%%)\n", tests_passed, tests_total);
    printf("===============================================================\n");

    return (tests_passed == tests_total) ? 0 : 1;
}
