import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('sub_node')
        self.sub_ = self.create_subscription(
            String,
            'chatter',
            self.chatter_cb
        )

    def chatter_cb(self, msg):
        self.get_logger().info('I get {}'.format(msg.data))

    
def main(args=None):
    rclpy.init(args=args)
    sub_node = SimpleSubscriber()
    rclpy.spin(sub_node)

    sub_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

