# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:20:02 2017

@author: Nathan
"""

import RPi.GPIO as GPIO
import time
import sys
from multiprocessing import Process
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ra_enable_pin = 18
Ra_A_1_pin = 4
Ra_A_2_pin = 17
Ra_B_1_pin = 23
Ra_B_2_pin = 24

dec_enable_pin = 12
dec_A_1_pin = 5
dec_A_2_pin = 26
dec_B_1_pin = 25
dec_B_2_pin = 16


GPIO.setup(Ra_enable_pin, GPIO.OUT)
GPIO.setup(Ra_A_1_pin, GPIO.OUT)
GPIO.setup(Ra_A_2_pin, GPIO.OUT)
GPIO.setup(Ra_B_1_pin, GPIO.OUT)
GPIO.setup(Ra_B_2_pin, GPIO.OUT)

GPIO.setup(dec_enable_pin, GPIO.OUT)
GPIO.setup(dec_A_1_pin, GPIO.OUT)
GPIO.setup(dec_A_2_pin, GPIO.OUT)
GPIO.setup(dec_B_1_pin, GPIO.OUT)
GPIO.setup(dec_B_2_pin, GPIO.OUT)

GPIO.output(Ra_enable_pin, 1)
GPIO.output(dec_enable_pin, 2)

'''
def forward(delay, steps, axis):  
  for i in range(0, steps):
    axis(1, 0, 1, 0)
    time.sleep(delay)
    axis(0, 1, 1, 0)
    time.sleep(delay)
    axis(0, 1, 0, 1)
    time.sleep(delay)
    axis(1, 0, 0, 1)
    time.sleep(delay)
'''
def forward(delay,steps):
  for i in range(0,steps):
    dec_setStep(1,0,1,0)
    RA_setStep(1,0,0,1)
    time.sleep(delay)
    dec_setStep(0,1,1,0)
    RA_setStep(0,1,0,1)
    time.sleep(delay)
    dec_setStep(0,1,0,1)
    RA_setStep(0,1,1,0)
    time.sleep(delay)
    dec_setStep(1,0,0,1)
    RA_setStep(1,0,1,0)
    time.sleep(delay)

def backwards(delay, steps,axis):  
  for i in range(0, steps):
    axis(1, 0, 0, 1)
    time.sleep(delay)
    axis(0, 1, 0, 1)
    time.sleep(delay)
    axis(0, 1, 1, 0)
    time.sleep(delay)
    axis(1, 0, 1, 0)
    time.sleep(delay)
  
def dec_setStep(w1, w2, w3, w4):
  GPIO.output(dec_A_1_pin, w1)
  GPIO.output(dec_A_2_pin, w2)
  GPIO.output(dec_B_1_pin, w3)
  GPIO.output(dec_B_2_pin, w4)
  
def RA_setStep(w1, w2, w3, w4):
  GPIO.output(Ra_A_1_pin, w4)
  GPIO.output(Ra_A_2_pin, w3)
  GPIO.output(Ra_B_1_pin, w2)
  GPIO.output(Ra_B_2_pin, w1)  

if __name__ == '__main__':
  delay = int(sys.argv[1])
  steps = int(sys.argv[2])
  t1 =  Process(target =  forward(int(delay) / 1000.0, int(steps)))
#  t1 = Process(target = backward(int(delay) / 1000.0, int(steps),RA_setStep))
  t1.start()
  #t2.start()
  t1.join()
  #t2.join()
	 
# steps = raw_input("How many steps backwards? ")
 # b2 = Process(target =  backwards(int(delay) / 1000.0, int(steps),dec_setStep))
 # b2.start()
 # b1 = Process(target = backwards(int(delay) / 1000.0, int(steps),RA_setStep))
 # b1.start()
