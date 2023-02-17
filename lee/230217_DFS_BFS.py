from collections import deque

# stack
'''
stack = []

stack.append(0)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack[::-1])

stack.pop()
print(stack)
stack.pop()
print(stack)
'''

# queue
'''
queue = deque()

queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
'''

# recursive
# gcd

'''
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)


print(gcd(192, 162))
'''

# DFS
