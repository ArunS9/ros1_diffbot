cmake_minimum_required(VERSION 2.8.3)
project(bot_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES bot_control
#  CATKIN_DEPENDS rospy std_msgs geometry_msgs sensor_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  scripts/my_script.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

