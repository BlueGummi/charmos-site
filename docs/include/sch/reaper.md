+++
title = "reaper"
author = "Unknown"
status = "unknown"
+++

# [include/sch/reaper.h](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h)

### struct [`thread_reaper`](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h#L6)

| Member Type | Member Name |
|-------------|-------------|
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h#L7) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h#L8) |
| [`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11) | [`cv`](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h#L9) |
| `uint64_t` | [`reaped_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/reaper.h#L10) |

