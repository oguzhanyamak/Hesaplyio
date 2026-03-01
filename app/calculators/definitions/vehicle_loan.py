from app.calculators.logic.vehicle_loan import calculate_vehicle_loan

VEHICLE_LOAN_CONFIG = {
    "id": "vehicle-loan",
    "slug": "tasit-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Taşıt Kredisi Hesaplama",
    "description": "0 km ve ikinci el araç kredisi taksit ve faiz maliyetlerini anında hesaplayın.",
    "seo": {
        "meta_title": "Taşıt Kredisi Hesaplama (Sıfır İkinci El Araç Kredisi) 2026",
        "meta_description": "Araç finansmanı için taşıt kredisi aylık taksit ödeme planını oluşturun. Ticari veya hususi binek.",
        "meta_keywords": ["kredi hesaplama", "taşıt kredisi", "kredi ödeme planı", "araba kredisi", "aylık taksit"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 800000",
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
            "placeholder": "Örnek: 48",
            "required": True,
            "min": 1,
            "max": 48,
            "tooltip": "Mevzuat gereği araç tutarına göre vade değişebilir"
        },
        {
            "name": "is_commercial",
            "type": "select",
            "label": "Müşteri Tipi",
            "options": [{"label": "Bireysel Müşteri", "value": "Bireysel"}, {"label": "Ticari / Şirket", "value": "Ticari"}],
            "default": "Bireysel",
            "tooltip": "Ticari kullandırımlarda vergiler çok daha düşüktür."
        }
    ],
    "logic_function": calculate_vehicle_loan,
    "faq": [
        {
            "question": "Taşıt kredilerinde vade en fazla kaç aydır?",
            "answer": "BDDK mevzuatına göre taşıt kredilerinde vade süreleri aracın fatura veya kasko değerine göre kısıtlanmaktadır. Örneğin 400.000 TL'ye kadar vadeler 48 ay iken, yüksek tutarlı araçlarda vade makası 12 aya kadar daralabilir."
        },
        {
            "question": "Bireysel ve Ticari taşıt kredisi farkı nedir?",
            "answer": "Bireysel taşıt kredisinde %15 KKDF ve %15 BSMV alınırken, ticarilerde genellikle KKDF alınmaz, BSMV ise indirimli uygulanarak maliyet çok ciddi şekilde düşürülür."
        }
    ]
}
