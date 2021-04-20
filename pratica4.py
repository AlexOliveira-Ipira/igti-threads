import threading
import time
import random

counte = 10


def tarefaA():
 global counte
 while counte < 30:
  counte += 1
  print(f'A tarefa incrementou o contador para {counte}')
  slepTime = random.randint(0,3)
  time.sleep(slepTime)

def tarefaB():
 global counte
 while counte > -30:
  counte -= 1
  print(f'A tarefa decremento o contado para {counte}')
  slepTime = random.randint(0, 4)
  time.sleep(slepTime)
  
t0 = time.time()
thread1 = threading.Thread(target=tarefaA)
thread2 = threading.Thread(target=tarefaB)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

t1 = time.time()

timaAtual = t1 -t0

print(f'Tempo total de execução {timaAtual}')
