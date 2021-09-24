######################################################## Q1 ############################################################
print("################### Q1 ##################")
print("################# part b #################")
arraySpecial = [[10, 20, 13, 28, 23], [17, 22, 16, 29, 23], [24, 28, 22, 34, 24],
      [11, 13, 6, 17, 7], [45, 44, 32, 37, 23], [36, 33, 19, 21, 6], [75, 66, 51, 53, 34]]
def specialArray(array2D):
    i = 0
    for r in array2D:
        if i + 1 < len(r):
            j = 0
            for c in r:
                if j+1 < len(r):
                    sumMustBeLess = array2D[i][j] + array2D[i+1][j+1]
                    sumMustBeGreater = array2D[i+1][j] + array2D[i][j+1]
                    if sumMustBeLess > sumMustBeGreater:
                        print("One of this in four elements must be change:",array2D[i][j], array2D[i+1][j+1], array2D[i+1][j], array2D[i][j+1])
                    j += 1
            i += 1


specialArray(arraySpecial)
print("################# part c #################")
def find_min(li, left, right):
    if left == right:
        return li[left]
    mid = int((left + right) / 2)
    min1 = find_min(li, left, mid)
    min2 = find_min(li, mid + 1, right)
    return min1 if min1 < min2 else min2

def applyAllRows(li):
    count = 0
    for r in li:
        count += 1
        print("Maximum element of row", count, "is :", find_min(r, 0, len(r) - 1))


applyAllRows(arraySpecial)

######################################################## Q2 ############################################################
print("################### Q2 ##################")


def kthElement(array1, array2, k):
    if len(array1) == 0:
        return array2[0]
    if len(array2) == 0:
        return array1[0]
    if k >= len(array1) + len(array2):
        print('invalid index')
    else:
        while k > 0:
            mid1 = int((k - 1) / 2)
            mid2 = int((k - 1) / 2)
            if mid1 >= len(array1):
                return kthElement(array2, array2[mid1 + 1:], k - mid2 - 1)
            if mid2 >= len(array2) or array1[mid1] <= array2[mid1]:
                return kthElement(array1[mid1 + 1:], array2, k - mid1 - 1)
            else:
                return kthElement(array1, array2[mid1 + 1:], k - mid2 - 1)
        return min(array1[0], array2[0])


##  indexes start at 1 , so 1st element is array[0], 2nd element is array[1]
A = [3, 4, 9, 12]
B = [1, 6, 8, 11, 14]
k = 1
while k <= 9:
    print("element", k, ":", kthElement(A, B, k - 1))
    k += 1

######################################################## Q3 ############################################################
print("################### Q3 ##################")
leftSum = -1000000
rightSum = -1000000


def maximumMidArray(array, low, mid, high):
    sum = 0
    leftSum = -1000000
    for i in range(mid, low - 1, -1):
        sum = sum + array[i]
        if (sum > leftSum):
            leftSum = sum
    sum = 0
    rightSum = -1000000
    for i in range(mid + 1, high + 1):
        sum = sum + array[i]
        if (sum > rightSum):
            rightSum = sum
    return leftSum + rightSum


def maximumSubarray(array, low, high):
    if high == low:
        return array[high]

    mid = int((high + low) // 2)
    leftMaximum = maximumSubarray(array, low, mid)
    rightMaximum = maximumSubarray(array, mid + 1, high)
    midMaximum = maximumMidArray(array, low, mid, high)

    return findMaximum(leftMaximum, rightMaximum, midMaximum)


def findMaximum(val1, val2, val3):
    if val1 >= val2 and val1 >= val3:
        return val1
    elif val2 >= val1 and val2 >= val3:
        return val2
    return val3


array = [5, -6, 6, 7, -6, 7, -4, 3]
print("Maximum sum is", maximumSubarray(array, 0, len(array) - 1))

######################################################## Q4 ############################################################
print("################### Q4 ##################")


def breadthFirstSearch(queue, visited, color, graph):
    while queue:
        u = queue.pop(0)
        visited[u] = True

        for neighbour in graph[u]:
            if neighbour == u:
                return False
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[u]
                queue.append(neighbour)
            if color[neighbour] == color[u]:
                return False
    return True


def checkBipartite(graph):
    queue = []
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            queue.append(i)
            color[i] = 0
            if not breadthFirstSearch(queue, visited, color, graph):
                return False
    return True


# Adjacency List of graph
exampleGraph = {0: [1, 3],
                1: [0, 2],
                2: [1, 3],
                3: [0, 2]}

print("Is graph bipartite ? :", checkBipartite(exampleGraph))

######################################################## Q5 ############################################################
print("################### Q5 ##################")

resultArray = []


def findGain(array, array2, left, right):
    if left == right:
        resultArray.append(array2[left] - array[left])
        return array2[left] - array[left]
    else:
        mid = int((left + right) // 2)
        left_hand = findGain(array, array2, left, mid)
        right_hand = findGain(array, array2, mid + 1, right)
        return max(resultArray)


C = ["-", 5, 11, 2, 21, 5, 7, 8, 12, 13]
P = [7, 9, 5, 21, 7, 13, 10, 14, 20, "-"]
C_New = C[1:len(C)]
P_New = P[0:len(P) - 1]
findGain(C_New, P_New, 0, len(P) - 2)
print("The gain array is :", resultArray)
print("The best gain is :", max(resultArray))
print("The best day to buy is :", resultArray.index(max(resultArray)) + 1)
