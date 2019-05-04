import time
import timeit

def bubbleSort(L):
    contcomparacoes=0
    controcas =0
    for j in range(len(L)):
        for i in range(len(L)-1, j, -1):
            contcomparacoes+=1
            if L[i] < L[i-1]:
                controcas+=1
                aux = L[i]
                L[i] = L[i-1]
                L[i-1] = aux
    return l

arq = open('dados10000.txt', 'r')
L = arq.readlines()
arq.close()

bubbleSort(L)


#inicio = timeit.default_timer()
#bubbleSort(L)
#fim = timeit.default_timer()
#print ('duracao: %f' % (fim - inicio))

#for linha in L :
   # print(linha)


