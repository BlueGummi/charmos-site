# [kernel/ubsan.c](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c)

<!-- Auto-generated from ubsan.c, do not edit manually -->

### struct [`ubsan_function_type_mismatch_data`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L87)

| Member Type | Member Name |
|-------------|-------------|
| [`source_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L19) | [`location`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L88) |
| `struct type_descriptor_t` | [`*type`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L89) |


### type alias
[`source_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L19) : `struct { const char *filename; uint32_t line; uint32_t column; }`
### type alias
[`type_descriptor_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L25) : `struct { uint16_t kind; uint16_t info; char name[]; }`
### type alias
[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31) : `struct { source_location_t location; }`
### type alias
[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35) : `struct { source_location_t location; type_descriptor_t *type; }`
### type alias
[`data_load_invalid_value_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L40) : `struct { source_location_t location; type_descriptor_t *type; }`
### type alias
[`data_nonnull_arg_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L45) : `struct { source_location_t location; source_location_t attr_location; int arg_index; }`
### type alias
[`data_shift_out_of_bounds_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L51) : `struct { source_location_t location; type_descriptor_t *lhs_type; type_descriptor_t *rhs_type; }`
### type alias
[`data_out_of_bounds_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L57) : `struct { source_location_t location; type_descriptor_t *array_type; type_descriptor_t *index_type; }`
### type alias
[`data_type_mismatch_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L63) : `struct { source_location_t location; type_descriptor_t *type; uint8_t alignment; uint8_t type_check_kind; }`
### type alias
[`data_alignment_assumption_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L70) : `struct { source_location_t location; source_location_t assumption_location; type_descriptor_t *type; }`
### type alias
[`data_implicit_conversion_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L76) : `struct { source_location_t location; type_descriptor_t *from_type; type_descriptor_t *to_type; uint8_t kind; }`
### type alias
[`data_invalid_builtin_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L83) : `struct { source_location_t location; uint8_t kind; }`
- [`kind_to_type()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L91) — `const char * kind_to_type(uint16_t kind)`
- [`info_to_bits()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L101) — `unsigned int info_to_bits(uint16_t info)`
- [`__ubsan_handle_load_invalid_value()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L104) — `void __ubsan_handle_load_invalid_value(`[`data_load_invalid_value_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L40)` *data`,`uintptr_t value)`
- [`__ubsan_handle_nonnull_arg()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L111) — `void __ubsan_handle_nonnull_arg(`[`data_nonnull_arg_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L45)` *data)`
- [`__ubsan_handle_nullability_arg()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L117) — `void __ubsan_handle_nullability_arg(`[`data_nonnull_arg_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L45)` *data)`
- [`__ubsan_handle_nonnull_return_v1()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L123) — `void __ubsan_handle_nonnull_return_v1(`[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31)` *data
                                      [[maybe_unused]]`,[`source_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L19)` *location)`
- [`__ubsan_handle_nullability_return_v1()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L130) — `void __ubsan_handle_nullability_return_v1(`[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31)` *data
                                          [[maybe_unused]]`,[`source_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L19)` *location)`
- [`__ubsan_handle_vla_bound_not_positive()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L137) — `void __ubsan_handle_vla_bound_not_positive(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t bound)`
- [`__ubsan_handle_add_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L147) — `void __ubsan_handle_add_overflow(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t lhs`,`uintptr_t rhs)`
- [`__ubsan_handle_sub_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L157) — `void __ubsan_handle_sub_overflow(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t lhs`,`uintptr_t rhs)`
- [`__ubsan_handle_mul_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L167) — `void __ubsan_handle_mul_overflow(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t lhs`,`uintptr_t rhs)`
- [`__ubsan_handle_function_type_mismatch()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L177) — `void __ubsan_handle_function_type_mismatch(void *data_raw`,`void *value_raw)`
- [`__ubsan_handle_divrem_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L185) — `void __ubsan_handle_divrem_overflow(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t lhs`,`uintptr_t rhs)`
- [`__ubsan_handle_negate_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L194) — `void __ubsan_handle_negate_overflow(`[`data_location_type_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L35)` *data`,`uintptr_t old)`
- [`__ubsan_handle_shift_out_of_bounds()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L202) — `void __ubsan_handle_shift_out_of_bounds(`[`data_shift_out_of_bounds_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L51)` *data`,`uintptr_t lhs`,`uintptr_t rhs)`
- [`__ubsan_handle_out_of_bounds()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L214) — `void __ubsan_handle_out_of_bounds(`[`data_out_of_bounds_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L57)` *data`,`uint64_t index)`
- [`__ubsan_handle_type_mismatch()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L226) — `void __ubsan_handle_type_mismatch(`[`data_type_mismatch_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L63)` *data`,`void *pointer)`
- [`__ubsan_handle_type_mismatch_v1()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L262) — `void __ubsan_handle_type_mismatch_v1(`[`data_type_mismatch_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L63)` *data`,`void *pointer)`
- [`__ubsan_handle_alignment_assumption()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L300) — `void __ubsan_handle_alignment_assumption(`[`data_alignment_assumption_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L70)` *data`,`void *`,`void *`,`void *)`
- [`__ubsan_handle_implicit_conversion()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L307) — `void __ubsan_handle_implicit_conversion(`[`data_implicit_conversion_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L76)` *data`,`void *`,`void *)`
- [`__ubsan_handle_invalid_builtin()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L313) — `void __ubsan_handle_invalid_builtin(`[`data_invalid_builtin_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L83)` *data)`
- [`__ubsan_handle_pointer_overflow()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L318) — `void __ubsan_handle_pointer_overflow(`[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31)` *data`,`void *`,`void *)`
- [`__ubsan_handle_builtin_unreachable()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L324) — `void __ubsan_handle_builtin_unreachable(`[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31)` *data)`
- [`__ubsan_handle_missing_return()`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L330) — `void __ubsan_handle_missing_return(`[`data_only_location_t`](https://github.com/bluegummi/charmos/blob/main/kernel/ubsan.c#L31)` *data)`

