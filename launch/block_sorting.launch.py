from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        # Gazebo を起動
        ExecuteProcess(
            cmd=['gazebo', '--verbose', 'worlds/block_sorting.world'],
            output='screen'
        ),

        # AI推論ノード
        Node(
            package='physical_ai_block_sorting',
            executable='ai_inference_node.py',
            output='screen'
        ),

        # 制御ノード
        Node(
            package='physical_ai_block_sorting',
            executable='control_node.py',
            output='screen'
        )
    ])

