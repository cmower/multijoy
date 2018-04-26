#!/usr/bin/env python
import rospy
import message_filters as mf
import multijoy.msg as mj
from sensor_msgs.msg import Joy

class MultiJoy(object):
    def __init__(self):
        
        if rospy.has_param('debug'):
            self.debug=rospy.get_param('debug')
        else:
            self.debug=False
        
        self.njoy=rospy.get_param('njoy')

        Msg='mj.MultiJoy{}'.format(self.njoy)
        self.msgtype=eval(Msg)
        self.msg=eval('{}()'.format(Msg))

        self.pub=rospy.Publisher('multijoy', eval(Msg), queue_size=10)
        
        self.subs=[None]*self.njoy
        for i in xrange(self.njoy):
            topic='joy/{}'.format(i+1)
            self.subs[i]=mf.Subscriber(topic, Joy)
        self.timeSync=mf.ApproximateTimeSynchronizer(self.subs, 10, self.njoy*100)
        self.timeSync.registerCallback(self.update)
            
    def update(self, *args):
        for i, arg in enumerate(args):
            attr='joy{}'.format(i+1)
            setattr(self.msg, attr, arg)
        self.msg.header.stamp=rospy.Time.now()
        if self.debug:
            print self.msg
        self.pub.publish(self.msg)

if __name__=='__main__':
    rospy.init_node('multijoy_node')
    mj=MultiJoy()
    rospy.spin()
