#include "unit5_backtracking_bb.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 1. N-Queens Honeypots Backtracking */
static void n_queens_solve(int row, int n, int *cols, int *diag1, int *diag2, int *queen_pos, NQueensResult *res, MetricsTracker *m) {
    if (m) m->recursive_calls++;

    if (row == n) {
        res->total_solutions++;
        if (res->total_solutions == 1) {
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    res->board[r][c] = (queen_pos[r] == c) ? 1 : 0;
                }
            }
        }
        return;
    }

    for (int col = 0; col < n; col++) {
        int d1 = row - col + (n - 1);
        int d2 = row + col;

        if (m) m->comparisons += 3;
        if (!cols[col] && !diag1[d1] && !diag2[d2]) {
            cols[col] = 1;
            diag1[d1] = 1;
            diag2[d2] = 1;
            queen_pos[row] = col;
            if (m) m->swaps_or_writes += 4;

            n_queens_solve(row + 1, n, cols, diag1, diag2, queen_pos, res, m);

            cols[col] = 0;
            diag1[d1] = 0;
            diag2[d2] = 0;
            if (m) m->swaps_or_writes += 3;
        } else {
            if (m) m->states_pruned++;
        }
    }
}

NQueensResult n_queens_honeypots(int n, MetricsTracker *m) {
    NQueensResult res;
    res.total_solutions = 0;
    res.board_size = n;
    memset(res.board, 0, sizeof(res.board));
    if (n <= 0 || n > MAX_HOSTS) return res;

    int cols[MAX_HOSTS] = {0};
    int diag1[2 * MAX_HOSTS] = {0};
    int diag2[2 * MAX_HOSTS] = {0};
    int queen_pos[MAX_HOSTS] = {0};

    n_queens_solve(0, n, cols, diag1, diag2, queen_pos, &res, m);
    return res;
}

/* 2. Sum of Subsets */
static void subset_sum_rec(int idx, int curr_sum, int remaining_sum, int *chosen, int chosen_count,
                           const int *weights, int n, int target, SumOfSubsetsResult *res, MetricsTracker *m) {
    if (m) m->recursive_calls++;

    if (curr_sum == target) {
        if (res->total_subsets_found < 64) {
            int slot = res->total_subsets_found;
            res->subset_lengths[slot] = chosen_count;
            for (int i = 0; i < chosen_count; i++) {
                res->subsets[slot][i] = chosen[i];
            }
            if (m) m->swaps_or_writes += chosen_count;
        }
        res->total_subsets_found++;
        return;
    }

    if (idx >= n) return;

    /* Bounding condition: if adding weights[idx] exceeds target, or remaining can't reach target */
    if (m) m->comparisons += 2;
    if (curr_sum + weights[idx] > target || curr_sum + remaining_sum < target) {
        if (m) m->states_pruned++;
        return;
    }

    /* Option 1: Include weights[idx] */
    chosen[chosen_count] = weights[idx];
    subset_sum_rec(idx + 1, curr_sum + weights[idx], remaining_sum - weights[idx],
                   chosen, chosen_count + 1, weights, n, target, res, m);

    /* Option 2: Exclude weights[idx] */
    subset_sum_rec(idx + 1, curr_sum, remaining_sum - weights[idx],
                   chosen, chosen_count, weights, n, target, res, m);
}

SumOfSubsetsResult sum_of_subsets_alerts(const int *alert_weights, int n, int target_sum, MetricsTracker *m) {
    SumOfSubsetsResult res;
    res.total_subsets_found = 0;
    res.max_solutions_stored = 64;
    memset(res.subset_lengths, 0, sizeof(res.subset_lengths));
    if (!alert_weights || n <= 0 || target_sum <= 0) return res;

    int sorted_w[MAX_HOSTS];
    int count = (n > MAX_HOSTS) ? MAX_HOSTS : n;
    int total_sum = 0;

    for (int i = 0; i < count; i++) {
        sorted_w[i] = alert_weights[i];
        total_sum += alert_weights[i];
    }

    /* Sort ascending for bounding efficiency */
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (m) m->comparisons++;
            if (sorted_w[j] > sorted_w[j + 1]) {
                int tmp = sorted_w[j];
                sorted_w[j] = sorted_w[j + 1];
                sorted_w[j + 1] = tmp;
                if (m) m->swaps_or_writes += 2;
            }
        }
    }

    int chosen[MAX_HOSTS];
    subset_sum_rec(0, 0, total_sum, chosen, 0, sorted_w, count, target_sum, &res, m);

    return res;
}

