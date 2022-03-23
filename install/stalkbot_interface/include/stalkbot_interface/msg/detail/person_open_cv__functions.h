// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__FUNCTIONS_H_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "stalkbot_interface/msg/rosidl_generator_c__visibility_control.h"

#include "stalkbot_interface/msg/detail/person_open_cv__struct.h"

/// Initialize msg/PersonOpenCv message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * stalkbot_interface__msg__PersonOpenCv
 * )) before or use
 * stalkbot_interface__msg__PersonOpenCv__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
bool
stalkbot_interface__msg__PersonOpenCv__init(stalkbot_interface__msg__PersonOpenCv * msg);

/// Finalize msg/PersonOpenCv message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
void
stalkbot_interface__msg__PersonOpenCv__fini(stalkbot_interface__msg__PersonOpenCv * msg);

/// Create msg/PersonOpenCv message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * stalkbot_interface__msg__PersonOpenCv__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
stalkbot_interface__msg__PersonOpenCv *
stalkbot_interface__msg__PersonOpenCv__create();

/// Destroy msg/PersonOpenCv message.
/**
 * It calls
 * stalkbot_interface__msg__PersonOpenCv__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
void
stalkbot_interface__msg__PersonOpenCv__destroy(stalkbot_interface__msg__PersonOpenCv * msg);


/// Initialize array of msg/PersonOpenCv messages.
/**
 * It allocates the memory for the number of elements and calls
 * stalkbot_interface__msg__PersonOpenCv__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
bool
stalkbot_interface__msg__PersonOpenCv__Sequence__init(stalkbot_interface__msg__PersonOpenCv__Sequence * array, size_t size);

/// Finalize array of msg/PersonOpenCv messages.
/**
 * It calls
 * stalkbot_interface__msg__PersonOpenCv__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
void
stalkbot_interface__msg__PersonOpenCv__Sequence__fini(stalkbot_interface__msg__PersonOpenCv__Sequence * array);

/// Create array of msg/PersonOpenCv messages.
/**
 * It allocates the memory for the array and calls
 * stalkbot_interface__msg__PersonOpenCv__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
stalkbot_interface__msg__PersonOpenCv__Sequence *
stalkbot_interface__msg__PersonOpenCv__Sequence__create(size_t size);

/// Destroy array of msg/PersonOpenCv messages.
/**
 * It calls
 * stalkbot_interface__msg__PersonOpenCv__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_stalkbot_interface
void
stalkbot_interface__msg__PersonOpenCv__Sequence__destroy(stalkbot_interface__msg__PersonOpenCv__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__FUNCTIONS_H_
