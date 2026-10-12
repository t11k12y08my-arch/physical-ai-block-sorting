cmake_minimum_required(VERSION 3.5)
project(physical_ai_block_sorting)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(
  PROGRAMS
    ai_inference_node.py
    control_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

