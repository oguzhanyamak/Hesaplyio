def calculate_loan_early_payoff(principal: float | str, remaining_months: int | str, current_interest_rate: float | str, total_installments: int | str) -> dict:
    try:
        principal = float(principal)
        remaining_months = int(remaining_months)
        total_installments = int(total_installments)
        interest_rate = float(current_interest_rate) / 100.0  
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # Approximate early payment penalty logic
    # Bankalar Erken Kapatma Durumunda faizi ve vergiyi siler, sadece anaparayı alır
    # Ancak Konut kredilerinde BDDK gereği %2 erken kapatma cezası (%1 kalan vadeye göre) uygulanabilir.
    
    # Basitleştirilmiş erken ödeme iskontosu hesabı (Mock representation of actual bank algorithms)
    # Varsayılan %10 faiz iadesi veya anapara üzerinden bakiye kapama.
    
    monthly_payment = principal * (interest_rate * (1 + interest_rate) ** total_installments) / ((1 + interest_rate) ** total_installments - 1)
    
    total_debt_if_not_paid = monthly_payment * remaining_months
    
    # Simple linear approximation for remaining principal just as an example
    paid_months = total_installments - remaining_months
    remaining_principal = principal * (remaining_months / total_installments) # VERY basic mock
    
    early_closing_fee = 0
    if "konut" in "type": # We can add type later if needed
        pass
    
    savings = total_debt_if_not_paid - remaining_principal
    
    return {
        "summary": {
            "label": "Erken Kapama Kazancınız",
            "value": round(savings, 2)
        },
        "breakdown": [
            {"label": "Kalan Vade (Ay)", "value": remaining_months},
            {"label": "Vade Sonuna Kadar Beklenirse Ödenecek Toplam Tutar", "value": round(total_debt_if_not_paid, 2)},
            {"label": "Şu An Komple Kapatırsanız Ödenecek Kalan Anapara Tutarı", "value": round(remaining_principal, 2)},
            {"label": "Kârınız (Faiz ve Vergiden Silinen)", "value": round(savings, 2)},
        ]
    }
