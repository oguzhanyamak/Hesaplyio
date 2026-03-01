def calculate_mortgage_loan(principal: float | str, interest_rate: float | str, term_months: int | str) -> dict:
    try:
        principal = float(principal)
        interest_rate = float(interest_rate) / 100.0  
        term_months = int(term_months)
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    if interest_rate <= 0:
        monthly_payment = principal / term_months
        total_payment = principal
        total_interest = 0
    else:
        # Konut kredisinde KKDF ve BSMV vergileri %0'dır.
        monthly_payment = principal * (interest_rate * (1 + interest_rate) ** term_months) / ((1 + interest_rate) ** term_months - 1)
        total_payment = monthly_payment * term_months
        total_interest = total_payment - principal

    payment_plan = []
    remaining_balance = principal
    
    for month in range(1, term_months + 1):
        if interest_rate > 0:
            month_interest = remaining_balance * interest_rate
        else:
            month_interest = 0
            
        month_principal = monthly_payment - month_interest
        remaining_balance -= month_principal
        
        if remaining_balance < 0.01:
            remaining_balance = 0
            
        payment_plan.append({
            "month": month,
            "installment": round(monthly_payment, 2),
            "principal": round(month_principal, 2),
            "interest": round(month_interest, 2),
            "remaining_balance": round(remaining_balance, 2)
        })

    return {
        "summary": {
            "label": "Aylık Taksit (*Vergisiz)",
            "value": round(monthly_payment, 2)
        },
        "breakdown": [
            {"label": "Kredi Tutarı", "value": round(principal, 2)},
            {"label": "Faiz Oranı (Aylık)", "value": round(interest_rate * 100, 2)},
            {"label": "Vade (Ay)", "value": term_months},
            {"label": "Toplam Geri Ödeme", "value": round(total_payment, 2)},
            {"label": "Toplam Faiz Masrafı", "value": round(total_interest, 2)},
        ],
        "payment_plan": payment_plan
    }
