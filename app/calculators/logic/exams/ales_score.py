def calc_ales(say1_c: int|str=0, say1_i: int|str=0, soz1_c: int|str=0, soz1_i: int|str=0) -> dict:
    s_c = int(say1_c); s_i = int(say1_i)
    z_c = int(soz1_c); z_i = int(soz1_i)
    
    say_net = max(0, s_c - (s_i / 4.0))
    soz_net = max(0, z_c - (z_i / 4.0))
    
    # Approx ALES constants
    say_base = 50 + (say_net * 0.75) + (soz_net * 0.25)
    ea_base = 50 + (say_net * 0.50) + (soz_net * 0.50)
    soz_base = 50 + (say_net * 0.25) + (soz_net * 0.75)
    
    return {
        "summary": {
            "label": "ALES Sayısal Puanınız",
            "value": round(say_base, 3)
        },
        "breakdown": [
            {"label": "Sayısal Net", "value": round(say_net, 2)},
            {"label": "Sözel Net", "value": round(soz_net, 2)},
            {"label": "ALES Sayısal (SAY)", "value": round(say_base, 3)},
            {"label": "ALES Eşit Ağırlık (EA)", "value": round(ea_base, 3)},
            {"label": "ALES Sözel (SÖZ)", "value": round(soz_base, 3)},
        ]
    }
