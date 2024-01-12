from queue import PriorityQueue

maxSize =100
a = PriorityQueue(maxSize)
a.empyt() # returns bool, True if queue is empty
a.full() # return bool, True if no space left in queue
a.get() # gets top item in pq
