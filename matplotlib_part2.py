import csv
import numpy as np
from matplotlib import pyplot as plt

def test1():
    ages_x = [*range(25,36)]
    x_indices = np.arange(len(ages_x))
    bar_width = 0.25

    dev_y = [38496, 42000, 46752, 49320, 53200, 
            56000, 62316, 64928, 67317, 68748, 73752]

    py_dev_y = [45372, 48876, 53850, 57287, 63016,
                65998, 70003, 70000, 71496, 75370, 83640]

    js_dev_y = [37810, 43515, 46823, 49293, 53437, 
                56373, 62375, 66674, 68745, 68746, 74583]

    plt.bar(x_indices - bar_width, dev_y, width=bar_width, label='All')
    plt.bar(x_indices, py_dev_y, width=bar_width, label='Python')
    plt.bar(x_indices + bar_width, js_dev_y, width=bar_width, label='Javescript')

    # using format string
    # plt.plot(ages_x, dev_y, 'k--', label='All')
    # plt.plot(ages_x, py_dev_y, 'b', label='Python')

    plt.xticks(ticks=x_indices, labels=ages_x)

    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('MEdian Salary (USD)')

    # plt.legend(['All', 'Python'])

    plt.legend()
    plt.tight_layout()

    # plt.savefig('test_files/plot.png')

    plt.show()         

def test2():

    from collections import Counter

    with open('test_files/languages.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        language_counter = Counter()

        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(';'))

    languages = []
    popularities = []

    for language, popularity in language_counter.most_common(15):
        languages.append(language)       
        popularities.append(popularity)       

    print(languages)
    print(popularities)

    languages.reverse()
    popularities.reverse()

    plt.barh(languages, popularities)
    plt.title('Most Popular Languages')
    plt.ylabel('Programming Languages')
    plt.xlabel('Number of Programmers')

    plt.tight_layout()
    plt.show()

def test3():

    from collections import Counter
    import pandas as pd

    data = pd.read_csv('test_files/languages.csv')

    print(data.columns)

    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages = []
    popularities = []

    for language, popularity in language_counter.most_common(15):
        languages.append(language)       
        popularities.append(popularity)       

    print(languages)
    print(popularities)

    languages.reverse()
    popularities.reverse()

    plt.barh(languages, popularities)
    plt.title('Most Popular Languages')
    plt.ylabel('Programming Languages')
    plt.xlabel('Number of Programmers')

    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    test3()


