# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Find all valid email addresses in the string using regex
        emails = re.findall(
            r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
            self.email_string
        )

        # Remove duplicates and return sorted list
        return sorted(set(emails))
