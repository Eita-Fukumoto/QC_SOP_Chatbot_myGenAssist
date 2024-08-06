# QC_SOP_Chatbot_myGenAssist
This is to make an assistant with Machine CWID via myGenAssist API. Then upload SOPs to myGenAssist and attach them to the Assistant.

## How QC SOP Chatbot work with myGenAssist
Assistant is made with Machine CWID.<br>
All QC SOPs are uploaded and attached to the Assistant so everyone can use it and search all info from SOPs.

## How to make the chatbot
myGenAssist_Assistant.py has a class related to commands in myGenAssist such as uploading files, creating chatbot, and attaching files.<br>
QCSOP_chatbot.py is to create a new Assistant. Proxy function helps set a proxy to access myGenAssist via API.<br>
Example of prompt is in py file as Japanse.

