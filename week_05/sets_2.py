"""
Working with sets.
"""


def main():
    """
    Drive the program.
    """
    exam = {'Abhi', 'Alex', 'Alzen', 'Annyn', 'Ardi', 'Juhyun'}
    project = {'Abhi', 'Jamie', 'Jarell', 'Joao', 'Jon', 'Jordan', 'Juhyun'}

    # Output the basic sets
    print('exam:', exam)
    print('project:', project)

    # Students taking both exam and project
    print(exam & project)

    # Only took the exam
    print(exam - project)

    # Only took the project
    print(project - exam)

    # All students
    print(exam | project)

    # Students who took the exam or the project but not both
    print(exam ^ project)


if __name__ == '__main__':
    main()
