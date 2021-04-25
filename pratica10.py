#Indentificando as Thread
import threading
import time


def myThread():
    getName = threading.current_thread().getName()
    print(f'Thread {getName} inicializada')
    time.sleep(10)
    print(f'Thread {getName} finalizada')
for i in range(4):
    threadName = "Thread " + str(i)
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()
 
numeroThread = threading.enumerate()
print(numeroThread)
