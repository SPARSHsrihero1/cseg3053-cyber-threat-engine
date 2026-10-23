#ifndef UNIT4_DP_H
#define UNIT4_DP_H

#include "domain.h"
#include "metrics.h"
#include <stddef.h>

/* 1. 0/1 Knapsack DP */
typedef struct {
    int max_risk_mitigated;
    int total_cost;
    int num_selected;
    int selected_ids[MAX_HOSTS];
} Knapsack01Result;

Knapsack01Result knapsack_01_dp(const ContainmentAction *actions, size_t n, int budget, MetricsTracker *m);

/* 2. Matrix Chain Multiplication DP */
typedef struct {
    int min_scalar_multiplications;
    char optimal_parens[256];
} MatrixChainResult;

MatrixChainResult matrix_chain_order_dp(const int *dims, int n, MetricsTracker *m);

/* 3. Longest Common Subsequence (LCS) Attack Correlation */
typedef struct {
    int lcs_length;
    char matched_sequence[MAX_PAYLOAD_LEN];
} LCSResult;

LCSResult lcs_attack_correlation(const char *observed_events, const char *killchain_pattern, MetricsTracker *m);

/* 4. Optimal Binary Search Tree (OBST) */
typedef struct {
    double min_expected_cost;
    int root_table[MAX_HOSTS][MAX_HOSTS];
} OBSTResult;

OBSTResult obst_signature_index(const ThreatSignature *sigs, int n, MetricsTracker *m);

/* 5. Bellman-Ford Shortest Path with Negative Cycle Detection */
typedef struct {
    int dist[MAX_HOSTS];
    int parent[MAX_HOSTS];
    int has_negative_cycle;
} BellmanFordResult;

BellmanFordResult bellman_ford_escalation(const AttackGraph *graph, int source, MetricsTracker *m);

/* 6. Floyd-Warshall All-Pairs Exposure Matrix */
typedef struct {
    int dist[MAX_HOSTS][MAX_HOSTS];
    int next_hop[MAX_HOSTS][MAX_HOSTS];
} FloydWarshallResult;

FloydWarshallResult floyd_warshall_exposure(const AttackGraph *graph, MetricsTracker *m);

/* 7. Travelling Salesperson Problem (TSP) Held-Karp Bitmask DP */
typedef struct {
    int min_tour_cost;
    int tour_length;
    int tour_nodes[MAX_HOSTS];
} TSPResult;

TSPResult tsp_held_karp_dp(const AttackGraph *graph, int n, MetricsTracker *m);

#endif /* UNIT4_DP_H */
