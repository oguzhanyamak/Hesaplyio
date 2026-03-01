def calculate_loan_restructure(old_principal: float | str, old_interest: float | str, new_interest: float | str, remaining_months: int | str, old_installments: int | str) -> dict:
    try:
        op = float(old_principal)
        oi = float(old_interest) / 100.0  
        ni = float(new_interest) / 100.0
        rm = int(remaining_months)
        ti = int(old_installments)
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # 1. Eski Durum:
    effective_oi = oi * 1.30 # Standart Tüketici %15 %15 vergiler
    old_monthly_payment = op * (effective_oi * (1 + effective_oi) ** ti) / ((1 + effective_oi) ** ti - 1)
    # Kalan anapara approx:
    remaining_principal = op * (rm / ti)
    
    # Kapanacak Tutar (Erken kapama simülasyonu - vergi vs muafiyeti)
    closing_amount = remaining_principal
    
    # 2. Yeni Durum (Kalan anaparayı yeni oranla baştan kredilendirme)
    effective_ni = ni * 1.30
    new_monthly_payment = closing_amount * (effective_ni * (1 + effective_ni) ** rm) / ((1 + effective_ni) ** rm - 1)
    
    old_total_future = old_monthly_payment * rm
    new_total_future = new_monthly_payment * rm
    
    savings = old_total_future - new_total_future

    payment_plan = [] # You could generate this if you wanted
    
    return {
        "summary": {
            "label": "Tasarruf Edilecek Tutar*",
            "value": round(savings, 2)
        },
        "breakdown": [
            {"label": "Kapatılacak Anapara Tutarı", "value": round(closing_amount, 2)},
            {"label": "Eski Kredinizin Aylık Taksiti", "value": round(old_monthly_payment, 2)},
            {"label": "Yapılandırma Sonrası Yeni Aylık Taksit", "value": round(new_monthly_payment, 2)},
            {"label": "Dokunulmazsa Ödenecek Kalan Toplam Tutar", "value": round(old_total_future, 2)},
            {"label": "Yapılandırma Seçilirse Ödenecek Toplam Tutar", "value": round(new_total_future, 2)},
            {"label": "Toplam Kârınız", "value": round(savings, 2)},
        ]
    }
