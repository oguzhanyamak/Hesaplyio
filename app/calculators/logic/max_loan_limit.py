def calculate_max_loan_limit(monthly_income: float | str, term_months: int | str, interest_rate: float | str) -> dict:
    try:
        monthly_income = float(monthly_income)
        term_months = int(term_months)
        interest_rate = float(interest_rate) / 100.0  
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # BDDK'ya göre genel kural: Aylık taksitler, kişinin aylık belgelenebilir gelirinin %50'sini geçemez.
    max_monthly_installment = monthly_income * 0.50
    
    if interest_rate <= 0:
        max_principal = max_monthly_installment * term_months
    else:
        # İhtiyaç Kredisi üzerinden vergilendirme yapılıyor (KKDF %15, BSMV %15)
        effective_interest_rate = interest_rate * 1.30
        
        # M = P * [ r(1 + r)^n ] / [ (1 + r)^n - 1 ]
        # Formülü P (anapara) için tersine çeviriyoruz:
        # P = M * [ (1 + r)^n - 1 ] / [ r(1 + r)^n ]
        
        factor = (effective_interest_rate * (1 + effective_interest_rate) ** term_months) / ((1 + effective_interest_rate) ** term_months - 1)
        max_principal = max_monthly_installment / factor

    return {
        "summary": {
            "label": "Maksimum Kredi Limiti",
            "value": round(max_principal, 2)
        },
        "breakdown": [
            {"label": "Aylık Gelir", "value": round(monthly_income, 2)},
            {"label": "Maksimum Aylık Taksit (Gelirin %50'si)", "value": round(max_monthly_installment, 2)},
            {"label": "Aylık Faiz Oranı", "value": round(interest_rate * 100, 2)},
            {"label": "Kredi Vadesi", "value": term_months},
        ]
    }
