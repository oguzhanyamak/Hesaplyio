def calc_dgs(say_c: int|str=0, say_i: int|str=0, soz_c: int|str=0, soz_i: int|str=0, diploma: float|str=0) -> dict:
    sc = int(say_c); si = int(say_i)
    zc = int(soz_c); zi = int(soz_i)
    dip = float(diploma)
    
    say_net = max(0, sc - (si / 4.0))
    soz_net = max(0, zc - (zi / 4.0))
    
    sayp = say_net * 3.0
    sozp = soz_net * 3.0
    
    # Approx base offsets
    dgs_say = 100 + sayp + (sozp * 0.5) 
    dgs_ea = 100 + sayp + sozp
    dgs_soz = 100 + (sayp * 0.5) + sozp
    
    # OBP: max 80 points. min 40. formula: dip * 0.8
    obp = dip * 0.8
    
    return {
        "summary": {
            "label": "DGS Sayısal Puanınız",
            "value": round(dgs_say + obp, 3)
        },
        "breakdown": [
            {"label": "Sayısal / Sözel Netleri", "value": f"{round(say_net, 2)} / {round(soz_net, 2)}"},
            {"label": "Diploma Puanı Etkisi (+ ÖBP)", "value": round(obp, 2)},
            {"label": "Yerleştirme DGS Sayısal", "value": round(dgs_say + obp, 3)},
            {"label": "Yerleştirme DGS Eşit Ağırlık", "value": round(dgs_ea + obp, 3)},
            {"label": "Yerleştirme DGS Sözel", "value": round(dgs_soz + obp, 3)},
        ]
    }
