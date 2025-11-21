+++
title = "topology"
author = "Unknown"
status = "unknown"
+++

# [include/smp/topology.h](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h)

### struct [`cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21)

| Member Type | Member Name |
|-------------|-------------|
| `bool` | [`uses_large`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L22) |
| `union { atomic_uint_fast64_t small; atomic_uint_fast64_t *large; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L23) |
| `size_t` | [`nbits`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L27) |


### struct [`topology_cache_info`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L30)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`level`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L31) |
| `uint8_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L32) |
| `uint32_t` | [`size_kb`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L33) |
| `uint32_t` | [`line_size`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L34) |
| `uint32_t` | [`cores_sharing`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L35) |


### struct [`topology_package_info`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L38)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`package_id`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L39) |
| [`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21) | [`cores`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L40) |


### struct [`topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43)

| Member Type | Member Name |
|-------------|-------------|
| [`enum topology_level`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L7) | [`level`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L44) |
| `uint64_t` | [`id`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L45) |
| `uint64_t` | [`parent`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L46) |
| [`struct topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43) | [`*parent_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L47) |
| `int32_t` | [`first_child`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L48) |
| `int32_t` | [`nr_children`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L53) |
| [`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21) | [`cpus`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L55) |
| [`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21) | [`idle`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L56) |
| [`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15) | [`*core`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L58) |
| `union { struct numa_node *numa; struct topology_cache_info *cache; struct topology_package_info *package; }` | [`data`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L60) |


### struct [`topology`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L67)

| Member Type | Member Name |
|-------------|-------------|
| [`struct topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43) | [`*level[TOPOLOGY_LEVEL_MAX]`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L68) |
| `uint16_t` | [`count[TOPOLOGY_LEVEL_MAX]`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L69) |


### enum [`topology_level`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L7)

| Name | Value |
|------|-------|
| [`TOPOLOGY_LEVEL_SMT`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L8) | `None` |
| [`TOPOLOGY_LEVEL_CORE`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L9) | `None` |
| [`TOPOLOGY_LEVEL_LLC`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L10) | `None` |
| [`TOPOLOGY_LEVEL_NUMA`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L14) | `None` |
| [`TOPOLOGY_LEVEL_PACKAGE`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L15) | `None` |
| [`TOPOLOGY_LEVEL_MACHINE`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L16) | `None` |
| [`TOPOLOGY_LEVEL_MAX`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L17) | `None` |
| [`TOPOLOGY_LEVEL_COUNT`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L18) | `TOPOLOGY_LEVEL_MAX` |



+++
title = "domain"
author = "Unknown"
status = "unknown"
+++

# [include/smp/domain.h](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h)

### struct [`domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `size_t` | [`id`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L10) |
| `size_t` | [`num_cores`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L11) |
| [`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15) | [`**cores`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L12) |
| [`struct numa_node`](https://github.com/bluegummi/charmos/blob/main/include/mem/numa.h#L6) | [`*associated_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L13) |


- [`domain_local()`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L16) — `static inline`[`struct domain *`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)`domain_local(void)`
- [`domain_local_id()`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L20) — `static inline size_t domain_local_id(void)`



+++
title = "smp"
author = "Unknown"
status = "unknown"
+++

# [include/smp/smp.h](https://github.com/bluegummi/charmos/blob/main/include/smp/smp.h)


+++
title = "core"
author = "Unknown"
status = "unknown"
+++

# [include/smp/core.h](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h)

### struct [`core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)

| Member Type | Member Name |
|-------------|-------------|
| [`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15) | [`*self`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L16) |
| `size_t` | [`id`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L17) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*current_thread`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L18) |
| `size_t` | [`domain_cpu_id`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L20) |
| `atomic_bool` | [`idle`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L22) |
| `bool` | [`in_interrupt`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L24) |
| [`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2) | [`current_irql`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L25) |
| `atomic_bool` | [`needs_resched`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L27) |
| `atomic_bool` | [`in_resched`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L28) |
| `atomic_uint_fast32_t` | [`scheduler_preemption_disable_depth`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L29) |
| [`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L31) |
| [`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80) | [`*domain_buddy`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L32) |
| [`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22) | [`*domain_arena`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L33) |
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*slab_domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L34) |
| `size_t` | [`rr_current_domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L35) |
| `struct tss` | [`*tss`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L37) |
| `uint32_t` | [`lapic_freq`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L39) |
| `uint64_t` | [`rcu_seen_gen`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L40) |
| `uint32_t` | [`rcu_nesting`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L41) |
| `bool` | [`rcu_quiescent`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L42) |
| [`struct topology_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L43) | [`*topo_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L44) |
| [`struct topology_cache_info`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L30) | [`llc`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L45) |
| `size_t` | [`numa_node`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L47) |
| `uint32_t` | [`package_id`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L48) |
| `uint32_t` | [`smt_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L49) |
| `uint32_t` | [`smt_id`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L50) |
| `uint32_t` | [`core_id`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L51) |
| `uint64_t` | [`tsc_hz`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L53) |
| `uint64_t` | [`last_us`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L54) |
| `uint64_t` | [`last_tsc`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L55) |
| [`struct dpc`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L9) | [`*tlb_shootdown_dpc`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L57) |


- [`smp_core_id()`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L60) — `static inline uint64_t smp_core_id()`
- [`smp_core()`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L68) — `static inline`[`struct core *`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)`smp_core(void)`



