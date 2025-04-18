import rospy
from std_msgs.msg import String
def callbake(data):
    rospy.loginfo("The message %s",data.data)

def listener():
    rospy.Subscriber('chatting',String,callbake)
    rospy.init_node("listener",anonymous=True)
    rospy.spin()
    return


if __name__ == '__main__' :
    
    listener()

