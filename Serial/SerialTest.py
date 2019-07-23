import serial
import threading
from multiprocessing import Process, Queue
from time import sleep
import binascii
import numpy as np

flag = True
data_srt = bytearray()
count = 0

def threadTest(ser):
    while True:
        if flag == True:
            global count
            global data_str
            #ser.read_all() #Read all bytes currently available in the buffer of the OS.
            #ser.read_until() #Read until a termination sequence is found ('' by default), the size is exceeded or until timeout occurs.
            #ser.readall() #Read until EOF, using multiple read() call.
            #ser.readline()
            #ser.readlines()
            
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
                #data = data_str.hex()
                #dataArray = np.asarray(data)
                if(data_str[0] == 2 and data_str[1] == 1 and data_str[2] == 4 and data_str[3] == 3 and data_str[4] == 6 and data_str[5] == 5 and data_str[6] == 8 and data_str[7]==7):
                    print((dataArray))
        else:
            break
        sleep(0.001)

def main():
    global flag
    ser = serial.Serial(port='COM7', baudrate = 921600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=None)
    ser.read
    print(ser.portstr)
    print(ser.is_open)
    thread = threading.Thread(target=threadTest, args=(ser,))
    threadProcess = threading.Thread(target=ProcessPointCloud)
    thread.start()
    threadProcess.start()
    sleep(5)
    flag = False
    thread.join()
    threadProcess.join()
    print('thread joined')
    ser.close()
    print('port closed')
    
    

if __name__ == "__main__":
    main()