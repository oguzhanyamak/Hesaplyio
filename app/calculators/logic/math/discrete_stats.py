import math

def calculate_stats(numbers_str: str) -> dict:
    try:
        # Expected comma-separated or space-separated numbers
        nums = [float(x.strip()) for x in numbers_str.replace(",", " ").split() if x.strip()]
        if not nums: return {"status": "error", "message": "Lütfen sayı listesi girin."}
        
        n = len(nums)
        mean = sum(nums) / n
        variance = sum((x - mean) ** 2 for x in nums) / (n - 1) if n > 1 else 0
        std_dev = math.sqrt(variance)
        
        return {
            "summary": { "label": "Standart Sapma", "value": round(std_dev, 4) },
            "breakdown": [
                {"label": "Sayı Adedi", "value": n},
                {"label": "Ortalama (Aritmetik)", "value": round(mean, 4)},
                {"label": "Varyans", "value": round(variance, 4)}
            ]
        }
    except Exception:
        raise ValueError("Lütfen geçerli bir sayı listesi girin (Örn: 10, 20, 30).")

def calculate_perm_comb(n: int | str, r: int | str, mode: str = "combination") -> dict:
    try:
        val_n = int(n)
        val_r = int(r)
        if val_r > val_n or val_n < 0 or val_r < 0:
            return {"status": "error", "message": "Hesaplama için n >= r ve n, r >= 0 olmalıdır."}
            
        import math
        if mode == "combination":
            result = math.comb(val_n, val_r)
            label = f"C({val_n}, {val_r}) Kombinasyon"
        else:
            result = math.perm(val_n, val_r)
            label = f"P({val_n}, {val_r}) Permütasyon"
            
    except ValueError:
        raise ValueError("Lütfen tamsayı girin.")
        
    return {
        "summary": { "label": label, "value": result },
        "breakdown": [{"label": "Sonuç", "value": result}]
    }

def calculate_base_conversion(num_str: str, from_base: int | str, to_base: int | str) -> dict:
    try:
        # Convert any from_base string to int
        fb = int(from_base)
        tb = int(to_base)
        
        # Original to base 10
        val_base10 = int(num_str, fb)
        
        # Base 10 to target base
        def decimal_to_base(n, base):
            if n == 0: return "0"
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while n > 0:
                res = digits[n % base] + res
                n //= base
            return res
            
        result = decimal_to_base(val_base10, tb)
        
    except Exception:
        raise ValueError("Taban dönüşümü sırasında hata oluştu. Lütfen değerleri kontrol edin.")
        
    return {
        "summary": { "label": f"{tb} Tabanındaki Değer", "value": result },
        "breakdown": [{"label": "10 Tabanındaki Değer", "value": val_base10}]
    }
