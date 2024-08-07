"""
Upload documents from local PC to myGenAssist Files. Get ids of uploaded docs to attach them to the Assistant.
Attach all documents to the Assistant.
"""

import requests
import time
from datetime import datetime

from myGenAssist_Assistant import MyGenAssist_Assistants_Management


def myproxy(cwid, password):
    http_proxy = f"http://{cwid}:{password}@10.185.190.100:8080"

    proxyDict = {"http": http_proxy, "https": http_proxy}

    return proxyDict


"""
Upload docs to myGenAssist
"""

uploaded_filepaths = "file paths in local environment are saved in list"
saved_filename = "file names saved in myGenAssit are stored in list"
myGenAssist_url = 'https://chat.int.bayer.com/api/v2/files'

mygen = MyGenAssist_Assistants_Management(
    myGenAssist_token="Your API", **myproxy("cwid", "password"))



for uploaed_filepath, saved_filename in zip(uploaded_filepaths, saved_filename):

    #Upload document to myGenAssist
    response = mygen.upload_file(uploaed_filepath, saved_filename, myGenAssist_url)

    #Show time and status and uploaed info, just in case
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Time: {current_time}")
    
    print(response.status_code)
    print(response.json())
    time.sleep(60)


"""
Get docs id in myGenAssit to attach them to the Assistant
"""

#Based on myGenAssist specification, limit to get file info is up to 200.
#Need offset to access more than 200 docs.
initial_offset = 0

#Save file info
files = []

#Save only file ids
file_ids = []

#Loop until getting all file info.
for i in range(100): #100 does not have meaning. It works to make loops up to the end.

    body = {
        "limit" : 200,
        "offset" : initial_offset + (200 * i)}
    
    response = mygen.get_uploaded_file_info(folder_url= myGenAssist_url, **body)

    for j in range(len(response.json())):
        files.append(response.json()[j])
        file_ids.append(response.json()[j]["id"])

    if len(response.json()) < 200:
        break


"""
Attach files to the Assistant
"""

assistant_id = "Your assistant id"

#To attach files to the assistant, no need to loop. It is possible to attach all files at once.
response = mygen.attach_files(assistant_id, file_ids)
print(response.status_code)