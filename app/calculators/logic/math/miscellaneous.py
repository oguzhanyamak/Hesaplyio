def calculate_interest_math(principal: float | str, rate: float | str, time: float | str, mode: str = "simple") -> dict:
    try:
        p = float(principal)
        r = float(rate) / 100.0
        t = float(time)
    except ValueError:
        raise ValueError("Sayısal değerler girin.")
        
    if mode == "simple":
        interest = p * r * t
        total = p + interest
    else: # Compound
        total = p * (1 + r) ** t
        interest = total - p
        
    return {
        "summary": { "label": "Toplam Faiz Getirisi", "value": round(interest, 2) },
        "breakdown": [
            {"label": "Anapara", "value": round(p, 2)},
            {"label": "Toplam Tutar (Anapara + Faiz)", "value": round(total, 2)}
        ]
    }

def calculate_conversions(val: float | str, unit_from: str, unit_to: str) -> dict:
    try:
        v = float(val)
    except ValueError:
        raise ValueError("Sayı girin.")
        
    # Conversions
    # 1 inch = 2.54 cm
    # 1 mile = 1.60934 km
    # 1 sq meter = 10.7639 sq ft
    result = 0
    label = ""
    
    if unit_from == "inch" and unit_to == "cm":
        result = v * 2.54
        label = f"{v} inç = {round(result, 4)} santimetre"
    elif unit_from == "cm" and unit_to == "inch":
        result = v / 2.54
        label = f"{v} santimetre = {round(result, 4)} inç"
    elif unit_from == "mile" and unit_to == "km":
        result = v * 1.60934
        label = f"{v} mil = {round(result, 4)} kilometre"
    elif unit_from == "km" and unit_to == "mile":
        result = v / 1.60934
        label = f"{v} kilometre = {round(result, 4)} mil"
    elif unit_from == "sqm" and unit_to == "sqft":
        result = v * 10.7639
        label = f"{v} metrekare = {round(result, 4)} metrekare (sqft)"
        
    return {
        "summary": { "label": "Dönüşüm Sonucu", "value": round(result, 4) },
        "breakdown": [{"label": "Birimsiz Sonuç", "value": result}]
    }

def calculate_golden_ratio(val: float | str, find: str = "larger") -> dict:
    try:
        v = float(val)
        phi = 1.61803398875
        if find == "larger":
            res = v * phi
        else: # find smaller
            res = v / phi
    except ValueError:
        raise ValueError("Sayı girin.")
        
    return {
        "summary": { "label": "Altın Oran Değeri", "value": round(res, 6) },
        "breakdown": [{"label": "Girdi", "value": v}]
    }

def calculate_modulo(a: int | str, b: int | str) -> dict:
    try:
        val_a = int(a)
        val_b = int(b)
        result = val_a % val_b
    except Exception:
        raise ValueError("Tamsayı girin.")
    return {
        "summary": { "label": "Kalan Değeri", "value": result },
        "breakdown": [{"label": "İşlem", "value": f"{val_a} mod {val_b}"}]
    }
