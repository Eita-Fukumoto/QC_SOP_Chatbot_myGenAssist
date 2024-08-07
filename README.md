# QC_SOP_Chatbot_myGenAssist
This is to make an assistant with Machine CWID via myGenAssist API. Then upload SOPs to myGenAssist and attach them to the Assistant.<br>
SOPs are stored in LifeDoc and employees check SOPs in daily operation, but search function in LifeDoc is not good. It results in much time to fetch info they want to know.<br>
This Chatbot support to give info they want to know and show which documents include the info.<br>
It is not allowed to operate based on myGenAssist answer because myGenAssist sometimes reply wrong info.<br>
Before moving to the operation, employees need to check original documents.

## How QC SOP Chatbot work with myGenAssist
Assistant is made with Machine CWID.<br>
All QC SOPs are uploaded and attached to the Assistant so everyone can use it and search all info from SOPs.<br>

## How to make the chatbot
myGenAssist_Assistant.py has a class related to commands in myGenAssist such as uploading files, creating chatbot, and attaching files.<br>
QCSOP_chatbot.py is to create a new Assistant. Proxy function helps set a proxy to access myGenAssist via API.<br>
Example of prompt is in py file as Japanse.

## How to upload files and attach files to the Assistant
upload_files_attach_files.py works to upload files saved in a local environment to myGenAssist files. <br>
Files uploaded in myGenAssist have identification each file. <br>
To attach files to the Assistant, the id is needed. Next step is to get id. <br>
Then, all files are attached to the Assistant by using ids.
