#Vendas de tickets
import threading
import time
import random

class TicketSales(threading.Thread):
    ticketsold = 0
    
    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print('Venda de ingressos iniciada')
    
    def run(self):
        global ticketAvailabel
        running = True
        while running:
            self.randomDelay()
            
            self.sem.acquire()
            if ticketAvailabel == 0:
                running = False
            else:
                self.ticketsold = self.ticketsold + 1
                ticketAvailabel = ticketAvailabel - 1
                getName = self.getName()
                print(f'{getName}, acabou de vender 1 {ticketAvailabel} restante')
            self.sem.release()
        print(f'Venda de ingresso {getName} ingressos vendidos no total {self.ticketsold}')
            

    def randomDelay(self):
        time.sleep(random.randint(0, 4)/4)


semaphore = threading.Semaphore()

#Variavel que controla numero de ingressos disponiveis
ticketAvailabel = 100

#Processo de venda automatizado
sallers = []
for i in range(4):
    saller = TicketSales(semaphore)
    saller.start()
    sallers.append(saller)
    
for saller in sallers:
    saller.join()
    