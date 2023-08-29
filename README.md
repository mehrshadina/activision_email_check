# Activision Email Checker

A simple Python script to check the validity of emails using the Activision API.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)

## Description

This script uses the Activision API to validate a list of emails provided in a text file. It sends a POST request for each email and checks if the email is valid according to the API's response.

## Features

- Check the validity of emails using the Activision API.
- Display progress using the `tqdm` library.
- Write valid emails to a separate text file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/email-checker.git
   cd email-checker
   ```

2. Install the required dependencies:

   ```bash
   pip install requests tqdm
   ```

## Usage

Prepare a text file named all_emails.txt containing a list of emails in the format email:password.

Run the script:

  ```bash
  python email_checker.py
  ```

OR 

  ```bash
  python email_checker_without_multi_threat.py
  ```

The script will send requests to the Activision API to check the validity of each email. Valid emails will be saved in the valid_emails.txt file and Unvalid emails will be saved in the unvalid_emails.txt file.

## Dependencies

    Python 3.x
    requests library
    tqdm library

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.
Make your changes and test them thoroughly.
Commit your changes: git commit -am 'Add some feature'.
Push the branch to your fork: git push origin feature-name.
Create a pull request explaining your changes.

Please read the CONTRIBUTING.md file for more details.
Changelog

For information about the changes in each version of the script, please refer to the CHANGELOG.md file.
License

This project is licensed under the MIT License.