/* 3. 0/1 Knapsack Backtracking with Fractional Upper Bound */
typedef struct {
    int id;
    int weight;
    int value;
    double ratio;
} SortedItem;

static double compute_bound(int idx, int curr_weight, int curr_val, int capacity, const SortedItem *items, int n, MetricsTracker *m) {
    if (curr_weight >= capacity) return 0.0;
    double bound = (double)curr_val;
    int remaining = capacity - curr_weight;

    for (int i = idx; i < n; i++) {
        if (m) m->comparisons++;
        if (items[i].weight <= remaining) {
            remaining -= items[i].weight;
            bound += (double)items[i].value;
        } else {
            bound += (double)items[i].value * ((double)remaining / (double)items[i].weight);
            break;
        }
    }
    return bound;
}

static void knapsack_backtrack_dfs(int idx, int curr_weight, int curr_val, int *curr_sel,
                                  const SortedItem *items, int n, int capacity,
                                  KnapsackBacktrackResult *res, MetricsTracker *m) {
    res->nodes_explored++;
    if (m) m->recursive_calls++;

    if (curr_val > res->max_value) {
        res->max_value = curr_val;
        res->total_weight = curr_weight;
        for (int i = 0; i < n; i++) {
            res->best_selection[i] = curr_sel[i];
        }
        if (m) m->swaps_or_writes += n;
    }

    if (idx >= n) return;

    /* Fractional upper bound check */
    double bound = compute_bound(idx, curr_weight, curr_val, capacity, items, n, m);
    if (m) m->comparisons++;
    if (bound <= (double)res->max_value) {
        if (m) m->states_pruned++;
        return;
    }

    /* Option 1: Include item if capacity allows */
    if (curr_weight + items[idx].weight <= capacity) {
        curr_sel[items[idx].id] = 1;
        knapsack_backtrack_dfs(idx + 1, curr_weight + items[idx].weight, curr_val + items[idx].value,
                               curr_sel, items, n, capacity, res, m);
        curr_sel[items[idx].id] = 0;
    } else {
        if (m) m->states_pruned++;
    }

    /* Option 2: Exclude item */
    knapsack_backtrack_dfs(idx + 1, curr_weight, curr_val, curr_sel, items, n, capacity, res, m);
}

KnapsackBacktrackResult knapsack_01_backtrack(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m) {
    KnapsackBacktrackResult res;
    res.max_value = 0;
    res.total_weight = 0;
    res.nodes_explored = 0;
    memset(res.best_selection, 0, sizeof(res.best_selection));
    if (!actions || n == 0 || capacity <= 0) return res;

    int count = (int)((n > MAX_HOSTS) ? MAX_HOSTS : n);
    SortedItem items[MAX_HOSTS];

    for (int i = 0; i < count; i++) {
        items[i].id = i;
        items[i].weight = actions[i].disruption_cost;
        items[i].value = actions[i].risk_mitigated;
        items[i].ratio = (items[i].weight > 0) ? ((double)items[i].value / (double)items[i].weight) : 0.0;
    }

    /* Sort descending by ratio */
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (m) m->comparisons++;
            if (items[j].ratio < items[j + 1].ratio) {
                SortedItem tmp = items[j];
                items[j] = items[j + 1];
                items[j + 1] = tmp;
                if (m) m->swaps_or_writes += 2;
            }
        }
    }

    int curr_sel[MAX_HOSTS] = {0};
    knapsack_backtrack_dfs(0, 0, 0, curr_sel, items, count, capacity, &res, m);

    return res;
}

/* 4. Branch & Bound Variants (FIFO, LIFO, LC) */
typedef struct {
    int level;
    int weight;
    int value;
    double bound;
    int selected[MAX_HOSTS];
} BBNode;

#define BB_MAX_QUEUE 65536

/* Helper: Prepare sorted items */
static int prepare_bb_items(const ContainmentAction *actions, size_t n, SortedItem *items, MetricsTracker *m) {
    int count = (int)((n > MAX_HOSTS) ? MAX_HOSTS : n);
    for (int i = 0; i < count; i++) {
        items[i].id = i;
        items[i].weight = actions[i].disruption_cost;
        items[i].value = actions[i].risk_mitigated;
        items[i].ratio = (items[i].weight > 0) ? ((double)items[i].value / (double)items[i].weight) : 0.0;
    }

    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (m) m->comparisons++;
            if (items[j].ratio < items[j + 1].ratio) {
                SortedItem tmp = items[j];
                items[j] = items[j + 1];
                items[j + 1] = tmp;
                if (m) m->swaps_or_writes += 2;
            }
        }
    }
    return count;
}

