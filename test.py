class Test:
    def __init__(self):
        pass

    def __getitem__(self, item):
        if item is None:
            return "MADAMA"

if __name__ == "__main__":
    t = Test()
    print(t[])