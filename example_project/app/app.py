import argparse
import os

from database import engine, Session
from models import Base, Client

APP_NAME = os.getenv('ENV_APP_NAME')

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name')
parser.add_argument('-p', '--pwd')
parser.add_argument('-e', '--email')

args = parser.parse_args()

Base.metadata.create_all(engine)

# Check and create guest client if appropriate

session = Session()

r = session.query(Client).filter_by(name='guest').first()

if not r:
    guest = Client(
        name='guest',
        email='guest@bogus.com',
        password='guestpwd'
    )

    session.add(guest)

if args.name and args.email and args.pwd:
    user = Client(
        name=args.name,
        email=args.email,
        password=args.pwd
    )

    session.add(user)

session.commit()

print("APP_NAME=", APP_NAME or 'Nombre no configurado')
