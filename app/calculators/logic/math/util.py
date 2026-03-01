import random

def calculate_random(min_val: int | str, max_val: int | str, count: int | str = 1) -> dict:
    try:
        mi = int(min_val)
        ma = int(max_val)
        c = int(count)
        if c <= 0 or mi > ma: return {"status": "error", "message": "Geçersiz aralık veya adet."}
        
        results = [random.randint(mi, ma) for _ in range(c)]
    except ValueError:
        raise ValueError("Tamsayı girin.")
        
    return {
        "summary": { "label": "Rastgele Sayı(lar)", "value": ", ".join(map(str, results)) },
        "breakdown": [{"label": "Seçilen Adet", "value": c}]
    }

def calculate_number_to_words(n: int | str) -> dict:
    try:
        num = int(n)
        if num < 0 or num > 999999999999: return {"status": "error", "message": "Lütfen 0 ile 1 trilyon arası bir sayı girin."}
        
        units = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
        tens = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
        thousands = ["", "Bin", "Milyon", "Milyar"]
        
        def convert_triplet(t):
            res = ""
            h = t // 100
            t %= 100
            if h > 0:
                res += (units[h] if h > 1 else "") + "Yüz"
            te = t // 10
            u = t % 10
            if te > 0:
                res += tens[te]
            if u > 0:
                res += units[u]
            return res
            
        if num == 0: return {"summary": {"label": "Okunuşu", "value": "Sıfır"}}
        
        final_res = ""
        triplet_idx = 0
        while num > 0:
            triplet = num % 1000
            if triplet > 0:
                triplet_word = convert_triplet(triplet)
                # Specific case for "Bir Bin" which is just "Bin"
                if triplet_idx == 1 and triplet == 1:
                    triplet_word = ""
                final_res = triplet_word + thousands[triplet_idx] + final_res
            num //= 1000
            triplet_idx += 1
            
        return {
            "summary": { "label": "Sayı Okunuşu", "value": final_res },
            "breakdown": [{"label": "Sayı", "value": n}]
        }
    except ValueError:
        raise ValueError("Geçerli bir tamsayı girin.")
