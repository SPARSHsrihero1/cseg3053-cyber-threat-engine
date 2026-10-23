#ifndef DOMAIN_H
#define DOMAIN_H

#include <stdint.h>
#include <stddef.h>

#define MAX_IP_LEN 16
#define MAX_PAYLOAD_LEN 256
#define MAX_PATTERN_LEN 64
#define MAX_HOSTS 64
#define INF_COST 100000000

typedef struct {
    uint32_t log_id;
    uint64_t timestamp;
    char src_ip[MAX_IP_LEN];
    char dst_ip[MAX_IP_LEN];
    int severity;                   /* 1 to 10 */
    int anomaly_delta;              /* Signed delta for Max Subarray burst analysis */
    char event_code;                /* 'A'-'Z' event type for LCS behavioral correlation */
    char payload[MAX_PAYLOAD_LEN];  /* Raw packet/syslog text for String Matching */
} EventLog;

typedef struct {
    int sig_id;
    char pattern[MAX_PATTERN_LEN];
    int risk_score;
    double hit_probability;         /* Used for Optimal BST (OBST) */
} ThreatSignature;

typedef struct {
    int action_id;
    char name[48];
    int disruption_cost;            /* Knapsack weight (SLA downtime minutes) */
    int risk_mitigated;             /* Knapsack value (Risk score reduced) */
    int start_time;                 /* Activity Selection / Interval Partitioning */
    int end_time;
} ContainmentAction;

typedef struct {
    int u;
    int v;
    int exploit_weight;             /* Dijkstra / Bellman-Ford / MST weight */
    int bandwidth_capacity;         /* Ford-Fulkerson capacity */
} NetworkEdge;

typedef struct {
    int num_hosts;
    int num_edges;
    int adj_weight[MAX_HOSTS][MAX_HOSTS];
    int adj_capacity[MAX_HOSTS][MAX_HOSTS];
    int comm_matrix[MAX_HOSTS][MAX_HOSTS];
    NetworkEdge edges[MAX_HOSTS * MAX_HOSTS];
} AttackGraph;

#endif /* DOMAIN_H */
