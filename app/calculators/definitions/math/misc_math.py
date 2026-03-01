from app.calculators.logic.math.miscellaneous import calculate_interest_math, calculate_conversions, calculate_golden_ratio, calculate_modulo

FAIZ_CONFIG = {
    "id": "faiz", "slug": "faiz-hesaplama", "category": "Matematik", "title": "Banka ve Mevduat Faizi",
    "description": "Basit veya bileşik faiz getirisi üzerinden anapara ve kâr hesabı yapın.",
    "seo": {
        "meta_title": "Faiz Hesaplama | Basit ve Bileşik Faiz Getirisi",
        "meta_description": "Online faiz hesaplama aracı. Mevduat ve kredi faizlerini basit veya bileşik olarak hesaplayın.",
        "meta_keywords": ["faiz hesapla", "bileşik faiz", "mevduat faizi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_interest_math,
    "inputs": [
        {"name": "principal", "type": "number", "label": "Anapara", "required": True},
        {"name": "rate", "type": "number", "label": "Yıllık Faiz Oranı (%)", "required": True},
        {"name": "time", "type": "number", "label": "Vade (Yıl)", "required": True},
        {"name": "mode", "type": "select", "label": "Faiz Türü", "options": [
            {"label": "Basit Faiz", "value": "simple"},
            {"label": "Bileşik Faiz", "value": "compound"}
        ], "default": "simple"}
    ],
    "faq": [
        {"question": "Bileşik faiz nedir?", "answer": "Faiz tutarının anaparaya eklenerek bir sonraki dönemde faiz üzerinden tekrar faiz hesaplanmasıdır."}
    ]
}

CONV_CONFIG = {
    "id": "conv", "slug": "inc-mil-hesaplama", "category": "Matematik", "title": "Birim Dönüşümü",
    "description": "İnç, mil, santimetre gibi farklı ölçü birimleri arası hızlı geçiş yapın.",
    "seo": {
        "meta_title": "Birim Dönüştürücü | İnç, Mil, CM ve KM",
        "meta_description": "Uzunluk ve alan birimleri arası online dönüşüm aracı. İnçten santimetreye, milden kilometreye çevrim.",
        "meta_keywords": ["inç cm çevir", "mil km hesapla"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_conversions,
    "inputs": [
        {"name": "val", "type": "number", "label": "Değer", "required": True},
        {"name": "unit_from", "type": "select", "label": "Hangi Birimden?", "options": [
            {"label": "İnç", "value": "inch"},
            {"label": "Santimetre", "value": "cm"},
            {"label": "Mil", "value": "mile"},
            {"label": "Kilometre", "value": "km"},
            {"label": "Metrekare", "value": "sqm"}
        ], "default": "inch"},
        {"name": "unit_to", "type": "select", "label": "Hangi Birime?", "options": [
            {"label": "Santimetre", "value": "cm"},
            {"label": "İnç", "value": "inch"},
            {"label": "Kilometre", "value": "km"},
            {"label": "Mil", "value": "mile"},
            {"label": "Metrekare (sqft)", "value": "sqft"}
        ], "default": "cm"}
    ],
    "faq": [
        {"question": "1 inç kaç santimetredir?", "answer": "1 inç tam olarak 2,54 santimetredir."}
    ]
}

GOLDEN_CONFIG = {
    "id": "golden", "slug": "altin-oran-hesaplama", "category": "Matematik", "title": "Altın Oran Hesaplama",
    "description": "Bir sayının altın oran karşılığını (büyük veya küçük parça) anında görün.",
    "seo": {
        "meta_title": "Altın Oran Hesaplama | Phi (1.618) Formülü",
        "meta_description": "Matematiksel altın oran hesaplayıcı. Bir değerin Phi oranına göre büyük ve küçük parçalarını bulun.",
        "meta_keywords": ["altın oran", "phi hesapla"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_golden_ratio,
    "inputs": [
        {"name": "val", "type": "number", "label": "Değer", "required": True},
        {"name": "find", "type": "select", "label": "Hedef", "options": [
            {"label": "Daha Büyük Parçayı Bul", "value": "larger"},
            {"label": "Daha Küçük Parçayı Bul", "value": "smaller"}
        ], "default": "larger"}
    ],
    "faq": [
        {"question": "Altın oran değeri kaçtır?", "answer": "Altın oran (Phi) yaklaşık olarak 1,618'dir."}
    ]
}

MODULO_CONFIG = {
    "id": "modulo", "slug": "moduler-aritmetik-hesaplama", "category": "Matematik", "title": "Modüler Aritmetik",
    "description": "A'nın B'den kalanını (Mod) anında bulun.",
    "seo": {
        "meta_title": "Modüler Aritmetik Hesaplama | Mod Alma",
        "meta_description": "Online mod hesaplayıcı. Bir sayının diğer bir sayıya bölümünden kalanı bulun.",
        "meta_keywords": ["mod hesapla", "kalanı bulma"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_modulo,
    "inputs": [
        {"name": "a", "type": "number", "label": "Sayı A", "required": True},
        {"name": "b", "type": "number", "label": "Sayı B", "required": True}
    ],
    "faq": [
        {"question": "Mod işlemi ne işe yarar?", "answer": "Bölme işlemindeki tam sayıyla bölünemeyen artan kısmı (kalanı) bulmaya yarar."}
    ]
}
