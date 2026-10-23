#ifndef METRICS_H
#define METRICS_H

#include <stddef.h>
#include <stdint.h>
#include <time.h>

typedef struct {
    const char *algorithm_name;
    const char *paradigm;
    size_t input_size;
    uint64_t comparisons;
    uint64_t swaps_or_writes;
    uint64_t recursive_calls;
    uint64_t graph_relaxations;
    uint64_t states_pruned;
    size_t bytes_allocated;
    double elapsed_ms;
    clock_t start_tick;
} MetricsTracker;

void metrics_init(MetricsTracker *m, const char *name, const char *paradigm, size_t n);
void metrics_start(MetricsTracker *m);
void metrics_stop(MetricsTracker *m);
void *tracked_malloc(size_t size, MetricsTracker *m);
void *tracked_calloc(size_t num, size_t size, MetricsTracker *m);
void metrics_print_table_header(void);
void metrics_print_row(const MetricsTracker *m);
int metrics_export_csv(const char *filepath, const MetricsTracker *m, int append);
int metrics_export_json(const char *filepath, const MetricsTracker *metrics_list, size_t count);

#endif /* METRICS_H */
