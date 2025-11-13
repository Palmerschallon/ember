#!/usr/bin/env python3
import requests, json

r = requests.post('http://localhost:8080/chat', 
                  json={'message': 'Who are you? What is your relationship to tools?'}, 
                  timeout=30)
print(json.loads(r.text).get('response', r.text))

