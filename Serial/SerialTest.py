import serial
import threading
from multiprocessing import Process, Queue
from time import sleep

flag = True

def threadTest(ser):
    while True:
        if flag == True:
            print(ser.read())
        else:
            break
        sleep(0.001)

def main():
    global flag
    ser = serial.Serial(port='COM7', baudrate = 921600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
    print(ser.portstr)
    print(ser.is_open)
    thread = threading.Thread(target=threadTest, args=(ser,))
    thread.start()
    sleep(10)
    flag = False
    thread.join()
    print('thread joined')
    ser.close()
    print('port closed')
    
    

if __name__ == "__main__":
    main()