from sqlalchemy import Column, Integer, String

from database import Base


class Phrase(Base):
    __tablename__ = 'phrases'

    id = Column(Integer, primary_key=True)
    phrase = Column(String, nullable=False)

    def __repr__(self):
        return f'id: {self.id}, phrase: {self.phrase}'