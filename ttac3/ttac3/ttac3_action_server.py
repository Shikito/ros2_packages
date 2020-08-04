import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import pyautogui
from ttac3_actions.action import TTAC3
from ttac3.xsel_controller import XselController


class TTAC3ActionServer(Node):

    def __init__(self, xsel_controller):
        super().__init__('ttac3_action_server')
        self._action_server = ActionServer(  # msgやsrvと同じノリ。actionの初期化
            self,
            TTAC3,
            'ttac3',
            self.execute_callback)

        self.xc = xsel_controller
    
    def execute_callback(self, goal_handle): # リクエストを受けたら実行される関数
        self.get_logger().info('Executing goal...')

        # process
        feedback_msg = TTAC3.Feedback()
        # for i in range(10):
        #     feedback_msg.current_state = f'{i} move'
        #     goal_handle.publish_feedback(feedback_msg)
        #     time.sleep(1)  # simulation
        
        feedback_msg.current_state = self.xc.move_to_xyz(
            goal_handle.request.xyz_goal
        )
        
        goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()
        
        result = TTAC3.Result()
        result.is_success = True
        return result


def main(args=None):
    rclpy.init(args=args)

    xc = XselController()
    xc.open_position_editor()
    xc.on_servo_motor()

    ttac3_action_server = TTAC3ActionServer(xsel_controller=xc)

    rclpy.spin(ttac3_action_server)

if __name__ == '__main__':
    main()