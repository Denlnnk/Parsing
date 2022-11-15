from linkedin import Linkedin
from email_creator import Email


def main():
    new_email = Email()
    new_email.create_email()
    first_name = str(input('Enter your first name: '))
    last_name = str(input('Enter your last name: '))
    number = str(input('Enter your number : '))
    register_link = Linkedin(first_name, last_name, number)
    register_link.account_register()


if __name__ == '__main__':
    main()
