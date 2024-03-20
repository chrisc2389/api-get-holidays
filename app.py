from datetime import date
import holidays
import json
from fastapi import FastAPI
from pydantic import BaseModel



class Body(BaseModel):
    state: str
    year: str

app = FastAPI()

@app.post("/get-state-holidays")
async def get_state_holidays(body: Body):
    data = {}
    print("STATE -"+body.state)
    print("YEAR -"+body.year)
    us_holidays = holidays.UnitedStates(state=body.state,years=body.year)

    # Print all holidays in the year 2024
    for date, name in sorted(us_holidays.items()):
        data[str(date)] = name


    json_payload = json.dumps(data)
    return json_payload
 