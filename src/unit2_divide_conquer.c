#include "unit2_divide_conquer.h"
#include <stdlib.h>
#include <string.h>

int binary_search_iterative(const EventLog *logs, size_t n, uint64_t target_timestamp, MetricsTracker *m) {
    if (!logs || n == 0) return -1;
    int low = 0;
    int high = (int)n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (m) m->comparisons++;

        if (logs[mid].timestamp == target_timestamp) {
            return mid;
        } else if (logs[mid].timestamp < target_timestamp) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int binary_search_recursive(const EventLog *logs, int low, int high, uint64_t target_timestamp, MetricsTracker *m) {
    if (m) m->recursive_calls++;
    if (!logs || low > high) return -1;

    int mid = low + (high - low) / 2;
    if (m) m->comparisons++;

    if (logs[mid].timestamp == target_timestamp) {
        return mid;
    } else if (logs[mid].timestamp < target_timestamp) {
        return binary_search_recursive(logs, mid + 1, high, target_timestamp, m);
    } else {
        return binary_search_recursive(logs, low, mid - 1, target_timestamp, m);
    }
}

BSTNode *bst_insert(BSTNode *root, ThreatSignature sig, MetricsTracker *m) {
    if (!root) {
        BSTNode *node = (BSTNode *)tracked_malloc(sizeof(BSTNode), m);
        if (!node) return NULL;
        node->key = sig.sig_id;
        node->sig = sig;
        node->left = NULL;
        node->right = NULL;
        if (m) m->swaps_or_writes++;
        return node;
    }

    if (m) {
        m->comparisons++;
        m->recursive_calls++;
    }

    if (sig.sig_id < root->key) {
        root->left = bst_insert(root->left, sig, m);
    } else if (sig.sig_id > root->key) {
        root->right = bst_insert(root->right, sig, m);
    }
    return root;
}

BSTNode *bst_search_iterative(BSTNode *root, int sig_id, MetricsTracker *m) {
    BSTNode *curr = root;
    while (curr) {
        if (m) m->comparisons++;
        if (curr->key == sig_id) {
            return curr;
        } else if (sig_id < curr->key) {
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }
    return NULL;
}

BSTNode *bst_search_recursive(BSTNode *root, int sig_id, MetricsTracker *m) {
    if (m) m->recursive_calls++;
    if (!root) return NULL;

    if (m) m->comparisons++;
    if (root->key == sig_id) {
        return root;
    } else if (sig_id < root->key) {
        return bst_search_recursive(root->left, sig_id, m);
    } else {
        return bst_search_recursive(root->right, sig_id, m);
    }
}

void bst_free(BSTNode *root) {
    if (!root) return;
    bst_free(root->left);
    bst_free(root->right);
    free(root);
}

static void merge_internal(EventLog *logs, EventLog *temp, int low, int mid, int high, MetricsTracker *m) {
    int i = low;
    int j = mid + 1;
    int k = low;

    while (i <= mid && j <= high) {
        if (m) m->comparisons++;
        if (logs[i].timestamp <= logs[j].timestamp) {
            temp[k++] = logs[i++];
        } else {
            temp[k++] = logs[j++];
        }
        if (m) m->swaps_or_writes++;
    }

    while (i <= mid) {
        temp[k++] = logs[i++];
        if (m) m->swaps_or_writes++;
    }
    while (j <= high) {
        temp[k++] = logs[j++];
        if (m) m->swaps_or_writes++;
    }

    for (i = low; i <= high; i++) {
        logs[i] = temp[i];
        if (m) m->swaps_or_writes++;
    }
}

static void merge_sort_recursive(EventLog *logs, EventLog *temp, int low, int high, MetricsTracker *m) {
    if (low >= high) return;
    if (m) m->recursive_calls++;

    int mid = low + (high - low) / 2;
    merge_sort_recursive(logs, temp, low, mid, m);
    merge_sort_recursive(logs, temp, mid + 1, high, m);
    merge_internal(logs, temp, low, mid, high, m);
}

void merge_sort(EventLog *logs, size_t n, MetricsTracker *m) {
    if (!logs || n <= 1) return;
    EventLog *temp = (EventLog *)tracked_malloc(n * sizeof(EventLog), m);
    if (!temp) return;
    merge_sort_recursive(logs, temp, 0, (int)n - 1, m);
    free(temp);
}

static int partition_deterministic(EventLog *logs, int low, int high, MetricsTracker *m) {
    uint64_t pivot = logs[high].timestamp;
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (m) m->comparisons++;
        if (logs[j].timestamp <= pivot) {
            i++;
            EventLog tmp = logs[i];
            logs[i] = logs[j];
            logs[j] = tmp;
            if (m) m->swaps_or_writes += 2;
        }
    }
    EventLog tmp = logs[i + 1];
    logs[i + 1] = logs[high];
    logs[high] = tmp;
    if (m) m->swaps_or_writes += 2;

    return i + 1;
}

void quick_sort_deterministic(EventLog *logs, int low, int high, MetricsTracker *m) {
    if (low >= high) return;
    if (m) m->recursive_calls++;

    int pi = partition_deterministic(logs, low, high, m);
    quick_sort_deterministic(logs, low, pi - 1, m);
    quick_sort_deterministic(logs, pi + 1, high, m);
}

void quick_sort_randomized(EventLog *logs, int low, int high, MetricsTracker *m) {
    if (low >= high) return;
    if (m) m->recursive_calls++;

    int random_idx = low + (rand() % (high - low + 1));
    EventLog tmp = logs[random_idx];
    logs[random_idx] = logs[high];
    logs[high] = tmp;
    if (m) m->swaps_or_writes += 2;

    int pi = partition_deterministic(logs, low, high, m);
    quick_sort_randomized(logs, low, pi - 1, m);
    quick_sort_randomized(logs, pi + 1, high, m);
}

static SubarrayResult max_cross_subarray(const EventLog *logs, int low, int mid, int high, MetricsTracker *m) {
    int left_sum = -INF_COST;
    int sum = 0;
    int max_left = mid;

    for (int i = mid; i >= low; i--) {
        sum += logs[i].anomaly_delta;
        if (m) m->comparisons++;
        if (sum > left_sum) {
            left_sum = sum;
            max_left = i;
        }
    }

    int right_sum = -INF_COST;
    sum = 0;
    int max_right = mid + 1;

    for (int j = mid + 1; j <= high; j++) {
        sum += logs[j].anomaly_delta;
        if (m) m->comparisons++;
        if (sum > right_sum) {
            right_sum = sum;
            max_right = j;
        }
    }

    return (SubarrayResult){ left_sum + right_sum, max_left, max_right };
}

SubarrayResult max_subarray_dc(const EventLog *logs, int low, int high, MetricsTracker *m) {
    if (!logs || low > high) return (SubarrayResult){0, -1, -1};
    if (low == high) {
        return (SubarrayResult){ logs[low].anomaly_delta, low, high };
    }

    if (m) m->recursive_calls++;
    int mid = low + (high - low) / 2;

    SubarrayResult left_res = max_subarray_dc(logs, low, mid, m);
    SubarrayResult right_res = max_subarray_dc(logs, mid + 1, high, m);
    SubarrayResult cross_res = max_cross_subarray(logs, low, mid, high, m);

    if (m) m->comparisons += 2;
    if (left_res.max_sum >= right_res.max_sum && left_res.max_sum >= cross_res.max_sum) {
        return left_res;
    } else if (right_res.max_sum >= left_res.max_sum && right_res.max_sum >= cross_res.max_sum) {
        return right_res;
    } else {
        return cross_res;
    }
}

SubarrayResult max_subarray_kadane(const EventLog *logs, size_t n, MetricsTracker *m) {
    if (!logs || n == 0) return (SubarrayResult){0, -1, -1};

    int max_so_far = logs[0].anomaly_delta;
    int curr_max = logs[0].anomaly_delta;
    int start = 0, end = 0, s = 0;

    for (size_t i = 1; i < n; i++) {
        if (m) m->comparisons++;
        if (logs[i].anomaly_delta > curr_max + logs[i].anomaly_delta) {
            curr_max = logs[i].anomaly_delta;
            s = (int)i;
        } else {
            curr_max += logs[i].anomaly_delta;
        }

        if (m) m->comparisons++;
        if (curr_max > max_so_far) {
            max_so_far = curr_max;
            start = s;
            end = (int)i;
        }
    }

    return (SubarrayResult){ max_so_far, start, end };
}

uint64_t fast_power_mod_recursive(uint64_t base, uint64_t exp, uint64_t mod, MetricsTracker *m) {
    if (m) m->recursive_calls++;
    if (mod == 0) return 0;
    if (exp == 0) return 1 % mod;

    uint64_t half = fast_power_mod_recursive(base, exp / 2, mod, m);
    uint64_t res = (half * half) % mod;
    if (m) m->swaps_or_writes++;

    if (exp % 2 == 1) {
        res = (res * (base % mod)) % mod;
        if (m) m->swaps_or_writes++;
    }
    return res;
}

uint64_t fast_power_mod_iterative(uint64_t base, uint64_t exp, uint64_t mod, MetricsTracker *m) {
    if (mod == 0) return 0;
    uint64_t res = 1 % mod;
    base = base % mod;

    while (exp > 0) {
        if (m) m->comparisons++;
        if (exp & 1) {
            res = (res * base) % mod;
            if (m) m->swaps_or_writes++;
        }
        base = (base * base) % mod;
        if (m) m->swaps_or_writes++;
        exp >>= 1;
    }
    return res;
}

int find_celebrity_c2(int n, const int comm_matrix[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m) {
    if (n <= 0 || n > MAX_HOSTS || !comm_matrix) return -1;

    /* Phase 1: Candidate elimination in O(N) */
    int candidate = 0;
    for (int i = 1; i < n; i++) {
        if (m) m->comparisons++;
        /* If candidate knows i (initiates outbound traffic to i), candidate cannot be C2 */
        if (comm_matrix[candidate][i] == 1) {
            candidate = i;
        }
    }

    /* Phase 2: Verification in O(N) */
    for (int i = 0; i < n; i++) {
        if (i == candidate) continue;
        if (m) m->comparisons += 2;
        /* Candidate must receive traffic from i, and must NOT send traffic to i */
        if (comm_matrix[i][candidate] == 0 || comm_matrix[candidate][i] == 1) {
            return -1;
        }
    }
    return candidate;
}

void matrix_mult_classical(int n, const int A[MAX_HOSTS][MAX_HOSTS], const int B[MAX_HOSTS][MAX_HOSTS], int C[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m) {
    if (n <= 0 || n > MAX_HOSTS) return;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
                if (m) m->swaps_or_writes++;
            }
        }
    }
}

