from app.calculators.logic.math.number_theory import calculate_gcd_lcm, calculate_prime_factors
from app.calculators.logic.math.discrete_stats import calculate_stats, calculate_perm_comb, calculate_base_conversion

EBOB_EKOK_CONFIG = {
    "id": "ebob-ekok", "slug": "ebob-ekok-hesaplama", "category": "Matematik", "title": "EBOB EKOK Hesaplama",
    "description": "İki sayının en büyük ortak bölenini ve en küçük ortak katını bulun.",
    "seo": {
        "meta_title": "EBOB EKOK Hesaplama | En Büyük Ortak Bölen",
        "meta_description": "Online EBOB ve EKOK hesaplama aracı. Girilen iki sayının bölenlerini ve katlarını bulun.",
        "meta_keywords": ["ebob hesapla", "ekok bul"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_gcd_lcm,
    "inputs": [
        {"name": "a", "type": "number", "label": "1. Sayı", "required": True},
        {"name": "b", "type": "number", "label": "2. Sayı", "required": True}
    ],
    "faq": [
        {"question": "EBOB nedir?", "answer": "Sayıların her ikisini de bölen sayıların en büyüğüne EBOB denir."}
    ]
}

ASAL_CARPAN_CONFIG = {
    "id": "asal-carpan", "slug": "asal-carpan-hesaplama", "category": "Matematik", "title": "Asal Çarpan Hesaplama",
    "description": "Bir sayının asal çarpanlarını ve üslü gösterimini bulun.",
    "seo": {
        "meta_title": "Asal Çarpanlara Ayırma | Matematik Hesaplayıcı",
        "meta_description": "Bir sayıyı asal çarpanlarına ayırın ve üslü ifade olarak sonucunu görün.",
        "meta_keywords": ["asal çarpan", "sayıyı çarpanlara ayırma"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_prime_factors,
    "inputs": [
        {"name": "n", "type": "number", "label": "Sayı", "required": True, "min": 2}
    ],
    "faq": [
        {"question": "Asal sayı nedir?", "answer": "Yalnızca 1'e ve kendisine bölünebilen 1'den büyük sayılara asal sayı denir."}
    ]
}

STATS_CONFIG = {
    "id": "stats", "slug": "standart-sapma-hesaplama", "category": "Matematik", "title": "Standart Sapma Hesaplama",
    "description": "Veri setinizin standart sapma, varyans ve ortalama değerlerini hesaplayın.",
    "seo": {
        "meta_title": "Standart Sapma Hesaplama | Ortalama ve Varyans",
        "meta_description": "İstatistiksel veri setleri için standart sapma ve varyans hesaplama motoru.",
        "meta_keywords": ["standart sapma", "varyans hesapla"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_stats,
    "inputs": [
        {"name": "numbers_str", "type": "text", "label": "Sayı Listesi (Virgül veya boşlukla ayırın)", "placeholder": "10, 20, 30, 45", "required": True}
    ],
    "faq": [
        {"question": "Standart sapma neyi ölçer?", "answer": "Verilerin aritmetik ortalamadan ne kadar uzaklaştığını (dağılımını) ölçer."}
    ]
}

PERM_COMB_CONFIG = {
    "id": "perm-comb", "slug": "kombinasyon-hesaplama", "category": "Matematik", "title": "Kombinasyon ve Permütasyon",
    "description": "n'in r'li kombinasyon (seçim) ve permütasyon (sıralama) değerlerini bulun.",
    "seo": {
        "meta_title": "Kombinasyon ve Permütasyon Hesapla | n, r Seçimi",
        "meta_description": "Olasılık ve istatistik hesaplamaları için kombinasyon (C) ve permütasyon (P) motoru.",
        "meta_keywords": ["kombinasyon", "permütasyon"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_perm_comb,
    "inputs": [
        {"name": "n", "type": "number", "label": "n değeri (Toplam)", "required": True},
        {"name": "r", "type": "number", "label": "r değeri (Seçilen)", "required": True},
        {"name": "mode", "type": "select", "label": "İşlem Türü", "options": [
            {"label": "Kombinasyon (Seçim)", "value": "combination"},
            {"label": "Permütasyon (Sıralama)", "value": "permutation"}
        ], "default": "combination"}
    ],
    "faq": [
        {"question": "Sıralama önemli mi?", "answer": "Kombinasyonda (C) sıralama önemli değildir, permütasyonda (P) ise elemanların diziliş sırası hesaba katılır."}
    ]
}

BASE_CONV_CONFIG = {
    "id": "base-conv", "slug": "taban-donusumu-hesaplama", "category": "Matematik", "title": "Taban Dönüşümü Hesaplama",
    "description": "Sayıları farklı sayı sistemleri (2'lik, 8'lik, 10'luk, 16'lık vb.) arasında dönüştürün.",
    "seo": {
        "meta_title": "Sayı Tabanı Dönüştürme | 10'luk, 2'lik, 16'lık",
        "meta_description": "Onaltılık, Onluk, Sekizlik ve İkilik sayı tabanları arasında hızlı dönüşüm aracı.",
        "meta_keywords": ["taban dönüşümü", "binary çevirme", "hexadecimal"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_base_conversion,
    "inputs": [
        {"name": "num_str", "type": "text", "label": "Sayı", "required": True},
        {"name": "from_base", "type": "number", "label": "Hangi Tabandan?", "default": 10},
        {"name": "to_base", "type": "number", "label": "Hangi Tabana?", "default": 2}
    ],
    "faq": [
        {"question": "Binary nedir?", "answer": "Bilgisayar sistemlerinde kullanılan 2 tabanındaki sayı sistemidir (0 ve 1)."}
    ]
}
