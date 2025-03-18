

## Demo
Visualize spinning wheels (setting joint state from `model1 state_publisher`):
```
$ ros2 launch model1 demo_launch.py
```
```
rviz2 -d install/model1/share/model1/model1.rviz
```
URDF mesh references are absolute and will need to be changed for each directory structure.

## ROS Control
```
sudo apt install ros-jazzy-ros2-control ros-jazzy-ros2-controllers
```
installs ros2_control and the ros2_controllers packages (for ROS jazzy)
```

```
cd src && git clone https://github.com/ros-controls/ros2_control_demos.git
```
installs the specific controller used in a demo (forward_velocity_controller in the RRBot demo)

Build and source, then:
```
ros2 launch model1 control_launch.py
```

A simple velocity publisher.
```
ros2 run model1 velocity_publisher
```


