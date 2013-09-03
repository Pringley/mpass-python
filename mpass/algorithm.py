import hmac
import hashlib
import base64

def mpass(master_password, domain):
    mac = hmac.new(master_password, domain, hashlib.sha512)
    return base64.b64encode(mac.digest())[:10]
