import pyotp
SECRET = "UOPKN6QFW3J6PW74"

def verify(code):
    return pyotp.TOTP(SECRET).verify(code)