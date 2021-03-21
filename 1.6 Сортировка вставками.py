def insertion_sort(elements):
    for i in range(1, len(elements)):
        insert = elements[i]
        j = i - 1
        while j >= 0 and int(elements[j]) > int(insert):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = insert


def main():
    len_of_list = int(input())
    elements = input().split()
    insertion_sort(elements)
    elements_str = " ".join(elements)
    print(elements_str)


if __name__ == '__main__':
    main()