/* FIFO Branch & Bound */
KnapsackBBResult knapsack_bb_fifo(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m) {
    KnapsackBBResult res;
    res.max_value = 0;
    res.total_weight = 0;
    res.nodes_generated = 0;
    res.nodes_pruned = 0;
    memset(res.best_selection, 0, sizeof(res.best_selection));
    if (!actions || n == 0 || capacity <= 0) return res;

    SortedItem items[MAX_HOSTS];
    int count = prepare_bb_items(actions, n, items, m);

    BBNode *queue = (BBNode *)tracked_malloc(BB_MAX_QUEUE * sizeof(BBNode), m);
    if (!queue) return res;

    int head = 0, tail = 0;

    BBNode root;
    root.level = 0;
    root.weight = 0;
    root.value = 0;
    root.bound = compute_bound(0, 0, 0, capacity, items, count, m);
    memset(root.selected, 0, sizeof(root.selected));

    queue[tail++] = root;
    res.nodes_generated++;

    while (head < tail) {
        BBNode curr = queue[head++];

        if (m) m->comparisons++;
        if (curr.bound <= (double)res.max_value) {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
            continue;
        }

        if (curr.level >= count) continue;

        /* Child 1: Include item */
        if (curr.weight + items[curr.level].weight <= capacity) {
            BBNode left = curr;
            left.level = curr.level + 1;
            left.weight = curr.weight + items[curr.level].weight;
            left.value = curr.value + items[curr.level].value;
            left.selected[items[curr.level].id] = 1;
            left.bound = compute_bound(left.level, left.weight, left.value, capacity, items, count, m);
            res.nodes_generated++;

            if (left.value > res.max_value) {
                res.max_value = left.value;
                res.total_weight = left.weight;
                memcpy(res.best_selection, left.selected, sizeof(res.best_selection));
            }

            if (left.bound > (double)res.max_value && tail < BB_MAX_QUEUE - 1) {
                queue[tail++] = left;
            } else {
                res.nodes_pruned++;
                if (m) m->states_pruned++;
            }
        }

        /* Child 2: Exclude item */
        BBNode right = curr;
        right.level = curr.level + 1;
        right.bound = compute_bound(right.level, right.weight, right.value, capacity, items, count, m);
        res.nodes_generated++;

        if (right.bound > (double)res.max_value && tail < BB_MAX_QUEUE - 1) {
            queue[tail++] = right;
        } else {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
        }
    }

    free(queue);
    return res;
}

/* LIFO Branch & Bound */
KnapsackBBResult knapsack_bb_lifo(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m) {
    KnapsackBBResult res;
    res.max_value = 0;
    res.total_weight = 0;
    res.nodes_generated = 0;
    res.nodes_pruned = 0;
    memset(res.best_selection, 0, sizeof(res.best_selection));
    if (!actions || n == 0 || capacity <= 0) return res;

    SortedItem items[MAX_HOSTS];
    int count = prepare_bb_items(actions, n, items, m);

    BBNode *stack = (BBNode *)tracked_malloc(BB_MAX_QUEUE * sizeof(BBNode), m);
    if (!stack) return res;

    int top = 0;

    BBNode root;
    root.level = 0;
    root.weight = 0;
    root.value = 0;
    root.bound = compute_bound(0, 0, 0, capacity, items, count, m);
    memset(root.selected, 0, sizeof(root.selected));

    stack[top++] = root;
    res.nodes_generated++;

    while (top > 0) {
        BBNode curr = stack[--top];

        if (m) m->comparisons++;
        if (curr.bound <= (double)res.max_value) {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
            continue;
        }

        if (curr.level >= count) continue;

        /* Exclude child first so include is popped next (depth-first exploration) */
        BBNode right = curr;
        right.level = curr.level + 1;
        right.bound = compute_bound(right.level, right.weight, right.value, capacity, items, count, m);
        res.nodes_generated++;

        if (right.bound > (double)res.max_value && top < BB_MAX_QUEUE - 1) {
            stack[top++] = right;
        } else {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
        }

        if (curr.weight + items[curr.level].weight <= capacity) {
            BBNode left = curr;
            left.level = curr.level + 1;
            left.weight = curr.weight + items[curr.level].weight;
            left.value = curr.value + items[curr.level].value;
            left.selected[items[curr.level].id] = 1;
            left.bound = compute_bound(left.level, left.weight, left.value, capacity, items, count, m);
            res.nodes_generated++;

            if (left.value > res.max_value) {
                res.max_value = left.value;
                res.total_weight = left.weight;
                memcpy(res.best_selection, left.selected, sizeof(res.best_selection));
            }

            if (left.bound > (double)res.max_value && top < BB_MAX_QUEUE - 1) {
                stack[top++] = left;
            } else {
                res.nodes_pruned++;
                if (m) m->states_pruned++;
            }
        }
    }

    free(stack);
    return res;
}

