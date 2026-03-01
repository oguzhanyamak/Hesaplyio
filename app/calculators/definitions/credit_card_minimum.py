from app.calculators.logic.credit_card_minimum import calculate_credit_card_minimum

CREDIT_CARD_MINIMUM_CONFIG = {
    "id": "credit-card-min",
    "slug": "kredi-karti-asgari-odeme-hesaplama",
    "category": "Kredi Kartı Hesaplama",
    "title": "Kredi Kartı Asgari Ödeme Tutarı Hesaplama",
    "description": "Güncel BDDK limit kurallarına göre kredi kartı dönem borcunuzun asgari ödeme tutarını anında hesaplayın.",
    "seo": {
        "meta_title": "Kredi Kartı Asgari Ödeme Tutarı Hesaplama 2026",
        "meta_description": "Kredi kartı dönem borcu asgari ödeme hesaplama. 25.000 TL altı ve üstü limitlere göre %20 ve %40 asgari ödeme oranları.",
        "meta_keywords": ["asgari ödeme", "kredi kartı asgari", "dönem borcu hesaplama", "asgari ödeme tutarı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "card_limit",
            "type": "number",
            "label": "Kredi Kartı Limiti (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 1000, 
            "tooltip": "Kartınıza tahsis edilen toplam limit."
        },
        {
            "name": "statement_balance",
            "type": "number",
            "label": "Güncel Dönem Borcu (₺)",
            "placeholder": "Örnek: 24500",
            "required": True,
            "min": 0,
            "tooltip": "Ekstrenizde kesilen toplam borç miktarı"
        },
        {
            "name": "is_new_card",
            "type": "select",
            "label": "Kartınız Son 1 Yıl İçinde mi Çıktı?",
            "options": [{"label": "Hayır (1 Yıldan Eski)", "value": "hayır"}, {"label": "Evet (Yeni Kart)", "value": "evet"}],
            "default": "hayır",
            "tooltip": "Yeni çıkan kredi kartlarında asgari ödeme oranı limiti gözetmeksizin %40 uygulanır."
        }
    ],
    "logic_function": calculate_credit_card_minimum,
    "faq": [
        {
            "question": "Kredi kartı asgari ödeme tutarı nasıl belirlenir?",
            "answer": "BDDK'nın düzenlemesine göre; limiti 25.000 TL’nin altında olan kredi kartları için asgari ödeme oranı dönem borcunun %20’sidir. Limiti 25.000 TL ve üzerinde olan kredi kartları için ise bu oran dönem borcunun %40’ıdır."
        }
    ]
}
