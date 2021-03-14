import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.As-AfBfP7J1ijKXqZ4QPrKkhvbdtcrfN0Qeci3X2DEzCEtvrG1xcj0v-QYmk-waFzJAvwRn9Qg7wb6h_2IGg6b_TxDKMp8ckV0qN_ZN9xpj9mer2iqrgV66HC6MEGGgoDo52oQ98mfc'
    transferData = TransferData(access_token)

    file_from = 'test.txt' 
    file_to = '/test.txt'

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__': 
    main()
