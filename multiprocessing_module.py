import time

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

start = time.perf_counter()

do_something()
do_something()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

import multiprocessing

start = time.perf_counter()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

def do_something_with_args(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'

start = time.perf_counter()

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something_with_args, args=[1.5])
    p.start()
    processes.append(p)

for p in processes:
    p.join()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

# use process pool executor

import concurrent.futures

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something_with_args, 1.5)
    f2 = executor.submit(do_something_with_args, 1.5)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    fs = [executor.submit(do_something_with_args, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(fs):
        print(f.result())

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    fs = [executor.submit(do_something_with_args, sec) for sec in secs]

    for f in concurrent.futures.as_completed(fs):
        print(f.result())

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

# every time we use a context manager as below. The code will 
# wait for all the process to completer (i.e. automatic join)
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something_with_args, secs)

    for result in results:
        # handle exception here
        try:
            print(result)
        except Exception as e:
            print(e)    

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

import os
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

size = (1200, 1200)

def process_image(img_name):
    image = Image.open(f'test_files/{img_name}')
    image.filter(ImageFilter.GaussianBlur(25))
    image.thumbnail(size)
    fname, _ = os.path.splitext(img_name)
    image.save(f'test_files/{fname}_1200.png')
    return f'{img_name} processed...'

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(process_image, img_names)
    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)
