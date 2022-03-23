// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__BUILDER_HPP_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__BUILDER_HPP_

#include "stalkbot_interface/msg/detail/person_open_cv__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace stalkbot_interface
{

namespace msg
{

namespace builder
{

class Init_PersonOpenCv_face_detected
{
public:
  explicit Init_PersonOpenCv_face_detected(::stalkbot_interface::msg::PersonOpenCv & msg)
  : msg_(msg)
  {}
  ::stalkbot_interface::msg::PersonOpenCv face_detected(::stalkbot_interface::msg::PersonOpenCv::_face_detected_type arg)
  {
    msg_.face_detected = std::move(arg);
    return std::move(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

class Init_PersonOpenCv_person_detected
{
public:
  explicit Init_PersonOpenCv_person_detected(::stalkbot_interface::msg::PersonOpenCv & msg)
  : msg_(msg)
  {}
  Init_PersonOpenCv_face_detected person_detected(::stalkbot_interface::msg::PersonOpenCv::_person_detected_type arg)
  {
    msg_.person_detected = std::move(arg);
    return Init_PersonOpenCv_face_detected(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

class Init_PersonOpenCv_foot_y
{
public:
  explicit Init_PersonOpenCv_foot_y(::stalkbot_interface::msg::PersonOpenCv & msg)
  : msg_(msg)
  {}
  Init_PersonOpenCv_person_detected foot_y(::stalkbot_interface::msg::PersonOpenCv::_foot_y_type arg)
  {
    msg_.foot_y = std::move(arg);
    return Init_PersonOpenCv_person_detected(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

class Init_PersonOpenCv_foot_x
{
public:
  explicit Init_PersonOpenCv_foot_x(::stalkbot_interface::msg::PersonOpenCv & msg)
  : msg_(msg)
  {}
  Init_PersonOpenCv_foot_y foot_x(::stalkbot_interface::msg::PersonOpenCv::_foot_x_type arg)
  {
    msg_.foot_x = std::move(arg);
    return Init_PersonOpenCv_foot_y(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

class Init_PersonOpenCv_head_y
{
public:
  explicit Init_PersonOpenCv_head_y(::stalkbot_interface::msg::PersonOpenCv & msg)
  : msg_(msg)
  {}
  Init_PersonOpenCv_foot_x head_y(::stalkbot_interface::msg::PersonOpenCv::_head_y_type arg)
  {
    msg_.head_y = std::move(arg);
    return Init_PersonOpenCv_foot_x(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

class Init_PersonOpenCv_head_x
{
public:
  Init_PersonOpenCv_head_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PersonOpenCv_head_y head_x(::stalkbot_interface::msg::PersonOpenCv::_head_x_type arg)
  {
    msg_.head_x = std::move(arg);
    return Init_PersonOpenCv_head_y(msg_);
  }

private:
  ::stalkbot_interface::msg::PersonOpenCv msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::stalkbot_interface::msg::PersonOpenCv>()
{
  return stalkbot_interface::msg::builder::Init_PersonOpenCv_head_x();
}

}  // namespace stalkbot_interface

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__BUILDER_HPP_
