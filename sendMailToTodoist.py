#!/usr/bin/env python3
import sys
import os
from todoist_api_python.api import TodoistAPI
import json

api = TodoistAPI(os.environ['todoist_api_key'])

if '/' in sys.argv[1]:
    projectid = int(sys.argv[1].split('/')[0])
    sectionid = int(sys.argv[1].split('/')[1])
else:
    projectid = int(sys.argv[1])
    sectionid = None
title = sys.argv[2]
print(sys.argv[1])

messages = []

for x in sys.stdin:
    messages.append(json.loads(x))

print(messages[0])
js = messages[0]

if title != "":
    content = '* ✉️ [**%s**](message://%%3c%s%%3e) %s' % (js['sender'], js['messageId'], title)
else:
    content = '* ✉️ [**%s**](message://%%3c%s%%3e) "%s"' % (js['sender'], js['messageId'], js['subject'])
desc = '%s' % (js['content'])

if sectionid is not None:
    api.add_task(content=content, description=desc, project_id=projectid, section_id=sectionid, due_string='Today')
else:
    api.add_task(content=content, description=desc, project_id=projectid, due_string='Today')

