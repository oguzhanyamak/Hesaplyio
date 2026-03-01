def calculate_gcd_lcm(a: int | str, b: int | str) -> dict:
    try:
        val1 = abs(int(a))
        val2 = abs(int(b))
    except ValueError:
        raise ValueError("Lütfen tamsayı girin.")
        
    import math
    gcd = math.gcd(val1, val2)
    lcm = 0 if (val1 * val2 == 0) else abs(val1 * val2) // gcd
    
    return {
        "summary": { "label": "EBOB / EKOK Sonucu", "value": f"EBOB: {gcd}, EKOK: {lcm}" },
        "breakdown": [
            {"label": "Sayı 1", "value": val1},
            {"label": "Sayı 2", "value": val2},
            {"label": "EBOB (En Büyük Ortak Bölen)", "value": gcd},
            {"label": "EKOK (En Küçük Ortak Kat)", "value": lcm}
        ]
    }

def calculate_prime_factors(n: int | str) -> dict:
    try:
        num = int(n)
        if num <= 1: return {"status": "error", "message": "Lütfen 1'den büyük bir sayı girin."}
        temp = num
        factors = {}
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1
            
        factors_str = " \u00d7 ".join([f"{k}^{v}" if v > 1 else str(k) for k, v in factors.items()])
        unique_factors = list(factors.keys())
    except ValueError:
        raise ValueError("Lütfen geçerli bir sayı girin.")
        
    return {
        "summary": { "label": "Asal Çarpan Analizi", "value": factors_str },
        "breakdown": [
            {"label": "Girilmiş Sayı", "value": num},
            {"label": "Benzersiz Asal Çarpanlar", "value": str(unique_factors)},
            {"label": "Üslü Gösterim", "value": factors_str}
        ]
    }
