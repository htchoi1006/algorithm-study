#include "Camera.h"

// TODO: fill up the following function properly 
void Camera::set_rotation(const glm::quat& _q)
{
  right_dir_ = glm::normalize(glm::mat3_cast(_q) * glm::vec3(1.0f, 0.0f, 0.0f));
  up_dir_ = glm::normalize(glm::mat3_cast(_q) * glm::vec3(0.0f, 1.0f, 0.0f));
  front_dir_ = glm::normalize(glm::mat3_cast(_q) * glm::vec3(0.0f, 0.0f, -1.0f));
  get_view_matrix();
} 

// TODO: re-write the following function properly 
const glm::quat Camera::get_rotation() const
{
  return glm::quat_cast(glm::mat3(right_dir_, up_dir_, -front_dir_));
  get_view_matrix();
}

// TODO: fill up the following function properly 
void Camera::set_pose(const glm::quat& _q, const glm::vec3& _t)
{
  set_rotation(_q);
  position_ = _t;
  get_view_matrix();
}

// TODO: fill up the following function properly 
void Camera::get_pose(glm::quat& _q, glm::vec3& _t) const
{
  _q = get_rotation();
  _t = position_;
  get_view_matrix();
}

// TODO: rewrite the following function properly 
const glm::mat4 Camera::get_pose() const
{
  return glm::translate(glm::mat4(1.0f), position_) * glm::mat4_cast(get_rotation());
  get_view_matrix();
}

// TODO: fill up the following function properly 
void Camera::set_pose(const glm::mat4& _frame)
{
  // +x_cam: right direction of the camera    (it should be a unit vector whose length is 1)
  // right_dir_ = ..... ; // +x
  // +y_cam: up direction of the camera       (it should be a unit vector whose length is 1)   
  // up_dir_    = ..... ;    // +y
  // -z_cam: front direction of the camera    (it should be a unit vector whose length is 1)
  // front_dir_ = ..... ;    // -z
  // pos_cam: position of the camera
  // position_  = ..... ;    // pos
  right_dir_ = glm::normalize(glm::vec3(_frame[0]));
  up_dir_ = glm::normalize(glm::vec3(_frame[1]));
  front_dir_ = -glm::normalize(glm::vec3(_frame[2]));
  position_ = glm::vec3(_frame[3]);
  get_view_matrix();
}

// TODO: fill up the following function properly 
void Camera::set_pose(const glm::vec3& _pos, const glm::vec3& _at, const glm::vec3& _up_dir)
{
  // up_dir_    = ..... ;
  // front_dir_ = ..... ;    // -z_cam direction
  // right_dir_ = ..... ;    // +x_cam direction
  // up_dir_    = ..... ;    // +y_cam direction

  // position_  = ..... ;      // pos
  position_ = _pos;
  front_dir_ = glm::normalize(_pos - _at);
  right_dir_ = glm::normalize(glm::cross(_up_dir, front_dir_));
  up_dir_ = glm::normalize(glm::cross(front_dir_, right_dir_));
  get_view_matrix();

}

// TODO: rewrite the following function properly 
const glm::mat4 Camera::get_view_matrix() const
{
  return glm::lookAt(position_, position_ + front_dir_, up_dir_);
  get_view_matrix();
}

// TODO: rewrite the following function properly 
const glm::mat4 Camera::get_projection_matrix() const
{
  // TODO: Considering the followings,
  //       You must return a proper projection matrix
  //       i) camera mode: it can be either kOrtho or kPerspective
  //       ii) zoom-in/-out: if the camera mode is kOrtho, 
  //                         utilize ortho_scale_ for zoom-in/-out
  //                         if the camera mode is kPerspective,
  //                         utilize fovy_ for zoom-in/-out
  //       iii) aspect ratio: utilize aspect_ in the both camera modes
  //       iv) near/far clipping planes: utilize near_, far_

  if (mode_ == kOrtho)
  {
    float halfWidth = ortho_scale_ * aspect_ / 2.0f;
    float halfHeight = ortho_scale_ / 2.0f;
    return glm::ortho(-halfWidth, halfWidth, -halfHeight, halfHeight, near_, far_);
    get_view_matrix();
  }
  else
  {
    return glm::perspective(glm::radians(fovy_), aspect_, near_, far_);
    get_view_matrix();
  }
}

// TODO: fill up the following functions properly 
void Camera::move_forward(float delta)
{
  position_ += delta * front_dir_;
  get_view_matrix();
}

// TODO: fill up the following functions properly 
void Camera::move_backward(float delta)
{
  position_ -= delta * front_dir_;
  get_view_matrix();
}

// TODO: fill up the following functions properly 
void Camera::move_left(float delta)
{
  position_ -= glm::normalize(glm::cross(front_dir_, up_dir_)) * delta;
  get_view_matrix();
}

// TODO: fill up the following functions properly 
void Camera::move_right(float delta)
{
  position_ += glm::normalize(glm::cross(front_dir_, up_dir_)) * delta;
  get_view_matrix();
}

// TODO: fill up the following functions properly 
void Camera::move_up(float delta)
{
  position_ += delta * up_dir_;
  get_view_matrix();
}

// TODO: fill up the following functions properly 
void Camera::move_down(float delta)
{
  position_ -= delta * up_dir_;
  get_view_matrix();
}
