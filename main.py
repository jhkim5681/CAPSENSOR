44# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
import matplotlib.pyplot as plt
from celluloid import Camera
from IPython.display import HTML

fig, ax = plt.subplots()
camera = Camera(fig)

ax.plot([0, 1], [0, 1])
camera.snap()  # ??????����?????? ��???
fig

ax.plot([0, 1], [1, 0])
camera.snap()
fig

animation = camera.animate(interval=500, repeat=True)


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation, PillowWriter

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
(ln,) = ax.plot([], [], "bo")
xdata, ydata = [], []


def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return (ln,)


def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return (ln,)


anim = FuncAnimation(
    fig, update, frames=np.linspace(0, 2 * np.pi, 128), init_func=init, blit=True
)

#anim.save("animation.gif", writer="imagemagick", fps=60)
#anim.save("animation.gif", writer="pillow", fps=60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)


def animate(i):
  x = np.linspace(0, 4, 1000)
  y = np.sin(2 * np.pi * (x - 0.01 * i))
  line.set_data(x, y)
  return line,


# anim = FuncAnimation(fig, animate, frames=200, interval=50)
anim = FuncAnimation(fig, animate, frames=200, interval=100)

plt.show()
"""
"""

import matplotlib.pyplot as plt
import serial

#print('serial'+serial.__version__)

ser=serial.Serial('COM8', 115200, timeout=1)


class CapSense:
    raw_count: int = None
    baseline: int = None
    diff_count: int = None

def CheckCapData():
    global index
    index = 0
    # ????????? ??????
    for i in range(len(y)):
        # header1, 0x0d
        if (index == 0 and bytearray[i] == 0x0d):
            index = 1
            print("first header i ", i, "value", bytearray[i])
            # input data

        # header2, 0x0a
        elif (index == 1 and bytearray[i] == 0x0a):
            index = 2
            print("second header", i, "arrayValue", bytearray[i])
            # senseData[1] = bytearray[i]

        # capsense raw_count
        elif (index == 2):
            capSenseRawCount = bytearray[i + 1]
            capSenseRawCount <<= 8
            capSenseRawCount |= bytearray[i]
            CapSense.raw_count = capSenseRawCount
            print("cap sense raw count value", CapSense.raw_count)
            index = 3

        # cap sensor base_line
        elif (index == 3):
            capSenseBaseline = bytearray[i + 2]
            capSenseBaseline <<= 8
            capSenseBaseline |= bytearray[i + 1]
            CapSense.baseline = capSenseBaseline
            index = 4
            print("cap sense base line value", CapSense.baseline)

        # cap sense diff count
        elif (index == 4):
            print(bytearray[i + 3], bytearray[i + 2])
            capSense_diff = bytearray[i + 3]
            capSense_diff <<= 8
            capSense_diff |= bytearray[i + 2]
            CapSense.diff_count = capSense_diff
            print("cap sense diff value", CapSense.diff_count)
            index = 0

        # tail check
        elif (index == 8):
            index = 0

        else:
            index = 0

# �׷�??? �ʱ� ??????
plt.ion()

# �׷�??? ??????
fig, ax = plt.subplots()

capSenseRawCount = 0
capSenseBaseline = 0
capSense_diff = 0
i = 0
while True:
    # ????????? ����
   # y = ser.readline()
   # bytearray = y
    # ?????? ?????? ?????
#    CheckCapData()

    # ????????? ??????

    i = i + 0.1
    x_data = 1 + i
    y_data = 1 + i
    # �׷�??? ????????????
    ax.plot(x_data, y_data)  # x_data??? y_data??? ����?????? ?????????
    #ax.plot(capSense_diff, capSenseBaseline)  # x_data??? y_data??? ����?????? ?????????

    # �׷�??? �����ֱ�
    plt.show()
    plt.pause(0.1)  # 0.1�ʸ�??? �׷�????? ????????????
