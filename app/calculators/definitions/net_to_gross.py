from app.calculators.logic.salary import calculate_net_to_gross

NET_TO_GROSS_CONFIG = {
    "id": "net-to-gross",
    "slug": "netten-brute-maas-hesaplama",
    "category": "Maaş Hesaplama",
    "title": "Netten Brüte Maaş Hesaplama",
    "description": "2026 yılı güncel vergi dilimleri ve SGK kesintileri ile net maaşınızdan brüt maaşınızı anında hesaplayın.",
    "seo": {
        "meta_title": "Netten Brüte Maaş Hesaplama 2026 | Anında Kesin Sonuç",
        "meta_description": "2026 güncel SGK ve vergi oranlarıyla netten brüte maaşınızı anında hesaplayın.",
        "meta_keywords": ["netten brüte", "maaş hesaplama", "2026 vergi dilimleri"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "net_salary",
            "type": "number",
            "label": "Aylık Net Maaş (₺)",
            "placeholder": "Örnek: 45000",
            "required": True,
            "min": 17002, 
            "tooltip": "Aylık olarak banka hesabınıza yatan net tutar"
        },
        {
            "name": "calc_year",
            "type": "select",
            "label": "Hesaplama Yılı",
            "options": [{"label": "2026", "value": "2026"}, {"label": "2025", "value": "2025"}],
            "default": "2026"
        }
    ],
    "logic_function": calculate_net_to_gross,
    "faq": [
        {
            "question": "Netten brüte maaş hesabı nasıl yapılır?",
            "answer": "Netten brüte hesaplama işlemi, net maaşın üzerine sırasıyla SGK, İşsizlik sigortası, Gelir Vergisi ve Damga vergisi eklenerek yapılır."
        }
    ]
}
