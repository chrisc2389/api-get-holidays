from datetime import date
import holidays
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    state: str
    year: str

@app.get("/get-state-holidays")
async def get_state_holidays(body: Body):
    data = {}
    #us_holidays = holidays.UnitedStates(state='TX',years=2023)
    us_holidays = holidays.UnitedStates(state=body.state,years=body.year)

    # Print all holidays in the year 2024
    for date, name in sorted(us_holidays.items()):
        data[str(date)] = name


    json_payload = json.dumps(data)
    return json_payload
 