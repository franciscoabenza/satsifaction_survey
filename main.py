from fastapi import FastAPI, HTTPException, Request
from requests import request
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
import sqlmodel
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



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
def read_root(request: Request, deviceId):
    devices = getDevices()
    satisfaction = getSatisfactions(deviceId)

    
    ig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=df['ts'], y=df['temperature'], name='Temperature', line=dict(color='Crimson')), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['ts'], y=df['humidity'], name='Humidity', line=dict(color='CornflowerBlue')), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['ts'], y=df['lightIntensity'], name='Light Intensity', line=dict(color='Burlywood')), secondary_y=True)

    fig.update_layout(title_text="The Holy Trifecta of Data") #Can add a ton of parameters here; height, width etc


    print(satisfaction, "🤪")
    return templates.TemplateResponse("device.html", {"request": request, "devices": devices, "satisfactions": satisfaction})

"""@app.get("/devices/{deviceId}/satisfactions")
def read_root(request: Request):
    satisfactions = getSatisfactions(devices.deviceId)
    return templates.TemplateResponse("satisfactions.html", {"request": request, "satisfactions": satisfactions})"""

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
    