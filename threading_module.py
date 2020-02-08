import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

import threading

def do_something_with_args(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)...'

start = time.perf_counter()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something_with_args, args=[1.5])
    t.start() 
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

# use thread pool executor

import concurrent.futures

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something_with_args, 1.5)
    f2 = executor.submit(do_something_with_args, 1.5)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    fs = [executor.submit(do_something_with_args, sec) for sec in secs]

    for f in concurrent.futures.as_completed(fs):
        print(f.result())        

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something_with_args, secs)

    # will complete in the order of submit

    for result in results:
        print(result)        

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)

import requests

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start = time.perf_counter()

def download_img(img_url):
    r = requests.get(img_url)
    img_bytes = r.content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(f'test_files/{img_name}', 'wb') as f:
        f.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)

finish = time.perf_counter()
print(f'Finish in {round(finish - start, 2)} seconds')

print('='*50)



