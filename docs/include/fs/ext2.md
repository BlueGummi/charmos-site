# [include/fs/ext2.h](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h)

<!-- Auto-generated from ext2.h, do not edit manually -->

### struct [`ext2_sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L106)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`inodes_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L107) |
| `uint32_t` | [`blocks_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L108) |
| `uint32_t` | [`r_blocks_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L109) |
| `uint32_t` | [`free_blocks_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L110) |
| `uint32_t` | [`free_inodes_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L111) |
| `uint32_t` | [`first_data_block`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L112) |
| `uint32_t` | [`log_block_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L113) |
| `uint32_t` | [`log_frag_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L114) |
| `uint32_t` | [`blocks_per_group`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L115) |
| `uint32_t` | [`frags_per_group`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L116) |
| `uint32_t` | [`inodes_per_group`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L117) |
| `uint32_t` | [`mtime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L118) |
| `uint32_t` | [`wtime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L119) |
| `uint16_t` | [`mnt_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L120) |
| `uint16_t` | [`max_mnt_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L121) |
| `uint16_t` | [`magic`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L122) |
| `uint16_t` | [`state`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L123) |
| `uint16_t` | [`errors`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L124) |
| `uint16_t` | [`minor_rev_level`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L125) |
| `uint32_t` | [`lastcheck`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L126) |
| `uint32_t` | [`checkinterval`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L127) |
| `uint32_t` | [`creator_os`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L128) |
| `uint32_t` | [`rev_level`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L129) |
| `uint16_t` | [`def_resuid`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L130) |
| `uint16_t` | [`def_resgid`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L131) |
| `uint32_t` | [`first_ino`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L132) |
| `uint16_t` | [`inode_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L133) |
| `uint16_t` | [`block_group_nr`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L134) |
| `uint32_t` | [`feature_compat`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L135) |
| `uint32_t` | [`feature_incompat`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L136) |
| `uint32_t` | [`feature_ro_compat`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L137) |
| `uint8_t` | [`uuid[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L138) |
| `char` | [`volume_name[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L139) |
| `char` | [`last_mounted[64]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L140) |
| `uint32_t` | [`algorithm_usage_bitmap`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L141) |
| `uint8_t` | [`prealloc_blocks`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L142) |
| `uint8_t` | [`prealloc_dir_blocks`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L143) |
| `uint16_t` | [`padding`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L144) |
| `union { struct { uint32_t journal_uuid[4]; uint32_t journal_inum; uint32_t journal_dev; uint32_t last_orphan; uint32_t hash_seed[4]; uint8_t def_hash_version; uint8_t journal_backup_type; uint16_t desc_size; uint32_t default_mount_opts; uint32_t first_meta_bg; uint32_t mkfs_time; uint32_t journal_blocks[17]; uint32_t quota_group_inode;   // [4] → offset 0x258 uint32_t quota_project_inode; // [5] → offset 0x25C }; uint32_t reserved[204]; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L146) |


### struct [`ext2_group_desc`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L167)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`block_bitmap`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L168) |
| `uint32_t` | [`inode_bitmap`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L169) |
| `uint32_t` | [`inode_table`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L170) |
| `uint16_t` | [`free_blocks_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L171) |
| `uint16_t` | [`free_inodes_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L172) |
| `uint16_t` | [`used_dirs_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L173) |
| `uint16_t` | [`pad`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L174) |
| `uint32_t` | [`reserved[3]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L175) |


### struct [`ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)

| Member Type | Member Name |
|-------------|-------------|
| `uint16_t` | [`mode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L179) |
| `uint16_t` | [`uid`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L180) |
| `uint32_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L181) |
| `uint32_t` | [`atime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L182) |
| `uint32_t` | [`ctime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L183) |
| `uint32_t` | [`mtime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L184) |
| `uint32_t` | [`dtime`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L185) |
| `uint16_t` | [`gid`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L186) |
| `uint16_t` | [`links_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L187) |
| `uint32_t` | [`blocks`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L188) |
| `uint32_t` | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L189) |
| `uint32_t` | [`osd1`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L190) |
| `uint32_t` | [`block[EXT2_NBLOCKS]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L192) |
| `uint32_t` | [`generation`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L193) |
| `uint32_t` | [`file_acl`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L194) |
| `uint32_t` | [`dir_acl`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L195) |
| `uint32_t` | [`faddr`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L196) |
| `uint8_t` | [`frag[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L197) |
| `uint8_t` | [`osd2[12]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L198) |


### struct [`ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)

| Member Type | Member Name |
|-------------|-------------|
| [`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178) | [`node`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L202) |
| `uint32_t` | [`inode_num`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L203) |
| [`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18) | [`*ent`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L204) |


### struct [`ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L208) |
| `uint16_t` | [`rec_len`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L209) |
| `uint8_t` | [`name_len`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L210) |
| `uint8_t` | [`file_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L211) |
| `char` | [`name[EXT2_NAME_LEN + 1]`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L212) |


### struct [`ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)

| Member Type | Member Name |
|-------------|-------------|
| [`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41) | [`*partition`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L216) |
| [`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68) | [`*drive`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L217) |
| [`struct ext2_sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L106) | [`*sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L218) |
| [`struct ext2_group_desc`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L167) | [`*group_desc`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L219) |
| [`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18) | [`*sbcache_ent`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L220) |
| [`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18) | [`*gdesc_cache_ent`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L221) |
| `uint32_t` | [`num_groups`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L222) |
| `uint32_t` | [`inodes_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L223) |
| `uint32_t` | [`inodes_per_group`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L224) |
| `uint32_t` | [`blocks_per_group`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L225) |
| `uint32_t` | [`block_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L226) |
| `uint32_t` | [`sectors_per_block`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L227) |
| `uint16_t` | [`inode_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L228) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L231) |


### type alias
[`(*dir_entry_callback)`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L234) : `bool (struct ext2_fs *fs, struct ext2_dir_entry *entry, void *ctx, uint32_t block_num, uint32_t entry_num, uint32_t entry_offset)`
### type alias
[`(*ext2_block_visitor)`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L239) : `void (struct ext2_fs *fs, struct ext2_inode *inode, uint32_t depth, uint32_t *block_ptr, void *user_data)`
- [`ext2_dealloc_inode()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L294) — `static inline void ext2_dealloc_inode(`[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *ino)`
- [`ext2_get_block_group()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L298) — `static inline uint32_t ext2_get_block_group(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block)`
- [`ext2_get_inode_group()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L303) — `static inline uint32_t ext2_get_inode_group(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode)`
- [`ext2_fs_lock()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L308) — `static inline bool ext2_fs_lock(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_fs_unlock()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L312) — `static inline void ext2_fs_unlock(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`bool b)`
- [`ext2_prefetch_block()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L316) — `static inline void ext2_prefetch_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block)`
- [`ext2_inode_lock()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L322) — `static inline void ext2_inode_lock(`[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *ino)`
- [`ext2_inode_unlock()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L326) — `static inline void ext2_inode_unlock(`[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *ino)`
- [`ext2_create_bcache_ent()`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L330) — `static inline uint8_t * ext2_create_bcache_ent(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` **out)`

