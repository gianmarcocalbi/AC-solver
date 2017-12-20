class Propagation:

    def __init__(self):
        self.queue = []  # contains constraints to parse
        self.graph = {}  # constraints' graph i.e. for each variable the set of constraints with regard to it

    def build_graph(self, constraints):
        if not bool(self.graph):
            self.rebuild_graph(constraints)

    def rebuild_graph(self, constraints):
        for c in constraints:
            if c.x.id not in self.graph:
                self.graph[c.x.id] = []

            if c.y.id not in self.graph:
                self.graph[c.y.id] = []

            self.graph[c.x.id].append(c)
            self.graph[c.y.id].append(c)

    def enqueue(self, *variables):
        """
        Add constraint (x,y) into queue whether not present
        :param variables: one or more pair (x,y)
        :return: True if all passed variables aren't already in the queue, False otherwise
        """
        ret = True
        for x in variables:
            if x not in self.queue:
                self.queue.append(x)
                ret = False

        return ret

    def dequeue(self):
        return self.queue.pop(0)

    def run(self):
        # loop through all variables in queue
        while len(self.queue) > 0:
            x = self.dequeue()
            for c in self.graph[x.id]:
                if not c.filter_from(x):
                    return False
            x.reset_delta()
        return True
