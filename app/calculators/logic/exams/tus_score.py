def calc_tus(p_c: int|str=0, p_i: int|str=0, c_c: int|str=0, c_i: int|str=0) -> dict:
    pc = int(p_c); pi = int(p_i)
    cc = int(c_c); ci = int(c_i)
    
    # 120 Temel Tip, 120 Klinik Tıp = 240 questions total
    p_net = max(0, pc - (pi / 4.0))
    c_net = max(0, cc - (ci / 4.0))
    
    # 2026 approx katsayilar
    # K Puanı = ~0.3 (Temel) + ~0.7 (Klinik), T Puanı = ~0.7 (Temel) + ~0.3 (Klinik) vb. x100 + 35 offset
    # Let's do a simplified standard formula for TUS
    
    klinik_score = 35 + (p_net * 0.15) + (c_net * 0.35)
    temel_score = 35 + (p_net * 0.35) + (c_net * 0.15)
    
    if klinik_score > 80: klinik_score = 85.0
    if temel_score > 80: temel_score = 85.0
    
    return {
        "summary": {
            "label": "Klinik Tıp (K Puanı)",
            "value": round(klinik_score, 3)
        },
        "breakdown": [
            {"label": "Temel Tıp Net", "value": round(p_net, 2)},
            {"label": "Klinik Tıp Net", "value": round(c_net, 2)},
            {"label": "K-Puanı (Uzmanlık)", "value": round(klinik_score, 3)},
            {"label": "T-Puanı (Temel)", "value": round(temel_score, 3)}
        ]
    }
