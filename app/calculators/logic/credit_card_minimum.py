def calculate_credit_card_minimum(card_limit: float | str, statement_balance: float | str, is_new_card: str = "Hayır") -> dict:
    try:
        card_limit = float(card_limit)
        statement_balance = float(statement_balance)
    except ValueError:
        raise ValueError("Lütfen geçerli sayısal değerler girin.")

    # BDDK Asgari Ödeme Oranları
    # 25.000 TL altı için %20
    # 25.000 TL ve üstü için %40
    # Yeni tahsis edilen kredi kartlarında ilk 1 yıl asgari oran limit farketmeksizin %40'tır.
    
    if is_new_card.lower() == "evet":
        min_payment_rate = 0.40
    else:
        if card_limit < 25000:
            min_payment_rate = 0.20
        else:
            min_payment_rate = 0.40
            
    minimum_payment = statement_balance * min_payment_rate
    
    return {
        "summary": {
            "label": "Asgari Ödeme Tutarı",
            "value": round(minimum_payment, 2)
        },
        "breakdown": [
            {"label": "Dönem Borcu", "value": round(statement_balance, 2)},
            {"label": "Kart Limiti", "value": round(card_limit, 2)},
            {"label": "Uygulanan Asgari Oran", "value": str(int(min_payment_rate * 100)) + " %"},
        ]
    }
