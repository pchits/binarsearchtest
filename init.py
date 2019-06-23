import random

N = 20

array = []
for i in range(N):
    array.append(int(random.random()*100))
array.sort()
print(array)

rand_key = random.randint(0,N)
number = array[rand_key]

print("We are seraching for ", number)

def binarysearch(needle, haystack):
    first = 0
    last = len(haystack)-1
    result = None
    while first <= last and not result:
        mid = (first + last)//2
        if haystack[mid] == needle:
            result = mid
        else:
            if needle < haystack[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return result

print(binarysearch(number, array))

