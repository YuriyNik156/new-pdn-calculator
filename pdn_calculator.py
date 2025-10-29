def calculate_pdn(monthly_income: float, monthly_payments: list[float]) -> float:
    """
    Расчет ПДН (показателя долговой нагрузки)
    :param monthly_income: среднемесячный доход заемщика
    :param monthly_payments: список ежемесячных платежей по всем кредитам
    :return: значение ПДН в процентах
    """

    # Проверка, чтобы доход был больше 0
    if monthly_income <= 0:
        raise ValueError("Доход должен быть больше нуля")

    # Расчет ПДН
    total_payments = sum(monthly_payments)
    pdn = (total_payments / monthly_income) * 100
    return round(pdn, 2)

# Пользователь вводит данные по доходам и расходам
income = float(input("Введите среднемесячный доход (₽): "))
payments_input = input("Введите платежи по кредитам через запятую (₽): ")

# Преобразование строки в числа
payments = [float(p.strip()) for p in payments_input.split(",") if p.strip()]

pdn_value = calculate_pdn(income, payments)
print(f"ПДН = {pdn_value}")

# Зоны риска <50%, 50-80%, >80%
if pdn_value < 50:
    print("У вас низкий уровень долговой нагрузки.")
elif pdn_value > 50 and pdn_value < 80:
    print("Ваш уровень долговой нагрузки - средний.")
else:
    print("У вас высокая долговая нагрузка. ")

