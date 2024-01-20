import queue
import itertools

class PQ(queue.PriorityQueue):
    def __init__(self):
        super().__init__()
        self.counter = itertools.count()

    def put(self, priorityObj):
        priority, obj = priorityObj
        super().put((priority, next(self.counter), obj))

    def get(self):
        priority, count, obj = super().get()
        return obj