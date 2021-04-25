#Em qual theread estamos
import threading
import time

def threadTargtth():
    atual = threading.current_thread()
    print(f'Thread atual {atual}')

thraeds = []

for i in range(10):
    thread = threading.Thread(target=threadTargtth)
    thread.start()
    thraeds.append(thread)

for i in thraeds:
    thread.join()
    