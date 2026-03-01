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
