def LookingForSum(thisarray, sumval):
    for i in range(len(thisarray)): 
        for j in range(i, len(thisarray)): #Lower bound for range needs to be the current value of i
            tempSum = sum(thisarray[i:j + 1:1]) #Splice input array between correct indexes and sum the members
            if tempSum == sumval: 
                return j - i + 2
    return -1

def main():
    thatarray = [3, 4, 2, -7, 5, 2, 1, -1]

    val1 = LookingForSum(thatarray, -2)
    print("val1 = ", val1)
    
    val2 = LookingForSum(thatarray, 8)
    print("val2 = ", val2)

main()