#!/usr/bin/python

import os

import time


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
#to initialize gpio pins

GPIO.setup(10, GPIO.IN)

GPIO.setup(11, GPIO.OUT)

#green

GPIO.setup(7,GPIO.OUT)

#red

GPIO.setup(8,GPIO.OUT)


GPIO.output(7,GPIO.HIGH)

#to set an infinite loop
while True:

   if ( GPIO.input(10) == False ):

      os.system('clear')

      print("Waiting for train")

      time.sleep(0.01)

   else:

      GPIO.output(7,GPIO.LOW)
      #to make red led to glow
      GPIO.output(8,GPIO.HIGH)

      time.sleep(0.01)
      #to close the gate

      for m in range(20):

         GPIO.output(11,1)

         time.sleep(0.0005)

         GPIO.output(11,0)

         time.sleep(0.01)

      os.system('clear')

      for n in reversed(range(0,3)):

         os.system('date')

         print ("Train is ariving in")

         print ('%s sec' %n)

         time.sleep(1)

         os.system('clear')

      GPIO.output(8,GPIO.LOW)
      #to make green led to glow

      GPIO.output(7,GPIO.HIGH)
      #to open the gate
      for m in range(12):

         GPIO.output(11,1)

         time.sleep(0.0015)

         GPIO.output(11,0)

         time.sleep(0.01)


GPIO.cleanup()
