class Propagation:

    def __init__(self, constrains):
        self.queue = []  # contains constraints to parse
        self.graph = {}  # constraints' graph i.e. for each variable the set of constraints with regard to it

        for c in constrains:
            if c.x.id not in self.graph:
                self.graph[c.x.id] = []

            if c.y.id not in self.graph:
                self.graph[c.y.id] = []

            self.graph[c.x.id].append(c)
            self.graph[c.y.id].append(c)

    """
    Add constraint (x,y) into queue whether not present
    """

    def enqueue(self, variables):
        for x in variables:
            if x not in self.queue:
                self.queue.append(x)

    def dequeue(self):
        return self.queue.pop(0)

    def run(self):
        # before starting run() method, all variable must be enqueued by user
        # loop through all variables in queue
        while len(self.queue) > 0:
            x = self.dequeue()
            for c in self.graph[x.id]:
                if not c.filter_from(x, self):
                    return False
            x.reset_delta()
        return True
