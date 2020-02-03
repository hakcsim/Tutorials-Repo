import random
import csv
import time
import os

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ['x_value', 'total_1', 'total_2']

with open('test_files/data_gen.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

start_time = time.perf_counter()

while True:

    with open('test_files/data_gen.csv', 'a') as f:

        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)

        data_row = { 'x_value': x_value, 'total_1': total_1, 'total_2': total_2 }
        print(data_row)

        csv_writer.writerow(data_row)

        x_value += 1
        total_1 = total_1 + random.randint(-5, 6)
        total_2 = total_2 + random.randint(-5, 6)

        time.sleep(1)

    if time.perf_counter() - start_time > 60:
        break

os.remove('test_files/data_gen.csv')



