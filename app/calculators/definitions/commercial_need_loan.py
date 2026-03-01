from app.calculators.logic.commercial_loan import calculate_commercial_loan

COMMERCIAL_NEED_LOAN_CONFIG = {
    "id": "commercial-need-loan",
    "slug": "ticari-ihtiyac-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Ticari İhtiyaç / Taksitli Esnaf Kredisi",
    "description": "Şirket nakit akışınızı düzenlemek için kullanacağınız taksitli ticari kredinin ödeme tablosunu çıkarın.",
    "seo": {
        "meta_title": "Ticari İhtiyaç ve Esnaf Kredisi Hesaplama 2026",
        "meta_description": "İşletme sermayesi veya acil şirket ihtiyaçları için kullanılan ticari kredinin BSMV indirimli olarak taksit hesaplaması.",
        "meta_keywords": ["ticari ihtiyaç kredisi", "esnaf kredisi hesaplama", "işletme kredisi", "kobi"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Talep Edilen Limit (₺)",
            "placeholder": "Örnek: 250000",
            "required": True,
            "min": 10000 
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Banka Faiz Oranı (%)",
            "placeholder": "Örnek: 2.50",
            "required": True,
            "min": 0
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 36",
            "required": True,
            "min": 1
        }
    ],
    "logic_function": calculate_commercial_loan,
    "faq": [
        {
            "question": "Ticari ihtiyaç (işletme) kredisinin farkı nedir?",
            "answer": "Bireysel ihtiyaç kredisinde %15 KKDF ve %15 BSMV uygulanırken, Ticari amaçla kullanılan nakit kredilerde (Taksitli Ticari Kredi - TTK) KKDF 0, BSMV %5 olarak faturalandırılır. Bu yüzden bireyselden çok daha ucuzdur."
        }
    ]
}
