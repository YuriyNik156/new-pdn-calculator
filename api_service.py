from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PDNRequest(BaseModel):
    monthly_income: float
    monthly_payments: list[float]

@app.post("/calculate_pdn")
def calculate_pdn_endpoint(request: PDNRequest):
    if request.monthly_income <= 0:
        return {"error": "Доход должен быть больше 0"}

    total = sum(request.monthly_payments)
    pdn = (total / request.monthly_income) * 100
    return {"pdn": round(pdn, 2)}
