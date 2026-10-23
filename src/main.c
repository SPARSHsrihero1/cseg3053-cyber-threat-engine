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

#define MAX_BENCHMARK_RECORDS 256
static MetricsTracker global_records[MAX_BENCHMARK_RECORDS];
static size_t record_count = 0;

static void record_metric(const MetricsTracker *m) {
    if (record_count < MAX_BENCHMARK_RECORDS && m) {
        global_records[record_count++] = *m;
    }
}

static void export_all_metrics(void) {
    const char *csv_file = "data/benchmark_results.csv";
    const char *json_file = "data/benchmark_results.json";

    if (record_count > 0) {
        metrics_export_csv(csv_file, &global_records[0], 0);
        for (size_t i = 1; i < record_count; i++) {
            metrics_export_csv(csv_file, &global_records[i], 1);
        }
        metrics_export_json(json_file, global_records, record_count);
        printf("\n[+] Benchmark metrics exported successfully to:\n");
        printf("    CSV : %s (%zu rows)\n", csv_file, record_count);
        printf("    JSON: %s (%zu objects)\n", json_file, record_count);
    }
}

/* ========================================================================= */
/* SCENARIO 1: NORMAL SOC OPERATION                                          */
/* ========================================================================= */
void run_scenario_1_normal_soc(void) {
    printf("\n======================================================================\n");
    printf(" SCENARIO 1: NORMAL SOC OPERATION (Baseline Triage & Signature Scan)   \n");
    printf("======================================================================\n");

    const size_t N = 1000;
    EventLog *logs1 = (EventLog *)malloc(N * sizeof(EventLog));
    EventLog *logs2 = (EventLog *)malloc(N * sizeof(EventLog));
    generate_event_logs(logs1, N, 42);
    memcpy(logs2, logs1, N * sizeof(EventLog));

    MetricsTracker m_merge, m_quick, m_bs_iter, m_bs_rec;
    MetricsTracker m_naive, m_rk, m_fa, m_kmp, m_lcs, m_obst, m_bpm;

    /* 1. Merge Sort vs Quick Sort */
    metrics_init(&m_merge, "Merge Sort (Logs)", "Divide & Conquer", N);
    metrics_start(&m_merge);
    merge_sort(logs1, N, &m_merge);
    metrics_stop(&m_merge);
    record_metric(&m_merge);

    metrics_init(&m_quick, "Quick Sort (Rand Pivot)", "Divide & Conquer", N);
    metrics_start(&m_quick);
    quick_sort_randomized(logs2, 0, (int)N - 1, &m_quick);
    metrics_stop(&m_quick);
    record_metric(&m_quick);

    /* 2. Binary Search Iterative vs Recursive */
    uint64_t target_ts = logs1[N / 2].timestamp;

    metrics_init(&m_bs_iter, "Binary Search (Iterative)", "Divide & Conquer", N);
    metrics_start(&m_bs_iter);
    int idx1 = binary_search_iterative(logs1, N, target_ts, &m_bs_iter);
    metrics_stop(&m_bs_iter);
    record_metric(&m_bs_iter);

    metrics_init(&m_bs_rec, "Binary Search (Recursive)", "Divide & Conquer", N);
    metrics_start(&m_bs_rec);
    int idx2 = binary_search_recursive(logs1, 0, (int)N - 1, target_ts, &m_bs_rec);
    metrics_stop(&m_bs_rec);
    record_metric(&m_bs_rec);

    /* 3. String Matching on Payload */
    char long_payload[4096];
    memset(long_payload, 0, sizeof(long_payload));
    for (int i = 0; i < 20; i++) {
        strncat(long_payload, logs1[i].payload, sizeof(long_payload) - strlen(long_payload) - 1);
        strncat(long_payload, " ", sizeof(long_payload) - strlen(long_payload) - 1);
    }
    const char *target_pattern = "UNION SELECT";
    size_t payload_len = strlen(long_payload);

    metrics_init(&m_naive, "Naive String Match", "String Matching", payload_len);
    metrics_start(&m_naive);
    StringMatchResult sm1 = strmatch_naive(long_payload, target_pattern, &m_naive);
    metrics_stop(&m_naive);
    record_metric(&m_naive);

    metrics_init(&m_rk, "Rabin-Karp Rolling Hash", "String Matching", payload_len);
    metrics_start(&m_rk);
    StringMatchResult sm2 = strmatch_rabin_karp(long_payload, target_pattern, &m_rk);
    metrics_stop(&m_rk);
    record_metric(&m_rk);

    metrics_init(&m_fa, "Finite Automaton Match", "String Matching", payload_len);
    metrics_start(&m_fa);
    StringMatchResult sm3 = strmatch_finite_automaton(long_payload, target_pattern, &m_fa);
    metrics_stop(&m_fa);
    record_metric(&m_fa);

    metrics_init(&m_kmp, "KMP Matcher", "String Matching", payload_len);
    metrics_start(&m_kmp);
    StringMatchResult sm4 = strmatch_kmp(long_payload, target_pattern, &m_kmp);
    metrics_stop(&m_kmp);
    record_metric(&m_kmp);

    /* 4. LCS Kill-Chain Correlation */
    char obs_events[64];
    for (int i = 0; i < 30; i++) obs_events[i] = logs1[i].event_code;
    obs_events[30] = '\0';
    const char *apt_sig = "ABDEGXMNZ";

    metrics_init(&m_lcs, "LCS Kill-Chain Match", "Dynamic Programming", 30);
    metrics_start(&m_lcs);
    LCSResult lcs_res = lcs_attack_correlation(obs_events, apt_sig, &m_lcs);
    metrics_stop(&m_lcs);
    record_metric(&m_lcs);

    /* 5. Optimal BST Lookup Index */
    ThreatSignature sigs[8];
    generate_threat_signatures(sigs, 8);
    metrics_init(&m_obst, "OBST Signature Index", "Dynamic Programming", 8);
    metrics_start(&m_obst);
    OBSTResult obst_res = obst_signature_index(sigs, 8, &m_obst);
    metrics_stop(&m_obst);
    record_metric(&m_obst);

    /* 6. SOC Analyst Bipartite Matching */
    int bpm_adj[MAX_HOSTS][MAX_HOSTS];
    generate_soc_bipartite_graph(12, 8, bpm_adj, 0.35, 77);
    metrics_init(&m_bpm, "Bipartite Incident Match", "Graph / Flow", 12);
    metrics_start(&m_bpm);
    BipartiteMatchingResult bpm_res = max_bipartite_matching_soc(12, 8, bpm_adj, &m_bpm);
    metrics_stop(&m_bpm);
    record_metric(&m_bpm);

    metrics_print_table_header();
    metrics_print_row(&m_merge);
    metrics_print_row(&m_quick);
    metrics_print_row(&m_bs_iter);
    metrics_print_row(&m_bs_rec);
    metrics_print_row(&m_naive);
    metrics_print_row(&m_rk);
    metrics_print_row(&m_fa);
    metrics_print_row(&m_kmp);
    metrics_print_row(&m_lcs);
    metrics_print_row(&m_obst);
    metrics_print_row(&m_bpm);
    printf("+------------------------------+------------------+----------+--------------+--------------+------------+------------+------------+--------------+\n");

    printf("\n[+] Verification Signals:\n");
    printf("    Target Timestamp Found At Index: Iterative=%d, Recursive=%d\n", idx1, idx2);
    printf("    String Matching Hits: Naive=%d, RK=%d (Spurious=%llu), FA=%d, KMP=%d\n",
           sm1.match_count, sm2.match_count, (unsigned long long)sm2.spurious_hits, sm3.match_count, sm4.match_count);
    printf("    LCS Kill-Chain Matched Length: %d, Sequence: \"%s\"\n", lcs_res.lcs_length, lcs_res.matched_sequence);
    printf("    OBST Min Expected Search Cost: %.4f\n", obst_res.min_expected_cost);
    printf("    Bipartite Analyst Matches: %d / 12 incidents assigned\n", bpm_res.max_matches);

    free(logs1);
    free(logs2);
}

