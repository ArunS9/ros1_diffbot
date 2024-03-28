# bot_description Package

This package contains the robot description files for the <insert robot name>.

## Description

The `bot_description` package provides the necessary URDF (Unified Robot Description Format) files for describing the robot's physical structure, as well as configuration files for simulating the robot in Gazebo and visualizing it in RViz.

## Contents

- `urdf/`: Contains the URDF files describing the robot's physical structure.
- `launch/`: Contains launch files for launching the robot in simulation environments.

## Dependencies

This package depends on the following ROS packages:
- `gazebo_ros`: For simulating the robot in Gazebo.
- `rviz`: For visualizing the robot in RViz.
- `teleop_twist_keyboard`: For tele-operating the robot using keyboard commands.

## Usage

1. Clone this package into your ROS workspace:

git clone <repository_url> <your_workspace>/src/bot_description


2. Build your workspace:

cd <your_workspace>
catkin_make


3. Launch the robot in Gazebo:

roslaunch bot_description spawn.launch


4. Visualize the robot in RViz:

roslaunch bot_description rviz.launch


5. Tele-operate the robot using keyboard commands:

roslaunch bot_description control.launch



