from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, create_engine, Enum

class Device(SQLModel, table=True):
    deviceId: str = Field(primary_key=True)
    location: Optional[str] = None

    satisfactions: List["Satisfaction"] = Relationship(back_populates="device")

class Satisfaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    satisfaction: str
    insertedAt: datetime

    deviceId: str = Field(foreign_key="device.deviceId")
    device: Device = Relationship(back_populates="satisfactions")


db_url = 'mysql+pymysql://frans-mbp:Plesken2@localhost:3306/project3'

engine = create_engine(db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    return engine
