// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "stalkbot_interface/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "stalkbot_interface/msg/detail/person_open_cv__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace stalkbot_interface
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_stalkbot_interface
cdr_serialize(
  const stalkbot_interface::msg::PersonOpenCv & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_stalkbot_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  stalkbot_interface::msg::PersonOpenCv & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_stalkbot_interface
get_serialized_size(
  const stalkbot_interface::msg::PersonOpenCv & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_stalkbot_interface
max_serialized_size_PersonOpenCv(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace stalkbot_interface

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_stalkbot_interface
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, stalkbot_interface, msg, PersonOpenCv)();

#ifdef __cplusplus
}
#endif

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
