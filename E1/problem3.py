def countLargerThan(val, alist):
    count = 0
    for i in range(len(alist)): count += 1 if abs(alist[i]) > val else 0
    return count

def main():
    list1 = [-5, 4.7, 3, 2, 9, 1, 3]
    list2 = [-5, 4.7, 3, 2, 9, 1, 3, -12, 10, 2]

    answer1 = countLargerThan(4.8, list1)
    print(answer1)

    answer2 = countLargerThan(4.1, list2)
    print(answer2)

main()