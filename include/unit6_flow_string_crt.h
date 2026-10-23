#ifndef UNIT6_FLOW_STRING_CRT_H
#define UNIT6_FLOW_STRING_CRT_H

#include "domain.h"
#include "metrics.h"
#include <stdint.h>
#include <stddef.h>

/* 1. Ford-Fulkerson / Edmonds-Karp Maximum Flow & Min-Cut */
typedef struct {
    int max_flow;
    int num_mincut_edges;
    NetworkEdge mincut_edges[MAX_HOSTS * MAX_HOSTS];
} FlowResult;

FlowResult ford_fulkerson_max_flow(const AttackGraph *graph, int source, int sink, MetricsTracker *m);

/* 2. Maximum Bipartite Matching for SOC Analysts */
typedef struct {
    int max_matches;
    int incident_assigned_to[MAX_HOSTS];
} BipartiteMatchingResult;

BipartiteMatchingResult max_bipartite_matching_soc(int num_incidents, int num_analysts, const int adj[MAX_HOSTS][MAX_HOSTS], MetricsTracker *m);

/* 3. Chinese Remainder Theorem (CRT) Telemetry Reconstruction */
typedef struct {
    int64_t reconstructed_counter;
    int64_t total_modulus;
    int success;
} CRTResult;

int64_t extended_gcd(int64_t a, int64_t b, int64_t *x, int64_t *y);
int64_t mod_inverse(int64_t a, int64_t m);
CRTResult crt_reconstruct_telemetry(int num_sensors, const int64_t *remainders, const int64_t *moduli, MetricsTracker *m);

/* 4. String-Matching Engines */
typedef struct {
    int match_count;
    int first_match_index;
    uint64_t spurious_hits; /* For Rabin-Karp hash collisions */
} StringMatchResult;

StringMatchResult strmatch_naive(const char *text, const char *pattern, MetricsTracker *m);
StringMatchResult strmatch_rabin_karp(const char *text, const char *pattern, MetricsTracker *m);
StringMatchResult strmatch_finite_automaton(const char *text, const char *pattern, MetricsTracker *m);
StringMatchResult strmatch_kmp(const char *text, const char *pattern, MetricsTracker *m);

#endif /* UNIT6_FLOW_STRING_CRT_H */
