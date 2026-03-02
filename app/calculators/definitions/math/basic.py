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
        {"question": "Matematiksel olarak yüzde hesaplama mantığı nedir?", "answer": "Bir sayının (A) belirlenen oranda (B) yüzdesini bulmak için (A * B) / 100 formülü kullanılır. Örneğin 200'ün yüzde 20'si: (200 * 20) / 100 = 40 eder."},
        {"question": "Yüzde artış ve azalış nasıl hesaplanır?", "answer": "Artış için sayı (1 + Oran/100) ile, azalış için sayı (1 - Oran/100) ile çarpılır. Maaş zamları veya indirim hesaplarında bu yöntem kullanılır."},
        {"question": "A sayısı B sayısının yüzde kaçıdır nasıl bulunur?", "answer": "Bu işlemi yapmak için A sayısı B'ye bölünür ve sonuç 100 ile çarpılır. Formül: (A / B) * 100."},
        {"question": "KDV dahil ve KDV hariç hesaplamaları için yüzde aracı kullanılır mı?", "answer": "Evet, KDV dâhil fiyatı bulmak için '% Kadar Ekle' işlemini, KDV hariç fiyatı bulmak için ise orantı kurarak '% azalış' mantığını kullanabilirsiniz."}
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
        {"question": "Üslü sayılarda taban ve üs nedir?", "answer": "Taban, çarpılacak olan sayıdır; üs (kuvvet) ise tabanın kendisiyle kaç kere çarpılacağını ifade eder. Örneğin 2^3 işleminde 2 taban, 3 üstür."},
        {"question": "Üslü sayıların günlük hayatta kullanımı nedir?", "answer": "Nüfus artışı, bileşik faiz hesaplamaları, deprem büyüklüğü (Richter ölçeği) ve bilgisayar veri birimlerinde (MB, GB) üslü sayılar kullanılır."},
        {"question": "Negatif sayıların üssü nasıl hesaplanır?", "answer": "Negatif bir sayının çift kuvveti pozitif, tek kuvveti ise negatiftir. Örneğin (-2)^2 = 4, (-2)^3 = -8 eder."}
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
        {"question": "Karekök dışına çıkarma işlemi nasıl yapılır?", "answer": "Bir sayı, kendisiyle çarpıldığında kök içindeki sayıyı veren 'X' sayısını bulma işlemidir. Örneğin 25'in karekökü 5'tir çünkü 5*5=25'tir."},
        {"question": "Küp kök ve dördüncü derece kök ne anlama gelir?", "answer": "Küp kök, bir sayının 3. dereceden köküdür; yani hangi sayının küpü (X*X*X) bu sayıya eşittir sorusunun cevabıdır. Dördüncü derecede ise bir sayı 4 kere çarpılır."},
        {"question": "Negatif sayıların kökü alınabilir mi?", "answer": "Reel sayılar kümesinde negatif sayıların çift dereceden (karekök gibi) kökü alınamaz; ancak tek dereceden (küp kök gibi) kökü alınabilir."}
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
        {"question": "Faktöriyel nerede kullanılır?", "answer": "Olasılık, kombinasyon ve permütasyon hesaplamalarında nesnelerin farklı dizilimlerini bulmak için faktöriyelden yararlanılır."},
        {"question": "1000! (faktöriyel) neden çok büyük bir sayıdır?", "answer": "Faktöriyel değerleri üstel olarak değil, çok daha hızlı (faktöriyel hızında) büyür. 1000! sayısı evrendeki atom sayısından daha fazla basamağa sahiptir."},
        {"question": "Gama fonksiyonu ve faktöriyel ilişkisi nedir?", "answer": "Faktöriyel sadece tam sayılar için tanımlıyken, Gama fonksiyonu faktöriyel kavramını ondalıklı ve karmaşık sayılara genişleten matematiksel bir fonksiyondur."}
    ]
}
