# Copyright: Jonas Oeing (all rights reserved)

# script to acces the Arduino and connected servos via the package pyfirmata
# Its important, that you run the basic_pyfirmata sketch on your arduino

from pyfirmata import Arduino, SERVO
from time import sleep

# setup Arduino
port = '/dev/cu.usbserial-11130'
board = Arduino(port)

# setup pins
pin_list = {'S1':2, 'S2':3, 'S3':6, 'S4':4, 'S5':5,}

# initiate servos
board.digital[pin_list['S1']].mode = SERVO
board.digital[pin_list['S2']].mode = SERVO
board.digital[pin_list['S3']].mode = SERVO
board.digital[pin_list['S4']].mode = SERVO
board.digital[pin_list['S5']].mode = SERVO

# servo range (min=Minimum angle, max = maximum angle, init= initial angle)
servo_range = {
    'S1':{'min':0, 'max':200, 'init':120},
    'S2':{'min':0, 'max':150, 'init':130},
    'S3':{'min':0, 'max':120, 'init':120}}
# functions
def rotate_servo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

# initiate servo position
rotate_servo(pin_list['S1'], servo_range['S1']['init']) # 0 - 200 (init: 120)
rotate_servo(pin_list['S2'], servo_range['S2']['init']) # 0 - 150 (init: 130)
rotate_servo(pin_list['S3'], servo_range['S3']['init']) # 0 - 120 (init: 120)

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import time

window = tk.Tk()
window.title('robotARMini control panel')

fig = ImageTk.PhotoImage(Image.open('./figures/robot.png'))
Label_FIG = Label(window, image=fig).grid(row=0, column=2)


variables = {'S1':IntVar(window, value=servo_range['S1']['init']),
             'S2':IntVar(window, value=servo_range['S2']['init']),
             'S3':IntVar(window, value=servo_range['S3']['init'])}

# slider Servo 1
label_S1 = tk.Label(window, text='Servo 1 (base)').grid(row=2, column=1)
slider_S1 = tk.Scale(window, variable=variables['S1'], from_=servo_range['S1']['min'], to=servo_range['S1']['max'], fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=2, column=2)

label_S2 = tk.Label(window, text='Servo 2').grid(row=3, column=1)
slider_S2 = tk.Scale(window, variable=variables['S2'], from_=servo_range['S2']['min'], to=servo_range['S2']['max'], fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=3, column=2)

label_S3 = tk.Label(window, text='Servo 3').grid(row=4, column=1)
slider_S3 = tk.Scale(window, variable=variables['S3'], from_=servo_range['S3']['min'], to=servo_range['S1']['max'], fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=4, column=2)

# Placeholder for servo 4 - 6
label_S4 = tk.Label(window, text='Servo 4').grid(row=5, column=1)
slider_S4 = tk.Scale(window, fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=5, column=2)

label_S5 = tk.Label(window, text='Servo 5').grid(row=6, column=1)
slider_S5 = tk.Scale(window, fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=6, column=2)

label_S6 = tk.Label(window, text='Servo 6').grid(row=7, column=1)
slider_S6 = tk.Scale(window, fg='green', orient=HORIZONTAL,
                     activebackground='green', length=220).grid(row=7, column=2)


while True:
    #print('servo 1: ', variables['S1'].get(), '     servo 2: ', variables['S2'].get(), '      servo 3: ', variables['S3'].get())
    rotate_servo(pin_list['S1'], variables['S1'].get()) # 0 - 200 (init: 120)
    rotate_servo(pin_list['S2'], variables['S2'].get()) # 0 - 150 (init: 130)
    rotate_servo(pin_list['S3'], variables['S3'].get()) # 0 - 120 (init: 120)
    #rotate_servo(pin_list['S1'], variables['S4'].get()) # 0 - 200 (init: 120)
    #rotate_servo(pin_list['S2'], variables['S5'].get()) # 0 - 150 (init: 130)
    #rotate_servo(pin_list['S3'], variables['S6'].get()) # 0 - 120 (init: 120)
    time.sleep(0.5)
    window.update()

