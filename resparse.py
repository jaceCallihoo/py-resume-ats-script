#!/usr/bin/python

from pyresparser import ResumeParser
import json
import sys

if (len(sys.argv) > 1):
    data = ResumeParser(sys.argv[1]).get_extracted_data()
    json_formatted_str = json.dumps(data, indent=4)
    print("resume data", json_formatted_str)
else:
    print("file argument required")
