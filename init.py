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

low = 0
high = N-1
while low <= high:
    mid = (low + high) // 2
    if number < mid:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print("Key:", mid)
        break
else:
    print("It's broken")
