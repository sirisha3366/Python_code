import pdb
# pdb - pip install NOT needed because it is preesnt in python 3.7 onwards by defaults
def addition(a,b):
    ans = a*b
    return ans

pdb.set_trace()
#breakpoint()
x = int(input("enter the value:"))
y = int(input("enter the value:"))
sum = addition(x,y)
print(sum)
