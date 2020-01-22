w = input("Width: ")
h = input("Height: ")


def display(w, h):
    for i in range(0, h):
        i += 1
        for j in range(0, w):
            j += 1
            print("*", end=" ")


while (int(w) > 1 or int(h) > 1):
    print(str(display(int(w), int(h))))