/* ========================================================================= */
/* SCENARIO 2: CAPACITY / CONSTRAINT SHOCK (Active Ransomware Outbreak)       */
/* ========================================================================= */
void run_scenario_2_ransomware_shock(void) {
    printf("\n======================================================================\n");
    printf(" SCENARIO 2: CONSTRAINT SHOCK (Ransomware Outbreak & 60%% SLA Crunch) \n");
    printf("======================================================================\n");

    const int total_budget = 100;
    const int crunched_budget = 40; /* 60% reduction in allowable downtime minutes */
    const size_t num_actions = 12;

    ContainmentAction actions[12];
    generate_containment_actions(actions, num_actions);

    MetricsTracker m_frac, m_dp, m_bt, m_bb_fifo, m_bb_lifo, m_bb_lc;
    MetricsTracker m_dij, m_bf, m_prim, m_kruskal, m_flow;

    /* 1. Containment Selection Solvers under SLA Crunch */
    metrics_init(&m_frac, "Fractional Knapsack (DPI)", "Greedy", num_actions);
    metrics_start(&m_frac);
    FractionalKnapsackResult fk = fractional_knapsack_dpi(actions, num_actions, (double)crunched_budget, &m_frac);
    metrics_stop(&m_frac);
    record_metric(&m_frac);

    metrics_init(&m_dp, "0/1 Knapsack Playbooks", "Dynamic Programming", num_actions);
    metrics_start(&m_dp);
    Knapsack01Result kp_dp = knapsack_01_dp(actions, num_actions, crunched_budget, &m_dp);
    metrics_stop(&m_dp);
    record_metric(&m_dp);

    metrics_init(&m_bt, "0/1 Knapsack Backtrack", "Backtracking", num_actions);
    metrics_start(&m_bt);
    KnapsackBacktrackResult kp_bt = knapsack_01_backtrack(actions, num_actions, crunched_budget, &m_bt);
    metrics_stop(&m_bt);
    record_metric(&m_bt);

    metrics_init(&m_bb_fifo, "0/1 Knapsack BB (FIFO)", "Branch & Bound", num_actions);
    metrics_start(&m_bb_fifo);
    KnapsackBBResult bb_fifo = knapsack_bb_fifo(actions, num_actions, crunched_budget, &m_bb_fifo);
    metrics_stop(&m_bb_fifo);
    record_metric(&m_bb_fifo);

    metrics_init(&m_bb_lifo, "0/1 Knapsack BB (LIFO)", "Branch & Bound", num_actions);
    metrics_start(&m_bb_lifo);
    KnapsackBBResult bb_lifo = knapsack_bb_lifo(actions, num_actions, crunched_budget, &m_bb_lifo);
    metrics_stop(&m_bb_lifo);
    record_metric(&m_bb_lifo);

    metrics_init(&m_bb_lc, "0/1 Knapsack BB (LC/PQ)", "Branch & Bound", num_actions);
    metrics_start(&m_bb_lc);
    KnapsackBBResult bb_lc = knapsack_bb_lc(actions, num_actions, crunched_budget, &m_bb_lc);
    metrics_stop(&m_bb_lc);
    record_metric(&m_bb_lc);

    /* 2. Shortest Attack Path: Dijkstra vs Bellman-Ford */
    AttackGraph net;
    generate_negative_weight_graph(&net, 10, 0);

    metrics_init(&m_dij, "Dijkstra Attack Path", "Greedy", 10);
    metrics_start(&m_dij);
    DijkstraResult dij = dijkstra_attack_path(&net, 0, 9, &m_dij);
    metrics_stop(&m_dij);
    record_metric(&m_dij);

    metrics_init(&m_bf, "Bellman-Ford Escalation", "Dynamic Programming", 10);
    metrics_start(&m_bf);
    BellmanFordResult bf = bellman_ford_escalation(&net, 0, &m_bf);
    metrics_stop(&m_bf);
    record_metric(&m_bf);

    /* 3. Out-of-Band Quarantine Spanning Tree: Prim vs Kruskal */
    AttackGraph sw_graph;
    generate_attack_graph(&sw_graph, 8, 0.6, 912);

    metrics_init(&m_prim, "Prim Quarantine MST", "Greedy", 8);
    metrics_start(&m_prim);
    MSTResult prim = prim_quarantine_mst(&sw_graph, &m_prim);
    metrics_stop(&m_prim);
    record_metric(&m_prim);

    metrics_init(&m_kruskal, "Kruskal Quarantine MST", "Greedy", 8);
    metrics_start(&m_kruskal);
    MSTResult kruskal = kruskal_quarantine_mst(&sw_graph, &m_kruskal);
    metrics_stop(&m_kruskal);
    record_metric(&m_kruskal);

    /* 4. Network Flow & Min-Cut Exfiltration Severing */
    AttackGraph flow_net;
    generate_flow_network(&flow_net, 10, 0, 9);

    metrics_init(&m_flow, "Ford-Fulkerson Max Flow", "Network Flow", 10);
    metrics_start(&m_flow);
    FlowResult flow_res = ford_fulkerson_max_flow(&flow_net, 0, 9, &m_flow);
    metrics_stop(&m_flow);
    record_metric(&m_flow);

    metrics_print_table_header();
    metrics_print_row(&m_frac);
    metrics_print_row(&m_dp);
    metrics_print_row(&m_bt);
    metrics_print_row(&m_bb_fifo);
    metrics_print_row(&m_bb_lifo);
    metrics_print_row(&m_bb_lc);
    metrics_print_row(&m_dij);
    metrics_print_row(&m_bf);
    metrics_print_row(&m_prim);
    metrics_print_row(&m_kruskal);
    metrics_print_row(&m_flow);
    printf("+------------------------------+------------------+----------+--------------+--------------+------------+------------+------------+--------------+\n");

    printf("\n[+] Verification Signals:\n");
    printf("    Downtime Budget Crunched from %d mins -> %d mins\n", total_budget, crunched_budget);
    printf("    Risk Mitigated: Fractional=%.1f, DP=%d, Backtracking=%d, LC-BB=%d\n",
           fk.total_risk_mitigated, kp_dp.max_risk_mitigated, kp_bt.max_value, bb_lc.max_value);
    printf("    Branch-and-Bound Nodes Pruned: FIFO=%llu, LIFO=%llu, LC=%llu\n",
           (unsigned long long)bb_fifo.nodes_pruned, (unsigned long long)bb_lifo.nodes_pruned, (unsigned long long)bb_lc.nodes_pruned);
    printf("    Shortest Exploit Cost to Host 9: Dijkstra=%d, Bellman-Ford=%d (NegCycle=%d)\n",
           dij.dist[9], bf.dist[9], bf.has_negative_cycle);
    printf("    Quarantine MST Total Cable Cost: Prim=%d, Kruskal=%d\n", prim.total_weight, kruskal.total_weight);
    printf("    Exfiltration Max Flow: %d MB/s. Firewall Min-Cut Links to Sever: %d\n",
           flow_res.max_flow, flow_res.num_mincut_edges);
}

