import re
str1 = """
This is where we paste our text. And start searching for Email . 
We can also use requests module to get data from internet.
 And, paste that here . the email are name123@gmail.com. 
 We also have another test Email Johncon26@gmail.com and Jhonny23@rediffmail.com"""
Email = re.findall(r'\w+\S@+\w+[.]+[a-zA-Z.0-9]+', str1)
op = open('Email_str1.txt', 'a')
j = 1
for i in Email:
    op.write(f"Email{j}:{i}\n")
    j += 1
print(f"Emails are {Email}")
print(f"Total number of emails present are {j-1}")
