#import time
#import timeit

def selectionSort(alist):
   # contcomparacao = 0
    #controca = 0
    for i in range(len(alist)):
        
      # Find the minimum element in remaining
        minPosition = i

        for j in range(i+1, len(alist)):
            #contcomparacao +=1
            if alist[minPosition] > alist[j]:
                minPosition = j
                #controca +=1
       # Swap the found minimum element with minPosition       
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp
    #print('troca: ',controca)
    #print('comparacao: ',contcomparacao)
    return alist



arq = open('dados100.txt', 'r')
L = arq.readlines()
arq.close()

print(selectionSort(L))


#inicio = timeit.default_timer()
#selectionSort(L)
#fim = timeit.default_timer()
#print ('duracao: %f' % (fim - inicio))

#for linha in L :
   # print(linha)


