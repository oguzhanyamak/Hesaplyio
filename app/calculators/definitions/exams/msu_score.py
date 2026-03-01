from app.calculators.logic.exams.tyt_score import calculate_yks_tyt # MSÜ uses TYT structure

EXAM_MSU_CONFIG = {
    "id": "msu-score",
    "slug": "msu-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "MSÜ Puan Hesaplama",
    "description": "Milli Savunma Üniversitesi (MSÜ) sınavı netlerinize göre tahmini puanınızı hesaplayın.",
    "seo": {
        "meta_title": "MSÜ Puan Hesaplama 2026 | Güncel ÖSYM Katsayıları",
        "meta_description": "2026 MSÜ puanı hesaplama aracı. Netlerinizi girerek MSÜ Sayısal, Sözel ve Eşit Ağırlık puanlarınızı öğrenin.",
        "meta_keywords": ["msü hesaplama", "msü puan", "msü net hesapla"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "tr_correct", "type": "number", "label": "Türkçe (Doğru)", "default": 0, "min": 0, "max": 40},
        {"name": "tr_incorrect", "type": "number", "label": "Türkçe (Yanlış)", "default": 0, "min": 0, "max": 40},
        {"name": "math_correct", "type": "number", "label": "Matematik (Doğru)", "default": 0, "min": 0, "max": 40},
        {"name": "math_incorrect", "type": "number", "label": "Matematik (Yanlış)", "default": 0, "min": 0, "max": 40},
        {"name": "soc_correct", "type": "number", "label": "Sosyal Bilimler (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "soc_incorrect", "type": "number", "label": "Sosyal Bilimler (Yanlış)", "default": 0, "min": 0, "max": 20},
        {"name": "sci_correct", "type": "number", "label": "Fen Bilimleri (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "sci_incorrect", "type": "number", "label": "Fen Bilimleri (Yanlış)", "default": 0, "min": 0, "max": 20}
    ],
    "logic_function": calculate_yks_tyt, # MSÜ uses similar logic, can be refined if exact weights differ
    "faq": [
        {
            "question": "MSÜ sınavında 4 yanlış 1 doğruyu götürür mü?",
            "answer": "Evet, MSÜ sınavında da 4 yanlış 1 doğruyu götürmektedir."
        }
    ]
}
