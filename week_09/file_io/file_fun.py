import io


def make_file():
    """
    Demonstrate how to append unicode characters to a text file.
    """
    with open('newfile.txt', 'a') as file_object:
        print(type(file_object))
        file_object.write("Hello\n")


def read_file():
    """
    Demonstrate how to read unicode characters from a text file.
    """
    with open('newfile.txt') as file_object:
        contents = file_object.read()
        print(type(contents))
        print(contents)
        file_object.seek(io.SEEK_SET)
        more_contents = file_object.read()
        print(more_contents)


def main():
    """
    Drive the program.
    """
    make_file()
    read_file()


if __name__ == "__main__":
    main()
