import rospy
from std_msgs.msg import String

def talker():
# create publisher
    pub = rospy.Publisher('chatting',String,queue_size=10)
# create talker node 
    rospy.init_node('talker',anonymous=True)
# rate of sending msg
    rate = rospy.Rate(10)
# 
    while not rospy.is_shutdown():
# sending hello message to chatting topic 
        hello_str = "Hello World %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__' :
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

