#include "unit3_greedy.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* --- Custom Sorting Helpers (Zero qsort shortcut) --- */

static void sort_actions_by_endtime(ContainmentAction *arr, int n, MetricsTracker *m) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (m) m->comparisons++;
            if (arr[j].end_time > arr[j + 1].end_time) {
                ContainmentAction tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
                if (m) m->swaps_or_writes += 2;
            }
        }
    }
}

static void sort_actions_by_starttime(ContainmentAction *arr, int *orig_indices, int n, MetricsTracker *m) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (m) m->comparisons++;
            if (arr[j].start_time > arr[j + 1].start_time) {
                ContainmentAction tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;

                int tmp_idx = orig_indices[j];
                orig_indices[j] = orig_indices[j + 1];
                orig_indices[j + 1] = tmp_idx;

                if (m) m->swaps_or_writes += 4;
            }
        }
    }
}

/* 1. Activity Selection */
ActivityResult activity_selection_scans(const ContainmentAction *actions, size_t n, MetricsTracker *m) {
    ActivityResult res;
    res.count = 0;
    if (!actions || n == 0) return res;

    int count = (int)((n > MAX_HOSTS) ? MAX_HOSTS : n);
    ContainmentAction copy[MAX_HOSTS];
    for (int i = 0; i < count; i++) {
        copy[i] = actions[i];
    }

    sort_actions_by_endtime(copy, count, m);

    res.selected_ids[res.count++] = copy[0].action_id;
    int last_end = copy[0].end_time;

    for (int i = 1; i < count; i++) {
        if (m) m->comparisons++;
        if (copy[i].start_time >= last_end) {
            res.selected_ids[res.count++] = copy[i].action_id;
            last_end = copy[i].end_time;
            if (m) m->swaps_or_writes++;
        }
    }
    return res;
}

/* 2. Interval Partitioning (Min Sandboxes) */
PartitionResult interval_partition_sandboxes(const ContainmentAction *actions, size_t n, MetricsTracker *m) {
    PartitionResult res;
    res.total_sandboxes = 0;
    if (!actions || n == 0) return res;

    int count = (int)((n > MAX_HOSTS) ? MAX_HOSTS : n);
    ContainmentAction copy[MAX_HOSTS];
    int orig_indices[MAX_HOSTS];

    for (int i = 0; i < count; i++) {
        copy[i] = actions[i];
        orig_indices[i] = i;
        res.sandbox_assignment[i] = -1;
    }

    sort_actions_by_starttime(copy, orig_indices, count, m);

    int sandbox_end_times[MAX_HOSTS];

    for (int i = 0; i < count; i++) {
        int assigned = -1;
        /* Look for an available sandbox */
        for (int s = 0; s < res.total_sandboxes; s++) {
            if (m) m->comparisons++;
            if (sandbox_end_times[s] <= copy[i].start_time) {
                assigned = s;
                sandbox_end_times[s] = copy[i].end_time;
                break;
            }
        }
        /* If no existing sandbox is free, allocate a new one */
        if (assigned == -1) {
            assigned = res.total_sandboxes;
            sandbox_end_times[res.total_sandboxes++] = copy[i].end_time;
        }

        res.sandbox_assignment[orig_indices[i]] = assigned;
        if (m) m->swaps_or_writes++;
    }

    return res;
}

/* 3. Fractional Knapsack (DPI Bandwidth Allocation) */
FractionalKnapsackResult fractional_knapsack_dpi(const ContainmentAction *actions, size_t n, double capacity, MetricsTracker *m) {
    FractionalKnapsackResult res;
    res.total_risk_mitigated = 0.0;
    for (size_t i = 0; i < MAX_HOSTS; i++) res.fractions[i] = 0.0;
    if (!actions || n == 0 || capacity <= 0.0) return res;

    size_t count = (n > MAX_HOSTS) ? MAX_HOSTS : n;
    int indices[MAX_HOSTS];
    double ratios[MAX_HOSTS];

    for (size_t i = 0; i < count; i++) {
        indices[i] = (int)i;
        ratios[i] = (actions[i].disruption_cost > 0) ?
            ((double)actions[i].risk_mitigated / (double)actions[i].disruption_cost) : 0.0;
    }

    /* Sort descending by ratio */
    for (size_t i = 0; i < count - 1; i++) {
        for (size_t j = 0; j < count - i - 1; j++) {
            if (m) m->comparisons++;
            if (ratios[j] < ratios[j + 1]) {
                double tr = ratios[j]; ratios[j] = ratios[j + 1]; ratios[j + 1] = tr;
                int ti = indices[j]; indices[j] = indices[j + 1]; indices[j + 1] = ti;
                if (m) m->swaps_or_writes += 4;
            }
        }
    }

    double remaining_cap = capacity;
    for (size_t i = 0; i < count; i++) {
        int idx = indices[i];
        double weight = (double)actions[idx].disruption_cost;
        double value = (double)actions[idx].risk_mitigated;

        if (remaining_cap <= 0.0) break;

        if (m) m->comparisons++;
        if (weight <= remaining_cap) {
            res.fractions[idx] = 1.0;
            res.total_risk_mitigated += value;
            remaining_cap -= weight;
            if (m) m->swaps_or_writes++;
        } else {
            double frac = remaining_cap / weight;
            res.fractions[idx] = frac;
            res.total_risk_mitigated += frac * value;
            remaining_cap = 0.0;
            if (m) m->swaps_or_writes++;
            break;
        }
    }

    return res;
}

