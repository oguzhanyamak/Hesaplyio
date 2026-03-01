from app.calculators.logic.commercial_loan import calculate_commercial_loan

COMMERCIAL_LOAN_CONFIG = {
    "id": "commercial-loan",
    "slug": "ticari-kredi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Ticari Kredi Hesaplama",
    "description": "Şirketlere özel avantajlı BSMV oranlarıyla taksitli ticari kredi ve ihtiyaç hesaplama aracı.",
    "seo": {
        "meta_title": "Ticari Kredi ve Taksitli Şirket Kredisi Hesaplama 2026",
        "meta_description": "Esnaf, KOBİ ve şirketler için düşük BSMV ve sıfır KKDF vergi avantajıyla taksitli ticari kredi hesaplama.",
        "meta_keywords": ["ticari kredi", "şirket kredisi hesaplama", "esnaf kredisi", "kredi hesaplama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 1500000",
            "required": True,
            "min": 10000, 
            "tooltip": "Çekmek istediğiniz limit"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 2.50",
            "required": True,
            "min": 0,
            "tooltip": ""
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 36",
            "required": True,
            "min": 1,
            "max": 60,
            "tooltip": "Taksitlendirme ayı"
        },
        {
            "name": "loan_type",
            "type": "select",
            "label": "Kredi Tipi",
            "options": [{"label": "Taksitli Ticari Kredi", "value": "Taksitli"}, {"label": "Eşit Anaparalı Kredi", "value": "Esit_Anaparali"}],
            "default": "Taksitli",
            "tooltip": "Şu anda sadece Taksitli varyant desteklenmektedir."
        }
    ],
    "logic_function": calculate_commercial_loan,
    "faq": [
        {
            "question": "Ticari kredilerde vergi kesintisi var mıdır?",
            "answer": "Evet, ticari kredilerde %0 KKDF uygulanırken, güncel BSMV oranı genellikle %5 olarak tahsil edilmektedir."
        }
    ]
}
