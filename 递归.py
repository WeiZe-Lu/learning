def factions(n):
    if n == 0:
        return 1
    else:
        return n * factions(n - 1)


def finds(s, star, shop, target):
    if star > shop:
        return False
    mid = (shop + star) // 2
    if s[mid] == target:
        return mid
    elif s[mid] < target:
        return finds(s, mid + 1, shop, target)
    elif s[mid] > target:
        return finds(s, star, mid - 1, target)


if __name__ == "__main__":
    # print(factions(n=5))
    S = (range(101))
    for k in (1, 3, 5, 8, 10, 11, 15, 80, 41):
        print(finds(S, 0, 100, k))
