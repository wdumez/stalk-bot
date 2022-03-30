// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_H_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/PersonOpenCv in the package stalkbot_interface.
typedef struct stalkbot_interface__msg__PersonOpenCv
{
  int32_t head_x;
  int32_t head_y;
  int32_t foot_x;
  int32_t foot_y;
  bool person_detected;
  bool face_detected;
} stalkbot_interface__msg__PersonOpenCv;

// Struct for a sequence of stalkbot_interface__msg__PersonOpenCv.
typedef struct stalkbot_interface__msg__PersonOpenCv__Sequence
{
  stalkbot_interface__msg__PersonOpenCv * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} stalkbot_interface__msg__PersonOpenCv__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_H_
