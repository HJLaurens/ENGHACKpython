import json as js

PATH = '$json-requests-path'

with open PATH as f:
	f.load(f)
	for j in f['images']:
		classified = j['classifiers']