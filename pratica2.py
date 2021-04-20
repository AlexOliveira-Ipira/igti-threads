import threading        #Modulo para a construção de Threading
import urllib.request   #Modulo para requisição de URL
import time             #Modulo de controle do tempo

def downloadimagens(imagePath, fileName):
    print('Realizando o download ...' , imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    
t0 = time.time()
for i in range(10):
    imageName = "imagens/image-" + str(i) + '.jpg'
    downloadimagens('http://lorempixel.com.br/400/200', imageName)
t1 = time.time()
totalTime = t1 - t0
print(f'Tempo total em execução {totalTime}')

