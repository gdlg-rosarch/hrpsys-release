#!/usr/bin/env python

"""
 this is example file for SampleRobot robot

 $ roslaunch hrpsys samplerobot.launch
 $ rosrun    hrpsys samplerobot-data-logger.py

"""

pkg = 'hrpsys'
import imp
try:
    imp.find_module(pkg)
except:
    import roslib
    roslib.load_manifest(pkg)

from hrpsys.hrpsys_config import *
import OpenHRP


def getRTCList ():
    return [
            ['seq', "SequencePlayer"],
            ['sh', "StateHolder"],
            ['fk', "ForwardKinematics"],
            ['log', "DataLogger"],
            ]

def init ():
    global hcf
    hcf = HrpsysConfigurator()
    hcf.getRTCList = getRTCList
    hcf.init ("SampleRobot(Robot)0")

if __name__ == '__main__':
    init()
    # set initial pose from sample/controller/SampleController/etc/Sample.pos
    initial_pose = [-7.779e-005,  -0.378613,  -0.000209793,  0.832038,  -0.452564,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -0.378613,  -0.000209794,  0.832038,  -0.452564,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]

    # Set max ring-buffer length : 200 [loop] * 0.002 [s] = 0.4 [s] data
    hcf.log_svc.maxLength(200)
    # Clear buffer
    hcf.log_svc.clear()
    hcf.seq_svc.setJointAngles(initial_pose, 2.0)
    hcf.seq_svc.waitInterpolation()
    # Save log files for each ports as /tmp/test-samplerobot-log.*
    #   file names are /tmp/test-samplerobot-log.[RTCName]_[PortName], c.f.,  /tmp/test-samplerobot-log.sh_qOut ... etc
    hcf.log_svc.save("/tmp/test-samplerobot-log")

## IGNORE ME: this code used for rostest
if [s for s in sys.argv if "--gtest_output=xml:" in s] :
    import unittest, rostest
    rostest.run('hrpsys', 'samplerobot_data_logger', unittest.TestCase, sys.argv)






