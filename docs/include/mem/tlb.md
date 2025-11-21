# [include/mem/tlb.h](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h)

<!-- Auto-generated from tlb.h, do not edit manually -->

### struct [`tlb_shootdown_cpu`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_uintptr_t` | [`queue[TLB_QUEUE_SIZE]`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L10) |
| `atomic_uint_fast32_t` | [`head`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L11) |
| `atomic_uint_fast32_t` | [`tail`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L12) |
| `atomic_uint_fast8_t` | [`ipi_pending`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L13) |
| `atomic_uint_fast64_t` | [`ack_gen`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L14) |
| `atomic_uint_fast8_t` | [`flush_all`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L15) |
| `atomic_uint_fast8_t` | [`dpc_queued`](https://github.com/bluegummi/charmos/blob/main/include/mem/tlb.h#L16) |

