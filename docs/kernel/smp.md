+++
title = "topology"
author = "Unknown"
status = "unknown"
+++

# [kernel/smp/topology.c](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c)

- [`cpu_mask_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L22) — `static void cpu_mask_print(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m)`
- [`print_topology_node()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L43) — `static void print_topology_node(`[`struct topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43)` *node`,`int depth)`
- [`cpu_mask_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L89) — [`struct cpu_mask *`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)`cpu_mask_create(void)`
- [`cpu_mask_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L93) — `bool cpu_mask_init(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m`,`size_t nbits)`
- [`cpu_mask_set()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L110) — `void cpu_mask_set(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m`,`size_t cpu)`
- [`cpu_mask_clear()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L118) — `void cpu_mask_clear(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m`,`size_t cpu)`
- [`cpu_mask_test()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L126) — `bool cpu_mask_test(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m`,`size_t cpu)`
- [`cpu_mask_or()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L134) — `void cpu_mask_or(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *dst`,[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *b)`
- [`cpu_mask_set_all()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L144) — `void cpu_mask_set_all(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *m)`
- [`cpu_mask_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L154) — `bool cpu_mask_empty(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *mask)`
- [`topology_dump()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L166) — `void topology_dump(void)`
- [`build_smt_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L178) — `static size_t build_smt_nodes(size_t n_cpus)`
- [`build_core_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L222) — `static size_t build_core_nodes(size_t n_cpus)`
- [`cpu_mask_intersects()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L268) — `static bool cpu_mask_intersects(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *a`,[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *b)`
- [`build_numa_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L297) — `static size_t build_numa_nodes(size_t n_cores`,`size_t n_llc)`
- [`build_llc_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L367) — `static size_t build_llc_nodes(size_t n_cores)`
- [`build_package_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L453) — `static size_t build_package_nodes(size_t n_cores`,`size_t n_llc)`
- [`build_machine_node()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L497) — `static void build_machine_node(size_t n_packages)`
- [`topology_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L521) — `void topology_init(void)`
- [`topology_get_smts_under_numa()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L548) — [`struct core * *`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)`topology_get_smts_under_numa(`[`struct topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43)` *numa`,`size_t *count)`
- [`topology_mark_core_idle()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L582) — `void topology_mark_core_idle(size_t cpu_id`,`bool idle)`
- [`topology_find_idle_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/topology.c#L599) — [`struct core *`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)`topology_find_idle_core(`[`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)` *local_core`,[`enum topology_level`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L7)` max_search)`



+++
title = "mp"
author = "Unknown"
status = "unknown"
+++

# [kernel/smp/mp.c](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c)

- [`detect_llc()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L17) — `static void detect_llc(`[`struct topology_cache_info`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L30)` *llc)`
- [`init_smt_info()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L44) — `static void init_smt_info(`[`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)` *c)`
- [`setup_cpu()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L71) — `static`[`struct core *`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)`setup_cpu(uint64_t cpu)`
- [`set_core_awake()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L87) — `static inline void set_core_awake(void)`
- [`smp_wakeup()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L95) — `__no_sanitize_address smp_wakeup()`
- [`smp_wakeup_processors()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L123) — `void smp_wakeup_processors(struct limine_mp_response *mpr)`
- [`smp_complete_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L128) — `void smp_complete_init()`
- [`smp_setup_bsp()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L139) — `void smp_setup_bsp()`
- [`smp_movealloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/mp.c#L163) — `static void smp_movealloc(void *a`,`void *b)`



+++
title = "domain"
author = "Unknown"
status = "unknown"
+++

# [kernel/smp/domain.c](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c)

- [`init_global_domain()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L9) — `static void init_global_domain(uint64_t domain_count)`
- [`construct_domains_from_numa_nodes()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L28) — `static void construct_domains_from_numa_nodes(void)`
- [`construct_domains_from_cores()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L47) — `static void construct_domains_from_cores(void)`
- [`domain_dump()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L82) — `void domain_dump(void)`
- [`domain_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L109) — `void domain_init(void)`
- [`domain_set_cpu_mask()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L126) — `void domain_set_cpu_mask(`[`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)` *mask`,[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *domain)`
- [`domain_create_cpu_mask()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L132) — [`struct cpu_mask *`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)`domain_create_cpu_mask(`[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *domain)`
- [`domains_move()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L150) — `static void domains_move(void *a`,`void *b)`
- [`domain_idle()`](https://github.com/bluegummi/charmos/blob/main/kernel/smp/domain.c#L158) — `bool domain_idle(`[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *domain)`



