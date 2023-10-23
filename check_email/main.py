import re

email_truth = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
email_input = input('Enter email:')
if re.search(email_truth,email_input):
    print('Right email')
else:
    print('Wrong email')