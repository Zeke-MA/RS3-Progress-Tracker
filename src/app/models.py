from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime

class RunescapeAccount(Base):
    __tablename__ = 'account'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    rsn = Column(String, nullable=False, unique=True)
    account_type = Column(String, nullable=False, unique=True)
    tracking = Column(Boolean, nullable=False)
    started_tracking = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime, default=datetime.now)