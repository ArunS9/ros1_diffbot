# bot_control Package

This package contains scripts and launch files for controlling and visualizing laser scan data.

## How to Test

1. Clone the package into your ROS workspace:

    ```bash
    git clone <URL_TO_BOT_CONTROL_REPO> /path/to/your/ros/workspace/src/bot_control
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

4. Launch the `bot_control.launch` file to execute the `reading_laser.py` script and visualize the filtered scan data on RViz:

    ```bash
    roslaunch bot_control bot_control.launch
    ```

5. RViz will launch, and you should see the filtered laser scan data visualized.

6. You can verify that the `reading_laser.py` script is running by checking the terminal where you launched the `roslaunch` command. You should see log messages indicating that the script is running and publishing data.

## Additional Notes

- Make sure you have RViz installed to visualize the laser scan data.
- Ensure that the `/scan` topic is being published with laser scan data for the script to process.
- If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository.

