from app.calculators.logic.credit_card_delay_interest import calculate_credit_card_delay_interest

CC_DELAY_INTEREST_CONFIG = {
    "id": "cc-delay",
    "slug": "kredi-karti-gecikme-faizi-hesaplama",
    "category": "Kredi Kartı Hesaplama",
    "title": "Kredi Kartı Gecikme Faizi Hesaplama",
    "description": "Ödenmeyen asgari tutar üzerinden işleyen kredi kartı gecikme faizini ve üzerine binen vergileri (KKDF, BSMV) hesaplayın.",
    "seo": {
        "meta_title": "Kredi Kartı Gecikme Faizi Hesaplama: Borç Limiti 2026",
        "meta_description": "Kredi kartını geç ödersem ne kadar gecikme faizi işler? TCMB oranları üzerinden günlük kredi kartı borç cezası hesaplama aracı.",
        "meta_keywords": ["kredi kartı gecikme", "gecikme faizi hesaplama", "kredi kartı borcu hesaplama", "KKDF", "BSMV"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "delayed_amount",
            "type": "number",
            "label": "Geciken Asgari Tutar (₺)",
            "placeholder": "Örnek: 15000",
            "required": True,
            "min": 1, 
            "tooltip": "Ödenmesi gereken fakat ödenmeyen asgari tutarı girin."
        },
        {
            "name": "passed_days",
            "type": "number",
            "label": "Gecikilen Gün Sayısı",
            "placeholder": "Örnek: 15",
            "required": True,
            "min": 1,
            "tooltip": "Son ödeme tarihinden bugüne kadar geçen iş günü"
        },
        {
            "name": "current_interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "TCMB Aylık Gecikme Faizi (%)",
            "placeholder": "Örnek: 4.55",
            "required": True,
            "min": 0,
            "default": "4.55",
            "tooltip": "TCMB tarafından belirlenen güncel gecikme faizi oranı."
        }
    ],
    "logic_function": calculate_credit_card_delay_interest,
    "faq": [
        {
            "question": "Kredi kartı gecikme faizi nasıl hesaplanır?",
            "answer": "Gecikme faizi günlük ve aylık olarak işler. Aylık faiz 30'a bölünür, günlük oran bulunur. Asgari ödeme tutarının ödenmeyen kısmı üzerinden günlük oran ve gecikilen gün çarpılıp; üzerine %15 KKDF ve %15 BSMV vergisi eklenerek faturanıza yansıtılır."
        }
    ]
}
