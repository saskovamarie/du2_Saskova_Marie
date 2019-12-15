from random import randint

LIST_LEN = 1
# create a list of length LIST_LEN
# with random ints in range 0 - 100
searchlist = [chr(randint(ord("a"),ord("z"))) for _ in range (LIST_LEN)]
searchlist.sort()

print(searchlist)

def bin_search(alist, num):
    left = 0
    right = len(alist)-1
    return _bin_search(alist,num,left,right)
    # returns True if num in list, else False

def _bin_search(alist,num,left,right):
    if left > right:
        return False

    mid = (left + right)//2
    if num == alist[mid]:
        return True
    elif num > alist[mid]:
        return _bin_search(alist,num,mid + 1, right )
    else:
        return _bin_search(alist,num,left, mid -1)


    # looks at half of the range
    # if num is there, return True
    # else recurse on the correct side of the list
ans = bin_search(searchlist,"v")
print(ans)