#!/usr/bin/env python3
"""
Nuster
~~~~~~

nuster is a under domain searcher tool writed on py3

Dev: `Host1let`

"""

import requests
import sys

def op(fn):
    with open(fn, 'r') as OP:
        return OP.read()
        
def sps(url, under_domain):
    return requests.get(f'{url}/{under_domain}').status_code

def sp(url, under_domain):
    return requests.get(url=url+under_domain).status_code




class MainActivity:
    def run():
        l = sys.argv
        
        if '-u' in l:
            url = l.index('-u')+1
            if str(l[url]).endswith('/'):
                if not '-o' in l:
                    domainList = ['index.php', "index" ,'admin.php', "admin", 'support.php', "support"]
                    for dl in domainList:
                        status = sp(url=l[url], under_domain=dl)
                        if str(status) == "200":
                            print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status}')
                            
                        else:
                            print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')
                else:
                    fileOpen = l.index('-o')+1
                    readIT = op(l[fileOpen]).split()
                    for rit in readIT:
                        status = sp(l[url], under_domain=rit)
                        if str(status) == "200":
                            print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{rit}\033[93m:\033[97m{status}')
                            
                        else:
                            print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{rit}\033[93m:\033[90m{status}')
            else:
                if not '-o' in l:
                    domainList = ['index', 'index.php', 'admin', 'admin.php', 'support', 'support.php']
                    for dl in domainList:
                        status = sps(l[url], under_domain=dl)
                        if str(status) == "200":
                            print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status}')
                            
                        else:
                            print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')
                else:
                    fileOpen = l.index('-o')+1
                    readIT = op(l[fileOpen]).split()
                    for rit in readIT:
                        status = sps(l[url], under_domain=rit)
                        if str(status) == "200":
                            print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{rit}\033[93m:\033[97m{status}')
                            
                        else:
                            print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{rit}\033[93m:\033[90m{status}')
                            

        if "-h" in l:
            print('nuster -u #< https://example.com/ | https://example.com > -o #<wordlist file name>')
            
        if "--help" in l:
            print('nuster -u #< https://example.com/ | https://example.com > -o #<wordlist file name>')

        if len(l) <= 1:
            print('nuster -u #< https://example.com/ | https://example.com > -o #<wordlist file name>')
            

if __name__ == '__main__':
    MainActivity.run()


