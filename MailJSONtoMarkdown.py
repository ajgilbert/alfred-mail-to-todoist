#!/usr/bin/python3
import sys
import json

for x in sys.stdin:
    js = json.loads(x)
    print('✉️ [**%s**](message://%%3c%s%%3e) "%s" (%s)\n```plaintext\n%s\n```' % (js['sender'], js['messageId'], js['subject'], js['dateReceived'], js['content']))
