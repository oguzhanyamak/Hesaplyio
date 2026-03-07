def calculate_net_to_gross(net_salary: str | float, calc_year: str = "2026") -> dict:
    """
    Mock calculation for Net to Gross.
    In a real app, this would use tax brackets.
    """
    try:
        net = float(net_salary)
    except ValueError:
        raise ValueError("Invalid salary provided.")

    if net < 17002: # Minimum wage check assumption
        result = "Net salary cannot be less than minimum wage (17,002 TL)"
    
    # Very rough approx for mock purposes
    gross = net * 1.41
    sgk = gross * 0.14
    unemployment = gross * 0.01
    income_tax = gross * 0.15 # Minimum bracket
    stamp_tax = gross * 0.00759
    
    return {
        "summary": {
            "label": "Brüt Maaşınız",
            "value": round(gross, 2)
        },
        "breakdown": [
            {"label": "Net Maaş", "value": round(net, 2)},
            {"label": "SGK Primi (%14)", "value": round(sgk, 2)},
            {"label": "İşsizlik Sig. Fonu (%1)", "value": round(unemployment, 2)},
            {"label": "Gelir Vergisi", "value": round(income_tax, 2)},
            {"label": "Damga Vergisi", "value": round(stamp_tax, 2)},
        ]
    }
def calculate_gross_to_net(gross_salary: str | float, calc_year: str = "2026") -> dict:
    """Brütten Nete Maaş Hesaplama."""
    try:
        gross = float(gross_salary)
    except ValueError:
        raise ValueError("Geçerli bir brüt maaş girin.")
    
    # Mock calculation based on standard ratios
    sgk = gross * 0.14
    unemployment = gross * 0.01
    tax_base = gross - sgk - unemployment
    income_tax = tax_base * 0.15 # Minimum vergi dilimi varsayıldı
    stamp_tax = gross * 0.00759
    
    # 2026 Asgari ücret istisnası varsayımı (Mock)
    exemption = 2550.0 # Örnek bir istisna tutarı
    
    net = gross - sgk - unemployment - max(0, income_tax - exemption) - (stamp_tax * 0.8)
    
    return {
        "summary": { "label": "Net Maaş", "value": round(net, 2) },
        "breakdown": [
            {"label": "Brüt Maaş", "value": round(gross, 2)},
            {"label": "SGK İşçi Payı (%14)", "value": round(sgk, 2)},
            {"label": "İşsizlik Sig. (%1)", "value": round(unemployment, 2)},
            {"label": "Hesaplanan Gelir Vergisi", "value": round(income_tax, 2)},
            {"label": "Asgari Ücret Vergi İstisnası", "value": round(exemption, 2)},
            {"label": "Damga Vergisi", "value": round(stamp_tax, 2)},
            {"label": "Ele Geçen Net Maaş", "value": round(net, 2)}
        ]
    }

def calculate_severance_pay(gross_salary: float, years: int, months: int, days: int) -> dict:
    """Kıdem ve İhbar Tazminatı Hesaplama (Genel Mantık)."""
    try:
        gross = float(gross_salary)
        total_days = (int(years) * 365) + (int(months) * 30) + int(days)
    except ValueError:
        raise ValueError("Geçerli sayısal değerler girin.")
        
    # Kıdem tazminatı tavanı (Mock 2026 Ocak varsayımı)
    ceiling = 60000.0
    effective_gross = min(gross, ceiling)
    
    severance = (effective_gross / 365) * total_days
    stamp_tax = severance * 0.00759
    net_severance = severance - stamp_tax
    
    return {
        "summary": { "label": "Net Kıdem Tazminatı", "value": round(net_severance, 2) },
        "breakdown": [
            {"label": "Brüt Kıdem Tazminatı", "value": round(severance, 2)},
            {"label": "Damga Vergisi Kesintisi", "value": round(stamp_tax, 2)},
            {"label": "Toplam Çalışma Günü", "value": total_days},
            {"label": "Ödenecek Net Tutar", "value": round(net_severance, 2)}
        ]
    }

def calculate_unemployment_benefit(avg_gross_4m: float) -> dict:
    """İşsizlik Maaşı Hesaplama."""
    try:
        avg_gross = float(avg_gross_4m)
    except ValueError:
        raise ValueError("Geçerli bir ortalama brüt maaş girin.")
        
    # İşsizlik maaşı, son 4 aylık brüt ortalamasının %40'ıdır.
    # Ancak asgari ücretin %80'ini geçemez.
    benefit = avg_gross * 0.4
    
    # Mock asgari ücret varsayımı
    min_wage_gross = 25000.0
    max_benefit = min_wage_gross * 0.8
    
    final_benefit = min(benefit, max_benefit)
    stamp_tax = final_benefit * 0.00759
    net_benefit = final_benefit - stamp_tax
    
    return {
        "summary": { "label": "Aylık İşsizlik Maaşı", "value": round(net_benefit, 2) },
        "breakdown": [
            {"label": "Brüt İşsizlik Ödeneği", "value": round(final_benefit, 2)},
            {"label": "Damga Vergisi", "value": round(stamp_tax, 2)},
            {"label": "Net Ödenecek Tutar", "value": round(net_benefit, 2)}
        ]
    }

def calculate_notice_pay(gross_salary: float, duration_months: int) -> dict:
    """İhbar Tazminatı Hesaplama."""
    try:
        gross = float(gross_salary)
        months = int(duration_months)
    except ValueError:
        raise ValueError("Geçerli değerler girin.")
        
    daily_gross = gross / 30.0
    
    # İhbar süreleri (Hafta bazında)
    if months < 6:
        weeks = 2
    elif months < 18:
        weeks = 4
    elif months < 36:
        weeks = 6
    else:
        weeks = 8
        
    days = weeks * 7
    total_gross = daily_gross * days
    
    # Kesintiler (İhbar tazminatında gelir vergisi ve damga vergisi vardır)
    income_tax = total_gross * 0.15 # Genelde ilk dilim
    stamp_tax = total_gross * 0.00759
    net_notice = total_gross - income_tax - stamp_tax
    
    return {
        "summary": { "label": "Net İhbar Tazminatı", "value": round(net_notice, 2) },
        "breakdown": [
            {"label": "Brüt İhbar Tazminatı", "value": round(total_gross, 2)},
            {"label": "İhbar Süresi (Hafta)", "value": weeks},
            {"label": "Hesaplanan Gün", "value": days},
            {"label": "Gelir Vergisi Kesintisi (%15)", "value": round(income_tax, 2)},
            {"label": "Damga Vergisi Kesintisi", "value": round(stamp_tax, 2)},
            {"label": "Ödenecek Net Tutar", "value": round(net_notice, 2)}
        ]
    }
