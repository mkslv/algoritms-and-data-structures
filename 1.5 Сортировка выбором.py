
def selection_sort(elements):
    for i in range(len(elements)):
        lowest_index = i
        # Смотрим несортированные элементы
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[lowest_index]:
                lowest_index = j
        elements[i], elements[lowest_index] = elements[lowest_index], elements[i]

def main():
    elements = input().split(sep=" ")
    selection_sort(elements)
    elements_str = " ".join(elements)
    print(elements_str)

if __name__ == '__main__':
    main()