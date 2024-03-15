"""
We can stack our decorators. Like patching unit tests!
"""


def make_bold(function_to_be_emboldened):
    """
    Embolden.
    """
    def emboldened():
        return "<b>" + function_to_be_emboldened() + "</b>"

    return emboldened


def make_italic(function_to_be_italicized):
    """
    Add italics.
    """
    def italicized():
        return "<i>" + function_to_be_italicized() + "</i>"

    return italicized


@make_bold
@make_italic
def challenge():
    """
    Is this a Pokemon quote?
    """
    return "Spearows, Do You Know Who I Am?"


def main():
    """
    Drive the program.
    """
    print(challenge())


if __name__ == "__main__":
    main()
