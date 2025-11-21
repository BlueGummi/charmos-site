+++
title = "chacha20"
author = "Unknown"
status = "unknown"
+++

# [kernel/crypto/chacha20.c](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c)

- [`load32_le()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c#L23) — `static uint32_t load32_le(uint8_t *src)`
- [`store32_le()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c#L28) — `static void store32_le(uint8_t *dst`,`uint32_t val)`
- [`chacha20_init_state()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c#L35) — `static void chacha20_init_state(uint32_t state[16]`,`uint8_t key[32]`,`uint8_t nonce[12]`,`uint32_t counter)`
- [`chacha20_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c#L54) — `static void chacha20_block(uint8_t output[64]`,`uint32_t input[16])`
- [`chacha20_encrypt()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/chacha20.c#L78) — `void chacha20_encrypt(uint8_t key[32]`,`uint8_t nonce[12]`,`uint32_t counter`,`uint8_t *in`,`uint8_t *out`,`uint64_t len)`



+++
title = "prng"
author = "Unknown"
status = "unknown"
+++

# [kernel/crypto/prng.c](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/prng.c)

- [`prng_seed()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/prng.c#L5) — `void prng_seed(uint64_t seed)`
- [`prng_next()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/prng.c#L10) — `uint64_t prng_next()`



+++
title = "entropy_pool"
author = "Unknown"
status = "unknown"
+++

# [kernel/crypto/entropy_pool.c](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c)

- [`entropy_pool_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L14) — `void entropy_pool_init(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool)`
- [`entropy_pool_add()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L21) — `void entropy_pool_add(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool`,`uint8_t *data`,`uint64_t len`,`uint64_t entropy_bits)`
- [`entropy_pool_extract()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L37) — `uint64_t entropy_pool_extract(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool`,`uint8_t *out`,`uint64_t len)`
- [`entropy_pool_bits()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L63) — `uint64_t entropy_pool_bits(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool)`
- [`entropy_pool_decrease()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L70) — `void entropy_pool_decrease(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool`,`uint64_t bits)`
- [`entropy_pool_seed()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L79) — `void entropy_pool_seed(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool)`
- [`entropy_pool_reseed()`](https://github.com/bluegummi/charmos/blob/main/kernel/crypto/entropy_pool.c#L91) — `void entropy_pool_reseed(`[`struct entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)` *pool)`



