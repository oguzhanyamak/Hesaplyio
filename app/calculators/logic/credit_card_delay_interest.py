def calculate_credit_card_delay_interest(delayed_amount: float | str, passed_days: int | str, current_interest_rate: float | str = "4.25") -> dict:
    try:
        delayed_amount = float(delayed_amount)
        passed_days = int(passed_days)
        interest_rate = float(current_interest_rate) / 100.0  
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # TCMB Kredi Kartı Gecikme Faizi Hesaplama Formülü
    # Gecikme Faizi = Geciken Tutar * (Aylık Gecikme Faiz Oranı / 30) * Gecikilen Gün Sayısı
    # Gecikme Faizi üzerinden %15 KKDF ve %15 BSMV kesilir (toplam vergi çarpanı %30)
    
    daily_interest_rate = interest_rate / 30.0
    
    raw_interest = delayed_amount * daily_interest_rate * passed_days
    bsmv = raw_interest * 0.15
    kkdf = raw_interest * 0.15
    
    total_interest_with_taxes = raw_interest + bsmv + kkdf
    total_debt = delayed_amount + total_interest_with_taxes
    
    return {
        "summary": {
            "label": "Gecikme Faizi ve Vergiler",
            "value": round(total_interest_with_taxes, 2)
        },
        "breakdown": [
            {"label": "Geciken Tutar", "value": round(delayed_amount, 2)},
            {"label": "Gecikilen Gün Süresi", "value": passed_days},
            {"label": "Uygulanan Aylık Faiz (%)", "value": round(interest_rate * 100, 2)},
            {"label": "Hesaplanan Net Faiz", "value": round(raw_interest, 2)},
            {"label": "KKDF (%15)", "value": round(kkdf, 2)},
            {"label": "BSMV (%15)", "value": round(bsmv, 2)},
            {"label": "Yaklaşık Toplam Borcunuz", "value": round(total_debt, 2)},
        ]
    }
