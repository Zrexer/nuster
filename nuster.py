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
    def usage():
        return 'nuster -u #< https://example.com/ | https://example.com > -o #<wordlist file name> -s [optional => save all 200 status on file: result.txt]'
    
    def version_():
        return '3.0.1'
    
    def run():
        l = sys.argv
        
        if '-u' in l:
            global url
            url = l.index('-u')+1
            # if / end of url
            if str(l[url]).endswith('/'):
                # Not request for wordList
                if not '-o' in l:
                    domainList = ['index.php', "index" ,'admin.php', "admin", 'support.php', "support"]
                    # Save Switch
                    if l[-1] == "-s":    
                        for dl in domainList:
                            status = sp(url=l[url], under_domain=dl)
                            if str(status) == "200":
                                print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}{dl} \033[91m]')
                                with open('result.txt', 'a') as fileSaver1:
                                    fileSaver1.write(f'\n{l[url]}{dl}')
                                    fileSaver1.close()
                                
                            else:
                                print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')
                            
                            
                            
                    # if Save Switch not call
                    else:
                        for dl in domainList:
                                status = sp(url=l[url], under_domain=dl)
                                if str(status) == "200":
                                    print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}{dl} \033[91m]')
     
                                else:
                                    print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')

                # request for read on wordList
                else:
                    fileOpen = l.index('-o')+1
                    readIT = op(l[fileOpen]).split()
                    for rit in readIT:
                        status = sp(l[url], under_domain=rit)
                        if str(status) == "200":
                            print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{rit}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}{rit} \033[91m]')
                            
                        else:
                            print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{rit}\033[93m:\033[90m{status}')
            
            # if not / end of  url
            else:
                # Not request for wordList
                if not '-o' in l:
                    domainList = ['index', 'index.php', 'admin', 'admin.php', 'support', 'support.php']
                    # request for Save Switch
                    if l[-1] == "-s":
                        for dl in domainList:
                            status = sps(l[url], under_domain=dl)
                            if str(status) == "200":
                                print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}/{dl} \033[91m]')
                                with open('result.txt', 'a') as fileSaver1:
                                    fileSaver1.write(f'\n{l[url]}/{dl}')
                                    fileSaver1.close()

                            else:
                                print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')
                    # not request for Save Switch
                    else:
                        for dl in domainList:
                            status = sps(l[url], under_domain=dl)
                            if str(status) == "200":
                                print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{dl}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}/{dl} \033[91m]')
                            else:
                                print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{dl}\033[93m:\033[90m{status}')
                
                # request for wordList
                else:
                    fileOpen = l.index('-o')+1
                    readIT = op(l[fileOpen]).split()
                    # request for Save Switch
                    if l[-1] == "-s":
                        for rit in readIT:
                            status = sps(l[url], under_domain=rit)
                            if str(status) == "200":
                                print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{rit}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}/{rit} \033[91m]')
                                with open('result.txt', 'a') as fileSaver1:
                                    fileSaver1.write(f'\n{l[url]}/{rit}')
                                    fileSaver1.close()
                    
                            else:
                                print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{rit}\033[93m:\033[90m{status}')
                    # not request for Save Switch
                    else:
                        for rit in readIT:
                            status = sps(l[url], under_domain=rit)
                            if str(status) == "200":
                                print(f'\033[94m[\033[91m*\033[94m] \033[92munder domain\033[93m: \033[97m{rit}\033[93m:\033[97m{status} \033[91m[ \033[97m{l[url]}/{rit} \033[91m]')
                                
                            else:
                                print(f'\033[94m[\033[91m!\033[94m] \033[90munder domain\033[93m: \033[90m{rit}\033[93m:\033[90m{status}')
                                

        if "-h" in l:
            print(MainActivity.usage())
            
        if "--help" in l:
            print(MainActivity.usage())
            
        if "-v" in l:
            print(MainActivity.version_())
        
        if "--version" in l:
            print(MainActivity.version_())

        if len(l) <= 1:
            print(MainActivity.usage())
            
            

if __name__ == '__main__':
    try:
        MainActivity.run()
    except BaseException and KeyboardInterrupt as ALLZ:
        if ALLZ == KeyboardInterrupt:
            print('exit')
        
        elif ALLZ == BaseException:
            print(BaseException)


