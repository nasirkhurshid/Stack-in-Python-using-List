'''
Created on Aug 30, 2021
@author: Nasir Khurshid
All right reserved.
'''

stack=[]
stack.insert(0, 3)
stack.insert(1, 2)
stack.insert(2, 4)

print("Displaying values of Stack:")
for x in range(len(stack)-1, -1, -1):
    print(stack[x])
    
print("Size: ", len(stack))
stack.pop()

print("Size: ", len(stack))

if len(stack) != 0:
    print("Making Stack empty...")
    stack.clear()
    if len(stack) == 0:
        print("Stack emptied successfully!")
    else:
        print("Stack could not be emptied!")
else:
    print("Stack is already empty!")