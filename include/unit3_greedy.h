#ifndef UNIT3_GREEDY_H
#define UNIT3_GREEDY_H

#include "domain.h"
#include "metrics.h"
#include <stddef.h>

/* Activity Selection / Interval Partitioning */
typedef struct {
    int count;
    int selected_ids[MAX_HOSTS];
} ActivityResult;

typedef struct {
    int total_sandboxes;
    int sandbox_assignment[MAX_HOSTS];
} PartitionResult;

ActivityResult activity_selection_scans(const ContainmentAction *actions, size_t n, MetricsTracker *m);
PartitionResult interval_partition_sandboxes(const ContainmentAction *actions, size_t n, MetricsTracker *m);

/* Fractional Knapsack (DPI Bandwidth Allocation) */
typedef struct {
    double total_risk_mitigated;
    double fractions[MAX_HOSTS];
} FractionalKnapsackResult;

FractionalKnapsackResult fractional_knapsack_dpi(const ContainmentAction *actions, size_t n, double capacity, MetricsTracker *m);

/* Huffman Coding */
typedef struct HuffmanNode {
    unsigned char ch;
    uint32_t freq;
    struct HuffmanNode *left;
    struct HuffmanNode *right;
} HuffmanNode;

typedef struct {
    char bit_string[MAX_PAYLOAD_LEN * 8];
    char code_table[256][64];
    HuffmanNode *root;
    size_t original_bytes;
    size_t compressed_bits;
} HuffmanResult;

HuffmanResult huffman_compress_logs(const char *input_text, MetricsTracker *m);
void huffman_decompress_logs(const HuffmanResult *huff, char *output_text, size_t max_out_len, MetricsTracker *m);
void huffman_free_tree(HuffmanNode *root);

/* Dijkstra's Single-Source Shortest Attack Path */
typedef struct {
    int dist[MAX_HOSTS];
    int parent[MAX_HOSTS];
    int path_length;
    int path_nodes[MAX_HOSTS];
} DijkstraResult;

DijkstraResult dijkstra_attack_path(const AttackGraph *graph, int source, int target, MetricsTracker *m);

/* Prim & Kruskal Minimum Spanning Tree */
typedef struct {
    int total_weight;
    int num_edges;
    NetworkEdge edges[MAX_HOSTS * MAX_HOSTS];
} MSTResult;

MSTResult prim_quarantine_mst(const AttackGraph *graph, MetricsTracker *m);
MSTResult kruskal_quarantine_mst(const AttackGraph *graph, MetricsTracker *m);

/* Disjoint Set Union (DSU) for Kruskal & Network Partitioning */
typedef struct {
    int parent[MAX_HOSTS];
    int rank[MAX_HOSTS];
    int count;
} DisjointSet;

void dsu_init(DisjointSet *dsu, int n);
int dsu_find(DisjointSet *dsu, int i);
int dsu_union(DisjointSet *dsu, int i, int j);

#endif /* UNIT3_GREEDY_H */
