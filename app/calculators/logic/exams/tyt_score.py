def calculate_yks_tyt(tr_correct: int|str=0, tr_incorrect: int|str=0, math_correct: int|str=0, math_incorrect: int|str=0, soc_correct: int|str=0, soc_incorrect: int|str=0, sci_correct: int|str=0, sci_incorrect: int|str=0, diploma: float|str=0) -> dict:
    tr_c = int(tr_correct); tr_i = int(tr_incorrect)
    ma_c = int(math_correct); ma_i = int(math_incorrect)
    so_c = int(soc_correct); so_i = int(soc_incorrect)
    sc_c = int(sci_correct); sc_i = int(sci_incorrect)
    dip = float(diploma)

    # Calculate Nets (4 YANLIS 1 DOGRUYU GOTURUR)
    tr_net = max(0, tr_c - (tr_i / 4.0))
    ma_net = max(0, ma_c - (ma_i / 4.0))
    so_net = max(0, so_c - (so_i / 4.0))
    sc_net = max(0, sc_c - (sc_i / 4.0))

    total_net = tr_net + ma_net + so_net + sc_net
    
    # OSYM Standard Deviations & Coefficients (approximate coefficients of 2025/2026)
    # Base Point usually 100
    base = 100
    tr_points = tr_net * 3.3
    ma_points = ma_net * 3.3
    so_points = so_net * 3.4
    sc_points = sc_net * 3.4
    
    raw_score = base + tr_points + ma_points + so_points + sc_points
    
    # OBP (Ortaöğretim Başarı Puanı) = Diploma Grade * 5
    # Exam Score Contribution = OBP * 0.12 = Diploma * 5 * 0.12 = Diploma * 0.6
    obp = dip * 5
    placement_contribution = dip * 0.6
    
    placement_score = raw_score + placement_contribution

    return {
        "summary": {
            "label": "TYT Yerleştirme Puanı",
            "value": round(placement_score, 3)
        },
        "breakdown": [
            {"label": "Toplam Doğru/Yanlış", "value": f"{tr_c+ma_c+so_c+sc_c} D / {tr_i+ma_i+so_i+sc_i} Y"},
            {"label": "Toplam Net", "value": round(total_net, 2)},
            {"label": "Ham TYT Puanı", "value": round(raw_score, 3)},
            {"label": "OBP Katkısı", "value": f"+{round(placement_contribution, 3)}"},
            {"label": "Yerleştirme TYT Puanı", "value": round(placement_score, 3)},
        ]
    }
