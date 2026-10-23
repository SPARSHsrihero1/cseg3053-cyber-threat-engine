#ifndef DATA_GENERATOR_H
#define DATA_GENERATOR_H

#include "domain.h"
#include <stddef.h>
#include <stdint.h>

/* Log Generation */
void generate_event_logs(EventLog *dest, size_t count, uint32_t seed);
void generate_adversarial_sorted_logs(EventLog *dest, size_t count);
void generate_adversarial_reversed_logs(EventLog *dest, size_t count);
void generate_adversarial_identical_logs(EventLog *dest, size_t count);
void generate_adversarial_string(char *dest, size_t len, const char *pattern);

/* Signatures & Containment Playbooks */
void generate_threat_signatures(ThreatSignature *dest, size_t count);
void generate_containment_actions(ContainmentAction *dest, size_t count);

/* Graph Generation */
void generate_attack_graph(AttackGraph *graph, int num_hosts, double edge_density, uint32_t seed);
void generate_flow_network(AttackGraph *graph, int num_hosts, int source, int sink);
void generate_negative_weight_graph(AttackGraph *graph, int num_hosts, int insert_negative_cycle);
void generate_c2_celebrity_graph(AttackGraph *graph, int num_hosts, int c2_node);

/* Bipartite Graph for SOC Analysts */
void generate_soc_bipartite_graph(int num_incidents, int num_analysts, int adj[MAX_HOSTS][MAX_HOSTS], double match_prob, uint32_t seed);

/* CRT Telemetry Congruences */
void generate_crt_telemetry_system(int num_sensors, uint64_t true_counter, int64_t *remainders, int64_t *moduli);

#endif /* DATA_GENERATOR_H */
