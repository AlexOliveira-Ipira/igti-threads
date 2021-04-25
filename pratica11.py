#Deadlok
import threading
import time
import random

class Filosofos(threading.Thread):
    
    def __init__(self, name, leftFork, rigntFork):
        print(f'{name}, sentou na mesa.')
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rigntFork = rigntFork
        
    def run(self):
        getName = threading.current_thread().getName()
        print(f'{getName}. começou a pensar.')
        while True:
            time.sleep(random.randint(1,5))
            print(f'{getName}, parou de pensar')
            self.leftFork.acquire()
            time.sleep(random.randint(1,5))
            try:
                print(f'{getName}, pegou o garfo da esquerda.')
                
                self.rigntFork.acquire()
                try:
                    print(f'{getName}, pegou os dois garfos e começou a pensar')
                finally:
                    self.rigntFork.release()
                    print(f'{getName}, soutou o garfo da direita')
            finally:
                self.leftFork.release()
                print(f'{getName}, soltou o garfo da esquera')
                
                
fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = Filosofos('Kant', fork1, fork2)
philosopher2 = Filosofos('Aristotle', fork1, fork2)
philosopher3 = Filosofos('Spinoza', fork1, fork2)
philosopher4 = Filosofos('Marx', fork1, fork2)
philosopher5 = Filosofos('Rossell', fork1, fork2)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()