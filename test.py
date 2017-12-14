class Head:
    def __init__(self):
        self.a = [1, 2, 3, 4]


class Body:
    def __init__(self, head):
        self.head = head

    def run(self):
        h = self.head
        h.a.pop()
        print(h.a)
        print(self.head.a)

if __name__ == "__main__":
    h = Head()
    b = Body(h)
    b.run()