"""




"""
    for i in range(len(y)):
        # header1, 0x0d
        if (index == 0 and bytearray[i] == 0x0d):
            index = 1
            print("first header i ", i, "value", bytearray[i])
            # input data

        # header2, 0x0a
        elif (index == 1 and bytearray[i] == 0x0a):
            index = 2
            print("second header", i, "arrayValue", bytearray[i])
            # senseData[1] = bytearray[i]

        # capsense raw_count
        elif (index == 2):
            capSenseRawCount = bytearray[i + 1]
            capSenseRawCount <<= 8
            capSenseRawCount |= bytearray[i]
            CapSense.raw_count = capSenseRawCount
            print("cap sense raw count value", CapSense.raw_count)
            index = 3

        # cap sensor base_line
        elif (index == 3):
            capSenseBaseline = bytearray[i + 2]
            capSenseBaseline <<= 8
            capSenseBaseline |= bytearray[i + 1]
            CapSense.baseline = capSenseBaseline
            index = 4
            print("cap sense base line value", CapSense.baseline)

        # cap sense diff count
        elif (index == 4):
            print(bytearray[i + 3], bytearray[i + 2])
            capSense_diff = bytearray[i + 3]
            capSense_diff <<= 8
            capSense_diff |= bytearray[i + 2]
            CapSense.diff_count = capSense_diff
            print("cap sense diff value", CapSense.diff_count)
            index = 0

        # tail check
        elif (index == 8):
            index = 0

        else:
            index = 0
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,TWOPI,-1,1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
                                      interval=10, blit=True, repeat=True)

plt.show()

