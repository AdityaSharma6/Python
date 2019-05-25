def insertionSort(array): 
    for i in range(len(array)):
        futureValue = array[i]
        j = i - 1
        while ((j >= 0) and (futureValue < array[j])): 
            array[j+1] = array[j]
            array[j] = futureValue
            j = j - 1
    print(array)
            
insertionSort([8,7,2,4,9,3,6,0,1,6,5])
