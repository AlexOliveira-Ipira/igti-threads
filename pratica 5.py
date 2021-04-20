import threading
import time

def thredWorker():
    print('A thread entrou em estado "Ruingin"')
    print('A thread entrou em estado "Non-Ruingin" ')
    time.sleep(10)
    print('Execução da thread foi finalizada...')
    
print('Thread Criada')
myThread = threading.Thread(target=thredWorker)

print('Theared no estado "Tuingin" ')
myThread.start()

myThread.join()
print('A Thread esta no estado de "Terminated"')
