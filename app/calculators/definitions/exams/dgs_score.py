from app.calculators.logic.exams.dgs_score import calc_dgs

EXAM_DGS_CONFIG = {
    "id": "dgs-score",
    "slug": "dgs-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "DGS Puan Hesaplama",
    "description": "Ön lisanstan Lisansa Geçiş Sınavı (DGS) netleri ve ÖBP (Diploma Puanı) baz alınarak güncel yerleştirme katsayılarıyla puan hesabı.",
    "seo": {
        "meta_title": "DGS Puan Hesaplama Modülü - 50 Say / 50 Söz (+ÖBP)",
        "meta_description": "2026 Dikey Geçiş Sınavı puanı hesaplama. Diploma notunun (ÖBP) sisteme dahil edildiği Sayısal ve Sözel net hesaplama motoru.",
        "meta_keywords": ["dgs önlisans", "dgs puan hesapla", "dgs standart sapma", "dgs yerleştirme puanı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "say_c", "type": "number", "label": "Sayısal (Doğru)", "placeholder": "50", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "say_i", "type": "number", "label": "Sayısal (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "soz_c", "type": "number", "label": "Sözel (Doğru)", "placeholder": "50", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "soz_i", "type": "number", "label": "Sözel (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "diploma", "type": "number", "step": "0.01", "label": "Ön Lisans Diploma Notu", "placeholder": "50-100", "default": 75, "min": 50, "max": 100
        }
    ],
    "logic_function": calc_dgs,
    "faq": [
        {
            "question": "DGS Puanı nasıl hesaplanıyor?",
            "answer": "Adayın testlerden aldığı 1 net 3 katsayıyla çarpılır (+100 temel taban) ve bu ham puana Ön Lisans Başarı Puanı (ÖBP - diploma x 0.8) eklenir."
        }
    ]
}
