// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice
#include "stalkbot_interface/msg/detail/person_open_cv__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
stalkbot_interface__msg__PersonOpenCv__init(stalkbot_interface__msg__PersonOpenCv * msg)
{
  if (!msg) {
    return false;
  }
  // head_x
  // head_y
  // foot_x
  // foot_y
  // person_detected
  // face_detected
  return true;
}

void
stalkbot_interface__msg__PersonOpenCv__fini(stalkbot_interface__msg__PersonOpenCv * msg)
{
  if (!msg) {
    return;
  }
  // head_x
  // head_y
  // foot_x
  // foot_y
  // person_detected
  // face_detected
}

stalkbot_interface__msg__PersonOpenCv *
stalkbot_interface__msg__PersonOpenCv__create()
{
  stalkbot_interface__msg__PersonOpenCv * msg = (stalkbot_interface__msg__PersonOpenCv *)malloc(sizeof(stalkbot_interface__msg__PersonOpenCv));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(stalkbot_interface__msg__PersonOpenCv));
  bool success = stalkbot_interface__msg__PersonOpenCv__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
stalkbot_interface__msg__PersonOpenCv__destroy(stalkbot_interface__msg__PersonOpenCv * msg)
{
  if (msg) {
    stalkbot_interface__msg__PersonOpenCv__fini(msg);
  }
  free(msg);
}


bool
stalkbot_interface__msg__PersonOpenCv__Sequence__init(stalkbot_interface__msg__PersonOpenCv__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  stalkbot_interface__msg__PersonOpenCv * data = NULL;
  if (size) {
    data = (stalkbot_interface__msg__PersonOpenCv *)calloc(size, sizeof(stalkbot_interface__msg__PersonOpenCv));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = stalkbot_interface__msg__PersonOpenCv__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        stalkbot_interface__msg__PersonOpenCv__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
stalkbot_interface__msg__PersonOpenCv__Sequence__fini(stalkbot_interface__msg__PersonOpenCv__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      stalkbot_interface__msg__PersonOpenCv__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

stalkbot_interface__msg__PersonOpenCv__Sequence *
stalkbot_interface__msg__PersonOpenCv__Sequence__create(size_t size)
{
  stalkbot_interface__msg__PersonOpenCv__Sequence * array = (stalkbot_interface__msg__PersonOpenCv__Sequence *)malloc(sizeof(stalkbot_interface__msg__PersonOpenCv__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = stalkbot_interface__msg__PersonOpenCv__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
stalkbot_interface__msg__PersonOpenCv__Sequence__destroy(stalkbot_interface__msg__PersonOpenCv__Sequence * array)
{
  if (array) {
    stalkbot_interface__msg__PersonOpenCv__Sequence__fini(array);
  }
  free(array);
}
