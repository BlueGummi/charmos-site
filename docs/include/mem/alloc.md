# [include/mem/alloc.h](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h)

<!-- Auto-generated from alloc.h, do not edit manually -->

### enum [`alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)

| Name | Value |
|------|-------|
| [`ALLOC_FLAG_PREFER_CACHE_ALIGNED`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L58) | `(1 << 0)` |
| [`ALLOC_FLAG_NO_CACHE_ALIGN`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L59) | `(1 << 1)` |
| [`ALLOC_FLAG_FLEXIBLE_LOCALITY`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L62) | `(1 << 2)` |
| [`ALLOC_FLAG_STRICT_LOCALITY`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L63) | `(1 << 3)` |
| [`ALLOC_FLAG_PAGEABLE`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L66) | `(1 << 4)` |
| [`ALLOC_FLAG_NONPAGEABLE`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L67) | `(1 << 5)` |
| [`ALLOC_FLAG_MOVABLE`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L70) | `(1 << 6)` |
| [`ALLOC_FLAG_NONMOVABLE`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L71) | `(1 << 7)` |
| [`ALLOC_FLAG_CLASS_DEFAULT`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L74) | `(0 << ALLOC_CLASS_SHIFT)` |
| [`ALLOC_FLAG_CLASS_INTERLEAVED`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L75) | `(1 << ALLOC_CLASS_SHIFT)` |
| [`ALLOC_FLAG_CLASS_HIGH_BANDWIDTH`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L76) | `(2 << ALLOC_CLASS_SHIFT)` |


### enum [`alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)

| Name | Value |
|------|-------|
| [`ALLOC_BEHAVIOR_NORMAL`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L127) | `None` |
| [`ALLOC_BEHAVIOR_ATOMIC`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L128) | `None` |
| [`ALLOC_BEHAVIOR_NO_WAIT`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L129) | `None` |
| [`ALLOC_BEHAVIOR_NO_RECLAIM`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L130) | `None` |
| [`ALLOC_BEHAVIOR_FAULT_SAFE`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L131) | `None` |
| [`ALLOC_BEHAVIOR_FLAG_FAST`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L132) | `1 << ALLOC_BEHAVIOR_FLAG_SHIFT` |


- [`alloc_flags_valid()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L84) — `static inline bool alloc_flags_valid(uint16_t flags)`
- [`alloc_behavior_base()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L169) — `static inline`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)`alloc_behavior_base(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_behavior_may_fault()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L174) — `static inline bool alloc_behavior_may_fault(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_behavior_may_block()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L183) — `static inline bool alloc_behavior_may_block(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_behavior_is_isr_safe()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L192) — `static inline bool alloc_behavior_is_isr_safe(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_behavior_no_reclaim()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L197) — `static inline bool alloc_behavior_no_reclaim(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_behavior_is_fast()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L203) — `static inline bool alloc_behavior_is_fast(`[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` raw)`
- [`alloc_flag_behavior_verify()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L207) — `static inline bool alloc_flag_behavior_verify(`[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` f`,[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` behavior)`
- [`alloc_request_sanitize()`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L224) — `static inline void alloc_request_sanitize(`[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` *f`,[`enum alloc_behavior`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L126)` *b)`

