def calculate_workplace_loan(principal: float | str, interest_rate: float | str, term_months: int | str) -> dict:
    try:
        p = float(principal)
        ir = float(interest_rate) / 100.0  
        t = int(term_months)
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # İş yeri (commercial property) mortgage'da BSMV ödenir (%5), ancak KKDF muafiyeti vardır (%0)
    bsmv = 0.05
    kkdf = 0.00
            
    effective_rate = ir * (1 + bsmv + kkdf)
    
    if ir <= 0:
        monthly_payment = p / t
        total_payment = p
        total_interest = 0
    else:
        monthly_payment = p * (effective_rate * (1 + effective_rate) ** t) / ((1 + effective_rate) ** t - 1)
        total_payment = monthly_payment * t
        total_interest = total_payment - p

    return {
        "summary": {
            "label": "Aylık Taksit (İş Yeri)",
            "value": round(monthly_payment, 2)
        },
        "breakdown": [
            {"label": "İş Yeri Kredisi", "value": round(p, 2)},
            {"label": "Kredi Vadesi", "value": t},
            {"label": "Banka Faiz Oranı", "value": round(ir * 100, 2)},
            {"label": "İş Yeri Vergilendirme (BSMV %5 - KKDF %0)", "value": "Aktif"},
            {"label": "Toplam Geri Ödenecek", "value": round(total_payment, 2)},
        ]
    }
