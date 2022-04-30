import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['./rosboard/run'],
            output='screen'
        ),
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_bringup', 'robot.launch.py'],
            output='screen'
        ),
        launch_ros.actions.Node(
            package='motor',
            executable='movement_controller'
        ),
        launch_ros.actions.Node(
            package='package_opencv',
            executable='talker'
        )
    ])

''' 
launch.actions.ExecuteProcess(
    cmd=['ros2', 'run', 'usb_cam', 'usb_cam_node_exe', '--ros-args', '--params-file', '/home/kasper/aruco_ws/camera_params/params.yaml'],
        output='screen'
)
'''