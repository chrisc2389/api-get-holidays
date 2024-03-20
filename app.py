from datetime import date
import holidays
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-state-holidays")
def get_state_holidays():
    data = {}
    us_holidays = holidays.UnitedStates(state='TX',years=2023)

    # Print all holidays in the year 2024
    for date, name in sorted(us_holidays.items()):
        data[str(date)] = name


    json_payload = json.dumps(data)
    return json_payload
 