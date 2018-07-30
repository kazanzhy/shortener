from random import choice
from .models import *

def generate_code(length = 5):
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join([choice(chars) for _ in range(length)])
    return(code)


def get_code(session, link):
    query_link = session.query(Link).filter_by(link=link).first()
    if query_link is None:
        code = generate_code()
        query_code = session.query(Link).filter_by(code=code).first()
        while query_code != None:
            code = generate_code()
            query_code = session.query(Link).filter_by(code=code).first()
        new_link = Link(code, link)
        session.add(new_link)
        session.commit()
    else:
        code = query_link.code
    return code

