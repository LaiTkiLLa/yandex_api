import requests

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {"Authorization": "AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM"}


# def disk_path(disk_file_path):
#     params = {'path': disk_file_path, 'overwrite': 'true'}
#     resp = requests.get(url, headers=headers, params=params)
#     print(resp)
#     upload_url = resp.json()['href']
#     return upload_url
# print(disk_path('C\\Users\\admin\\PycharmProjects\\Yandex'))
#
# def load_file(disk_file_path, filename):
#     load_url = disk_path(disk_file_path)
#     print(load_url)
#     with open(filename, 'rb') as file:
#         response = requests.put(load_url, params=file)
#         return response
#
# #
# print(load_file('C\\Users\\admin\\PycharmProjects\\Yandex', 'Test'))

def new_folder(name_folder):
    params = {'path' : name_folder}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(url=url, params=params, headers=headers)
    return response

def disk_load_test(disk_file_path, name_folder, name_file):
    params = {'path': disk_file_path, 'overwrite': 'true'}
    name_folder = new_folder(name_folder)
    params_2 = {'path' : name_folder}
    resp = requests.get(url, headers=headers, params=params)
    upload_url = resp.json()['href']
    with open(name_file, 'rb') as f:
        response = requests.put(url=upload_url, params=params_2, files={'file':f})
        return response
print(disk_load_test('C\\Users\\admin\\PycharmProjects\\Yandex', 'Netology', 'Test'))