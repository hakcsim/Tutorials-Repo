from matplotlib import pyplot as plt
import pandas as pd

def test1():

    plt.style.use('fivethirtyeight')

    ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
    bins = [10,20,30,40,50,60]
    plt.hist(ages, bins=bins, edgecolor='black')

    plt.title('Ages of Respondents')
    plt.ylabel('Total Respondents')
    plt.xlabel('Ages')

    plt.legend()
    plt.tight_layout()
    plt.show()

def test2():

    plt.style.use('fivethirtyeight')

    data = pd.read_csv('test_files/ages.csv')
    ids = data['Responder_id']
    ages = data['Age']

    bins = [10,20,30,40,50,60,70,80,90,100]
    plt.hist(ages, bins=bins, edgecolor='black', log=True)

    median_age = 29
    plt.axvline(median_age, color='#fc4f30', label='Median Age', linewidth=2)

    plt.title('Ages of Respondents')
    plt.ylabel('Total Respondents')
    plt.xlabel('Ages')

    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test2()
