def calculate_loan_expense(principal: float | str) -> dict:
    try:
        p = float(principal)
    except ValueError:
        raise ValueError("Lütfen geçerli bir tutar girin.")

    # BDDK rules: Allocation fee (Tahsis ücreti) is capped at %0.5 of the principal.
    allocation_fee = p * 0.005
    # BSMV of 15% is applied to the allocation fee
    bsmv = allocation_fee * 0.15
    
    total_bank_fee = allocation_fee + bsmv
    
    return {
        "summary": {
            "label": "Yasal Maksimum Dosya Masrafı",
            "value": round(total_bank_fee, 2)
        },
        "breakdown": [
            {"label": "Kredi Miktarı", "value": round(p, 2)},
            {"label": "Kredi Tahsis Ücreti (%0.5 Kesinti)", "value": round(allocation_fee, 2)},
            {"label": "Tahsis Ücreti Üzerinden BSMV (%15)", "value": round(bsmv, 2)},
            {"label": "Toplam Hesabınızdan Kesilecek Tutar", "value": round(total_bank_fee, 2)},
        ]
    }
