from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Подключение шаблонов и статики
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def calculate_pdn(monthly_income: float, monthly_payments: list[float]) -> float:
    """
    Расчет ПДН (показателя долговой нагрузки)
    """
    if monthly_income <= 0:
        raise ValueError("Доход должен быть больше 0")

    total_payments = sum(monthly_payments)
    pdn = (total_payments / monthly_income) * 100
    return round(pdn, 2)


@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
async def calculate_pdn_form(
    request: Request,
    income: float = Form(...),
    payments: str = Form(...)
):
    try:
        payments_list = [float(p.strip()) for p in payments.split(",") if p.strip()]
        pdn_value = calculate_pdn(income, payments_list)

        # Интерпретация результата
        if pdn_value < 50:
            print("У вас низкий уровень долговой нагрузки.")
        elif pdn_value > 50 and pdn_value < 80:
            print("Ваш уровень долговой нагрузки - средний.")
        else:
            print("У вас высокая долговая нагрузка. ")

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": f"ПДН = {pdn_value}%", "status": status}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": "Ошибка: проверьте введённые данные.", "status": str(e)}
        )
