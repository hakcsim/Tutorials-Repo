from matplotlib import pyplot as plt

def test1():

    plt.style.use('fivethirtyeight')

    slices = [120, 80, 30, 20]   # does not need to add up to 100
    labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
    colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

    plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black' })

    plt.title('My Awesome Pie Chart')
    plt.tight_layout()
    plt.show()

def test2():

    slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 
              23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 
              'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
    explode = [0, 0, 0, 0.1, 0] # 10% of radius

    plt.pie(slices[:5], labels=labels[:5], 
            explode=explode,
            shadow=True,
            startangle=90,
            autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title('')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test2()
