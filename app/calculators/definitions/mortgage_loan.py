from app.calculators.logic.mortgage_loan import calculate_mortgage_loan

MORTGAGE_LOAN_CONFIG = {
    "id": "mortgage-loan",
    "slug": "konut-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Konut Kredisi Hesaplama",
    "description": "Ev sahibi olmak isteyenler için %0 BSMV ve KKDF (vergisiz) konut kredisi taksit hesaplama aracı ve ödeme tablosu.",
    "seo": {
        "meta_title": "Konut Kredisi Hesaplama 2026 | Taksit Ödeme Planı",
        "meta_description": "2026 konut kredisi faiz oranlarıyla aylık taksit hesaplama. 120 ay veya 240 ay vadeli ev kredisi ödeme planı ve toplam maliyet hesabı.",
        "meta_keywords": ["konut kredisi hesaplama", "ev kredisi", "kredi ödeme planı", "ev kredisi faizi", "vergisiz kredi"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 2000000",
            "required": True,
            "min": 10000, 
            "tooltip": "Satın alacağınız evin tutarı değil, çekeceğiniz kredi tutarı"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 2.80",
            "required": True,
            "min": 0,
            "tooltip": "Bankanın sunduğu konut kredisi aylık faiz oranı"
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 120",
            "required": True,
            "min": 1,
            "max": 240,
            "tooltip": "Genellikle konut kredilerinde 120 veya 240 aya kadar çıkar"
        }
    ],
    "logic_function": calculate_mortgage_loan,
    "faq": [
        {
            "question": "Konut kredisinde vergi kesintisi var mıdır?",
            "answer": "Hayır, Türkiye'de devletin konut alımını desteklemesi amacıyla konut kredilerinde BSMV (Banka ve Sigorta Muameleleri Vergisi) ve KKDF (Kaynak Kullanımını Destekleme Fonu) oranları %0 (Sıfır) olarak uygulanmaktadır."
        },
        {
            "question": "Konut kredisi en fazla kaç ay vade ile verilir?",
            "answer": "Bankaların politikalarına göre değişmekle birlikte genellikle en fazla 120 ay (10 Yıl) vade yapılmaktadır. Ancak bazı özel kampanyalarda 240 aya kadar vadeli konut kredileri de mevcuttur."
        }
    ]
}
