import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.subscription = self.create_subscription(
            String,
            'block_color',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        color = msg.data
        if color == 'red':
            self.get_logger().info('赤ブロックを右へ移動')
        elif color == 'blue':
            self.get_logger().info('青ブロックを左へ移動')
        else:
            self.get_logger().info(f'未知の色: {color}')

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

