from matplotlib import pyplot as plt

print(plt.style.available)

plt.style.use('ggplot')
plt.xkcd()

ages_x = [*range(25,36)]
dev_y = [38496, 42000, 46752, 49320, 53200, 
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, py_dev_y, color='#5a7b9a', marker='o', linewidth=3, label='Python')
plt.plot(ages_x, js_dev_y, color='#adad3b', marker='.', linewidth=3, label='Javescript')
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All')

# using format string
# plt.plot(ages_x, dev_y, 'k--', label='All')
# plt.plot(ages_x, py_dev_y, 'b', label='Python')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('MEdian Salary (USD)')

# plt.legend(['All', 'Python'])

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('test_files/plot.png')

plt.show()         


