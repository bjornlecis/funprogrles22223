import queue
q = queue.lifoQueue(3)
q.put(1)
q.put(2)
q.put(3)
for elem in range(q.maxsize):
    print(q.get())
