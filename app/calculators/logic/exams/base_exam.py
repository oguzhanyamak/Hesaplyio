def calculate_base_exam(c: int|str=0, i: int|str=0, max_question: int=100, exam_name: str="Test", base: int=0, coefficient: float=1.0) -> dict:
    cor = int(c)
    inc = int(i)
    
    net = max(0, cor - (inc / 4.0)) # 4 wrong 1 right default
    
    score = base + (net * coefficient)
    
    return {
        "summary": {
            "label": f"{exam_name} Puanınız",
            "value": round(score, 3)
        },
        "breakdown": [
            {"label": "Doğru Sayısı", "value": cor},
            {"label": "Yanlış Sayısı", "value": inc},
            {"label": "Net Sayısı (- \u00BC)", "value": round(net, 2)},
        ]
    }
