from collections import deque

#Stacks
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack, "stack")
# Removes the last item
stack.pop()
stack.pop()
print(stack, "stack after popping")

# Queues
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
queue.append("Birbal")
print(queue, "queue")
# Removes the first item
queue.popleft()
queue.popleft()
print(queue, "queue after popping")
