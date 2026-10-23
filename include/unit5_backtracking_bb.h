#ifndef UNIT5_BACKTRACKING_BB_H
#define UNIT5_BACKTRACKING_BB_H

#include "domain.h"
#include "metrics.h"
#include <stddef.h>

/* 1. N-Queens Honeypots Placement */
typedef struct {
    int total_solutions;
    int board_size;
    int board[MAX_HOSTS][MAX_HOSTS];
} NQueensResult;

NQueensResult n_queens_honeypots(int n, MetricsTracker *m);

/* 2. Sum of Subsets Micro-Alert Correlation */
typedef struct {
    int total_subsets_found;
    int max_solutions_stored;
    int subset_lengths[64];
    int subsets[64][MAX_HOSTS];
} SumOfSubsetsResult;

SumOfSubsetsResult sum_of_subsets_alerts(const int *alert_weights, int n, int target_sum, MetricsTracker *m);

/* 3. 0/1 Knapsack by Backtracking (DFS with Fractional Upper Bound) */
typedef struct {
    int max_value;
    int total_weight;
    int best_selection[MAX_HOSTS];
    uint64_t nodes_explored;
} KnapsackBacktrackResult;

KnapsackBacktrackResult knapsack_01_backtrack(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m);

/* 4. 0/1 Knapsack Branch & Bound Variants (FIFO, LIFO, Least-Cost) */
typedef struct {
    int max_value;
    int total_weight;
    int best_selection[MAX_HOSTS];
    uint64_t nodes_generated;
    uint64_t nodes_pruned;
} KnapsackBBResult;

KnapsackBBResult knapsack_bb_fifo(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m);
KnapsackBBResult knapsack_bb_lifo(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m);
KnapsackBBResult knapsack_bb_lc(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m);

/* 5. TSP Least-Cost Branch & Bound */
typedef struct {
    int min_tour_cost;
    int tour_length;
    int tour_nodes[MAX_HOSTS];
    uint64_t nodes_generated;
    uint64_t nodes_pruned;
} TSPBBResult;

TSPBBResult tsp_bb_lc(const AttackGraph *graph, int n, MetricsTracker *m);

#endif /* UNIT5_BACKTRACKING_BB_H */
