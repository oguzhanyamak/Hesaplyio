from app.calculators.logic.loan import calculate_loan_repayment

LOAN_CONFIG = {
    "id": "consumer-loan",
    "slug": "kredi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "İhtiyaç Kredisi Hesaplama",
    "description": "Güncel faiz oranları, KKDF ve BSMV vergileri dahil olarak ihtiyaç kredisi ve aylık taksit tutarlarınızı anında hesaplayın.",
    "seo": {
        "meta_title": "İhtiyaç Kredisi Hesaplama 2026 | Taksit Ödeme Planı",
        "meta_description": "Ne kadar kredi çekebilirim? Güncel banka faiz oranlarıyla ihtiyaç kredisi hesaplama, aylık taksit tutarı ve ödeme planı çıkarın.",
        "meta_keywords": ["kredi hesaplama", "ihtiyaç kredisi", "kredi ödeme planı", "kredi faizi hesaplama", "aylık taksit"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 1000, 
            "tooltip": "Çekmek istediğiniz toplam tutar"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 3.50",
            "required": True,
            "min": 0,
            "tooltip": "Bankanın belirlediği aylık baz faiz oranı"
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 24",
            "required": True,
            "min": 1,
            "max": 36,
            "tooltip": "Aylık taksit sayınız"
        }
    ],
    "logic_function": calculate_loan_repayment,
    "faq": [
        {
            "question": "İhtiyaç kredisi hesaplamasında faiz harici neler eklenir?",
            "answer": "Kredi taksitleri hesaplanırken, aylık faiz oranının üzerine banka ve sigorta muameleleri vergisi (BSMV) ve kaynak kullanımı destekleme fonu (KKDF) kesintileri de eklenerek efektif faiz oranı bulunur."
        },
        {
            "question": "Taksitlerimi erken ödersem ne olur?",
            "answer": "Kredi taksitlerinizi erken kapattığınız takdirde kalan ayların faizi, KKDF ve BSMV kesintileri tahsil edilmez ve anapara üzerinden borcunuzu kapatırsınız."
        }
    ]
}