/* Least-Cost (LC) Branch & Bound with Max-Heap Priority Queue */
typedef struct {
    BBNode *data;
    int size;
    int capacity;
} BBMaxHeap;

static void bb_heap_push(BBMaxHeap *h, BBNode node) {
    if (h->size >= h->capacity) return;
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].bound >= node.bound) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i] = node;
}

static BBNode bb_heap_pop(BBMaxHeap *h) {
    BBNode top = h->data[0];
    BBNode last = h->data[--h->size];
    if (h->size > 0) {
        int i = 0;
        while (i * 2 + 1 < h->size) {
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            int largest = left;
            if (right < h->size && h->data[right].bound > h->data[left].bound) {
                largest = right;
            }
            if (last.bound >= h->data[largest].bound) break;
            h->data[i] = h->data[largest];
            i = largest;
        }
        h->data[i] = last;
    }
    return top;
}

KnapsackBBResult knapsack_bb_lc(const ContainmentAction *actions, size_t n, int capacity, MetricsTracker *m) {
    KnapsackBBResult res;
    res.max_value = 0;
    res.total_weight = 0;
    res.nodes_generated = 0;
    res.nodes_pruned = 0;
    memset(res.best_selection, 0, sizeof(res.best_selection));
    if (!actions || n == 0 || capacity <= 0) return res;

    SortedItem items[MAX_HOSTS];
    int count = prepare_bb_items(actions, n, items, m);

    BBMaxHeap heap;
    heap.capacity = BB_MAX_QUEUE;
    heap.size = 0;
    heap.data = (BBNode *)tracked_malloc(heap.capacity * sizeof(BBNode), m);
    if (!heap.data) return res;

    BBNode root;
    root.level = 0;
    root.weight = 0;
    root.value = 0;
    root.bound = compute_bound(0, 0, 0, capacity, items, count, m);
    memset(root.selected, 0, sizeof(root.selected));

    bb_heap_push(&heap, root);
    res.nodes_generated++;

    while (heap.size > 0) {
        BBNode curr = bb_heap_pop(&heap);

        if (m) m->comparisons++;
        if (curr.bound <= (double)res.max_value) {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
            continue;
        }

        if (curr.level >= count) continue;

        /* Left child: take item */
        if (curr.weight + items[curr.level].weight <= capacity) {
            BBNode left = curr;
            left.level = curr.level + 1;
            left.weight = curr.weight + items[curr.level].weight;
            left.value = curr.value + items[curr.level].value;
            left.selected[items[curr.level].id] = 1;
            left.bound = compute_bound(left.level, left.weight, left.value, capacity, items, count, m);
            res.nodes_generated++;

            if (left.value > res.max_value) {
                res.max_value = left.value;
                res.total_weight = left.weight;
                memcpy(res.best_selection, left.selected, sizeof(res.best_selection));
            }

            if (left.bound > (double)res.max_value && heap.size < heap.capacity - 1) {
                bb_heap_push(&heap, left);
            } else {
                res.nodes_pruned++;
                if (m) m->states_pruned++;
            }
        }

        /* Right child: skip item */
        BBNode right = curr;
        right.level = curr.level + 1;
        right.bound = compute_bound(right.level, right.weight, right.value, capacity, items, count, m);
        res.nodes_generated++;

        if (right.bound > (double)res.max_value && heap.size < heap.capacity - 1) {
            bb_heap_push(&heap, right);
        } else {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
        }
    }

    free(heap.data);
    return res;
}

/* 5. TSP Least-Cost Branch & Bound */
typedef struct {
    int level;
    int curr_node;
    int cost;
    int bound;
    int visited_mask;
    int path[MAX_HOSTS];
} TSPBBNode;

typedef struct {
    TSPBBNode *data;
    int size;
    int capacity;
} TSPMinHeap;

static void tsp_heap_push(TSPMinHeap *h, TSPBBNode node) {
    if (h->size >= h->capacity) return;
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].bound <= node.bound) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i] = node;
}

