def largestNumber (array):
    counter = 0
    compare = 0
    largest = 0

    while counter < len(array):
        number = array[counter]

        if number > largest:
            largest = number
        counter += 1

    return largest

def main ():
    print (largestNumber([100,2,3,4101,5]))

main ()

