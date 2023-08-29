import requests
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from time import sleep

def check_email(email_line):
    full_line = email_line.strip()
    if full_line == '':
        return False

    splited_full_line = full_line.split(':')
    username = splited_full_line[0]
    pasword = splited_full_line[1]

    url = 'https://s.activision.com/activision/signup/checkEmail'
    params = {
        'email': username
    }

    try:
        response = requests.post(url, params=params)
        #print(response.url)
        response.raise_for_status()  # پرتاب خطا در صورتی که پاسخ غیر 200 باشد
        json_response = response.json()

        if json_response['status'] == 'valid':
            with open(os.path.dirname(os.path.realpath(__file__)) + '/valid_emails.txt', 'a') as valid_emails_file:
                valid_emails_file.write(email_line)
            return True

        return False

    except requests.exceptions.RequestException as e:
        print(f"Error processing email {username}: {e}")


if __name__ == "__main__":
    all_mails_file =  open(os.path.dirname(os.path.realpath(__file__)) + '/all_emails.txt', 'r')
    email_lines = all_mails_file.readlines()


    total_lines = len(email_lines)
    successful_count = 0

    with ThreadPoolExecutor(max_workers=2) as executor:
        for result in tqdm(executor.map(check_email, email_lines), total=total_lines):
            if result:
                successful_count += 1

    success_rate = (successful_count / total_lines) * 100
    print(f"Success Rate: {success_rate:.2f}%")
