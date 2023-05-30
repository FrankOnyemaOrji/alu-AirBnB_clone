#!/usr/bin/python3
"""W3C validator for ALU
For HTML and CSS files.

Based on 2 APIs:
- https://validator.w3.org/nu/

usage:
Simple file:
```
./w3c_validator.py index.html
```
Multiple files:
```
./w3c_validator.py index.html header.html styles/common.css
```
All errors are printed in `STDERR`
Return:
Exit status is the # of errors, 0 on Success
"""

import sys
import requests
import os


def __print_stdout(msg):
    """Print message in STDOUT"""
    sys.stdout.buffer.write(msg.encode('utf-8'))


def __print_stderr(msg):
    """Print message in STDERR"""
    sys.stderr.buffer.write(msg.encode('utf-8'))


def __is_empty(file_path):
    """Check if file is empty"""
    if os.path.getsize(file_path) == 0:
        raise OSError("File '{}' is empty".format(file_path))
    

def __validate(file_path, type):
    """Start validation of file process"""
    h = {'Content-Type': "{}; charset=utf-8".format(type)}
    # open file in binary mode
    # https://requests.readthedocs.io/en/master/user/advanced/
    d = open(file_path, 'rb').read()
    u = 'https://validator.w3.org/nu/?out=json'
    r = requests.post(u, headers=h, data=d)

    if not r.status_code < 400:
        raise ConnectionError("Can't connect to API endpoint")
    
    res = []
    mesg = r.json().get('messages', [])
    for m in mesg:
        if m.get('type') == 'error':
            res.append("'{}' => {}".format(file_path, m['message']))
        else:
            res.append("[{}: {}] => {}".format(
                file_path, m['lastLine'], m['message']))
    return res


def __analyze(file_path, type):
    """Analyze file type and start validation"""
    nb_err = 0
    try:
        results = None

        if file_path.endswith('.css'):
            __is_empty(file_path)
            results = __validate(file_path, type='text/css')
        elif file_path.endswith('.html', ".htm"):
            __is_empty(file_path)
            results = __validate(file_path, type='text/html')
        elif file_path.endswith('.svg'):
            __is_empty(file_path)
            results = __validate(file_path, type='image/svg+xml')
        else:
            allowed_files = ['.css', '.html', '.htm', '.svg']
            raise OSError(
                "File {} does not have valid file extension.\nOnly {} are"
                " allowed".format(file_path, allowed_files)
            )
        
        if len(results) > 0:
            for r in results:
                __print_stderr("[W3C] {}\n".format(r))
                nb_err += len(results)
        else:
            __print_stdout("'{}' => OK\n".format(file_path))

    except OSError as e:
        __print_stderr("'{}' => {}\n".format(e.__class__.__name__, e))
        return nb_err
    

def __files_loop():
    """Loops through files and anaylzes them"""
    nb_err = 0
    for file_path in sys.argv[1:]:
        nb_err += __analyze(file_path)
    return nb_err


if __name__ == "__main__":
    """Main function"""
    if len(sys.argv) < 2:
        __print_stderr("Please pass at least one file to validate\n")
        exit(1)
    """Execute files loop"""
    sys.exit(__files_loop())