/* ========================================================================= */
/* SCENARIO 3: LARGE-DATA STRESS & ADVERSARIAL CASES                         */
/* ========================================================================= */
void run_scenario_3_adversarial_stress(void) {
    printf("\n======================================================================\n");
    printf(" SCENARIO 3: LARGE-DATA STRESS & ADVERSARIAL BENCHMARK                \n");
    printf("======================================================================\n");

    /* 1. Scale Progression for Merge Sort vs Quick Sort */
    const size_t sizes[] = { 100, 2500, 10000 };
    for (int s = 0; s < 3; s++) {
        size_t n = sizes[s];
        EventLog *l1 = (EventLog *)malloc(n * sizeof(EventLog));
        EventLog *l2 = (EventLog *)malloc(n * sizeof(EventLog));
        generate_event_logs(l1, n, 888);
        memcpy(l2, l1, n * sizeof(EventLog));

        char name_buf1[64], name_buf2[64];
        snprintf(name_buf1, sizeof(name_buf1), "MergeSort (N=%zu)", n);
        snprintf(name_buf2, sizeof(name_buf2), "QuickSort-Rand (N=%zu)", n);

        MetricsTracker m1, m2;
        metrics_init(&m1, name_buf1, "Divide & Conquer", n);
        metrics_start(&m1);
        merge_sort(l1, n, &m1);
        metrics_stop(&m1);
        record_metric(&m1);

        metrics_init(&m2, name_buf2, "Divide & Conquer", n);
        metrics_start(&m2);
        quick_sort_randomized(l2, 0, (int)n - 1, &m2);
        metrics_stop(&m2);
        record_metric(&m2);

        if (s == 0) metrics_print_table_header();
        metrics_print_row(&m1);
        metrics_print_row(&m2);

        free(l1);
        free(l2);
    }

    /* 2. Pathological Adversarial Input for Deterministic Quick Sort */
    const size_t adv_n = 2000;
    EventLog *adv_logs_det = (EventLog *)malloc(adv_n * sizeof(EventLog));
    EventLog *adv_logs_merge = (EventLog *)malloc(adv_n * sizeof(EventLog));
    generate_adversarial_sorted_logs(adv_logs_det, adv_n);
    memcpy(adv_logs_merge, adv_logs_det, adv_n * sizeof(EventLog));

    MetricsTracker m_adv_det, m_adv_merge;
    metrics_init(&m_adv_det, "QuickSort Det (Sorted)", "Adversarial O(N^2)", adv_n);
    metrics_start(&m_adv_det);
    quick_sort_deterministic(adv_logs_det, 0, (int)adv_n - 1, &m_adv_det);
    metrics_stop(&m_adv_det);
    record_metric(&m_adv_det);

    metrics_init(&m_adv_merge, "MergeSort (Sorted)", "Stable O(N log N)", adv_n);
    metrics_start(&m_adv_merge);
    merge_sort(adv_logs_merge, adv_n, &m_adv_merge);
    metrics_stop(&m_adv_merge);
    record_metric(&m_adv_merge);

    metrics_print_row(&m_adv_det);
    metrics_print_row(&m_adv_merge);

    free(adv_logs_det);
    free(adv_logs_merge);

    /* 3. Adversarial String Matching: Repetitive 'A' text */
    const size_t adv_str_len = 10000;
    char *adv_text = (char *)malloc(adv_str_len);
    const char *adv_pat = "AAAAAAAAB";
    generate_adversarial_string(adv_text, adv_str_len, adv_pat);

    MetricsTracker m_sn, m_skmp;
    metrics_init(&m_sn, "Naive Match (Adversarial)", "String Matching", adv_str_len);
    metrics_start(&m_sn);
    strmatch_naive(adv_text, adv_pat, &m_sn);
    metrics_stop(&m_sn);
    record_metric(&m_sn);

    metrics_init(&m_skmp, "KMP Match (Adversarial)", "String Matching", adv_str_len);
    metrics_start(&m_skmp);
    strmatch_kmp(adv_text, adv_pat, &m_skmp);
    metrics_stop(&m_skmp);
    record_metric(&m_skmp);

    metrics_print_row(&m_sn);
    metrics_print_row(&m_skmp);
    free(adv_text);

    /* 4. Classical vs Strassen on 16x16 Matrix */
    int matA[MAX_HOSTS][MAX_HOSTS], matB[MAX_HOSTS][MAX_HOSTS], matC1[MAX_HOSTS][MAX_HOSTS], matC2[MAX_HOSTS][MAX_HOSTS];
    for (int i = 0; i < 16; i++) {
        for (int j = 0; j < 16; j++) {
            matA[i][j] = (i + j) % 7;
            matB[i][j] = (i * j + 1) % 5;
        }
    }
    MetricsTracker m_mc, m_ms;
    metrics_init(&m_mc, "Classical Matrix 16x16", "Classical O(N^3)", 16);
    metrics_start(&m_mc);
    matrix_mult_classical(16, matA, matB, matC1, &m_mc);
    metrics_stop(&m_mc);
    record_metric(&m_mc);

    metrics_init(&m_ms, "Strassen Matrix 16x16", "Divide & Conquer", 16);
    metrics_start(&m_ms);
    matrix_mult_strassen(16, matA, matB, matC2, &m_ms);
    metrics_stop(&m_ms);
    record_metric(&m_ms);

    metrics_print_row(&m_mc);
    metrics_print_row(&m_ms);

    /* 5. TSP: Held-Karp Bitmask DP vs Least-Cost Branch-and-Bound */
    AttackGraph tsp_g;
    tsp_g.num_hosts = 12;
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            tsp_g.adj_weight[i][j] = (i == j) ? 0 : (abs(i - j) * 7 + (i * 3 + j * 5) % 19 + 5);
        }
    }

    MetricsTracker m_tsp_dp, m_tsp_bb;
    metrics_init(&m_tsp_dp, "TSP Held-Karp DP (N=12)", "Dynamic Programming", 12);
    metrics_start(&m_tsp_dp);
    TSPResult r_dp = tsp_held_karp_dp(&tsp_g, 12, &m_tsp_dp);
    metrics_stop(&m_tsp_dp);
    record_metric(&m_tsp_dp);

    metrics_init(&m_tsp_bb, "TSP LC-BB (N=12)", "Branch & Bound", 12);
    metrics_start(&m_tsp_bb);
    TSPBBResult r_bb = tsp_bb_lc(&tsp_g, 12, &m_tsp_bb);
    metrics_stop(&m_tsp_bb);
    record_metric(&m_tsp_bb);

    metrics_print_row(&m_tsp_dp);
    metrics_print_row(&m_tsp_bb);
    printf("+------------------------------+------------------+----------+--------------+--------------+------------+------------+------------+--------------+\n");

    printf("\n[+] Verification Signals:\n");
    printf("    Adversarial Sorted Log Comparisons: QuickSort Det=%llu vs MergeSort=%llu\n",
           (unsigned long long)m_adv_det.comparisons, (unsigned long long)m_adv_merge.comparisons);
    printf("    Adversarial String Comparisons: Naive=%llu vs KMP=%llu\n",
           (unsigned long long)m_sn.comparisons, (unsigned long long)m_skmp.comparisons);
    printf("    TSP Tour Cost: Held-Karp DP=%d, Least-Cost BB=%d\n", r_dp.min_tour_cost, r_bb.min_tour_cost);
}

