print("*****************************************************************************")
print("TEST FOR QUESTION 3")
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]  # pivot

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Quick sort
def quickSort(arr, low, high):
    if low < high:
        global counter
        counter += 1
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5, 20]
n = len(arr)
counter = 0

quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")
print("\ncounter for quick sort: ", counter)


arr2 = [12, 11, 13, 5, 6]
n = len(arr2)
counter = 0

quickSort(arr2, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr2[i], end=" "),
print("\ncounter for quick sort: ", counter)

def insertionSort(my_list):
    # for every element in our array
    global counter2
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            my_list[position] = my_list[position-1]
            position -= 1
            counter2 += 1
        my_list[position] = current

    return my_list

arr =  [10, 7, 8, 9, 1, 5, 20]

counter2 = 0
print(insertionSort(arr))
print("\ncounter for insertion sort: ", counter2)
arr2 = [12, 11, 13, 5, 6]
counter2 = 0
print(insertionSort(arr2))
print("\ncounter for insertion sort: ", counter2)
############################################################################################################
print("*****************************************************************************")
print("TEST FOR QUESTION 4")
import random

def select(L, k):
    pivot = random.choice(L)
    # less then pivot
    L1 = []
    # greater then pivot
    L2 = []

    for i in L:
        if i < pivot:
            L1.append(i)
        elif i > pivot:
            L2.append(i)
        else:
            pass

    if k <= len(L1):
        return select(L1, k)
    elif k > len(L) - len(L2):
        return select(L2, k - (len(L) - len(L2)))
    else:
        return pivot

arr = [5, 6, 2, 3, 9, 12, 7, 16]
mid = len(arr) // 2 + 1
print("Median is ", select(arr, mid))

arr2 = [25, 16, 2, 3, 9, 7]
mid = len(arr2) // 2 + 1
print("Median is ", select(arr2, mid))

####################################################################################
print("*****************************************************************************")
print("TEST FOR QUESTION 5")
def subsets(nums):
    res = []
    findMult(res, [], nums, 0)
    return res

def findMult(res, temp, nums, start):

    res.append(temp[:])
    count = 1
    for i in range(start, len(nums)):
        temp.append(nums[i])
        count = (min(temp) + max(temp)) * len(temp) / 4
        print(count)
        if count < 36:
            print(temp ,"multiplication less than 36 > ", count)
        findMult(res, temp, nums, i + 1)
        temp.pop()

subsets([2, 4, 7, 5, 22, 11])