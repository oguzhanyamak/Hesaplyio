from app.calculators.logic.math.util import calculate_random, calculate_number_to_words

RANDOM_CONFIG = {
    "id": "random_num", "slug": "rastgele-sayi-hesaplama", "category": "Matematik", "title": "Rastgele Sayı Üretici",
    "description": "İstenen aralıkta tamamen rastgele tamsayılar üretin.",
    "seo": {
        "meta_title": "Rastgele Sayı Üretici | Online Random Number Generator",
        "meta_description": "Belirlediğiniz aralıkta rastgele sayılar üreten ücretsiz online araç.",
        "meta_keywords": ["rastgele sayı", "random sayı üret"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_random,
    "inputs": [
        {"name": "min_val", "type": "number", "label": "Alt Sınır", "default": 1},
        {"name": "max_val", "type": "number", "label": "Üst Sınır", "default": 100},
        {"name": "count", "type": "number", "label": "Üretilecek Adet", "default": 1}
    ],
    "faq": [
        {"question": "Sayılar gerçekten rastgele mi?", "answer": "Evet, Python'un güvenli rastgele sayı üreticisi kullanılmaktadır."}
    ]
}

WORDS_CONFIG = {
    "id": "num_to_words", "slug": "sayi-okunusu-hesaplama", "category": "Matematik", "title": "Sayı Okunuşu",
    "description": "Rakamla yazılan bir sayının yazı ile okunuşunu anında öğrenin.",
    "seo": {
        "meta_title": "Sayıyı Yazıya Çevirme | Sayı Okunuşu Hesapla",
        "meta_description": "Rakamla girilen sayıların Türkçe okunuşunu ve yazı ile yazılışını gösteren araç.",
        "meta_keywords": ["sayı okunuşu", "rakamı yazıya çevir"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_number_to_words,
    "inputs": [
        {"name": "n", "type": "number", "label": "Sayı", "required": True}
    ],
    "faq": [
        {"question": "Kaç basamağa kadar destekliyor?", "answer": "Şu an için 1 trilyon (12 basamak) sınırına kadar destek sunmaktadır."}
    ]
}
