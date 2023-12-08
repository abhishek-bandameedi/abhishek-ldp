import re

# matching dates
pattern = r'\d{2}/\d{2}/\d{4}'
text = 'Date: 01/15/2023, Time: 12/30/2022'
matches = re.findall(pattern, text)
print('Dates:', matches)

# Extracting Email Addresses

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = 'Emails: user1@example.com, user2@gmail.com'
emails = re.findall(pattern, text)
print('Emails:', emails)