/* ========================================================================= */
/* UNIT LAB RUNNERS                                                          */
/* ========================================================================= */
void run_unit2_lab(void) {
    printf("\n[+] Running Unit II Lab Evaluation...\n");
    EventLog logs[20];
    generate_event_logs(logs, 20, 123);
    MetricsTracker m;
    metrics_init(&m, "Unit2 Lab", "D&C", 20);
    merge_sort(logs, 20, &m);
    SubarrayResult sub = max_subarray_kadane(logs, 20, &m);
    printf("    Logs sorted. Peak anomaly burst detected: Sum=%d (from log #%d to #%d)\n",
           sub.max_sum, sub.start_index, sub.end_index);
}

void run_unit3_lab(void) {
    printf("\n[+] Running Unit III Lab Evaluation...\n");
    MetricsTracker m;
    metrics_init(&m, "Unit3 Lab", "Greedy", 10);
    const char *text = "CRITICAL_INTRUSION_DETECTED_HOST_5";
    HuffmanResult huff = huffman_compress_logs(text, &m);
    printf("    Forensic log compressed from %zu bytes -> %zu bits (Compression ratio: %.2fx)\n",
           huff.original_bytes, huff.compressed_bits, (double)(huff.original_bytes * 8) / (double)huff.compressed_bits);
    huffman_free_tree(huff.root);
}