/* 4. Huffman Coding */
typedef struct {
    HuffmanNode *items[512];
    int size;
} HuffmanMinHeap;

static void heap_push(HuffmanMinHeap *h, HuffmanNode *node, MetricsTracker *m) {
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (m) m->comparisons++;
        if (h->items[p]->freq <= node->freq) break;
        h->items[i] = h->items[p];
        i = p;
        if (m) m->swaps_or_writes++;
    }
    h->items[i] = node;
    if (m) m->swaps_or_writes++;
}

static HuffmanNode *heap_pop(HuffmanMinHeap *h, MetricsTracker *m) {
    if (h->size == 0) return NULL;
    HuffmanNode *top = h->items[0];
    HuffmanNode *last = h->items[--h->size];
    if (h->size > 0) {
        int i = 0;
        while (i * 2 + 1 < h->size) {
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            int smallest = left;
            if (right < h->size) {
                if (m) m->comparisons++;
                if (h->items[right]->freq < h->items[left]->freq) {
                    smallest = right;
                }
            }
            if (m) m->comparisons++;
            if (last->freq <= h->items[smallest]->freq) break;
            h->items[i] = h->items[smallest];
            i = smallest;
            if (m) m->swaps_or_writes++;
        }
        h->items[i] = last;
        if (m) m->swaps_or_writes++;
    }
    return top;
}

static void build_huffman_codes(HuffmanNode *root, char *current_code, int depth, char code_table[256][64], MetricsTracker *m) {
    if (!root) return;
    if (m) m->recursive_calls++;

    if (!root->left && !root->right) {
        current_code[depth] = '\0';
        strncpy(code_table[root->ch], current_code, 63);
        code_table[root->ch][63] = '\0';
        if (m) m->swaps_or_writes++;
        return;
    }

    if (root->left) {
        current_code[depth] = '0';
        build_huffman_codes(root->left, current_code, depth + 1, code_table, m);
    }
    if (root->right) {
        current_code[depth] = '1';
        build_huffman_codes(root->right, current_code, depth + 1, code_table, m);
    }
}

HuffmanResult huffman_compress_logs(const char *input_text, MetricsTracker *m) {
    HuffmanResult res;
    memset(&res, 0, sizeof(res));
    if (!input_text || strlen(input_text) == 0) return res;

    res.original_bytes = strlen(input_text);

    uint32_t freq[256] = {0};
    for (size_t i = 0; i < res.original_bytes; i++) {
        freq[(unsigned char)input_text[i]]++;
    }

    HuffmanMinHeap heap;
    heap.size = 0;

    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            HuffmanNode *node = (HuffmanNode *)tracked_malloc(sizeof(HuffmanNode), m);
            node->ch = (unsigned char)i;
            node->freq = freq[i];
            node->left = NULL;
            node->right = NULL;
            heap_push(&heap, node, m);
        }
    }

    if (heap.size == 1) {
        /* Single distinct char edge case */
        HuffmanNode *single = heap_pop(&heap, m);
        HuffmanNode *parent = (HuffmanNode *)tracked_malloc(sizeof(HuffmanNode), m);
        parent->ch = 0;
        parent->freq = single->freq;
        parent->left = single;
        parent->right = NULL;
        heap_push(&heap, parent, m);
    }

    while (heap.size > 1) {
        HuffmanNode *n1 = heap_pop(&heap, m);
        HuffmanNode *n2 = heap_pop(&heap, m);

        HuffmanNode *parent = (HuffmanNode *)tracked_malloc(sizeof(HuffmanNode), m);
        parent->ch = 0;
        parent->freq = n1->freq + n2->freq;
        parent->left = n1;
        parent->right = n2;

        heap_push(&heap, parent, m);
    }

    res.root = heap_pop(&heap, m);

    char code_buf[64];
    build_huffman_codes(res.root, code_buf, 0, res.code_table, m);

    size_t bit_pos = 0;
    for (size_t i = 0; i < res.original_bytes; i++) {
        const char *c = res.code_table[(unsigned char)input_text[i]];
        while (*c && bit_pos < sizeof(res.bit_string) - 1) {
            res.bit_string[bit_pos++] = *c++;
            if (m) m->swaps_or_writes++;
        }
    }
    res.bit_string[bit_pos] = '\0';
    res.compressed_bits = bit_pos;

    return res;
}

