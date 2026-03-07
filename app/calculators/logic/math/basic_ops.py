import math

def calculate_percentage(val: float | str, pct: float | str, operation: str = "calculate") -> dict:
    try:
        v = float(val)
        p = float(pct)
    except ValueError:
        raise ValueError("Lütfen geçerli sayısal değerler girin.")

    result = 0
    label = ""
    
    if operation == "calculate":
        result = v * (p / 100.0)
        label = f"{v} sayısının %{p} değeri"
    elif operation == "add":
        result = v * (1 + (p / 100.0))
        label = f"{v} sayısına %{p} eklenmiş hali"
    elif operation == "subtract":
        result = v * (1 - (p / 100.0))
        label = f"{v} sayısından %{p} çıkarılmış hali"
    elif operation == "change":
        # What percentage is P of V?
        if v == 0: return {"status": "error", "message": "Payda sıfır olamaz."}
        result = (p / v) * 100
        label = f"{p} sayısı, {v} sayısının yüzde kaçıdır?"
        
    return {
        "summary": {
            "label": "Sonuç",
            "value": round(result, 4)
        },
        "breakdown": [
            {"label": "İşlem", "value": label},
            {"label": "Net Değer", "value": round(result, 4)}
        ]
    }

def calculate_power(base: float | str, exponent: float | str) -> dict:
    try:
        b = float(base)
        e = float(exponent)
        result = b ** e
    except OverflowError:
        return {"status": "error", "message": "Sayı çok büyük."}
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")
    except Exception as e:
        return {"status": "error", "message": f"Hata: {str(e)}"}
        
    return {
        "summary": { "label": "Üslü Sayı Değeri", "value": result },
        "breakdown": [{"label": "Taban", "value": b}, {"label": "Üs", "value": e}]
    }

def calculate_root(val: float | str, degree: float | str = 2) -> dict:
    try:
        v = float(val)
        d = float(degree)
        if v < 0 and d % 2 == 0:
            return {"status": "error", "message": "Negatif sayıların çift dereceli kökü reel sayı değildir."}
        result = v ** (1.0/d) if v >= 0 else -((-v)**(1.0/d))
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")
        
    return {
        "summary": { "label": "Kök Değeri", "value": round(result, 6) },
        "breakdown": [{"label": "Sayı", "value": v}, {"label": "Derece", "value": d}]
    }

def calculate_factorial(n: int | str) -> dict:
    try:
        num = int(n)
        if num < 0: return {"status": "error", "message": "Faktöriyel negatif sayılar için tanımsızdır."}
        if num > 1000: return {"status": "error", "message": "Sayı çok büyük (Maksimum 1000)."}
        result = math.factorial(num)
    except ValueError:
        raise ValueError("Lütfen tam sayı girin.")
        
    return {
        "summary": { "label": f"{num}! Sonucu", "value": str(result) if num > 20 else result },
        "breakdown": [{"label": "Sayı", "value": num}]
    }
def calculate_vat(value: float, rate: float, mode: str = "add") -> dict:
    """KDV Hesaplama: Dahil (add) veya Hariç (subtract)."""
    try:
        v = float(value)
        r = float(rate)
    except ValueError:
        raise ValueError("Geçerli sayısal değerler girin.")
    
    if mode == "add":
        # Hariçten Dahile
        vat_amount = v * (r / 100.0)
        total_amount = v + vat_amount
    else:
        # Dahilden Harice
        total_amount = v / (1 + (r / 100.0))
        vat_amount = v - total_amount
        
    return {
        "summary": { "label": "Toplam Tutar", "value": round(total_amount, 2) },
        "breakdown": [
            {"label": "Matrah (KDV Hariç)", "value": round(v if mode=="add" else total_amount, 2)},
            {"label": "KDV Tutarı", "value": round(vat_amount, 2)},
            {"label": "Toplam (KDV Dahil)", "value": round(total_amount if mode=="add" else v, 2)}
        ]
    }

def calculate_discount(price: float, rate: float) -> dict:
    """İndirim Hesaplama."""
    try:
        p = float(price)
        r = float(rate)
    except ValueError:
        raise ValueError("Geçerli sayısal değerler girin.")
        
    discount_amount = p * (r / 100.0)
    final_price = p - discount_amount
    
    return {
        "summary": { "label": "İndirimli Fiyat", "value": round(final_price, 2) },
        "breakdown": [
            {"label": "Eski Fiyat", "value": round(p, 2)},
            {"label": "İndirim Oranı", "value": f"%{r}"},
            {"label": "İndirim Tutarı", "value": round(discount_amount, 2)},
            {"label": "Ödenecek Tutar", "value": round(final_price, 2)}
        ]
    }
