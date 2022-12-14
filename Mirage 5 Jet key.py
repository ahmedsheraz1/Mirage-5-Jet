Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Mirage 5 Jet')
m.hexdigest()
'e1e60d0fcf9fdf1bd56254452286a05fa37afae3c2badefbedfb9cdc85c6a0e9'