static TSPBBNode tsp_heap_pop(TSPMinHeap *h) {
    TSPBBNode top = h->data[0];
    TSPBBNode last = h->data[--h->size];
    if (h->size > 0) {
        int i = 0;
        while (i * 2 + 1 < h->size) {
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            int smallest = left;
            if (right < h->size && h->data[right].bound < h->data[left].bound) {
                smallest = right;
            }
            if (last.bound <= h->data[smallest].bound) break;
            h->data[i] = h->data[smallest];
            i = smallest;
        }
        h->data[i] = last;
    }
    return top;
}

static int compute_tsp_bound(int n, int visited_mask, int curr_node, int current_cost, const AttackGraph *graph, MetricsTracker *m) {
    if (visited_mask == (1 << n) - 1) {
        return current_cost + graph->adj_weight[curr_node][0];
    }

    int lower_bound = current_cost;

    /* Outgoing edge from curr_node to an unvisited node */
    int min_curr_out = INF_COST;
    for (int v = 1; v < n; v++) {
        if (!(visited_mask & (1 << v))) {
            int w = graph->adj_weight[curr_node][v];
            if (m) m->comparisons++;
            if (w < min_curr_out) min_curr_out = w;
        }
    }
    if (min_curr_out < INF_COST) lower_bound += min_curr_out;

    /* For each unvisited node u, find min outgoing edge to another unvisited node or 0 */
    for (int u = 1; u < n; u++) {
        if (!(visited_mask & (1 << u))) {
            int min_out = INF_COST;
            for (int v = 0; v < n; v++) {
                if (v == u) continue;
                if (v == 0 || !(visited_mask & (1 << v))) {
                    int w = graph->adj_weight[u][v];
                    if (m) m->comparisons++;
                    if (w < min_out) min_out = w;
                }
            }
            if (min_out < INF_COST) lower_bound += min_out;
        }
    }

    return lower_bound;
}

TSPBBResult tsp_bb_lc(const AttackGraph *graph, int n, MetricsTracker *m) {
    TSPBBResult res;
    res.min_tour_cost = INF_COST;
    res.tour_length = 0;
    res.nodes_generated = 0;
    res.nodes_pruned = 0;
    if (!graph || n <= 1 || n > 16) return res;

    TSPMinHeap heap;
    heap.capacity = BB_MAX_QUEUE;
    heap.size = 0;
    heap.data = (TSPBBNode *)tracked_malloc(heap.capacity * sizeof(TSPBBNode), m);
    if (!heap.data) return res;

    TSPBBNode root;
    root.level = 1;
    root.curr_node = 0;
    root.cost = 0;
    root.visited_mask = 1;
    root.path[0] = 0;
    root.bound = compute_tsp_bound(n, root.visited_mask, 0, 0, graph, m);

    tsp_heap_push(&heap, root);
    res.nodes_generated++;

    while (heap.size > 0) {
        TSPBBNode curr = tsp_heap_pop(&heap);

        if (m) m->comparisons++;
        if (curr.bound >= res.min_tour_cost) {
            res.nodes_pruned++;
            if (m) m->states_pruned++;
            continue;
        }

        if (curr.level == n) {
            /* Try returning to node 0 */
            int ret_w = graph->adj_weight[curr.curr_node][0];
            if (ret_w < INF_COST) {
                int final_cost = curr.cost + ret_w;
                if (m) m->comparisons++;
                if (final_cost < res.min_tour_cost) {
                    res.min_tour_cost = final_cost;
                    for (int i = 0; i < n; i++) {
                        res.tour_nodes[i] = curr.path[i];
                    }
                    res.tour_nodes[n] = 0;
                    res.tour_length = n + 1;
                }
            }
            continue;
        }

        for (int v = 0; v < n; v++) {
            if (!(curr.visited_mask & (1 << v))) {
                int w = graph->adj_weight[curr.curr_node][v];
                if (w >= INF_COST) continue;

                TSPBBNode child;
                child.level = curr.level + 1;
                child.curr_node = v;
                child.cost = curr.cost + w;
                child.visited_mask = curr.visited_mask | (1 << v);
                memcpy(child.path, curr.path, sizeof(curr.path));
                child.path[curr.level] = v;
                child.bound = compute_tsp_bound(n, child.visited_mask, v, child.cost, graph, m);
                res.nodes_generated++;

                if (child.bound < res.min_tour_cost && heap.size < heap.capacity - 1) {
                    tsp_heap_push(&heap, child);
                } else {
                    res.nodes_pruned++;
                    if (m) m->states_pruned++;
                }
            }
        }
    }

    free(heap.data);
    return res;
}
