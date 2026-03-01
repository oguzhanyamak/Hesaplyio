from app.calculators.logic.workplace_loan import calculate_workplace_loan

WORKPLACE_LOAN_CONFIG = {
    "id": "workplace-loan",
    "slug": "is-yeri-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "İş Yeri Kredisi Hesaplama",
    "description": "Dükkan, ofis ve ticari mülk alımlarınızda KKDF muafiyetine sahip avantajlı mortgage taksitlerini hesaplayın.",
    "seo": {
        "meta_title": "İş Yeri ve Ticari Gayrimenkul Kredisi Hesaplama 2026",
        "meta_description": "Esnaf ve yatırımcılar için dükkan/ofis alımında kullanılan iş yeri kredisini hesaplama motoru. KKDF muafiyeti ile ticari mortgage faizini görün.",
        "meta_keywords": ["iş yeri kredisi", "dükkan kredisi", "ofis kredisi", "ticari emlak kredi hesaplama", "mortgage hesaplama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Ticari Emlak Kredisi Tutarı (₺)",
            "placeholder": "Örnek: 5000000",
            "required": True,
            "min": 100000, 
            "tooltip": "Ekspertiz değerine göre çekebileceğiniz yasal limiti giriniz."
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Banka Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 2.95",
            "required": True,
            "min": 0
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 120",
            "required": True,
            "min": 12,
            "max": 144
        }
    ],
    "logic_function": calculate_workplace_loan,
    "faq": [
        {
            "question": "İş yeri (dükkan) kredisi işlemlerinde vergi ödenir mi?",
            "answer": "Bireysel konut kredilerinde %0 olan vergiler, ticari iş yeri kredilerinde farklılık gösterir. Kaynak Kullanımı Destekleme Fonu (KKDF) %0 olarak kesilmezken, Banka Sigorta Muameleleri Vergisi (BSMV) %5 olarak uygulanır."
        }
    ]
}
