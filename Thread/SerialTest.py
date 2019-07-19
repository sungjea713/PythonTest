import threading
from multiprocessing import Process, Queue
from time import sleep

flag = True

def threadTest():
    while True:
        if flag == True:
            print('hi')
        else:
            break
        sleep(0.1)

def threadTest2():
    while True:
        if flag == True:
            print('hi2')
        else:
            break
        sleep(0.2)


def main():
    global flag
    thread = threading.Thread(target=threadTest)
    thread2 = threading.Thread(target=threadTest2)
    thread.start()
    thread2.start()

    sleep(5)
    flag = False
    thread.join()
    thread2.join()
    print('thread exit')

if __name__ == "__main__":
    main()