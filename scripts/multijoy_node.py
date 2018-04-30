#!/usr/bin/env python
import rospy
import message_filters as mf
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy

class MultiJoyParser(object):
    def __init__(self):

        # Retrieve parameters
        if rospy.has_param('debug'):
            self.debug=rospy.get_param('debug')
        else:
            self.debug=False
        self.njoys=rospy.get_param('njoys')

        # Setup ros publisher
        self.multijoy_pub=rospy.Publisher('/multijoy', MultiJoy, queue_size=10)

        # Setup ros subscribers
        self.joy_subs=[mf.Subscriber('/joy/'+str(i),Joy) for i in xrange(self.njoys)]
        self.timeSync=mf.ApproximateTimeSynchronizer(self.subs, 10, self.njoy*100)
        self.timeSync.registerCallback(self.update)

    def update(self, *args):
        msg=MultiJoy()
        msg.header.stamp=rospy.Time.now()
        msg.njoys=len(args)
        msg.joys=args
        self.multijoy_pub.publish(msg)

if __name__=='__main__':
    rospy.init_node('multijoy_node')
    parser=MultiJoyParser()
    rospy.spin()
