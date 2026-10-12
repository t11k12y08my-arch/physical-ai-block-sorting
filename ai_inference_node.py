import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AIInferenceNode(Node):
    def __init__(self):
        super().__init__('ai_inference_node')
        self.publisher_ = self.create_publisher(String, 'block_color', 10)
        self.timer = self.create_timer(1.0, self.inference_callback)

    def inference_callback(self):
        # 仮のAI推論：赤と青を交互に publish
        import random
        color = random.choice(['red', 'blue'])

        msg = String()
        msg.data = color
        self.publisher_.publish(msg)
        self.get_logger().info(f'AI推論結果: {color}')

def main(args=None):
    rclpy.init(args=args)
    node = AIInferenceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

