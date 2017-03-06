# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:20:02 2017

@author: N. Papapietro and M. Seat
"""

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

angle_per_step = 0.25

RA_pins = [4,17,23,24]
RA_enable = 18
Dec_pins = [5,26,25,16]# [16,25,26,5] 
Dec_enable = 12

sequence = [[1,0,1,0],[0,1,1,0],[0,1,0,1],[1,0,0,1]]

def setup():
	GPIO.setup(RA_enable,GPIO.OUT)
	GPIO.setup(Dec_enable,GPIO.OUT)
	for i in RA_pins:
		GPIO.setup(i, GPIO.OUT)
	for i in Dec_pins:
		GPIO.setup(i, GPIO.OUT)

setup()
GPIO.output(RA_enable,1)
GPIO.output(RA_enable,1)

def set_step(pins,sequence):
	for i,j in zip(pins,sequence):
		GPIO.output(i,j)
	
def forward(delay, axis):
	for i in sequence:
		set_step(axis,i)
		time.sleep(delay)

def backward(delay, axis):
	for i in reversed(sequence):
		set_step(axis,i)
		time.sleep(delay)

def move(delay, axis, pos):
	if pos==True:
		forward(delay,axis)
	else:
		backward(delay,axis)
		

def RA_count(current, target):
	''' Takes a list in form [hrs,min,sec] and 
		return minutes which is 1-1 for steps  '''
	minutes_cur = int(round(current[1]+current[2]/60)+current[0]*24 )
	minutes_target = int(round(target[1]+target[2]/60)+target[0]*24 )
	return minutes_target-minutes_cur

def Dec_count(current, target):
	'''	 Takes a list in form [deg,min,sec] and 
		return minutes which is 1-1 for steps   '''
	steps_cur = int(4*round(current[0] + current[1]/60 + current[2]/3600) )
	steps_tar = int(4*round(target[0] + target[1]/60 + target[2]/3600) )
	return steps_tar-steps_cur

def goto_cmd(RA_steps, Dec_steps):
	delay = 5/1000.0
	pos_RA = True
	pos_Dec = True
	if RA_steps < 0:
		pos_RA = False
		RA_steps*=-1
	if Dec_steps < 0:
		pos_Dec = False	
		Dec_steps*=-1	
	while(True):
		if RA_steps != 0:
			move(delay, RA_pins, pos_RA)
			RA_steps-=1
			#continue
		if Dec_steps != 0:
			move(delay, Dec_pins, pos_Dec)
			Dec_steps-=1
			#continue
		if Dec_steps == 0 and RA_steps == 0:
			break
def test():
	delay = 5 / 1000.0
	while True:
		#forward(delay, RA_pins)
		forward(delay, Dec_pins)


if __name__ == '__main__':
	if sys.argv[1]== 'test':
		test()
        else:
		in_1 = map(int, sys.argv[1].strip('[]').split(','))
		in_2 = map(int, sys.argv[2].strip('[]').split(','))
		RA = int( RA_count([0,0,0], in_1) )
		DEC = int( Dec_count([0,0,0], in_2) )
		print RA, DEC
		goto_cmd(RA,DEC)
	
	
		
