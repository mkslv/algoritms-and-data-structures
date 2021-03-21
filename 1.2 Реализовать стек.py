import sys


class Stack:
    def __init__(self):
        self.elements = []

    def is_null(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)
        print("ok")

    def pop(self):
        if self.is_null():
            print("error")
        else:
            print(self.elements[-1][0])
            self.elements.pop()

    def back(self):
        if self.is_null():
            print("error")
        else:
            print(self.elements[-1][0])

    def size(self):
        print(len(self.elements))

    def clear(self):
        print("ok")
        self.elements = []

    def exit(self):
        print("bye")
        sys.exit()


def main():
     st = Stack()

    while True:
        command, *element = input().split(sep=" ")
        if command == "push":
            st.push(element)
        elif command == "pop":
            st.pop()
        elif command == "back":
            st.back()
        elif command == "size":
            st.size()
        elif command == "clear":
            st.clear()
        elif command == "exit":
            st.exit()

if __name__ == "__main__":
    # execute only if run as a script
    main()
