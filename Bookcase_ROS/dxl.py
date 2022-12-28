#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

from dynamixel_sdk import * # Uses Dynamixel SDK library

ADDR_TORQUE_ENABLE          = 64
ADDR_GOAL_POSITION          = 116
ADDR_GOAL_VELOCITY          = 104
ADDR_PRESENT_POSITION       = 132
ADDR_PRESENT_VELOCITY       = 128
ADDR_PRO_TORQUE_ENABLE      = 64               
ADDR_PRO_GOAL_POSITION      = 116
ADDR_PRO_PRESENT_POSITION   = 132
ADDR_PROFILE_VELOCITY       = 112
ADDR_PROFILE_ACCELERATION   = 108
DXL_MINIMUM_POSITION_VALUE  = 0         # Refer to the Minimum Position Limit of product eManual
DXL_MAXIMUM_POSITION_VALUE  = 4095      # Refer to the Maximum Position Limit of product eManual
BAUDRATE                    = 57600
ADDR_PRO_GOAL_VELOCITY      = 104
ADDR_PRO_OPERATING_MODE     = 11
DXL_POSITION_MODE           = 4
DXL_VELOCITY_MODE           = 1

PROTOCOL_VERSION            = 2.0

# DXL_ID                      = 1

DEVICENAME                  = '/dev/ttyACM0'

TORQUE_ENABLE               = 1     # Value for enabling the torque
TORQUE_DISABLE              = 0     # Value for disabling the torque
DXL_MOVING_STATUS_THRESHOLD = 10    # Dynamixel moving status threshold

portHandler = PortHandler(DEVICENAME)

packetHandler = PacketHandler(PROTOCOL_VERSION)

class bringup:
    def __init__(self, dxl_id):
        self.DXL_ID = dxl_id
        # Open port
        if portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            quit()

        # Set port baudrate
        if portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            quit()

        # Disable Dynamixel Torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.DXL_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel has been successfully connected")

        # Set dxl's operating mode = position mode
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.DXL_ID, ADDR_PRO_OPERATING_MODE, DXL_POSITION_MODE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))


        # Enable Dynamixel Torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel has been successfully connected")

class setting:
    def __init__(self, dxl_id, velocity, acceleration):
        self.DXL_ID = dxl_id
        self.vel = velocity
        self.acc = acceleration

        # Write profile velocity
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.DXL_ID, ADDR_PROFILE_VELOCITY, self.vel)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        # Write profile acceleration
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.DXL_ID, ADDR_PROFILE_ACCELERATION, self.acc)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

class goal:
    def __init__(self, dxl_id, goal):
        self.DXL_ID = dxl_id
        self.goal = goal

	# Write goal position
	dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.DXL_ID, ADDR_GOAL_POSITION, self.goal)
	if dxl_comm_result != COMM_SUCCESS:
	    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
	    print("%s" % packetHandler.getRxPacketError(dxl_error))

class stop:
    def __init__(self, dxl_id):
        self.DXL_ID = dxl_id

        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, self.DXL_ID, ADDR_PRESENT_POSITION)
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.DXL_ID, ADDR_GOAL_POSITION, dxl_present_position)
        print("PresPos-%02d : %02d" %(self.DXL_ID, dxl_present_position))

class read:
    def __init__(self, dxl_id):
        self.DXL_ID = dxl_id

    def call(self):
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, self.DXL_ID, ADDR_PRESENT_POSITION)
        return dxl_present_position
