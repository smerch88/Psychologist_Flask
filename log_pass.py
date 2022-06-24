import os


os.chdir('/Users/SS/Desktop/mail-data')
print(os.getcwd())
print(os.listdir())

try:
    filename = 'data.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()

except os.error:

    print('Problem reading: ' + filename)


def log_pass(text_info):
    a=(text_info.find("Mail:",0,len(text)))
    b=text_info.find("Pass:",0,len(text))
    login = text_info[a+5:b-1:]
    password = text_info[b+5::]
    return {"login": login, "password": password}


acces_data=log_pass(text)
print(acces_data)