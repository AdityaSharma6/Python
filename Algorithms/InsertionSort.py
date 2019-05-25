def insertionSort(array): 
    for i in range(len(array)):
        futureValue = array[i]
        j = i - 1
        while (j >= 0):
            if futureValue < array[j]:
                array[j+1] = array[j]
                array[j] = futureValue
                j = j - 1
            else:
                break
    
    print(array)
            
            
            
insertionSort([8,3,6,0,2,6,4,0,1])