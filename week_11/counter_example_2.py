from collections import Counter


def main():
    """
    Drive the program. Demonstrate how to use Counter from the collections module.
    """
    ages = [20, 20, 22, 23, 55, 52, 87, 20, 17, 23, 1, 52, 52]

    age_counts = Counter(ages)

    print(age_counts.most_common())
    print(sum(age_counts.values()))
    print(list(age_counts))


if __name__ == '__main__':
    main()
