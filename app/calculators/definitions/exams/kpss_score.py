from app.calculators.logic.exams.kpss_score import calculate_kpss

EXAM_KPSS_CONFIG = {
    "id": "kpss-score",
    "slug": "kpss-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "KPSS Lisans P3 Puan Hesaplama",
    "description": "Genel Yetenek ve Genel Kültür netlerinizi (4 yanlış 1 boş) girerek Öğretmen Memur (Lisans P3) puanınızı tahmin edin.",
    "seo": {
        "meta_title": "KPSS Puan Hesaplama Modülü - 2026",
        "meta_description": "Memurluk sınavı KPSS Lisans P3 puanınızı Genel Yetenek (Matematik/Türkçe) ve Genel Kültür netlerinize göre hesaplayın.",
        "meta_keywords": ["kpss hesabı", "kpss p3", "lisans memur atama puan hesaplama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "gy_correct", "type": "number", "label": "GENEL YETENEK (Doğru)", "placeholder": "60", "default": 0, "min": 0, "max": 60
        },
        {
            "name": "gy_incorrect", "type": "number", "label": "GENEL YETENEK (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 60
        },
        {
            "name": "gk_correct", "type": "number", "label": "GENEL KÜLTÜR (Doğru)", "placeholder": "60", "default": 0, "min": 0, "max": 60
        },
        {
            "name": "gk_incorrect", "type": "number", "label": "GENEL KÜLTÜR (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 60
        }
    ],
    "logic_function": calculate_kpss,
    "faq": [
        {
            "question": "P3 Puanı nedir?",
            "answer": "P3 puan türü, kpss p3 puanı, lisans (üniversite) mezunlarının B grubu kadrolara atamalarında kullanılan puandır."
        }
    ]
}
