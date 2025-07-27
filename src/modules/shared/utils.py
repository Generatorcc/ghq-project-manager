# src/modules/shared/utils.py

from datetime import datetime

def utc_now():
    return datetime.utcnow()

def mask_email(email):
    """example@email.com" -> "e*****e@email.com"""
    if not email or "@" not in email:
        return email
    name, domain = email.split("@")
    return name[0] + "*"*(len(name)-2) + name[-1] + "@" + domain
