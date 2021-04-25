#Queue - Juntando threads
import threading
import time
from queue import Queue


def consumidor(q):
    while (True):
        name = threading.currentThread().getName()
        data = time.strftime('%H:%M:%S')
        size = q.qsize()
        print(f'Thread {name}, deseja obter um item da queue, tamanho atual {size} '
              f'na data {data}')
        item = q.get()
        time.sleep(3)
        print(f'Thread {name}, deseja obter um item da queue, tamanho atual '
              f'na data {data}')
        q.task_done()

def produtor(q):
    
    for i in range(10):
        name = threading.currentThread().getName()
        tamanho = q.qsize()
        data = time.strftime('%H:%M:%S')
        print(f'Thread {name}, deseja obter um item da queue, tamanho atual {tamanho} '
          f'na data {data}')
        item = 'Item ' + str(1)
        q.put(item)
        print(f'Thread {name}, deseja obter um item da queue, tamanho atual '
          f'na data {data}')
    q.join()

if __name__ == '__main__':
    q = Queue(maxsize=3)
    threads_num = 3
    for i in range(threads_num):
        t = threading.Thread(name='ThreadConstrutora-'+ str(i), target=consumidor, args=(q,))
        t.start()
    
    t = threading.Thread(name='ThreadProdutos', target=produtor, args=(q,))
    t.start()
    
    q.join()
    