void huffman_decompress_logs(const HuffmanResult *huff, char *output_text, size_t max_out_len, MetricsTracker *m) {
    if (!huff || !huff->root || !output_text || max_out_len == 0) return;

    size_t out_idx = 0;
    HuffmanNode *curr = huff->root;

    for (size_t i = 0; i < huff->compressed_bits && out_idx < max_out_len - 1; i++) {
        char bit = huff->bit_string[i];
        if (m) m->comparisons++;

        if (bit == '0') {
            curr = curr->left;
        } else {
            curr = curr->right;
        }

        if (curr && !curr->left && !curr->right) {
            output_text[out_idx++] = (char)curr->ch;
            if (m) m->swaps_or_writes++;
            curr = huff->root;
        }
    }
    output_text[out_idx] = '\0';
}

void huffman_free_tree(HuffmanNode *root) {
    if (!root) return;
    huffman_free_tree(root->left);
    huffman_free_tree(root->right);
    free(root);
}

/* 5. Dijkstra's Algorithm */
typedef struct {
    int u;
    int dist;
} DijHeapItem;

typedef struct {
    DijHeapItem data[MAX_HOSTS * MAX_HOSTS];
    int size;
} DijMinHeap;

static void dij_push(DijMinHeap *h, int u, int dist) {
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].dist <= dist) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i] = (DijHeapItem){u, dist};
}

static DijHeapItem dij_pop(DijMinHeap *h) {
    DijHeapItem top = h->data[0];
    DijHeapItem last = h->data[--h->size];
    if (h->size > 0) {
        int i = 0;
        while (i * 2 + 1 < h->size) {
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            int smallest = left;
            if (right < h->size && h->data[right].dist < h->data[left].dist) {
                smallest = right;
            }
            if (last.dist <= h->data[smallest].dist) break;
            h->data[i] = h->data[smallest];
            i = smallest;
        }
        h->data[i] = last;
    }
    return top;
}

DijkstraResult dijkstra_attack_path(const AttackGraph *graph, int source, int target, MetricsTracker *m) {
    DijkstraResult res;
    res.path_length = 0;
    if (!graph || source < 0 || source >= graph->num_hosts) return res;

    int n = graph->num_hosts;
    for (int i = 0; i < n; i++) {
        res.dist[i] = INF_COST;
        res.parent[i] = -1;
    }

    res.dist[source] = 0;

    DijMinHeap pq;
    pq.size = 0;
    dij_push(&pq, source, 0);

    while (pq.size > 0) {
        DijHeapItem item = dij_pop(&pq);
        int u = item.u;
        int d = item.dist;

        if (d > res.dist[u]) continue;

        for (int v = 0; v < n; v++) {
            int w = graph->adj_weight[u][v];
            if (w < INF_COST && u != v) {
                if (m) m->comparisons++;
                if (res.dist[u] + w < res.dist[v]) {
                    res.dist[v] = res.dist[u] + w;
                    res.parent[v] = u;
                    if (m) {
                        m->graph_relaxations++;
                        m->swaps_or_writes++;
                    }
                    dij_push(&pq, v, res.dist[v]);
                }
            }
        }
    }

    /* Path reconstruction */
    if (target >= 0 && target < n && res.dist[target] < INF_COST) {
        int temp[MAX_HOSTS];
        int count = 0;
        int curr = target;
        while (curr != -1) {
            temp[count++] = curr;
            curr = res.parent[curr];
        }
        for (int i = 0; i < count; i++) {
            res.path_nodes[i] = temp[count - 1 - i];
        }
        res.path_length = count;
    }

    return res;
}

/* 6. Prim & Kruskal MST */

