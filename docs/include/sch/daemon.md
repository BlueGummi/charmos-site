# [include/sch/daemon.h](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h)

<!-- Auto-generated from daemon.h, do not edit manually -->

### struct [`daemon_thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L20)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list_node`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L21) |
| `bool` | [`background`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L22) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L23) |
| [`struct daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L86) | [`*daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L24) |
| `atomic_bool` | [`executing_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L26) |
| [`enum daemon_thread_command`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L10) | [`command`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L27) |


### struct [`daemon_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L39)

| Member Type | Member Name |
|-------------|-------------|
| `daemon_fn` | [`function`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L40) |
| [`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17) | [`args`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L41) |
| [`struct daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L86) | [`*daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L42) |
| `void` | [`*private`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L43) |


### struct [`daemon_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L57)

| Member Type | Member Name |
|-------------|-------------|
| `size_t` | [`max_timesharing_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L58) |
| `atomic_size_t` | [`timesharing_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L59) |
| `atomic_size_t` | [`idle_timesharing_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L60) |
| `atomic_bool` | [`background_thread_present`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L61) |
| `int64_t` | [`thread_cpu`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L66) |
| [`enum daemon_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L48) | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L68) |


### struct [`daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L86)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L87) |
| [`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9) | [`ts_sem`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L88) |
| [`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9) | [`bg_sem`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L89) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`timesharing_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L91) |
| [`struct daemon_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L39) | [`*timesharing_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L92) |
| [`struct daemon_thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L20) | [`*background_thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L94) |
| [`struct daemon_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L39) | [`*background_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L95) |
| [`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194) | [`*workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L97) |
| [`struct daemon_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L57) | [`attrs`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L99) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L101) |
| [`enum daemon_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L71) | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L102) |


### enum [`daemon_thread_command`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L10)

| Name | Value |
|------|-------|
| [`DAEMON_THREAD_COMMAND_NONE`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L11) | `None` |
| [`DAEMON_THREAD_COMMAND_EXIT`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L12) | `None` |
| [`DAEMON_THREAD_COMMAND_RESTART`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L13) | `None` |
| [`DAEMON_THREAD_COMMAND_SLEEP`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L14) | `None` |
| [`DAEMON_THREAD_COMMAND_DEFAULT`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L15) | `DAEMON_THREAD_COMMAND_SLEEP` |


### enum [`daemon_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L48)

| Name | Value |
|------|-------|
| [`DAEMON_FLAG_HAS_WORKQUEUE`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L49) | `1` |
| [`DAEMON_FLAG_HAS_NAME`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L50) | `1 << 1` |
| [`DAEMON_FLAG_AUTO_SPAWN`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L51) | `1 << 2` |
| [`DAEMON_FLAG_NO_TS_THREADS`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L52) | `1 << 3` |
| [`DAEMON_FLAG_UNMIGRATABLE_THREADS`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L53) | `1 << 4` |
| [`DAEMON_FLAG_NONE`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L54) | `0` |


### enum [`daemon_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L71)

| Name | Value |
|------|-------|
| [`DAEMON_STATE_ACTIVE`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L72) | `None` |
| [`DAEMON_STATE_DESTROYING`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L73) | `None` |
| [`DAEMON_STATE_DEAD`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L74) | `None` |


### type alias
[`(*daemon_fn)`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L32) : `enum daemon_thread_command (struct daemon_work *work, struct daemon_thread *executor, void *arg, void *arg2)`
- [`daemon_state_str()`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L77) — `static inline const char * daemon_state_str(`[`enum daemon_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L71)` s)`

