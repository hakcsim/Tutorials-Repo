import requests

r = requests.get('https://xkcd.com/353/')

# print(dir(r))
# print(help(r))

html = r.text
# print(html)

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.status_code)

# 200 - success
# 300 - redirect
# 400 - client error - no permission to access site
# 500 - server error - server crash

# True if not 400 or 500
print(r.ok) 

print(r.headers) 

with open('comic.png', 'wb') as f:
    f.write(r.content)

payload = { 'page': 2, 'key': 25}

r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)
print(r.text)

payload = {'username': 'corey', 'password': 'testing' }
r = requests.post('https://httpbin.org/post', data=payload)

print(r.url)
print(r.text)
print(r.json())

r_dict = r.json()
print(r_dict['form'])

