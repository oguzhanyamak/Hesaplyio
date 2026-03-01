from app.calculators.logic.exams.tyt_score import calculate_yks_tyt

EXAM_POMEM_CONFIG = {
    "id": "pomem-score",
    "slug": "pomem-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "POMEM / PMYO Puan Hesaplama",
    "description": "Polis Meslek Eğitim Merkezi (POMEM) ve PMYO giriş puanınızı TYT netlerinize göre hesaplayın.",
    "seo": {
        "meta_title": "POMEM Puan Hesaplama 2026 | Polislik Sınav Puanı",
        "meta_description": "2026 POMEM ve PMYO puanı hesaplama aracı. TYT puanı üzerine mülakat ve fiziki parkur katkısını simüle edin.",
        "meta_keywords": ["pomem hesaplama", "pmyo puanı", "polislik puan hesapla"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "tr_correct", "type": "number", "label": "TYT Türkçe (Doğru)", "default": 0, "min": 0, "max": 40},
        {"name": "math_correct", "type": "number", "label": "TYT Matematik (Doğru)", "default": 0, "min": 0, "max": 40},
        {"name": "soc_correct", "type": "number", "label": "TYT Sosyal (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "sci_correct", "type": "number", "label": "TYT Fen (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "diploma", "type": "number", "step": "0.01", "label": "Diploma Notu", "default": 70, "min": 50, "max": 100}
    ],
    "logic_function": calculate_yks_tyt,
    "faq": [
        {
            "question": "PMYO için baraj puanı kaçtır?",
            "answer": "PMYO girişleri için genellikle TYT'den ham puan olarak 250 ve üzeri almak gerekmektedir (Yıla göre değişebilir)."
        }
    ]
}