"""


import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import serial


# Class example
class Capsensor:
    #super class
    raw_count: float = None 
    baseline: float = None
    diff_count: float = None

    def show(slef):
        print("cap sensor class")

#ĸ��??? Class ??????
class CapSense:
    raw_count: float = None
    baseline: float = None
    diff_count: float = None
    cap2_raw_count: float = None
    cap2_baseline: float = None
    cap2_diff_count: float = None

    
print('serial'+serial.VERSION) #VERSION ���?

ser = serial.Serial('COM8', 115200, timeout=0) # COMx ?????? OPEN, Baudrate 115200

x_max = 1         #�ʱ� X ?? ��?????
frame_count = 200   #????????? ???
x_step = 0.01
Num_interval = 5000
max_points = 5000
x_axis_value = 0.999
y_axis_value = 1.001
fix_diffValue = 50000.0

x = np.linspace(0, 1000, Num_interval)
y = np.linspace(0, 45000, 70000)
fig = plt.figure(1)
ax = plt.axes(xlim=(0, x_max), ylim=(45000, 70000))

ax.set_title('CAP SENSOR DATA1')
ax.set_xlabel('[TIME]')
ax.set_ylabel('[HZ]')

line, = ax.plot(np.arange(max_points),
                np.ones(max_points, dtype=np.cfloat)*np.nan, 'g',
                lw=1, label='raw')

line2, = ax.plot(np.arange(max_points),
                 np.ones(max_points, dtype=np.cfloat)*np.nan, 'b',
                 lw=1, label='base')

line3, = ax.plot(np.arange(max_points),
                 np.ones(max_points, dtype=np.cfloat)*np.nan, 'r',
                 lw=1, label='diff')
plt.legend(loc='upper right')
fig2_max_points = 5000
fig2 = plt.figure(2)
ax2 = plt.axes(xlim=(0, x_max), ylim=(45000, 70000))
ax2.set_title('CAP SENSOR DATA2')
ax2.set_xlabel('[TIME]')
ax2.set_ylabel('[HZ]')
line4, = ax2.plot(np.arange(fig2_max_points),
                np.ones(fig2_max_points, dtype=np.cfloat)*np.nan, 'g',
                lw=1, label='raw')

line5, = ax2.plot(np.arange(fig2_max_points),
                 np.ones(fig2_max_points, dtype=np.cfloat)*np.nan, 'b',
                 lw=1, label='base')

line6, = ax2.plot(np.arange(fig2_max_points),
                 np.ones(fig2_max_points, dtype=np.cfloat)*np.nan, 'r',
                 lw=1, label='diff')

plt.legend(loc='upper right')
                        
data = 0
serData = 0
index = 0
serialValue = []
position = 0

#??????????? ?????? ???????? ���???????
def getDataFunc():
    global data
    data = random.randrange(45000, 70000)
    return data

#UART data parsing
def DataCheckFunc(lst):
    global serialValue
    global index
    global position

    list_size = len(serialValue)

    for i in range(len(lst)):
        serialValue.append(lst[i])

    print("serialValue:", serialValue, "size", len(serialValue))

    if (len(serialValue) >= 29):
    # Header && tail check
        if (index == 0):
            for i in range(len(serialValue)):
                if (index == 0):
                    if (serialValue[i] == 0x0d):
                   #     print("first header i: ", i, "value", serialValue[i])
                        # header2, 0x0A Check
                        if (serialValue[i+1] == 0x0a):
                    #        print("second header", serialValue[i+1])
                            index = 1
                            position = i
                            break
                    #for?? ????? ????????? ???????? index = 0, data clear
            if(index == 0):
                print("index clear")
                #serialValue.clear()
                del serialValue[0:len(serialValue)]
                index = 0

        # tail check
        if (index == 1):
            if(len(serialValue) > (position + 26)):
                if (serialValue[position + 26] == 0x00):
                #   print("tail ", position, "value", serialValue[position + 26])
                    # header2, 0x0A Check
                    if (serialValue[position + 27] == 0xff):
                #      print("second tail", serialValue[position + 27])
                        if (serialValue[position + 28] == 0xff):
                #          print("second header", serialValue[position + 28])
                            index = 2
                        else:
                            print("index and serialValue clear")
                            serialValue.clear()
                            index = 0
                    else:
                        print("index and serialValue clear")
                        serialValue.clear()
                        index = 0
                else:
                    print("index and serialValue clear")
                    serialValue.clear()
                    index = 0

    if(index == 2):
   
        CapSense.raw_count = serialValue[position + 2]
        CapSense.raw_count <<= 8
        CapSense.raw_count |= serialValue[position + 3]
        
        CapSense.baseline = serialValue[position + 4]
        CapSense.baseline <<= 8
        CapSense.baseline |= serialValue[position + 5]
        
        CapSense.diff_count = serialValue[position + 6]
        CapSense.diff_count <<= 8
        CapSense.diff_count |= serialValue[position + 7]


        CapSense.cap2_raw_count = serialValue[position + 8]
        CapSense.cap2_raw_count <<= 8
        CapSense.cap2_raw_count |= serialValue[position + 9]
        
        CapSense.cap2_baseline = serialValue[position + 10]
        CapSense.cap2_baseline <<= 8
        CapSense.cap2_baseline |= serialValue[position + 11]
        
        CapSense.cap2_diff_count = serialValue[position + 12]
        CapSense.cap2_diff_count <<= 8
        CapSense.cap2_diff_count |= serialValue[position + 13]


        print("**** [cap sensor1] **** \n raw: ", CapSense.raw_count, "base:", CapSense.baseline, "diff:", CapSense.diff_count)
        print("**** [cap sensor2] **** \n raw: ", CapSense.cap2_raw_count, "base:", CapSense.cap2_baseline, "diff:", CapSense.cap2_diff_count)

        index = 0
        del serialValue[0:position+28]

    return 1

def animate(i):

    global serData
    global x_max  # x_max ??????? ????????????????? ?????? nonlocal ??????
    global Num_interval
    # serial data ???????? ???? ??????
    if ser.readable():
        serData = ser.readline() #serData list??? ??????
        #serData = ser.readline().decode('utf-8').strip()
        print("serData:", serData, "size:", len(serData))

        # ????????? ????????? ??????
        DataCheckFunc(serData)
        #print("cap sense check", CapSense.raw_count)


    #Random function 
    #capRawCount = float(getDataFunc())
    #capBaseLine = float(getDataFunc())
    #capDiffCnt  = float(getDataFunc())

    if(CapSense.diff_count == 0):
        capDiffCnt = fix_diffValue
    else:
        capDiffCnt = fix_diffValue

    if ((CapSense.raw_count != None) and (CapSense.baseline != None)):
        capRawCount = float(CapSense.raw_count)
        capBaseLine = float(CapSense.baseline)
      
    else:
        capRawCount = 0
        capBaseLine = 0

    x_max += x_step  # X ?? ���� ??????
    ax2.set_xlim(0, x_max)  # X ?? ���� ????????????

    # y?? ���� ??????  
    if((CapSense.raw_count != None) and (CapSense.baseline != None)):
        if(capRawCount > capBaseLine):
            ax2.set_ylim(capBaseLine * x_axis_value, capRawCount * y_axis_value)
        else:
            ax2.set_ylim(capRawCount * x_axis_value, capBaseLine * y_axis_value)

    x = np.linspace(0, x_max, Num_interval) #x?? ?????????????? ?????????

    # raw count line
    old_y = line4.get_ydata()
    new_y = np.r_[old_y[1:], capRawCount]
    line4.set_data(x, new_y)

    # baseline
    old_y = line5.get_ydata()
    new_y = np.r_[old_y[1:], capBaseLine]
    line5.set_data(x, new_y)
            
    # diff line      
    old_y = line6.get_ydata()
    new_y = np.r_[old_y[1:], capDiffCnt]
    line6.set_data(x, new_y)
    
    #ax.set_xlim(0, x_max + i * x_step)

    return line4, line5, line6


def animate2(i):

    global serData
    global x_max  # x_max ??????? ????????????????? ?????? nonlocal ??????
    global Num_interval
    # serial data ???????? ???? ??????
   
    #Random function 
    #capRawCount = float(getDataFunc())
    #capBaseLine = float(getDataFunc())
    #capDiffCnt  = float(getDataFunc())

    if(CapSense.cap2_diff_count == 0):
        capDiffCnt = fix_diffValue
    else:
        capDiffCnt = fix_diffValue

    if ((CapSense.cap2_raw_count != None) and (CapSense.cap2_baseline != None)):
        capRawCount = float(CapSense.cap2_raw_count)
        capBaseLine = float(CapSense.cap2_baseline)
      
    else:
        capRawCount = 0
        capBaseLine = 0

    #x_max += x_step  # X ?? ���� ??????
    ax.set_xlim(0, x_max)  # X ?? ���� ????????????

    # y?? ���� ??????  
    if((CapSense.cap2_raw_count != None) and (CapSense.cap2_baseline != None)):
        if(capRawCount > capBaseLine):
            ax.set_ylim(capBaseLine * x_axis_value, capRawCount * y_axis_value)
        else:
            ax.set_ylim(capRawCount * x_axis_value, capBaseLine * y_axis_value)

    x = np.linspace(0, x_max, Num_interval) #x?? ?????????????? ?????????

    # raw count line
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], capRawCount]
    line.set_data(x, new_y)

    # baseline
    old_y = line2.get_ydata()
    new_y = np.r_[old_y[1:], capBaseLine]
    line2.set_data(x, new_y)
            
    # diff line      
    old_y = line3.get_ydata()
    new_y = np.r_[old_y[1:], capDiffCnt]
    line3.set_data(x, new_y)

    return line, line2, line3

def CapSense2(i):

    y = float(getDataFunc())
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
   
    return line



anim = animation.FuncAnimation(
                                fig,
                                animate2,
                                init_func=lambda:line,
                                #frames = range(frame_count),
                                interval=100)


anim2 = animation.FuncAnimation(fig2, 
                               animate, 
                               init_func=lambda:line, 
                               #frames = range(frame_count), 
                               interval=100)
plt.show()