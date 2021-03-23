size = input()
arr = [int(i) for i in input().split()]
print(max(arr)-min(arr)+1-size)
