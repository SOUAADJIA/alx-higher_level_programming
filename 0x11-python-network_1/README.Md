# 0x11. Python - Network #1

## Description
This repository contains solutions for tasks related to fetching internet resources using the Python package urllib and the Requests package. The tasks cover topics such as making HTTP GET, POST, PUT requests, decoding response bodies, and manipulating data from external services.

## Learning Objectives
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- README.md file at the root of the folder of this project is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using wc
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary value by key
- Documentation should be meaningful sentences

## Tasks

### 0. What's my status? #0
Write a Python script that fetches https://alx-intranet.hbtn.io/status
- Use the package urllib
- Do not import any packages other than urllib
- Display the body of the response with specific information

Example:
```bash
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$

