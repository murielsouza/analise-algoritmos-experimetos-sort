#import time
#import timeit

def bubbleSort(A):
    #contcomparacoes=0
    #controcas =0
    if len(A) <= 1:
        sA = A
    else:
        for j in range(0,len(A)):
            for i in range(0,len(A)-1):
                #contcomparacoes += 1
                if A[i]>A[i+1]:
                    #controcas +=1
                    Aux = A[i+1]
                    A[i+1] = A[i]
                    A[i] = Aux
        sA = A
        #print(controcas)
    return sA


arq = open('dados100000.txt', 'r')
L = arq.readlines()
arq.close()

bubbleSort(L)


#inicio = timeit.default_timer()
#bubbleSort(L)
#fim = timeit.default_timer()
#print ('duracao: %f' % (fim - inicio))

#for linha in L :
   # print(linha)


