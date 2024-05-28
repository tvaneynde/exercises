class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []

    def add(self, item):
        if len(self.buffer) == self.size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def __getitem__(self, index):
        return self.buffer[index]

    def __len__(self):
        return len(self.buffer)
