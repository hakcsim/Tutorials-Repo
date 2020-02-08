import time
import requests
import json

def get_count(x):
    return list(x.items())[0][1]

def download():
    r = requests.get('https://formulae.brew.sh/api/formula.json')

    packages_json = r.json()

    print(json.dumps(packages_json[0], indent=2))

    results = []

    t1 = time.perf_counter()

    for package in packages_json:

        package_url = f'https://formulae.brew.sh/api/formula/{package["name"]}.json'

        r = requests.get(package_url)    
        package_json = r.json()

        # print(json.dumps(package_json, indent=2))

        print(f'{package_json["name"]} took {r.elapsed.total_seconds()} seconds')

        results.append({
            'name': package_json['name'],
            'desc': package_json['desc'],
            'analytics': 
            {
                '30d': get_count(package_json['analytics']['install_on_request']['30d']),
                '90d': get_count(package_json['analytics']['install_on_request']['90d']),
                '365d': get_count(package_json['analytics']['install_on_request']['365d']),
            }
        })

        time.sleep(r.elapsed.total_seconds())

    t2 = time.perf_counter()

    print(f'Processing time = {(t2 - t1) / 60} mins')

    with open('test_files/packages.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def get_30d_key(x):
    return x['analytics']['30d']

def get_90d_key(x):
    return x['analytics']['90d']

def get_365d_key(x):
    return x['analytics']['365d']

def sort():

    with open('test_files/packages.json', 'r') as f:
        packages_json = json.load(f)

    print(len(packages_json))

    x = packages_json[0]

    # packages_json = [item for item in package_json if 'video' in item['desc']]    

    sorted_30d = sorted(packages_json, key=get_30d_key, reverse=True)
    sorted_90d = sorted(packages_json, key=get_90d_key, reverse=True)
    sorted_365d = sorted(packages_json, key=get_365d_key, reverse=True)

    print(f"30 days most popular = {sorted_30d[0]['name']}, {sorted_30d[0]['analytics']['30d']}")
    print(f"90 days most popular = {sorted_90d[0]['name']}, {sorted_90d[0]['analytics']['90d']}")
    print(f"365 days most popular = {sorted_365d[0]['name']}, {sorted_365d[0]['analytics']['365d']}")

if __name__ == '__main__':
    download()
    sort()