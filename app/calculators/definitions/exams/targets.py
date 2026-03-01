from app.calculators.definitions.exams.univ_target import calculate_target_nets

EXAM_DGS_TABAN_CONFIG = {
    "id": "dgs-target",
    "slug": "dgs-taban-puanlari-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "DGS Hedef Net Hesaplama",
    "description": "Geçiş yapmak istediğiniz lisans bölümünün taban puanı için kaç DGS neti yapmalısınız?",
    "seo": {
        "meta_title": "DGS Kaç Net Kaç Puan? | Hedef Hesaplama",
        "meta_description": "DGS'de hedeflediğiniz hukuk, mühendislik gibi bölümlere girmek için yapmanız gereken sayısal ve sözel net hesabı.",
        "meta_keywords": ["dgs taban puanlari", "dgs hedef puan", "dgs kaç net"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "target_score", "type": "number", "label": "Hedef DGS Puanı", "default": 300, "min": 100, "max": 450}
    ],
    "logic_function": calculate_target_nets,
    "faq": [
        {
            "question": "DGS'de katsayılar nasıldır?",
            "answer": "Sayısal ve sözel netler yaklaşık 3 puan getirirken, diploma notunuz (ÖBP) da sonuca eklenir."
        }
    ]
}

EXAM_LISE_TABAN_CONFIG = {
    "id": "lise-target",
    "slug": "lise-lgs-taban-puanlari-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "Lise (LGS) Hedef Net Hesaplama",
    "description": "Hedeflediğiniz lisenin (Fen, Anadolu vs) taban puanına ulaşmak için LGS'de çıkarmanız gereken netleri bulun.",
    "seo": {
        "meta_title": "LGS Hedef Puan Hesaplama 2026",
        "meta_description": "Hedeflediğiniz lise için gereken netler. 500 tam puan üzerinden hedef hesaplama motoru.",
        "meta_keywords": ["lise taban puanları", "lgs hedef", "kaç netle hangi lise"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "target_score", "type": "number", "label": "Hedef LGS Puanı", "default": 450, "min": 200, "max": 500}
    ],
    "logic_function": calculate_target_nets,
    "faq": [
        {
            "question": "LGS taban puanları neye göre değişir?",
            "answer": "Sınavın o yılki genel zorluğu ve öğrencilerin tercih eğilimlerine göre yüzdelik dilimler üzerinden belirlenir."
        }
    ]
}
