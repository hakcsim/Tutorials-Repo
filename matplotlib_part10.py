import pandas as pd
from matplotlib import pyplot as plt

def test1():

    plt.style.use('seaborn')

    data = pd.read_csv('test_files/dev_salaries.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, py_salaries, label='Python')
    plt.plot(ages, js_salaries, label='JavaScript')
    plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.legend()
    plt.tight_layout()
    plt.show()

def test2():

    plt.style.use('seaborn')

    data = pd.read_csv('test_files/dev_salaries.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    fig, ax = plt.subplots()

    print(ax)

    ax.plot(ages, py_salaries, label='Python')
    ax.plot(ages, js_salaries, label='JavaScript')
    ax.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

    ax.set_title('Median Salary (USD) by Age')
    ax.set_xlabel('Ages')
    ax.set_ylabel('Median Salary (USD)')

    ax.legend()
    plt.tight_layout()
    plt.show()

def test3():

    plt.style.use('seaborn')

    data = pd.read_csv('test_files/dev_salaries.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

    print(ax1)
    print(ax2)

    ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

    ax2.plot(ages, py_salaries, label='Python')
    ax2.plot(ages, js_salaries, label='JavaScript')

    ax1.legend()
    ax1.set_title('Median Salary (USD) by Age')
    ax1.set_ylabel('Median Salary (USD)')

    ax2.legend()
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary (USD)')

    plt.tight_layout()
    plt.show()


def test4():

    plt.style.use('seaborn')

    data = pd.read_csv('test_files/dev_salaries.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    print(ax1)
    print(ax2)

    ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

    ax2.plot(ages, py_salaries, label='Python')
    ax2.plot(ages, js_salaries, label='JavaScript')

    ax2.legend(loc='upper left')
    ax1.set_title('Median Salary (USD) by Age')
    ax1.set_xlabel('Ages')
    ax1.set_ylabel('Median Salary (USD)')

    ax2.legend(loc='upper left')
    ax2.set_title('Median Salary (USD) by Age')
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary (USD)')

    plt.tight_layout()
    plt.show()

    fig1.savefig('test_files/fig1.png')
    fig2.savefig('test_files/fig2.png')


if __name__ == '__main__':
    test4()
