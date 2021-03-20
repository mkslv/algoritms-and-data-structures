import sys

class Queue:
    def __init__(self):
        self.elements = []

    def is_null(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)
        print("ok")

    def pop(self):
        if self.is_null():
            print('error')
        else:
            elementsBeforeOperation = self.elements
            elementsAfterOperation = elementsBeforeOperation[1:]
            self.elements = elementsAfterOperation
            print(elementsBeforeOperation[0][0])

    def front(self):
        if self.is_null():
            print("error")
        else:
            print(self.elements[0][0])

    def size(self):
        print(len(self.elements))

    def clear(self):
        print("ok")
        self.elements = []

    def exit(self):
        print("bye")
        sys.exit()

def main():

    qe = Queue()

    while True:
        command, *element = input().split(sep=" ")
        if command == "push":
            qe.push(element)
        elif command == "pop":
            qe.pop()
        elif command == "front":
            qe.front()
        elif command == "size":
            qe.size()
        elif command == "clear":
            qe.clear()
        elif command == "exit":
            qe.exit()

if __name__ == '__main__':
    main()