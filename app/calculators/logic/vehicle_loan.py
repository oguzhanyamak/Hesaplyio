def calculate_vehicle_loan(principal: float | str, interest_rate: float | str, term_months: int | str, is_commercial: str = "Bireysel") -> dict:
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
        # Taşıt Kredisi: BSMV = 15%, KKDF = 15% (Bireysel)
        # Ticari Taşıt Kredisi: BSMV = 5%, KKDF = 0%     
        if is_commercial == "Ticari":
            bsmv = 0.05
            kkdf = 0.00
        else:
            bsmv = 0.15
            kkdf = 0.15
            
        effective_interest_rate = interest_rate * (1 + bsmv + kkdf)
    
        monthly_payment = principal * (effective_interest_rate * (1 + effective_interest_rate) ** term_months) / ((1 + effective_interest_rate) ** term_months - 1)
        total_payment = monthly_payment * term_months
        total_interest = total_payment - principal

    payment_plan = []
    remaining_balance = principal
    
    for month in range(1, term_months + 1):
        if interest_rate > 0:
            month_interest = remaining_balance * effective_interest_rate
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
            "label": "Aylık Taksit",
            "value": round(monthly_payment, 2)
        },
        "breakdown": [
            {"label": "Kredi Türü", "value": is_commercial},
            {"label": "Kredi Tutarı", "value": round(principal, 2)},
            {"label": "Faiz Oranı (Aylık)", "value": round(interest_rate * 100, 2)},
            {"label": "Vade (Ay)", "value": term_months},
            {"label": "Toplam Geri Ödeme", "value": round(total_payment, 2)},
            {"label": "Toplam Faiz ve Vergiler", "value": round(total_interest, 2)},
        ],
        "payment_plan": payment_plan
    }
