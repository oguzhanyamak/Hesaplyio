from app.calculators.logic.exams.kpss_score import calculate_kpss # EKPSS logic is similar to KPSS

EXAM_EKPSS_CONFIG = {
    "id": "ekpss-score",
    "slug": "ekpss-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "EKPSS Puan Hesaplama",
    "description": "Engelli Kamu Personeli Seçme Sınavı (EKPSS) netlerinize göre tahmini puanınızı hesaplayın.",
    "seo": {
        "meta_title": "EKPSS Puan Hesaplama 2026 | Güncel ÖSYM Katsayıları",
        "meta_description": "2026 EKPSS puanı hesaplama aracı. Genel Yetenek ve Genel Kültür netlerinizi girerek puanınızı öğrenin.",
        "meta_keywords": ["ekpss hesaplama", "ekpss puan", "engelli kpss hesapla"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "gy_correct", "type": "number", "label": "Genel Yetenek (Doğru)", "default": 0, "min": 0, "max": 30},
        {"name": "gy_incorrect", "type": "number", "label": "Genel Yetenek (Yanlış)", "default": 0, "min": 0, "max": 30},
        {"name": "gk_correct", "type": "number", "label": "Genel Kültür (Doğru)", "default": 0, "min": 0, "max": 30},
        {"name": "gk_incorrect", "type": "number", "label": "Genel Kültür (Yanlış)", "default": 0, "min": 0, "max": 30}
    ],
    "logic_function": calculate_kpss, # Refine if needed, EKPSS has 60 questions
    "faq": [
        {
            "question": "EKPSS'de 4 yanlış 1 doğruyu götürür mu?",
            "answer": "Evet, EKPSS sınavında da 4 yanlış 1 doğruyu götürmektedir."
        }
    ]
}
