def balanced_parath(str):
    open = ["(", "[", "{"]
    close = [")", "]", "}"]

    st = []

    for bracket in str:
        if bracket in open:
            st.append(bracket)
        elif bracket in close:
            position = close.index(bracket)
            if len(st) > 0 and open[position] == st[len(st) - 1]:
                st.pop()
            else:
                return print("no")

    if len(st) == 0:
        return print("yes")
    else:
        return print("no")



def main():
    elements = input()
    balanced_parath(elements)


if __name__ == '__main__':
    main()
