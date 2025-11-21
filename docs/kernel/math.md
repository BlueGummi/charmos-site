+++
title = "levenshtein"
author = "Unknown"
status = "unknown"
+++

# [kernel/math/levenshtein.c](https://github.com/bluegummi/charmos/blob/main/kernel/math/levenshtein.c)

- [`levenshtein_distance()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/levenshtein.c#L7) — `int64_t levenshtein_distance(char *s1`,`char *s2)`



+++
title = "sort"
author = "Unknown"
status = "unknown"
+++

# [kernel/math/sort.c](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c)

### type alias
[`cmp_t`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L180) : `int (void *, void *, void *)`
### type alias
[`cmp_t`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L182) : `int (void *, void *)`
- [`heapsort()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L126) — `int heapsort(void *vbase`,`size_t nmemb`,`size_t size`,`int (*compar)(const void *`,` const void *))`
- [`swapfunc()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L212) — `static inline void swapfunc(char *a`,`char *b`,`size_t n`,`size_t swaptype)`
- [`med3()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L239) — `static inline char * med3(char *a`,`char *b`,`char *c`,[`cmp_t`](https://github.com/bluegummi/charmos/blob/main/include/math/sort.h#L3)` *cmp`,`void *thunk)`
- [`flsl_like()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L249) — `int flsl_like(unsigned long x)`
- [`_qsort()`](https://github.com/bluegummi/charmos/blob/main/kernel/math/sort.c#L261) — `static void _qsort(void *a`,`size_t n`,`size_t es`,`I_AM_QSORT_R *thunk`,`thunk *cmp`,`int depth_limit)`