void run_unit4_lab(void) {
    printf("\n[+] Running Unit IV Lab Evaluation...\n");
    MetricsTracker m;
    metrics_init(&m, "Unit4 Lab", "DP", 4);
    int dims[5] = {10, 100, 5, 50, 20};
    MatrixChainResult mcm = matrix_chain_order_dp(dims, 5, &m);
    printf("    Telemetry Matrix Chain Multiplications: %d ops. Optimal Parens: %s\n",
           mcm.min_scalar_multiplications, mcm.optimal_parens);
}

void run_unit5_lab(void) {
    printf("\n[+] Running Unit V Lab Evaluation...\n");
    MetricsTracker m;
    metrics_init(&m, "Unit5 Lab", "Backtracking", 8);
    NQueensResult nq = n_queens_honeypots(8, &m);
    printf("    Honeypot Sensor Grid (8x8): %d total non-interfering placements found.\n", nq.total_solutions);
}

void run_unit6_lab(void) {
    printf("\n[+] Running Unit VI Lab Evaluation...\n");
    MetricsTracker m;
    metrics_init(&m, "Unit6 Lab", "Flow/CRT", 4);
    int64_t rems[3], mods[3];
    uint64_t true_counter = 459128ULL;
    generate_crt_telemetry_system(3, true_counter, rems, mods);
    CRTResult crt = crt_reconstruct_telemetry(3, rems, mods, &m);
    printf("    Distributed Packet Counter Reconstruction: True=%llu, Reconstructed=%lld (Success=%d)\n",
           (unsigned long long)true_counter, (long long)crt.reconstructed_counter, crt.success);
}

