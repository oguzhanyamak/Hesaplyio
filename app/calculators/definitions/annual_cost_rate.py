from app.calculators.logic.annual_cost_rate import calculate_apr

ANNUAL_COST_RATE_CONFIG = {
    "id": "annual-cost-rate",
    "slug": "kredi-yillik-maliyet-orani-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Kredi Yıllık Maliyet Oranı Hesaplama",
    "description": "Gizli sigortalar, tahsis ücretleri ve kredi sözleşme masrafları dahil edildiğinde çektiğiniz kredinin TEORİK YILLIK FAİZ (APR) oranının gerçekte ne kadar yüksek olduğunu öğrenin.",
    "seo": {
        "meta_title": "Kredi Yıllık Maliyet Oranı Hesaplama (Apr/Efektif Faiz) 2026",
        "meta_description": "Bankanın bana önerdiği kredinin gerçek faizi (Yıllık Maliyet Oranı - APR) iç verim oranı (IRR) metoduyla nasıl hesaplanır? Dosya masrafı dahil gerçek aylık efektif faizi hesaplayın.",
        "meta_keywords": ["yıllık maliyet oranı", "etkin faiz oranı hesaplama", "apr", "gerçek kredi hesaplama", "IRR"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Tüm Kredi (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 1000
        },
        {
            "name": "monthly_payment",
            "type": "number",
            "label": "Banka Tarafından İstenen Sabit Aylık Taksit (₺)",
            "placeholder": "Örnek: 6250",
            "required": True,
            "min": 0
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 24",
            "required": True,
            "min": 1,
            "max": 360
        },
        {
            "name": "allocation_fee",
            "type": "number",
            "label": "Banka Sizden Peşin Aldığı Dosya/Tahsis/Sigorta Masrafı (₺)",
            "placeholder": "Örnek: 1500",
            "required": True,
            "min": 0,
            "tooltip": "Elime geçen paradan bankanın başlangıçta kestiği tüm tutar"
        }
    ],
    "logic_function": calculate_apr,
    "faq": [
        {
            "question": "Yıllık maliyet oranı (YMO) nedir ve neden bankanın verdiğinden daha yüksektir?",
            "answer": "Banka size rekabet edebilmek için faiz oranını düşük (örneğin %2.5) söyleyebilir ancak başlangıçta aldığı Dosya Masrafı, Zorunlu Sigorta gibi tutarları anaparadan kestiği için sizin 'eliniize net geçen tutar' azalır. Vade bitiminde ödenen nakit ile başta alınan net nakit arasındaki gerçek denklik faizine Yıllık Efektif Maliyet Oranı denir ve tüm yasal platformlarda bu oranı müşteriye beyan etmek mecburi bir BDDK kuralıdır."
        }
    ]
}
