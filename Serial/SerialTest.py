import serial
import threading
from multiprocessing import Process, Queue
from time import sleep
import binascii
import numpy as np
from bitstring import BitArray
import os

filePath = "C:\InCabin"
flag = True
data_srt = bytearray()
count = 0

def threadTest(ser):
    while True:
        if flag == True:
            global count
            global data_str

            '''
            if (ser.inWaiting()>0):
                data_str = ser.read(ser.inWaiting())
                for i in data_str:
                    print('{:02x}'.format(i), end='')
                    print('-', end='')
                print('\n')
                print('\n')
            '''

            if (ser.inWaiting()>0):
                #print("Real:")
                #print(ser.inWaiting())
                data_str = ser.read(ser.inWaiting()) ##속도를 많이 잡아먹음
                print(count)
                count += 1

        else:
            break
        sleep(0.001)

def ProcessPointCloud():
    sleep(0.5)
    while True:
        if flag == True:
            if(len(data_str)>7):
                data = data_str.hex()
                if(''.join(data[:8*2]) == '0201040306050807'):
                    actualData = ''.join(data[:FindPacketLength(data[12*2:(12+4)*2])])
                    #numTarget = FindNumOfTarget(actualData[28*2:32*2])
                    
                    while True:
                        try:
                            f = open(filePath+"\point_cloud.txt", 'w')
                            f.write(actualData)
                            f.close()
                            print("Write Done!")
                            break
                        except:
                            sleep(0.001)


                    #print("Actual")
                    #print(FindPacketLength(data[12*2:(12+4)*2]))
                    #print(numTarget)
        else:
            break
        sleep(0.001)

def FindNumOfTarget(bList):
    if(len(bList)>0):  
        rList = bList[::-1]
        tempList = []
        for i in range(4):
            tempList.append(rList[2*i+1])
            tempList.append(rList[2*i])
        nList = ''.join(tempList)
        num = int(nList, 16)
        return num 

def FindPacketLength(bList):
    try:
        if(len(bList)>0):   
            rList = bList[::-1]
            tempList = []
            for i in range(4):
                tempList.append(rList[2*i+1])
                tempList.append(rList[2*i])
            nList = ''.join(tempList)
            length = int(nList, 16)
            return length 
    except:
        return 0

def main():
    global flag

    #Create point cloud directory
    if not os.path.isdir(filePath):
        os.mkdir(filePath)


    ser = serial.Serial(port='COM5', baudrate = 921600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=None)
    ser.read
    print(ser.portstr)
    print(ser.is_open)
    thread = threading.Thread(target=threadTest, args=(ser,))
    threadProcess = threading.Thread(target=ProcessPointCloud)
    thread.start()
    threadProcess.start()
    sleep(12000)
    flag = False
    thread.join()
    threadProcess.join()
    print('thread joined')
    ser.close()
    print('port closed')
    
    

if __name__ == "__main__":
    main()