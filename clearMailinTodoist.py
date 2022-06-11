#!/usr/bin/env python3
import sys
import os
import json
from todoist_api_python.api import TodoistAPI

messages = list()
for x in sys.stdin:
    messages.append(json.loads(x))

messageids = [m["messageId"] for m in messages]
print(messageids)

api = TodoistAPI(os.environ['todoist_api_key'])

try:
    tasks = api.get_tasks() 
except Exception as error:
    print(error)


for t in tasks:
    for mid in messageids:
        if mid in t.content:
            print(t)
            try:
                is_success = api.close_task(task_id=t.id)
                print(is_success)
            except Exception as error:
                print(error)
