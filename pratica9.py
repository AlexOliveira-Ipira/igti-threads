#Main Thread
import threading
import time

def myChildThread():
    print('Thread filha iniciada ----')
    time.sleep(5)
    print('Thread atual -----')
    print(threading.current_thread())
    print('----------------------')
    print('Main Thread ----------')
    print(threading.main_thread())
    print('Thread finalizada ')
    
child = threading.Thread(target=myChildThread)
child.start()
child.join()
