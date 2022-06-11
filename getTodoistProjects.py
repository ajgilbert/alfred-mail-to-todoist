# import sys
import json
import os
from todoist_api_python.api import TodoistAPI

api = TodoistAPI(os.environ['todoist_api_key'])
try:
    projects = api.get_projects()
    sections = api.get_sections()
    # print(sections)
except Exception as error:
    print(error)


res = {"items": list()}
project_name_map = {}
for p in projects:
    project_name_map[p.id] = p.name
    res["items"].append({
        "uid": str(p.id),
        "title": p.name,
        "arg": p.name,
        "variables": {"id": str(p.id)}
    })
    #print(p.name)
for p in sections:
    sec_name = p.name
    if p.project_id in project_name_map:
        sec_name = project_name_map[p.project_id] + ' / ' + sec_name
    res["items"].append({
        "uid": str(p.id),
        "title": sec_name,
        "arg": sec_name,
        "variables": {"id": (str(p.project_id) + "/" + str(p.id))}
    })

    # Get the parent project
print(json.dumps(res))
