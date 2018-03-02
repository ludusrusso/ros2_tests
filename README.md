# Testing ROS 2

Here is a testing repository for ROS2.0 and the **rclpy** (Python ROS Client Library).

## Usage

 -  Install ROS e Ament
 -  Setup an ament workspace and clone this repository:
    
    ```
    $ mkdir -p ~/ros2_ws/src
    $ cd ~/ros2_ws/src
    $ git clone 
    ````
 - build with ament and source the workspace

    ```
    $ cd ~/ros2_ws
    $ ament build
    $ source install/setup.bash
    ```

 - run subs e pubs
   ```
   $ ros2 run ros2_test pub &
   $ ros2 run ros2_test sub 
   ``` 
