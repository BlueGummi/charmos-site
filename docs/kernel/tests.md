+++
title = "sched"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/sched.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c)

- [`workqueue_fn()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c#L12) — `static void workqueue_fn(void *arg`,`void *unused)`
- [`sleepy_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c#L48) — `static void sleepy_entry(void)`
- [`wq_test_2()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c#L63) — `static void wq_test_2(void *a`,`void *b)`
- [`enqueue_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c#L73) — `static void enqueue_thread(void)`
- [`daemon_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/sched.c#L120) — `static`[`enum daemon_thread_command`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L10)`daemon_work(`[`struct daemon_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L39)` *work`,[`struct daemon_thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L20)` *thread`,`void *a`,`void *b)`



+++
title = "defer"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/defer.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/defer.c)

- [`defer_func()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/defer.c#L16) — `static void defer_func(void *boo`,`void *unused)`



+++
title = "ext2"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/ext2.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/ext2.c)

- [`flush()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/ext2.c#L37) — `static void flush()`



+++
title = "mem"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/mem.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c)

### struct [`stress_arg`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c#L281)

| Member Type | Member Name |
|-------------|-------------|
| `int` | [`id`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c#L282) |
| `int` | [`*done_flag`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c#L283) |


- [`mt_kmalloc_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c#L122) — `static void mt_kmalloc_worker()`
- [`stress_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mem.c#L288) — `static void stress_worker()`



+++
title = "rcu"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/rcu.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c)

### struct [`rcu_test_data`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c#L12)

| Member Type | Member Name |
|-------------|-------------|
| `int` | [`value`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c#L13) |


- [`rcu_reader_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c#L20) — `static void rcu_reader_thread(void)`
- [`rcu_free_fn()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c#L44) — `static void rcu_free_fn(void *ptr)`
- [`rcu_writer_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/rcu.c#L50) — `static void rcu_writer_thread(void)`



+++
title = "mutex"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/mutex.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mutex.c)

- [`contender()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mutex.c#L19) — `static void contender()`
- [`many_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mutex.c#L45) — `static void many_worker()`
- [`chaos()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mutex.c#L71) — `static void chaos()`



+++
title = "apc"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/apc.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/apc.c)

- [`the_apc()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/apc.c#L10) — `static void the_apc(`[`struct apc`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L35)` *a`,`void *arg1`,`void *arg2)`
- [`apc_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/apc.c#L15) — `static void apc_thread(void)`



+++
title = "tmpfs"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/tmpfs.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/tmpfs.c)


+++
title = "bio_sched"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/bio_sched.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio_sched.c)

- [`bio_sch_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio_sched.c#L29) — `static void bio_sch_callback(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sch_callback1()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio_sched.c#L42) — `static void bio_sch_callback1(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sch_callback2()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio_sched.c#L49) — `static void bio_sch_callback2(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`



+++
title = "runner"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/runner.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/runner.c)

- [`run()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/runner.c#L22) — `static void run(bool run_units`,[`struct kernel_test`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L10)` *start`,[`struct kernel_test`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L10)` *end)`
- [`tests_run()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/runner.c#L66) — `void tests_run(void)`



+++
title = "minheap"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/minheap.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/minheap.c)

- [`mhtest_do_inserts()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/minheap.c#L9) — `static void mhtest_do_inserts(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *mh)`



+++
title = "test"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/test.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/test.c)


+++
title = "bio"
author = "Unknown"
status = "unknown"
+++

# [kernel/tests/bio.c](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio.c)

- [`bio_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/bio.c#L25) — `static void bio_callback(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`



