import requests

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
token = str(input('Введите свой токен\n'))
headers = {"Authorization": token}
disk_file_path = str(input('Введите путь до файла\n'))
filename = str(input('Как назвать файл?\n'))

def disk_path():
    params = {'path': filename, 'overwrite': 'true'}
    resp = requests.get(url, headers=headers, params=params)
    upload_url = resp.json()['href']
    print(upload_url)
    with open(disk_file_path, 'r') as file:
        response = requests.put(url=upload_url, files={'file':file})
        return response

print(disk_path())
