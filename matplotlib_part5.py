from matplotlib import pyplot as plt
import pandas as pd

def test1():

    data = pd.read_csv('test_files/dev_salaries.csv')

    print(data.columns)

    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
    plt.plot(ages, py_salaries, label='Python')

    plt.title('Median Salary (USD) by Age')
    plt.ylabel('Median Salary (USD)')
    plt.xlabel('Ages')

    overall_median = 57287

    plt.fill_between(ages, py_salaries, overall_median, 
                    where=(py_salaries > overall_median),
                    interpolate=True,
                    alpha='0.25')

    plt.fill_between(ages, py_salaries, overall_median, 
                    where=(py_salaries <= overall_median),
                    interpolate=True,
                    color='red',
                    alpha='0.25')

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def test2():

    data = pd.read_csv('test_files/dev_salaries.csv')

    print(data.columns)

    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
    plt.plot(ages, py_salaries, label='Python')

    plt.title('Median Salary (USD) by Age')
    plt.ylabel('Median Salary (USD)')
    plt.xlabel('Ages')

    plt.fill_between(ages, py_salaries, dev_salaries, 
                    where=(py_salaries > dev_salaries),
                    interpolate=True,
                    alpha=0.25,
                    label='Above Avg')

    plt.fill_between(ages, py_salaries, dev_salaries, 
                    where=(py_salaries <= dev_salaries),
                    interpolate=True,
                    color='red',
                    alpha=0.25,
                    label='Below Avg')

    plt.legend()

    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    #test1()
    test2()