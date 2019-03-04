def largestNumber (array):
    largestValue = 0
    for i in array:
        if i > largestValue:
            largestValue = i
    print(largestValue)

def main():
    largestNumber([1,22,3,101])

main()

