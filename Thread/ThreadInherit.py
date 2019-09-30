import threading

class Messanger(threading.Thread):
    def run(self):
        for i in range(0, 20):
            print(threading.current_thread().getName() + str(i) + "\n")

send = Messanger(name="Sending out Messages")

receive = Messanger(name = "Receiving Messages")

send.start()
send.join()
receive.start()