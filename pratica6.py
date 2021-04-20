from threading import Thread

class MinhaClasseThread(Thread):
    def __init__(self):
        print('Olá, construtor Thread')
        Thread.__init__(self)
        
    def run(self):
        print("\n Thread em execução. ")
        
minhaThread = MinhaClasseThread()
print('Objeto criado')

minhaThread.start()
print('Objeto iniciado')

minhaThread.join()
print('Objeto Parado')
