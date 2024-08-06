import requests


class MyGenAssist_Assistants_Management:

    def __init__(self, myGenAssist_token, **kwargs):
        self.myGenAssist_token = myGenAssist_token
        self.header = {
            "Authorization": "Bearer " + self.myGenAssist_token,
            "Accept": "application/json",
        }
        self.proxy = kwargs

    def create_assistant(self, logo_path, **kwargs):

        url_assistant = "https://chat.int.bayer.com/api/v2/assistants"

        headers = self.header

        files = {"assistant_logo": ("logo.jpg", open(logo_path, "rb"), "image/jpeg")}

        data = kwargs

        response = requests.post(
            url_assistant, files=files, data=data, headers=headers, proxies=self.proxy
        )

        return response

    def get_created_assistant(self, assistant_id):

        url = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}"

        headers = self.header

        response = requests.get(url, headers=headers)

        return response

    def update_assistant(self, assistant_id, **kwargs):

        url = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}"

        headers = self.header

        data = kwargs

        response = requests.patch(url, headers=headers, proxies=self.proxy, data=data)

        return response

    def upload_file(self, uploaded_filepath, saved_filename, folder_url):

        headers = self.header

        file = {
            "files": (
                saved_filename,
                open(uploaded_filepath, "rb"),
                "multipart/form-data",
            )
        }

        response = requests.post(
            folder_url, proxies=self.proxy, headers=headers, files=file
        )

        return response

    def add_users(self, assistant_id, user_id):

        headers = self.header

        url_access = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}/users/{user_id}"

        response = requests.post(url_access, headers=headers)

        return response

    def get_uploaded_file_info(self, folder_url, **kwargs):

        headers = self.header

        data = kwargs

        response = requests.get(
            folder_url, params=data, proxies=self.proxy, headers=headers
        )

        return response

    def confirm_attachedfiles(self, assistant_id):

        url_files = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}/files"

        headers = self.header

        response = requests.get(url_files, headers=headers)

        return response

    def attach_files(self, assistant_id, fileidlist):

        url_files = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}/files"

        headers = self.header

        data = {
            "file_ids": fileidlist,
        }

        response = requests.post(url_files, headers=headers, json=data)

        return response

    def detach_files(self, assistant_id, fileid):
        url_detach_files = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}/files/{fileid}"

        headers = self.header

        response = requests.delete(url_detach_files, headers=headers)

        return response

    def delete_assistant(self, assistant_id):

        url = f"https://chat.int.bayer.com/api/v2/assistants/{assistant_id}"

        headers = self.header

        response = requests.delete(url, headers=headers)

        return response
