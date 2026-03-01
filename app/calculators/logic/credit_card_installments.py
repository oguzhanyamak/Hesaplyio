def calculate_credit_card_installments(amount: float | str, term: int | str, monthly_interest: float | str = "4.25") -> dict:
    try:
        a = float(amount)
        t = int(term)
        ir = float(monthly_interest) / 100.0
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")
        
    # Kredi Kartı İşlem Taksitlendirme, normal kredilerle aynı BSMV/KKDF çarpanıyla çalışır (ikisi de %15)
    effective_rate = ir * 1.30
    
    if ir <= 0:
        monthly_payment = a / t
        total_payment = a
        total_interest = 0
    else:
        monthly_payment = a * (effective_rate * (1 + effective_rate) ** t) / ((1 + effective_rate) ** t - 1)
        total_payment = monthly_payment * t
        total_interest = total_payment - a

    return {
        "summary": {
            "label": "Karta Yansıyacak Taksit",
            "value": round(monthly_payment, 2)
        },
        "breakdown": [
            {"label": "Taksitlendirilen Tutar", "value": round(a, 2)},
            {"label": "Vade Sayısı", "value": t},
            {"label": "Aylık Banka Faizi", "value": round(ir * 100, 2)},
            {"label": "Toplam Vade Farkı (Vergi Dahil)", "value": round(total_interest, 2)},
            {"label": "Toplam Geri Ödenecek Tutar", "value": round(total_payment, 2)},
        ]
    }
