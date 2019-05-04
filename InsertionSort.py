import time
import timeit

def insertionSort(alist):
    
    contcomparacao = 0
    controca = 0

    for i in range(1,len(alist)):
        current = alist[i]
        contcomparacao +=1 
       
        while i>0 and alist[i-1]>current:
            controca +=1
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current

        #print(alist)
        print('trocas ',controca)
        print('comparações ',contcomparacao)

    return alist

#print(insertionSort([5,2,1,9,0,4,6]))



arq = open('dados100000.txt', 'r')
L = arq.readlines()
arq.close()

print(insertionSort(L))


inicio = timeit.default_timer()
insertionSort(L)
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

#for linha in L :
   # print(linha)


