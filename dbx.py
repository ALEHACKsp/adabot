import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
    
    def download_file(self, file_path):
        dbx = dropbox.Dropbox(self.access_token)
        md, res = dbx.files_download(file_path)
        return res.content

def main():

    access_token = os.environ['dropbox_token']

    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    data = transferData.download_file(file_to)
    print(data)

if __name__ == '__main__':
    main()