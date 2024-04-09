# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def main():
    data = pd.read_csv('sample_data.csv')
    print(data)
    features = data.iloc[:, :-1].values
    target = data.iloc[:, 1].values
    print(features)
    print(target)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
