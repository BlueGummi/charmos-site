+++
title = "chacha20"
author = "Unknown"
status = "unknown"
+++

# [include/crypto/chacha20.h](https://github.com/bluegummi/charmos/blob/main/include/crypto/chacha20.h)


+++
title = "prng"
author = "Unknown"
status = "unknown"
+++

# [include/crypto/prng.h](https://github.com/bluegummi/charmos/blob/main/include/crypto/prng.h)


+++
title = "entropy_pool"
author = "Unknown"
status = "unknown"
+++

# [include/crypto/entropy_pool.h](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h)

### struct [`entropy_pool`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L7)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`buffer[ENTROPY_POOL_SIZE]`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L8) |
| `uint64_t` | [`write_pos`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L9) |
| `uint64_t` | [`entropy_bits`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L10) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/crypto/entropy_pool.h#L11) |



