def calc_lgs(tc_c: int|str=0, tc_i: int|str=0, mat_c: int|str=0, mat_i: int|str=0, fen_c: int|str=0, fen_i: int|str=0, ink_c: int|str=0, ink_i: int|str=0, din_c: int|str=0, din_i: int|str=0, yab_c: int|str=0, yab_i: int|str=0) -> dict:
    
    def get_net(c, i, questions, w_p=3.0):
        c, i = int(c), int(i)
        # LGS'de 3 yanlis 1 dogruyu goturur.
        return max(0, c - (i / w_p))
    
    # Kapsamlı Katsayılar LGS için (Tü/Ma/Fen=4; İn/Di/Ya=1 Katsayı)
    tr_net = get_net(tc_c, tc_i, 20)
    mat_net = get_net(mat_c, mat_i, 20)
    fen_net = get_net(fen_c, fen_i, 20)
    ink_net = get_net(ink_c, ink_i, 10)
    din_net = get_net(din_c, din_i, 10)
    yab_net = get_net(yab_c, yab_i, 10)
    
    total_net = (tr_net + mat_net + fen_net + ink_net + din_net + yab_net)
    
    # Standart puanlama: Taban Puan = 195 civari. Max Puan = 500
    # Katsayılar: Tr/Mat/Fen * ~3.8 , Digerleri * ~1.2
    
    tr_p = tr_net * 4.30
    mat_p = mat_net * 4.60
    fen_p = fen_net * 4.10
    ink_p = ink_net * 1.50
    din_p = din_net * 1.60
    yab_p = yab_net * 1.40
    
    base_lgs_points = 195  
    total_score = base_lgs_points + tr_p + mat_p + fen_p + ink_p + din_p + yab_p
    
    if total_score > 500: total_score = 500.0
    
    return {
        "summary": {
            "label": "LGS Puanınız (Nispi)",
            "value": round(total_score, 3)
        },
        "breakdown": [
            {"label": "Toplam Netiniz (-1/3 Katı)", "value": round(total_net, 2)},
            {"label": "Türkçe / Mat / Fen Netleri", "value": f"{round(tr_net, 1)} / {round(mat_net, 1)} / {round(fen_net, 1)}"},
            {"label": "İnkılap / Din / Yabancı Dil", "value": f"{round(ink_net, 1)} / {round(din_net, 1)} / {round(yab_net, 1)}"},
            {"label": "MEB Taban Puanı", "value": base_lgs_points},
            {"label": "Yerleştirme LGS Puanınız", "value": round(total_score, 3)},
        ]
    }
