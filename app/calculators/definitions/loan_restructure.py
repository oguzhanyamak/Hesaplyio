from app.calculators.logic.loan_restructure import calculate_loan_restructure

LOAN_RESTRUCTURE_CONFIG = {
    "id": "loan-restructure",
    "slug": "kredi-yapilandirma-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Kredi Yapılandırma Hesaplama",
    "description": "Faiz oranları düştüğünde mevcut kredinizi yeni oranla yapılandırmanın (refinansman) size ne kadar tasarruf sağlayacağını görün.",
    "seo": {
        "meta_title": "Kredi Yapılandırma (Refinansman) Hesaplama 2026",
        "meta_description": "Faizler düşünce kredi yapılandırması kârlı mıdır? Kredi borcunuzu daha düşük bir orandan kapattığınızda doğacak aylık taksit ve toplam bakiye indirimini hesaplayın.",
        "meta_keywords": ["kredi yapılandırma hesaplama", "kredi transferi", "refinansman", "kredi aylık taksit düşürme", "yapılandırma kârı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "old_principal",
            "type": "number",
            "label": "Eski Kredi Başlangıç Tutarı (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 10000
        },
        {
            "name": "old_installments",
            "type": "number",
            "label": "Eski Kredinin İlk Çekildiği Vade (Ay)",
            "placeholder": "Örnek: 36",
            "required": True,
            "min": 6
        },
        {
            "name": "old_interest",
            "type": "number",
            "step": "0.01",
            "label": "Eski Kredi Faiz Oranı (%)",
            "placeholder": "Örnek: 3.50",
            "required": True,
            "min": 0
        },
        {
            "name": "remaining_months",
            "type": "number",
            "label": "Hali Hazırda Kalan Vadeniz (Ay)",
            "placeholder": "Örnek: 24",
            "required": True,
            "min": 2,
            "tooltip": "Kredinin bitmesine kaç ay kaldı?"
        },
        {
            "name": "new_interest",
            "type": "number",
            "step": "0.01",
            "label": "Sunulan Yeni Düşük Faiz Oranı (%)",
            "placeholder": "Örnek: 2.10",
            "required": True,
            "min": 0,
            "tooltip": "Banka tarafından önerilen güncel indirimli oran."
        }
    ],
    "logic_function": calculate_loan_restructure,
    "faq": [
        {
            "question": "Kredi yapılandırması mantıklı mı?",
            "answer": "Bu, mevcut kredinizin ne kadarlık bir bölümünü ödediğinize ve faiz oranındaki düşüş miktarına bağlıdır. Kredinin başında (ilk yıl) yapılandırma yapmak en kârlı olanıyken, vadenin geneli bittiyse (faiz yerine çoğunlukla anapara ödüyorsanız) yeni dosya masrafı ve cezalar sebebiyle yapılandırma zararlı olabilir."
        }
    ]
}
