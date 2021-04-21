import requests

token = ''
files_list = ['UploadFiles/file.txt', 'UploadFiles/file copy.txt']

class YaUploader:
    def __init__(self, files_list):
        self.files_list = files_list
        self.file_path = ''
        self.dir_path = ''
        self.all_path = ''

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, path):
        file_path = ''
        i = len(path) - 1
        while path[i] != '/':
            file_path += path[i]
            i -= 1
        self.file_path = file_path[::-1]
        self.dir_path = path[0:i+1]
        self.all_path = self.dir_path + self.file_path
        href = self._get_upload_link(disk_file_path = self.all_path).get('href', '')
        response = requests.put(href, data=open(self.all_path , 'rb'))

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # href = self._get_upload_link(disk_file_path=self.dir_path).get("href", "")
        # response = requests.put(href + self.dir_path)
        # response.raise_for_status()
        for j in range(len(self.files_list)):
            response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources/?path=' + self.dir_path, headers = self.get_headers())
            response = self.upload_file_to_disk(files_list[j])
        

if __name__ == '__main__':
    uploader = YaUploader(files_list)
    result = uploader.upload()