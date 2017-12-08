import time
from datetime import datetime as dt

hosts_tmp=r'C:\Users\Usuario\Desktop\Udemy\app3_blocker\hosts'
hosts_path=r'C:\Windows\System32\drivers\etc\hosts' # r row string or double \\
redirect='127.0.0.1'
website_list=['www.facebook.com','facebook.com','inbox.google.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours...')
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n') # pay attention to line breaks
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun hours...')

    time.sleep(5)