MSTResult prim_quarantine_mst(const AttackGraph *graph, MetricsTracker *m) {
    MSTResult res;
    res.total_weight = 0;
    res.num_edges = 0;
    if (!graph || graph->num_hosts <= 0) return res;

    int n = graph->num_hosts;
    int in_mst[MAX_HOSTS] = {0};
    int key[MAX_HOSTS];
    int parent[MAX_HOSTS];

    for (int i = 0; i < n; i++) {
        key[i] = INF_COST;
        parent[i] = -1;
    }

    key[0] = 0;

    for (int count = 0; count < n; count++) {
        int min_key = INF_COST;
        int u = -1;

        for (int v = 0; v < n; v++) {
            if (!in_mst[v]) {
                if (m) m->comparisons++;
                if (key[v] < min_key) {
                    min_key = key[v];
                    u = v;
                }
            }
        }

        if (u == -1 || min_key == INF_COST) break;

        in_mst[u] = 1;
        if (parent[u] != -1) {
            res.edges[res.num_edges++] = (NetworkEdge){
                parent[u], u, graph->adj_weight[parent[u]][u], 0
            };
            res.total_weight += graph->adj_weight[parent[u]][u];
            if (m) m->swaps_or_writes++;
        }

        for (int v = 0; v < n; v++) {
            int w = graph->adj_weight[u][v];
            if (!in_mst[v] && w < INF_COST && u != v) {
                if (m) m->comparisons++;
                if (w < key[v]) {
                    key[v] = w;
                    parent[v] = u;
                    if (m) {
                        m->graph_relaxations++;
                        m->swaps_or_writes++;
                    }
                }
            }
        }
    }

    return res;
}

/* Disjoint Set Union (DSU) implementation */
void dsu_init(DisjointSet *dsu, int n) {
    if (!dsu) return;
    dsu->count = n;
    for (int i = 0; i < n; i++) {
        dsu->parent[i] = i;
        dsu->rank[i] = 0;
    }
}

int dsu_find(DisjointSet *dsu, int i) {
    if (dsu->parent[i] == i) return i;
    /* Path compression */
    dsu->parent[i] = dsu_find(dsu, dsu->parent[i]);
    return dsu->parent[i];
}

int dsu_union(DisjointSet *dsu, int i, int j) {
    int root_i = dsu_find(dsu, i);
    int root_j = dsu_find(dsu, j);
    if (root_i == root_j) return 0;

    /* Union by rank */
    if (dsu->rank[root_i] < dsu->rank[root_j]) {
        dsu->parent[root_i] = root_j;
    } else if (dsu->rank[root_i] > dsu->rank[root_j]) {
        dsu->parent[root_j] = root_i;
    } else {
        dsu->parent[root_j] = root_i;
        dsu->rank[root_i]++;
    }
    dsu->count--;
    return 1;
}

static void sort_edges_by_weight(NetworkEdge *edges, int n, MetricsTracker *m) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (m) m->comparisons++;
            if (edges[j].exploit_weight > edges[j + 1].exploit_weight) {
                NetworkEdge tmp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = tmp;
                if (m) m->swaps_or_writes += 2;
            }
        }
    }
}

MSTResult kruskal_quarantine_mst(const AttackGraph *graph, MetricsTracker *m) {
    MSTResult res;
    res.total_weight = 0;
    res.num_edges = 0;
    if (!graph || graph->num_hosts <= 0) return res;

    int n = graph->num_hosts;
    int edge_count = 0;
    NetworkEdge all_edges[MAX_HOSTS * MAX_HOSTS];

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int w = (graph->adj_weight[i][j] < graph->adj_weight[j][i]) ?
                     graph->adj_weight[i][j] : graph->adj_weight[j][i];
            if (w < INF_COST && edge_count < MAX_HOSTS * MAX_HOSTS) {
                all_edges[edge_count++] = (NetworkEdge){i, j, w, 0};
            }
        }
    }

    sort_edges_by_weight(all_edges, edge_count, m);

    DisjointSet dsu;
    dsu_init(&dsu, n);

    for (int i = 0; i < edge_count; i++) {
        int u = all_edges[i].u;
        int v = all_edges[i].v;

        if (m) m->comparisons++;
        if (dsu_find(&dsu, u) != dsu_find(&dsu, v)) {
            dsu_union(&dsu, u, v);
            res.edges[res.num_edges++] = all_edges[i];
            res.total_weight += all_edges[i].exploit_weight;
            if (m) m->swaps_or_writes++;

            if (res.num_edges == n - 1) break;
        }
    }

    return res;
}
