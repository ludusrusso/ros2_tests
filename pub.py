import rclpy

from rclpy.node import Node
from std_msgs.msg import String


class PubNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.pub_ = self.create_publisher(String, 'chatter')
        
        self.timer = self.create_timer(0.1, self.timer_cb)
        self.cnt = 0

    def timer_cb(self):
        msg = String()
        msg.data = 'hey ROS 2.0: {}'.format(self.cnt)
        self.pub_.publish(msg)
        self.get_logger().info('sto pubblicando "{}"'.format(msg.data))
        self.cnt += 1


def main(args=None):
    rclpy.init(args=args)

    pub_node = PubNode()
    rclpy.spin(pub_node)

    pub_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
