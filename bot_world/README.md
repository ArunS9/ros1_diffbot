# bot_world Package

This package contains Gazebo world files and launch files to simulate the robot in a virtual environment.

## How to Test

1. Clone the package into your ROS workspace:

    ```bash
    git clone <URL_TO_BOT_WORLD_REPO> /path/to/your/ros/workspace/src/bot_world
    ```

2. Build your ROS workspace:

    ```bash
    cd /path/to/your/ros/workspace
    catkin_make
    ```

3. Source your ROS workspace:

    ```bash
    source devel/setup.bash
    ```

4. Launch the bot_world.launch file to load the Gazebo world and spawn the robot URDF in the center:

    ```bash
    roslaunch bot_world bot_world.launch
    ```

5. Gazebo should launch with the specified world file, and the robot should be spawned in the center of the world.

## Additional Notes

- Make sure you have Gazebo installed to simulate the robot in a virtual environment.
- If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository.


