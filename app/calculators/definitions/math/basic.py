from app.calculators.logic.math.basic_ops import calculate_percentage, calculate_power, calculate_root, calculate_factorial

YUZDE_CONFIG = {
    "id": "yuzde", "slug": "yuzde-hesaplama", "category": "Matematik", "title": "Yüzde Hesaplama",
    "description": "Her türlü yüzde artış, azalış ve oran hesaplamalarını anında yapın.",
    "seo": {
        "meta_title": "Yüzde Hesaplama 2026 | Pratik Yüzde Hesaplama Motoru",
        "meta_description": "2026 yüzde hesaplama aracı. % artış, % azalış ve bir sayının yüzdesini kolayca hesaplayın.",
        "meta_keywords": ["yüzde hesapla", "yüzde kaçı", "yüzde artış hesaplama"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_percentage,
    "inputs": [
        {"name": "val", "type": "number", "label": "Sayı", "required": True},
        {"name": "pct", "type": "number", "label": "Yüzde Oranı (%)", "required": True},
        {"name": "operation", "type": "select", "label": "İşlem", "options": [
            {"label": "% Değerini Hesapla", "value": "calculate"},
            {"label": "% Kadar Ekle", "value": "add"},
            {"label": "% Kadar Çıkar", "value": "subtract"},
            {"label": "A, B'nin yüzde kaçıdır?", "value": "change"}
        ], "default": "calculate"}
    ],
    "faq": [
        {"question": "Yüzde hesaplama nasıl yapılır?", "answer": "Bir sayının yüzdesini bulmak için o sayıyı yüzde oranı ile çarpıp yüze bölmeniz yeterlidir."},
        {"question": "Yüzde artış formülü nedir?", "answer": "Anapara * (1 + (Oran/100)) formülüyle artış tutarı hesaplanır."}
    ]
}

USLU_CONFIG = {
    "id": "uslu", "slug": "uslu-sayi-hesaplama", "category": "Matematik", "title": "Üslü Sayı Hesaplama",
    "description": "Bir sayının kuvvetini (ünsünü) hızlıca hesaplayın.",
    "seo": {
        "meta_title": "Üslü Sayı Hesaplama | Sayıların Kuvvetini Bul",
        "meta_description": "Herhangi bir sayının üssünü (kuvvetini) hesaplayan online araç.",
        "meta_keywords": ["üslü sayılar", "kuvvet hesaplama", "taban üs"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_power,
    "inputs": [
        {"name": "base", "type": "number", "label": "Taban", "required": True},
        {"name": "exponent", "type": "number", "label": "Üs (Kuvvet)", "required": True}
    ],
    "faq": [
        {"question": "Sıfırıncı kuvvet kaçtır?", "answer": "Sıfır hariç tüm sayıların sıfırıncı kuvveti 1'dir."}
    ]
}

KOKLU_CONFIG = {
    "id": "koklu", "slug": "koklu-sayi-hesaplama", "category": "Matematik", "title": "Köklü Sayı Hesaplama",
    "description": "Karekök, küp kök veya herhangi bir dereceden kök hesaplayın.",
    "seo": {
        "meta_title": "Köklü Sayı Hesaplama | Karekök ve Küp Kök",
        "meta_description": "Online köklü sayı hesaplama motoru. Tüm derecelerden kök alma.",
        "meta_keywords": ["karekök hesapla", "küp kök", "kök derecesi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_root,
    "inputs": [
        {"name": "val", "type": "number", "label": "Sayı", "required": True},
        {"name": "degree", "type": "number", "label": "Kök Derecesi", "default": 2}
    ],
    "faq": [
        {"question": "Karekök nedir?", "answer": "Bir sayının ikinci dereceden köküne karekök denir."}
    ]
}

FAKTORIYEL_CONFIG = {
    "id": "faktoryel", "slug": "faktoryel-hesaplama", "category": "Matematik", "title": "Faktöriyel Hesaplama",
    "description": "Bir sayının faktöriyelini (n!) tek tıkla bulun.",
    "seo": {
        "meta_title": "Faktöriyel Hesapla (n!) | Online Matematik Araçları",
        "meta_description": "0-1000 arası sayıların faktöriyelini anında hesaplayan online araç.",
        "meta_keywords": ["faktöriyel", "n faktöriyel", "matematik araçları"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_factorial,
    "inputs": [
        {"name": "n", "type": "number", "label": "Sayı (n)", "required": True, "min": 0, "max": 1000}
    ],
    "faq": [
        {"question": "0 faktöriyel neden 1'dir?", "answer": "Matematiksel tanım gereği ve kombinasyon hesaplarının tutarlı olması için 0! = 1 kabul edilir."}
    ]
}
