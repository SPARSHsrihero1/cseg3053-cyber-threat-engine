#include "metrics.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void metrics_init(MetricsTracker *m, const char *name, const char *paradigm, size_t n) {
    if (!m) return;
    m->algorithm_name = name ? name : "Unknown";
    m->paradigm = paradigm ? paradigm : "General";
    m->input_size = n;
    m->comparisons = 0;
    m->swaps_or_writes = 0;
    m->recursive_calls = 0;
    m->graph_relaxations = 0;
    m->states_pruned = 0;
    m->bytes_allocated = 0;
    m->elapsed_ms = 0.0;
    m->start_tick = 0;
}

void metrics_start(MetricsTracker *m) {
    if (!m) return;
    m->start_tick = clock();
}

void metrics_stop(MetricsTracker *m) {
    if (!m) return;
    clock_t end_tick = clock();
    double diff = ((double)(end_tick - m->start_tick) * 1000.0) / (double)CLOCKS_PER_SEC;
    m->elapsed_ms = diff;
}

void *tracked_malloc(size_t size, MetricsTracker *m) {
    void *ptr = malloc(size);
    if (ptr && m) {
        m->bytes_allocated += size;
        m->swaps_or_writes++;
    }
    return ptr;
}

void *tracked_calloc(size_t num, size_t size, MetricsTracker *m) {
    void *ptr = calloc(num, size);
    if (ptr && m) {
        m->bytes_allocated += (num * size);
        m->swaps_or_writes++;
    }
    return ptr;
}

void metrics_print_table_header(void) {
    printf("+------------------------------+------------------+----------+--------------+--------------+------------+------------+------------+--------------+\n");
    printf("| %-28s | %-16s | %8s | %12s | %12s | %10s | %10s | %10s | %12s |\n",
           "Algorithm", "Paradigm", "N", "Comparisons", "Swaps/Writes", "Rec Calls", "Relaxations", "Pruned", "Time (ms)");
    printf("+------------------------------+------------------+----------+--------------+--------------+------------+------------+------------+--------------+\n");
}

void metrics_print_row(const MetricsTracker *m) {
    if (!m) return;
    printf("| %-28s | %-16s | %8zu | %12llu | %12llu | %10llu | %10llu | %10llu | %12.4f |\n",
           m->algorithm_name,
           m->paradigm,
           m->input_size,
           (unsigned long long)m->comparisons,
           (unsigned long long)m->swaps_or_writes,
           (unsigned long long)m->recursive_calls,
           (unsigned long long)m->graph_relaxations,
           (unsigned long long)m->states_pruned,
           m->elapsed_ms);
}

int metrics_export_csv(const char *filepath, const MetricsTracker *m, int append) {
    if (!filepath || !m) return -1;
    FILE *f = fopen(filepath, append ? "a" : "w");
    if (!f) return -1;

    if (!append) {
        fprintf(f, "Algorithm,Paradigm,InputSize,Comparisons,SwapsOrWrites,RecursiveCalls,GraphRelaxations,StatesPruned,BytesAllocated,ElapsedMs\n");
    }

    fprintf(f, "\"%s\",\"%s\",%zu,%llu,%llu,%llu,%llu,%llu,%zu,%.4f\n",
            m->algorithm_name,
            m->paradigm,
            m->input_size,
            (unsigned long long)m->comparisons,
            (unsigned long long)m->swaps_or_writes,
            (unsigned long long)m->recursive_calls,
            (unsigned long long)m->graph_relaxations,
            (unsigned long long)m->states_pruned,
            m->bytes_allocated,
            m->elapsed_ms);

    fclose(f);
    return 0;
}

int metrics_export_json(const char *filepath, const MetricsTracker *metrics_list, size_t count) {
    if (!filepath || (!metrics_list && count > 0)) return -1;
    FILE *f = fopen(filepath, "w");
    if (!f) return -1;

    fprintf(f, "[\n");
    for (size_t i = 0; i < count; i++) {
        const MetricsTracker *m = &metrics_list[i];
        fprintf(f, "  {\n");
        fprintf(f, "    \"algorithm\": \"%s\",\n", m->algorithm_name);
        fprintf(f, "    \"paradigm\": \"%s\",\n", m->paradigm);
        fprintf(f, "    \"input_size\": %zu,\n", m->input_size);
        fprintf(f, "    \"comparisons\": %llu,\n", (unsigned long long)m->comparisons);
        fprintf(f, "    \"swaps_or_writes\": %llu,\n", (unsigned long long)m->swaps_or_writes);
        fprintf(f, "    \"recursive_calls\": %llu,\n", (unsigned long long)m->recursive_calls);
        fprintf(f, "    \"graph_relaxations\": %llu,\n", (unsigned long long)m->graph_relaxations);
        fprintf(f, "    \"states_pruned\": %llu,\n", (unsigned long long)m->states_pruned);
        fprintf(f, "    \"bytes_allocated\": %zu,\n", m->bytes_allocated);
        fprintf(f, "    \"elapsed_ms\": %.4f\n", m->elapsed_ms);
        fprintf(f, "  }%s\n", (i + 1 < count) ? "," : "");
    }
    fprintf(f, "]\n");

    fclose(f);
    return 0;
}
