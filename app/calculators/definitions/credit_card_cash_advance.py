from app.calculators.logic.credit_card_installments import calculate_credit_card_installments # Uses exact same logic math

CREDIT_CARD_CASH_ADVANCE_CONFIG = {
    "id": "cc-cash-advance",
    "slug": "kredi-karti-taksitli-nakit-avans-hesaplama",
    "category": "Kredi Kartı Hesaplama",
    "title": "Taksitli Nakit Avans Hesaplama",
    "description": "Kredi kartından ATM veya mobil şube aracılığıyla çekeceğiniz nakit avansın işlem ücretlerini ve taksitlerini hesaplayın.",
    "seo": {
        "meta_title": "Taksitli Nakit Avans Hesaplama 2026",
        "meta_description": "Kredi kartından taksitli nakit çekmek ne kadar masraflı? BSMV, KKDF vergi dilimleri ve komisyon tutarı ile net avans faizi hesaplama tablosu.",
        "meta_keywords": ["nakit avans hesaplama", "taksitli nakit avans", "kredi kartı para çekme", "TCMB faiz oranları"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "amount",
            "type": "number",
            "label": "Çekilecek Nakit Tutar (₺)",
            "placeholder": "Örnek: 10000",
            "required": True,
            "min": 100
        },
        {
            "name": "term",
            "type": "number",
            "label": "Taksit Sayısı (Ay)",
            "placeholder": "Örnek: 6",
            "required": True,
            "min": 2,
            "max": 12,
            "tooltip": "Güncel BDDK taksit sınırları gereği."
        },
        {
            "name": "monthly_interest",
            "type": "number",
            "step": "0.01",
            "label": "TCMB Avans Faizi (%)",
            "placeholder": "Örnek: 5.00",
            "required": True,
            "default": "5.00",
            "tooltip": "TCMB'nin onayladığı azami nakit çekim faizi."
        }
    ],
    "logic_function": calculate_credit_card_installments,
    "faq": [
        {
            "question": "Nakit avans çekerken ek ücret alınır mı?",
            "answer": "Evet. Taksitli veya taksitsiz olması farketmeksizin ATM veya diğer kanallardan nakit çekim komisyonu (Meblağa Göre %1 - %1.5 Arası + BSMV Sabit Ücret) bankanız tarafından ilk ekstrede peşin olarak yansıtılabilir."
        }
    ]
}
