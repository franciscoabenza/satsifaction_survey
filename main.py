from fastapi import FastAPI, HTTPException, Request
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates

from models.device import Device, Satisfaction, create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    global engine
    engine = create_db_and_tables()


templates = Jinja2Templates(directory="templates")


def getDevices():
    with Session(engine) as session:
        devices = session.exec(select(Device)).all()
        return devices

# Website Section

@app.get("/")
def read_root(request: Request):
    devices = getDevices()
    # get index.html / pass devices to it and run the dynamic python code inside the html / and return the html to the client
    return templates.TemplateResponse("index.html", {"request": request, "devices": devices})


@app.get("/devices/{deviceId}")
def read_root(request: Request):
    devices = getDevices()
    return templates.TemplateResponse("device.html", {"request": request, "devices": devices})

# API section

@app.get("/devices")
def listDevices():
    return getDevices()


@app.get("/devices/{deviceId}/satisfactions")
def getSatisfactions(deviceId: str):
    print(deviceId)
    with Session(engine) as session:
        device = session.exec(select(Device).where(
            Device.deviceId == deviceId)).first()
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")
        satisfactions = session.exec(select(Satisfaction).where(
            Satisfaction.deviceId == deviceId)).all()
        return satisfactions


@app.post("/devices")
def createDevice(device: Device):
    with Session(engine) as session:
        session.add(device)
        session.commit()
        return device


@app.post("/satisfactions")
def createSatisfaction(satisfaction: Satisfaction):
    with Session(engine) as session:
        session.add(satisfaction)
        session.commit()
        return satisfaction
    