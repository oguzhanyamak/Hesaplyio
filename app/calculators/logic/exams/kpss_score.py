from app.calculators.logic.exams.base_exam import calculate_base_exam

def calculate_kpss(gy_correct: int|str=0, gy_incorrect: int|str=0, gk_correct: int|str=0, gk_incorrect: int|str=0) -> dict:
    gy_c = int(gy_correct); gy_i = int(gy_incorrect)
    gk_c = int(gk_correct); gk_i = int(gk_incorrect)
    
    gy_net = max(0, gy_c - (gy_i / 4.0))
    gk_net = max(0, gk_c - (gk_i / 4.0))
    total_net = gy_net + gk_net
    
    # 2026 Approx coefficients: Base = ~40, GY_coef = ~0.50, GK_coef = ~0.50 
    # Max score ~ 100 for 120 net. So (0.50 * 120) + 40 = 100
    
    score = 40 + (gy_net * 0.50) + (gk_net * 0.50)
    if score > 100: score = 100.0
    if total_net <= 0: score = 0
    
    return {
        "summary": {
            "label": "KPSS P3 (Lisans) Puanı*",
            "value": round(score, 3)
        },
        "breakdown": [
            {"label": "Puan Türü", "value": "KPSSP3"},
            {"label": "Genel Yetenek Neti", "value": round(gy_net, 2)},
            {"label": "Genel Kültür Neti", "value": round(gk_net, 2)},
            {"label": "Toplam Net", "value": round(total_net, 2)},
            {"label": "Tahmini Puan", "value": round(score, 3)}
        ]
    }
