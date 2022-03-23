// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from stalkbot_interface:msg/PersonOpenCv.idl
// generated code does not contain a copyright notice

#ifndef STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_HPP_
#define STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__stalkbot_interface__msg__PersonOpenCv __attribute__((deprecated))
#else
# define DEPRECATED__stalkbot_interface__msg__PersonOpenCv __declspec(deprecated)
#endif

namespace stalkbot_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PersonOpenCv_
{
  using Type = PersonOpenCv_<ContainerAllocator>;

  explicit PersonOpenCv_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->head_x = 0l;
      this->head_y = 0l;
      this->foot_x = 0l;
      this->foot_y = 0l;
      this->person_detected = false;
      this->face_detected = false;
    }
  }

  explicit PersonOpenCv_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->head_x = 0l;
      this->head_y = 0l;
      this->foot_x = 0l;
      this->foot_y = 0l;
      this->person_detected = false;
      this->face_detected = false;
    }
  }

  // field types and members
  using _head_x_type =
    int32_t;
  _head_x_type head_x;
  using _head_y_type =
    int32_t;
  _head_y_type head_y;
  using _foot_x_type =
    int32_t;
  _foot_x_type foot_x;
  using _foot_y_type =
    int32_t;
  _foot_y_type foot_y;
  using _person_detected_type =
    bool;
  _person_detected_type person_detected;
  using _face_detected_type =
    bool;
  _face_detected_type face_detected;

  // setters for named parameter idiom
  Type & set__head_x(
    const int32_t & _arg)
  {
    this->head_x = _arg;
    return *this;
  }
  Type & set__head_y(
    const int32_t & _arg)
  {
    this->head_y = _arg;
    return *this;
  }
  Type & set__foot_x(
    const int32_t & _arg)
  {
    this->foot_x = _arg;
    return *this;
  }
  Type & set__foot_y(
    const int32_t & _arg)
  {
    this->foot_y = _arg;
    return *this;
  }
  Type & set__person_detected(
    const bool & _arg)
  {
    this->person_detected = _arg;
    return *this;
  }
  Type & set__face_detected(
    const bool & _arg)
  {
    this->face_detected = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> *;
  using ConstRawPtr =
    const stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__stalkbot_interface__msg__PersonOpenCv
    std::shared_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__stalkbot_interface__msg__PersonOpenCv
    std::shared_ptr<stalkbot_interface::msg::PersonOpenCv_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PersonOpenCv_ & other) const
  {
    if (this->head_x != other.head_x) {
      return false;
    }
    if (this->head_y != other.head_y) {
      return false;
    }
    if (this->foot_x != other.foot_x) {
      return false;
    }
    if (this->foot_y != other.foot_y) {
      return false;
    }
    if (this->person_detected != other.person_detected) {
      return false;
    }
    if (this->face_detected != other.face_detected) {
      return false;
    }
    return true;
  }
  bool operator!=(const PersonOpenCv_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PersonOpenCv_

// alias to use template instance with default allocator
using PersonOpenCv =
  stalkbot_interface::msg::PersonOpenCv_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace stalkbot_interface

#endif  // STALKBOT_INTERFACE__MSG__DETAIL__PERSON_OPEN_CV__STRUCT_HPP_