static void print_banner(void) {
    printf("======================================================================\n");
    printf("  CSEG3053 DESIGN & ANALYSIS OF ALGORITHMS - PROJECT 03               \n");
    printf("  Cybersecurity Log Threat Detection & Algorithmic SOC Engine         \n");
    printf("  Standard: Pure C17 (-std=c17 -Wall -Wextra -O2)                     \n");
    printf("======================================================================\n");
}

int main(int argc, char *argv[]) {
    print_banner();

    if (argc > 1) {
        if (strcmp(argv[1], "--run-all-demos") == 0) {
            printf("[*] Non-interactive execution: Running all demonstration scenarios...\n");
            run_scenario_1_normal_soc();
            run_scenario_2_ransomware_shock();
            run_scenario_3_adversarial_stress();
            export_all_metrics();
            return 0;
        } else if (strcmp(argv[1], "--scenario1") == 0) {
            run_scenario_1_normal_soc();
            export_all_metrics();
            return 0;
        } else if (strcmp(argv[1], "--scenario2") == 0) {
            run_scenario_2_ransomware_shock();
            export_all_metrics();
            return 0;
        } else if (strcmp(argv[1], "--scenario3") == 0) {
            run_scenario_3_adversarial_stress();
            export_all_metrics();
            return 0;
        } else if (strcmp(argv[1], "--unit2") == 0) {
            run_unit2_lab();
            return 0;
        } else if (strcmp(argv[1], "--unit3") == 0) {
            run_unit3_lab();
            return 0;
        } else if (strcmp(argv[1], "--unit4") == 0) {
            run_unit4_lab();
            return 0;
        } else if (strcmp(argv[1], "--unit5") == 0) {
            run_unit5_lab();
            return 0;
        } else if (strcmp(argv[1], "--unit6") == 0) {
            run_unit6_lab();
            return 0;
        } else {
            printf("Usage: %s [--run-all-demos | --scenario1 | --scenario2 | --scenario3 | --unit2 | --unit3 | --unit4 | --unit5 | --unit6]\n", argv[0]);
            return 1;
        }
    }

    int choice = 0;
    while (1) {
        printf("\n----------------------- INTERACTIVE MENU -----------------------\n");
        printf(" 1. Run Scenario 1: Normal SOC Operation (Baseline Triage)\n");
        printf(" 2. Run Scenario 2: Constraint Shock (Ransomware Outbreak & SLA)\n");
        printf(" 3. Run Scenario 3: Large-Data Stress & Adversarial Inputs\n");
        printf(" 4. Run All Scenarios & Export Empirical Benchmarks (CSV/JSON)\n");
        printf(" 5. Unit II Workbench: Divide and Conquer\n");
        printf(" 6. Unit III Workbench: Greedy Method\n");
        printf(" 7. Unit IV Workbench: Dynamic Programming\n");
        printf(" 8. Unit V Workbench: Backtracking and Branch & Bound\n");
        printf(" 9. Unit VI Workbench: Flow, CRT & String Matching\n");
        printf(" 0. Exit SOC Analytics Engine\n");
        printf("----------------------------------------------------------------\n");
        printf("Enter selection [0-9]: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: run_scenario_1_normal_soc(); break;
            case 2: run_scenario_2_ransomware_shock(); break;
            case 3: run_scenario_3_adversarial_stress(); break;
            case 4:
                run_scenario_1_normal_soc();
                run_scenario_2_ransomware_shock();
                run_scenario_3_adversarial_stress();
                export_all_metrics();
                break;
            case 5: run_unit2_lab(); break;
            case 6: run_unit3_lab(); break;
            case 7: run_unit4_lab(); break;
            case 8: run_unit5_lab(); break;
            case 9: run_unit6_lab(); break;
            case 0:
                printf("\nExiting SOC Analytics Engine. Goodbye!\n");
                return 0;
            default:
                printf("Invalid option. Please select 0-9.\n");
                break;
        }
    }

    return 0;
}
