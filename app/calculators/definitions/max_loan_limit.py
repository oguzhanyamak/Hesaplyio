from app.calculators.logic.max_loan_limit import calculate_max_loan_limit

MAX_LOAN_LIMIT_CONFIG = {
    "id": "max-loan",
    "slug": "ne-kadar-kredi-cekebilirim-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Ne Kadar Kredi Çekebilirim?",
    "description": "Gelirinize ve banka kredi politikalarına (BDDK %50 kuralı) göre alabileceğiniz maksimum kredi tutarını hesaplayın.",
    "seo": {
        "meta_title": "Aylık Gelirime Göre Ne Kadar Kredi Çekebilirim? 2026",
        "meta_description": "Maaşıma göre ne kadar kredi alabilirim? BDDK belgelenebilir gelir kurallarına göre maksimum ihtiyaç veya konut kredisi limitinizi hesaplayın.",
        "meta_keywords": ["ne kadar kredi çekebilirim", "kredi limit hesaplama", "maaşıma göre kredi"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "monthly_income",
            "type": "number",
            "label": "Aylık Net Geliriniz (₺)",
            "placeholder": "Örnek: 45000",
            "required": True,
            "min": 0, 
            "tooltip": "Belgelenebilir net maaşınız ve diğer ek gelirleriniz."
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Kredi Vadesi (Ay)",
            "placeholder": "Örnek: 36",
            "required": True,
            "min": 1,
            "tooltip": "Kaç ay vade ile borçlanmak istersiniz?"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Ortalama Banka Faizi (%)",
            "placeholder": "Örnek: 3.50",
            "required": True,
            "min": 0.01,
            "tooltip": "Hesaplama yapılacak varsayılan faiz oranı."
        }
    ],
    "logic_function": calculate_max_loan_limit,
    "faq": [
        {
            "question": "Kredi taksitlerim maaşımın ne kadarı olabilir?",
            "answer": "Bankalar BDDK tavsiyeleri doğrultusunda, tüm kredi kartı ve kredi ödemelerinizin toplam aylık belgelenebilir gelirinizin yarısını (%50) geçmemesini bekler."
        }
    ]
}
