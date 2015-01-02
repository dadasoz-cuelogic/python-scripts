from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
print(d)
print("-"*30)

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(data)
heapify(data)     
print(data)                 # rearrange the list into heap order
heappush(data, -5)
print(data)                 # add a new entry
print([heappop(data) for i in range(3)])
print(data)