def calculate_apr(principal: float | str, monthly_payment: float | str, allocation_fee: float | str, term_months: int | str) -> dict:
    try:
        p = float(principal)
        mp = float(monthly_payment)
        af = float(allocation_fee)
        t = int(term_months)
    except ValueError:
        raise ValueError("Lütfen geçerli değerler girin.")

    # IRR (Internal Rate of Return) computation to find the real effective rate
    # Cash flow: at t=0, we get P - F (allocation fee)
    # Then we pay MP for 't' months.
    
    cashflows = [p - af] + [-mp] * t
    
    # We use Newton-Raphson method or standard secant to find IRR
    # Let's do a simple bounded search for the monthly rate
    low, high = 0.0, 1.0
    for _ in range(100):
        mid = (low + high) / 2
        npv = cashflows[0]
        for i in range(1, len(cashflows)):
            npv += cashflows[i] / ((1 + mid) ** i)
        
        if npv > 0:
            low = mid
        else:
            high = mid
            
    monthly_effective_rate = mid
    
    # Annual percentage rate (Yıllık Maliyet Oranı) calculation (Compounded)
    # in Turkey, generally calculated as simple nominal or effective compounded:
    # APR = ((1 + monthly_rate) ** 12 - 1) * 100
    
    apr = ((1 + monthly_effective_rate) ** 12 - 1) * 100
    
    return {
        "summary": {
            "label": "Yıllık Maliyet Oranı (Erişim Maliyeti)**",
            "value": round(apr, 2)
        },
        "breakdown": [
            {"label": "Kredi Tutarı", "value": round(p, 2)},
            {"label": "Kesilen Dosya/Tahsis Masrafı", "value": round(af, 2)},
            {"label": "Net Eline Geçen Para", "value": round(p - af, 2)},
            {"label": "Toplanan Aylık Taksit (Bankaya Giden)", "value": round(mp * t, 2)},
            {"label": "Gizli Efektif Aylık Faiz Oranı", "value": round(monthly_effective_rate * 100, 2)},
            {"label": "Yıllık Bileşik Maliyet Oranı", "value": str(round(apr, 2)) + "%"},
        ]
    }
