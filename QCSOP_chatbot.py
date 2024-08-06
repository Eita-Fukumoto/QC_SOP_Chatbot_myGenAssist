"""
Import class as MyGenAssist_Assistants_Management from myGenAssist_Assistant.py and use it to create an assistant.

"""

import requests
from myGenAssist_Assistant import MyGenAssist_Assistants_Management


def myproxy(cwid, password):
    http_proxy = f"http://{cwid}:{password}@10.185.190.100:8080"

    proxyDict = {"http": http_proxy, "https": http_proxy}

    return proxyDict


# Assistant prompt for QC SOP Assistant

assistant_prompt = """
#Request：
あなたは{{#Role}}です。問い合わせ内容に対して{{#Rules}}に従って回答してください。
回答は{{#Regulation}}形式に従ってください。

#Role : 
あなたは製薬会社のQuality ControlのExpertiseです。新たな逸脱が発生した際、膨大な過去の逸脱情報から類似案件の有無、ある場合は、類似案件の情報を提供してくれる優秀なチャットボットです。

#Regulation :
下記ポイントを簡潔に教えてください。
・ 過去に類似の逸脱の有無
類似の逸脱がある場合、
1 . 参照したドキュメント名。
2. 逸脱の概要
3. 結果の要約
4. 逸脱の原因 

#Rules :
・質問された内容をアップロードされた資料を参照して回答する。
・Regulationで要求された内容を回答するために情報が不足している場合は、追加で伝えるべき情報を質問者に確認する。
・回答は問い合わせの言語と同じ言語で出力すること。
・ドキュメントに書いてある内容をなるべくそのまま出力すること。
"""

# Discription of the assistant. It does not affect the function of the Assistant.
assistant_description = """
Search deviation that could happen past and tell the information.
"""

# Dictionary including body of Assistant.
data = {
    "access": "private",
    "instructions": assistant_prompt,
    "model": "gpt-4o",
    "name": "QC deviation master in Shiga",
    "temperature": "0.0",
    "description": assistant_description,
}

# Make an instance.
mygen = MyGenAssist_Assistants_Management(
    myGenAssist_token="Your API", **myproxy("cwid", "password")
)

# Need logo photo to create an assistant.
create_assistant = mygen.create_assistant(logo_path="Logo.jpg", **data)
