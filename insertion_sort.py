import random
randomlist = []
for i in range(0,1000):
    n = random.randint(1,1000)
    randomlist.append(n)

# insertion sort is good for sorting lists in place 


# check if a list is sorted or not 
def is_sorted(li): 
    for i in range(len(li) - 1):
        if li[i]>li[i+1]:
            return False
    return True


def insertion_sort(arr):
    for n in range(0, len(arr)):
        i = n-1 
        while i >=0 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i-=1

insertion_sort(randomlist)
print(is_sorted(randomlist))
print(randomlist)