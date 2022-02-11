from typing import List, Union
from icecream import ic
from datetime import datetime


def time_format():
    return f'{datetime.now().strftime("%m/%d/%Y, %I:%M:%S")}|>'


ic.configureOutput(prefix=time_format, includeContext=True)


class Queue:
    def __init__(self):
        self.items = []

    def size(self) -> int:
        return len(self.items)

    def dequeue(self) -> Union[int, str, float]:
        if len(self.items) == 0:
            return 'UNDERFLOW'
        return self.items.pop(0)

    def enqueue(self, item) -> List:
        self.items.append(item)
        return self.items


if __name__ == '__main__':
    queue = Queue()
    ic(queue.enqueue(23))
    ic(queue.enqueue(2))
    ic(queue.enqueue(3))
    ic(queue.dequeue())
    ic(queue.size())
