################################################## Part1 ###############################################################

print("######### Part1 ###########")
def minimumCost(n, m, nCostArray, sCostArray):
    minimumS = 0
    minimumN = 0
    for i in range(0, n - 1):
        lastS = minimumS
        lastN = minimumN
        minimumN = nCostArray[i] + min(lastN, m + lastS)
        minimumS = sCostArray[i] + min(lastS, m + lastN)

    return min(minimumS, minimumN)


n = 4
m = 10
nArray = [1, 3, 20, 30]
sArray = [50, 20, 2, 4]
print("Minimum cost is :", minimumCost(n + 1, m, nArray, sArray))

################################################## Part2 ###############################################################
print("######### Part2 ###########")
def attendSymposium(activity, start, finish, n):
  resultArray = [0]*n
  resultArray[1] = activity[1]
  k = 1
  iter = 1


  for i in range(2, n+1):
    if(start[i] >= finish[k]):
      iter = iter+1
      resultArray[iter] = activity[i]
      k=i

  resultArray[0] = iter;
  return resultArray


activity = [0, 1, 2, 3, 4, 5]
start = [0, 0, 1, 3, 4, 1]
finish = [0, 2, 3, 4, 6, 6]
p = attendSymposium(activity, start, finish, len(activity) - 1)

print("Selectin activities : ", end = '')
for i in range(1, p[0]+1):
    print(p[i], end = ' ')
print()
################################################## Part3 ###############################################################

print("######### Part3 ###########")


def subsetSum(index, target,  positiveSum, negativeSum, myArray, nonZeros ):

    if target < negativeSum or target > positiveSum:
        return False
    if index == 0:
        return nonZeros[0] == target
    key = (index, target)
    if key in myArray:
        return myArray[key]

    result = nonZeros[index] == target or subsetSum(index - 1, target, positiveSum, negativeSum, myArray,nonZeros) \
             or subsetSum(index - 1, target - nonZeros[index], positiveSum, negativeSum, myArray,nonZeros)

    myArray[key] = result
    return result
def subsetSumWNegative(integers, target_sum=0):

    positiveIntegers = [integer for integer in integers if integer > 0]
    negativeIntegers = [integer for integer in integers if integer < 0]

    nonZeros = positiveIntegers + negativeIntegers

    pos_sum = sum(positiveIntegers)
    neg_sum = sum(negativeIntegers)

    myArray = {}

    return subsetSum(len(nonZeros) - 1, target_sum, pos_sum, neg_sum, myArray, nonZeros)


values = [10, 3, 9, -5, 4, 2, -7, 8]
valuesNonZero = [10, 3, 9, 4, 2, 8]
target = 0
result = subsetSumWNegative(values, target)
result2 = subsetSumWNegative(valuesNonZero, target)
if result == True :
    print(values, "There is a subset sum equal to 0")
else:
    print(values,"There is not a subset sum equal to 0")
if result2 == True :
    print(valuesNonZero, "There is a subset sum equal to 0")
else:
    print(valuesNonZero,"There is not a subset sum equal to 0")

################################################## Part4 ###############################################################
print("######### Part4 ###########")
### i got help from the internet ###
class ScoreParam:

    def __init__(self, match, mismatch, gap, gap_start=0):
        self.gap_start = gap_start
        self.gap = gap
        self.match = match
        self.mismatch = mismatch

    def matchchar(self, a, b):
        assert len(a) == len(b) == 1
        if a == b:
            return self.match
        else:
            return self.mismatch

    def __str__(self):
        return "match = %d; mismatch = %d; gap_start = %d; gap_extend = %d" % (
                self.match, self.mismatch, self.gap_start, self.gap
        )


def make_matrix(sizex, sizey):
    return [[0]*sizey for i in range(sizex)]


def local_align(x, y, score=ScoreParam(2, -2, -1)):

    A = make_matrix(len(x) + 1, len(y) + 1)

    best = 0
    optloc = (0,0)

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):

            A[i][j] = max(
               A[i][j-1] + score.gap,
               A[i-1][j] + score.gap,
               A[i-1][j-1] + score.matchchar(x[i-1], y[j-1]),
               0
            )

            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i,j)

    print("Scoring:", str(score))
    print("Optimal Score =", best)
    print("Max location in matrix =", optloc)
    return best, optloc


print(local_align("alignment", "sli  me"))

################################################## Part5 ###############################################################
print("######### Part5 ###########")


def sumArray(array):

    resultSum = 0
    for x in array:
        if x < 0:
            x = -1 * x
        resultSum += x
    return resultSum


array = [12, 3, 4, 15, 12]
print(array, "Sum of the array is ", sumArray(array))
arrayWithNegative = [-12, 3, 4, -15, 12]
print(arrayWithNegative, "Sum of the array(with negative) is ", sumArray(arrayWithNegative))




