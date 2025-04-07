import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = 'model1.urdf'
    urdf = os.path.join(get_package_share_directory('model1'), urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
    
    
    controller_yaml = PathJoinSubstitution(
        [
            FindPackageShare("model1"),
            "controllers.yaml",
        ]
    )
    robot_controller = LaunchConfiguration("robot_controller")
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument(
            "robot_controller",
            default_value="forward_velocity_controller",
            description="Robot controller to start.",
        ),
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[controller_yaml],
            output='both',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf]),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=[robot_controller, "--param-file", controller_yaml],
        )
    ])
    
    
    """
    ros2 topic pub /forward_velocity_controller/commands std_msgs/msg/Float64MultiArray "data:
- 5
- 5
- 5
- 5"
    
    """
