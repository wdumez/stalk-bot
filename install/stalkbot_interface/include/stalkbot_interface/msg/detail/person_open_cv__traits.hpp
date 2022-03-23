// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__TRAITS_HPP_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__TRAITS_HPP_

#include "stalkbot_interface/msg/detail/person_open_cv__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<stalkbot_interface::msg::PersonOpenCv>()
{
  return "stalkbot_interface::msg::PersonOpenCv";
}

template<>
inline const char * name<stalkbot_interface::msg::PersonOpenCv>()
{
  return "stalkbot_interface/msg/PersonOpenCv";
}

template<>
struct has_fixed_size<stalkbot_interface::msg::PersonOpenCv>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<stalkbot_interface::msg::PersonOpenCv>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<stalkbot_interface::msg::PersonOpenCv>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__TRAITS_HPP_
