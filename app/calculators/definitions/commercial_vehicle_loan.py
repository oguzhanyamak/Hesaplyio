from app.calculators.logic.vehicle_loan import calculate_vehicle_loan

COMMERCIAL_VEHICLE_LOAN_CONFIG = {
    "id": "commercial-vehicle",
    "slug": "ticari-arac-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Ticari Araç Kredisi Hesaplama",
    "description": "Şirketiniz için alacağınız hafif ve ağır ticari araçların %0 KKDF imkanıyla kredi maliyetini hesaplayın.",
    "seo": {
        "meta_title": "Ticari Araç ve Kamyon Kredisi Hesaplama",
        "meta_description": "Esnaf ve KOBİ'ler için avantajlı BSMV/KKDF oranlarıyla 2. el ve sıfır ticari taşıt kredisi tahmini. Aylık ödeme planı çıkar.",
        "meta_keywords": ["ticari araç kredisi hesaplama", "kamyon kredisi", "şirket aracı kredisi", "minibüs kredisi"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Araç Kredisi Tutarı (₺)",
            "placeholder": "Örnek: 1200000",
            "required": True,
            "min": 50000
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Banka Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 2.75",
            "required": True,
            "min": 0
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 48",
            "required": True,
            "min": 1,
            "max": 60
        },
        {
            "name": "is_commercial",
            "type": "hidden",
            "default": "Ticari" # Forces vehicle logic to use Commercial tax logic
        }
    ],
    "logic_function": calculate_vehicle_loan,
    "faq": [
        {
            "question": "Ticari araç kredilerinde vade ve vergi farkı nedir?",
            "answer": "Bireysel otomobil kredilerinde araç değerine göre vade 12 aya kadar düşebilirken ve %15 KKDF alınırken; ticari amaçlı kullanım (TIR, Kamyon, Ticari Minibüs) kredilerinde vade daha uzundur ve %0 KKDF ve indirimli %5 BSMV alınarak faiz maliyeti ciddi şekilde düşürülür."
        }
    ]
}
