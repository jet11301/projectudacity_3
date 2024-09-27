from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, TIMESTAMP

HungTHP1Base = declarative_base()

class Token(HungTHP1Base):
    __tablename__ = 'tokens'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)  
    token = Column(String(6), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    used_at = Column(TIMESTAMP)
    def __repr__(self):  
          return (f"<Token(id={self.id}, "
                f"user_id={self.user_id}, "
                f"token='{self.token}', "
                f"created_at='{self.created_at}', "
                f"used_at='{self.used_at}')>")