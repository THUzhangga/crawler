import requests

urls = open('江泽民/urls.txt')

num = 0
for url in urls:
    try:
        r = requests.get(url[:-1])
        with open(f'江泽民/{num}.jpg', 'wb') as file:
            file.write(r.content)
        print(num)
    except:
        pass
    num += 1