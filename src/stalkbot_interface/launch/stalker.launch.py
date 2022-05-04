import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['export', 'ROS_DOMAIN_ID=1'],
            output='screen'
        ),
        # launch.actions.ExecuteProcess(
        #     cmd=['/home/ubuntu/rosboard/run'], # for turtlebot
        #     output='screen'
        # ),
        launch.actions.ExecuteProcess(
            cmd=['export', 'TURTLEBOT3_MODEL=burger'],
            output='screen'
        ),
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_bringup', 'robot.launch.py'],
            output='screen'
        ),
        launch_ros.actions.Node(
            package='stalk_bot',
            executable='movement'
        ),
        # launch_ros.actions.Node(
        #     package='stalk_bot',
        #     executable='camera'
        # ),
        launch_ros.actions.Node(
            package='stalk_bot',
            executable='main'
        )
    ])

''' 
launch.actions.ExecuteProcess(
    cmd=['ros2', 'run', 'usb_cam', 'usb_cam_node_exe', '--ros-args', '--params-file', '/home/kasper/aruco_ws/camera_params/params.yaml'],
        output='screen'
)
'''