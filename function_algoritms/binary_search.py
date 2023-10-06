a = [y for y in range(1, 40, 1)]
c = [x for x in range(1, 10000, 1)]
v = [s for s in range(1, 1, 1)]

def binary_search(m, item):
    low = 0
    high = len(m) - 1
    iterations = 0

    is_found = False

    while not is_found and low <= high:
        center = int((low + high) // 2)
        # iterations += 1
        if m[center] == item:
            print(iterations)
            return m.index(m[center])
        else:
            if item < m[center]:
                high = center - 1
            else:
                low = center + 1
    print(iterations)
    return False

b = int(input("Введите число:"))

print(binary_search(c, b))
print(b + 1)

