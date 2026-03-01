from app.calculators.logic.credit_card_installments import calculate_credit_card_installments

CREDIT_CARD_INSTALLMENTS_CONFIG = {
    "id": "cc-installments",
    "slug": "kredi-karti-islem-taksitlendirme-hesaplama",
    "category": "Kredi Kartı Hesaplama",
    "title": "Kredi Kartı İşlem Taksitlendirme",
    "description": "Peşin yaptığınız harcamayı sonradan taksitlendirirseniz ekstreye ne kadar aylık vade farkı yansıyacağını hesaplayın.",
    "seo": {
        "meta_title": "Kredi Kartı Peşin İşlem Sonradan Taksitlendirme 2026",
        "meta_description": "Tek çekim e-ticaret harcamalarını 3, 6, veya 12 aya banka uygulaması üzerinden taksitlendirirken ödenecek vade farkı faizini hesaplayın.",
        "meta_keywords": ["kart işlem taksitlendirme", "sonradan taksit", "kredi kartı vade farkı hesaplama", "peşine taksit"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "amount",
            "type": "number",
            "label": "Peşin Harcama Tutarı (₺)",
            "placeholder": "Örnek: 14500",
            "required": True,
            "min": 100
        },
        {
            "name": "term",
            "type": "number",
            "label": "Taksitlendirme Sayısı (Ay)",
            "placeholder": "Örnek: 3",
            "required": True,
            "min": 2,
            "max": 18
        },
        {
            "name": "monthly_interest",
            "type": "number",
            "step": "0.01",
            "label": "Banka Aylık Taksitlendirme Faizi (%)",
            "placeholder": "Örnek: 4.25",
            "required": True,
            "default": "4.25"
        }
    ],
    "logic_function": calculate_credit_card_installments,
    "faq": [
        {
            "question": "Sonradan taksitlendirme işlemlerinden vergi alınır mı?",
            "answer": "Evet. Her tüketici işleminde olduğu gibi yansıtılan vade farkı (faiz) üzerinden ek faiz olarak %15 Banka ve Sigorta Muameleleri Vergisi ve %15 KKDF alınır."
        }
    ]
}
