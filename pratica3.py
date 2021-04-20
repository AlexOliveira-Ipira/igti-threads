import threading  # Modulo para a construção de Threading
import urllib.request  # Modulo para requisição de URL
import time  # Modulo de controle do tempo


def downloadimagens(imagePath, fileName):
    print('Realizando o download ...', imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print('Download finalizado')
    
def execulteThead(i):
    imageName = "imagens_thread/image-" + str(i) + '.jpg'
    downloadimagens('http://lorempixel.com.br/400/200', imageName)


t0 = time.time()

threads = [] #Criando uma lista vazia para os threads criados

for i in range(10):
    thread = threading.Thread(target=execulteThead, args=(i,))
    threads.append(thread)
    thread.start()
    
for i in threads:
    i.join()
   
t1 = time.time()
totalTime = t1 - t0

print(f'Tempo total em execução {totalTime}')