/* Recursive helper for Strassen matrix multiplication */
static void strassen_rec(int n, int A[MAX_HOSTS][MAX_HOSTS], int B[MAX_HOSTS][MAX_HOSTS], int C[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m) {
    if (n <= 2) {
        matrix_mult_classical(n, A, B, C, m);
        return;
    }

    if (m) m->recursive_calls++;

    int k = n / 2;
    int A11[MAX_HOSTS][MAX_HOSTS] = {0}, A12[MAX_HOSTS][MAX_HOSTS] = {0}, A21[MAX_HOSTS][MAX_HOSTS] = {0}, A22[MAX_HOSTS][MAX_HOSTS] = {0};
    int B11[MAX_HOSTS][MAX_HOSTS] = {0}, B12[MAX_HOSTS][MAX_HOSTS] = {0}, B21[MAX_HOSTS][MAX_HOSTS] = {0}, B22[MAX_HOSTS][MAX_HOSTS] = {0};
    int T1[MAX_HOSTS][MAX_HOSTS] = {0}, T2[MAX_HOSTS][MAX_HOSTS] = {0};
    int P1[MAX_HOSTS][MAX_HOSTS] = {0}, P2[MAX_HOSTS][MAX_HOSTS] = {0}, P3[MAX_HOSTS][MAX_HOSTS] = {0}, P4[MAX_HOSTS][MAX_HOSTS] = {0};
    int P5[MAX_HOSTS][MAX_HOSTS] = {0}, P6[MAX_HOSTS][MAX_HOSTS] = {0}, P7[MAX_HOSTS][MAX_HOSTS] = {0};

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + k];
            A21[i][j] = A[i + k][j];
            A22[i][j] = A[i + k][j + k];

            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + k];
            B21[i][j] = B[i + k][j];
            B22[i][j] = B[i + k][j + k];
        }
    }

    /* P1 = (A11 + A22) * (B11 + B22) */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T1[i][j] = A11[i][j] + A22[i][j]; T2[i][j] = B11[i][j] + B22[i][j]; }
    strassen_rec(k, T1, T2, P1, m);

    /* P2 = (A21 + A22) * B11 */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T1[i][j] = A21[i][j] + A22[i][j]; }
    strassen_rec(k, T1, B11, P2, m);

    /* P3 = A11 * (B12 - B22) */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T2[i][j] = B12[i][j] - B22[i][j]; }
    strassen_rec(k, A11, T2, P3, m);

    /* P4 = A22 * (B21 - B11) */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T2[i][j] = B21[i][j] - B11[i][j]; }
    strassen_rec(k, A22, T2, P4, m);

    /* P5 = (A11 + A12) * B22 */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T1[i][j] = A11[i][j] + A12[i][j]; }
    strassen_rec(k, T1, B22, P5, m);

    /* P6 = (A21 - A11) * (B11 + B12) */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T1[i][j] = A21[i][j] - A11[i][j]; T2[i][j] = B11[i][j] + B12[i][j]; }
    strassen_rec(k, T1, T2, P6, m);

    /* P7 = (A12 - A22) * (B21 + B22) */
    for (int i = 0; i < k; i++) for (int j = 0; j < k; j++) { T1[i][j] = A12[i][j] - A22[i][j]; T2[i][j] = B21[i][j] + B22[i][j]; }
    strassen_rec(k, T1, T2, P7, m);

    /* C11 = P1 + P4 - P5 + P7 */
    /* C12 = P3 + P5 */
    /* C21 = P2 + P4 */
    /* C22 = P1 - P2 + P3 + P6 */
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            C[i][j] = P1[i][j] + P4[i][j] - P5[i][j] + P7[i][j];
            C[i][j + k] = P3[i][j] + P5[i][j];
            C[i + k][j] = P2[i][j] + P4[i][j];
            C[i + k][j + k] = P1[i][j] - P2[i][j] + P3[i][j] + P6[i][j];
            if (m) m->swaps_or_writes += 4;
        }
    }
}

void matrix_mult_strassen(int n, const int A[MAX_HOSTS][MAX_HOSTS], const int B[MAX_HOSTS][MAX_HOSTS], int C[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m) {
    if (n <= 0 || n > MAX_HOSTS) return;

    /* Next power of 2 */
    int m_size = 1;
    while (m_size < n) m_size *= 2;

    if (m_size > MAX_HOSTS) {
        matrix_mult_classical(n, A, B, C, m);
        return;
    }

    int padA[MAX_HOSTS][MAX_HOSTS] = {0};
    int padB[MAX_HOSTS][MAX_HOSTS] = {0};
    int padC[MAX_HOSTS][MAX_HOSTS] = {0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            padA[i][j] = A[i][j];
            padB[i][j] = B[i][j];
        }
    }

    strassen_rec(m_size, padA, padB, padC, m);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = padC[i][j];
        }
    }
}
