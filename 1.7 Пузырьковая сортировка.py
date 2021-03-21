def bubble_sort(elements):
    objectsWillSwapped = True
    while objectsWillSwapped:
        objectsWillSwapped = False
        for i in range(len(elements) - 1):
            if int(elements[i]) > int(elements[i + 1]):
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                objectsWillSwapped = True


def main():
    len_of_list = int(input())
    elements = input().split()
    bubble_sort(elements)
    elements_str = " ".join(elements)
    print(elements_str)


if __name__ == '__main__':
    main()
