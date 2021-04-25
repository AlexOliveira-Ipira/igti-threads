#Contando Threads ativas
import threading
import random
import time

def minhaThread(i):
    print(f'Thread {i} iniciada:')
    time.sleep(random.randint(1,5))
    print(f'\nTheread {i} Finalizada:')
    
for i in range(random.randint(2,50)):
    thread = threading.Thread(target=minhaThread, args=(i,))
    thread.start()
time.sleep(4)
ativas = threading.active_count()
print(f'Total de thread ativas {ativas}')