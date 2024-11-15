import array as arr

num = arr.array("i", [1,2,3,4,5,6,6,6,6,7,7,5,5,4,4])
print(num.count(6))
num.reverse()
print(num)