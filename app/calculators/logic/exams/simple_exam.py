def calculate_simple_exam(c: int|str=0, i: int|str=0, total_q: int=80, correct_coeff: float=1.25, base: int=0, penalize: bool=True) -> dict:
    cor = int(c)
    inc = int(i)
    
    net = max(0, cor - (inc / 4.0)) if penalize else cor
    
    score = base + (net * correct_coeff)
    if score > 100: score = 100
    
    return {
        "summary": {
            "label": "Sonuç Puanınız",
            "value": round(score, 3)
        },
        "breakdown": [
            {"label": "Toplam Soru", "value": total_q},
            {"label": "Doğru", "value": cor},
            {"label": "Yanlış", "value": inc},
            {"label": "Net Sayısı (- \u00BC)" if penalize else "Soru Başı Puan", "value": round(net, 2) if penalize else correct_coeff},
            {"label": "Puan", "value": round(score, 3)}
        ]
    }
