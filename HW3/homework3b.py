def LookingForSum(thisarray, sumval):
    for i in range(len(thisarray)): #Loop through the elements of the array
        for j in range(i, len(thisarray)): #Loop through elements of the array with lower bound for range as the current value of i
            tempSum = sum(thisarray[i:j + 1:1]) #Splice input array between correct indexes and sum the members
            if tempSum == sumval: 
                return j - i + 2 #Return the location of the sequence that sums to sumval
    return -1 #Return -1 if no sequences sum to sumval

def main():
    thatarray = [3, 4, 2, -7, 5, 2, 1, -1]

    print("val1 = ", LookingForSum(thatarray, -2))
    print("val2 = ", LookingForSum(thatarray, 8))

main()