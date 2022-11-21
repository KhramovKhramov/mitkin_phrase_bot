from database import create_db, db_session
from models import Phrase

def create_database():
    create_db(db_session)

if __name__ == '__main__':
    create_database()