def read_input():
    lst1 = []
    lst2 = []
    with open("inputs/01", "r") as f:
        for line in f.readlines():
            item = line.strip().split()
            lst1.append(int(item[0]))
            lst2.append(int(item[1]))
    return lst1, lst2

def part_one(lst1, lst2):
    lst1.sort()
    lst2.sort()
    distance = 0
    for l1, l2 in zip(lst1, lst2):
        distance += l2 - l1 if l2 > l1 else l1 - l2
    print(distance)

def part_two(lst1, lst2):
    similarity_score = 0
    for item in lst1:
        similarity_score += item * lst2.count(item)
    print(similarity_score)


def main():
    lst1, lst2 = read_input()
    # part_one(lst1, lst2)
    part_two(lst1, lst2)


if __name__ == "__main__":
    main()
