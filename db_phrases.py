from database import db_session
from models import Phrase
from random import choice


def add_phrase(check):
    new_phrase = Phrase(phrase=check)
    db_session.add(new_phrase)
    db_session.commit()
    db_session.close()


def get_random_phrase():
    all_phrases = Phrase.query.all()
    random_phrase = choice(all_phrases)
    
    return random_phrase.phrase
