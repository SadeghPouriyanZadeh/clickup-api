import os

import requests

task_id = os.environ.get("TASK_ID")
url = "https://api.clickup.com/api/v2/task/" + task_id + "/comment"

query = {"custom_task_ids": "true", "team_id": "123"}
comment = input("Type your comment text:\n")

payload = {"comment_text": f"{comment}", "assignee": 183, "notify_all": True}

authorization = os.environ.get("AUTHORIZATION")

headers = {"Content-Type": "application/json", "Authorization": authorization}

response = requests.post(url, json=payload, headers=headers, params=query)

if response.status_code == 200:
    print("Comment posted successfully")
else:
    print("Failed to post comment")
