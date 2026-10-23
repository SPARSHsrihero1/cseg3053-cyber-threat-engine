#ifndef UNIT2_DIVIDE_CONQUER_H
#define UNIT2_DIVIDE_CONQUER_H

#include "domain.h"
#include "metrics.h"
#include <stdint.h>
#include <stddef.h>

/* BST Node for Lab Requirement */
typedef struct BSTNode {
    int key;
    ThreatSignature sig;
    struct BSTNode *left;
    struct BSTNode *right;
} BSTNode;

/* Maximum Subarray Result */
typedef struct {
    int max_sum;
    int start_index;
    int end_index;
} SubarrayResult;

/* 1. Binary Search (Iterative & Recursive) */
int binary_search_iterative(const EventLog *logs, size_t n, uint64_t target_timestamp, MetricsTracker *m);
int binary_search_recursive(const EventLog *logs, int low, int high, uint64_t target_timestamp, MetricsTracker *m);

/* BST Search (Iterative & Recursive) */
BSTNode *bst_insert(BSTNode *root, ThreatSignature sig, MetricsTracker *m);
BSTNode *bst_search_iterative(BSTNode *root, int sig_id, MetricsTracker *m);
BSTNode *bst_search_recursive(BSTNode *root, int sig_id, MetricsTracker *m);
void bst_free(BSTNode *root);

/* 2. Merge Sort */
void merge_sort(EventLog *logs, size_t n, MetricsTracker *m);

/* 3. Quick Sort (Deterministic & Randomized) */
void quick_sort_deterministic(EventLog *logs, int low, int high, MetricsTracker *m);
void quick_sort_randomized(EventLog *logs, int low, int high, MetricsTracker *m);

/* 4. Maximum Subarray (Divide-and-Conquer & Kadane) */
SubarrayResult max_subarray_dc(const EventLog *logs, int low, int high, MetricsTracker *m);
SubarrayResult max_subarray_kadane(const EventLog *logs, size_t n, MetricsTracker *m);

/* 5. Fast Exponentiation (Modular Power) */
uint64_t fast_power_mod_recursive(uint64_t base, uint64_t exp, uint64_t mod, MetricsTracker *m);
uint64_t fast_power_mod_iterative(uint64_t base, uint64_t exp, uint64_t mod, MetricsTracker *m);

/* 6. Celebrity Problem (C2 Command-and-Control Sinkhole Detection) */
int find_celebrity_c2(int n, const int comm_matrix[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m);

/* 7. Matrix Multiplication (Classical vs. Strassen) */
void matrix_mult_classical(int n, const int A[MAX_HOSTS][MAX_HOSTS], const int B[MAX_HOSTS][MAX_HOSTS], int C[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m);
void matrix_mult_strassen(int n, const int A[MAX_HOSTS][MAX_HOSTS], const int B[MAX_HOSTS][MAX_HOSTS], int C[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m);

#endif /* UNIT2_DIVIDE_CONQUER_H */
