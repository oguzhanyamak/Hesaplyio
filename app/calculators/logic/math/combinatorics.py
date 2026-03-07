import math

def calculate_comb_perm(n: int, r: int, mode: str = "combination") -> dict:
    """Kombinasyon ve Permütasyon Hesaplama."""
    try:
        num_n = int(n)
        num_r = int(r)
        if num_n < 0 or num_r < 0:
            return {"status": "error", "message": "Sayılar negatif olamaz."}
        if num_r > num_n:
            return {"status": "error", "message": "r sayısı n sayısından büyük olamaz."}
    except ValueError:
        raise ValueError("Lütfen tam sayı girin.")
        
    if mode == "combination":
        # C(n, r) = n! / (r! * (n-r)!)
        result = math.comb(num_n, num_r)
        label = f"C({num_n}, {num_r}) Kombinasyon"
    else:
        # P(n, r) = n! / (n-r)!
        result = math.perm(num_n, num_r)
        label = f"P({num_n}, {num_r}) Permütasyon"
        
    return {
        "summary": { "label": "Sonuç", "value": result },
        "breakdown": [
            {"label": "İşlem Türü", "value": label},
            {"label": "n değeri", "value": num_n},
            {"label": "r değeri", "value": num_r},
            {"label": "Hesaplanan Değer", "value": result}
        ]
    }
