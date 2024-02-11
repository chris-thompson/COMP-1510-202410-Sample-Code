"""
A program that continually prompts that user for words and produces
a count of each type of letter or symbol entered.
"""


def main():
    """
    Drive the program. Let's use a dictionary!
    """
    counts = {}

    word = input("Enter a word, or -1 to quit: ")
    while word.strip() != "-1":
        for char in word:
            if char in counts:
                counts[char] = counts[char] + 1
            else:
                counts[char] = 1
        word = input("Enter a word, or -1 to quit: ")

    key_string = "\n"
    val_string = ""
    for key, value in sorted(counts.items()):
        key_string = key_string + key + "  "
        val_string = val_string + str(value) + "  "

    print(key_string)
    print(val_string)


if __name__ == "__main__":
    main()
