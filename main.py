from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from requests import request
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
import openAI
import sqlmodel


from datetime import datetime
import json



from models.device import Device, Satisfaction, create_db_and_tables

app = FastAPI()


@app.on_event("startup") #this happens only once
def on_startup():
    global engine
    engine = create_db_and_tables()
    now = datetime.now()


templates = Jinja2Templates(directory="templates")


def getDevices():
    with Session(engine) as session:
        devices = session.exec(select(Device)).all()
        return devices

def getDeviceById(deviceId):
    with Session(engine) as session:
        device = session.exec(select(Device).where(
            Device.deviceId == deviceId)).first()
        return device

# Website Section

@app.get("/")
def read_root(request: Request):
    devices = getDevices()
    # get index.html / pass devices to it and run the dynamic python code inside the html / and return the html to the client
    return templates.TemplateResponse("index.html", {"request": request, "devices": devices}) #ninja needs access to the request

@app.get("/devices/{deviceId}")
def read_root(request: Request, deviceId):
    devices = getDevices()
    satisfactions = [s.toJSON() for s in getSatisfactions(deviceId) ]
    return templates.TemplateResponse("device.html", {"request": request, "devices": devices, "satisfactions": satisfactions})


# API section


@app.get("/devices")
def listDevices():
    return getDevices()


@app.get("/devices/{deviceId}/location")
def getLocation(deviceId: str):
    with Session(engine) as session:
        device = session.exec(select(Device).where(
            Device.deviceId == deviceId)).first()
        return device.location


@app.get("/devices/{deviceId}/satisfactions")
def getSatisfactions(deviceId: str):
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


@app.post("/satisfactions") #for the python sending json
def createSatisfaction(satisfaction: Satisfaction):
    with Session(engine) as session:
        session.add(satisfaction)
        session.commit()
        return satisfaction

@app.post("/devices/{deviceId}", response_class=RedirectResponse, status_code=302) #redirect to "/" page
def updateDevice(deviceId: str, location: str = Form()):
    print(location, deviceId)
    with Session(engine) as session:
        device = session.exec(select(Device).where(
            Device.deviceId == deviceId)).first()
        device.location = location
        session.commit()
        return "/"

#website graphical interface for collecting surveys (survey.html)
@app.get("/devices/{deviceId}/survey")
def read_root(request: Request, deviceId):
    device = getDeviceById(deviceId)
    satisfactions = getSatisfactions(deviceId)
    return templates.TemplateResponse("survey.html", {"request": request, "device": device, "satisfactions": satisfactions})


@app.post("/satisfactions/{deviceId}", response_class=RedirectResponse, status_code=302)
def createSatisfaction(deviceId: str, satisfaction: str = Form(), time: str = Form(), comment = Form(default="")):
    
    category = openAI.get_category(satisfaction.comment) # here

    satisfactionRecord = Satisfaction(deviceId=deviceId, satisfaction= satisfaction, insertedAt=time, comment=comment, category=category)
    with Session(engine) as session:
        session.add(satisfactionRecord)
        session.commit()

    url = "/devices/{}/survey".format(deviceId)
    return url
    #satisfaction.category = openAI_getcategory(satisfaction.comment)
    # with Session(engine) as session:
    #     session.add(satisfaction)
    #     session.commit()
    #     return satisfaction