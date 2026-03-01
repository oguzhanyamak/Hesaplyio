from app.calculators.logic.exams.lgs_score import calc_lgs

EXAM_PYBS_CONFIG = {
    "id": "pybs-score",
    "slug": "pybs-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "PYBS / Bursluluk Sınavı Puan Hesaplama",
    "description": "İlköğretim ve Ortaöğretim Kurumları Bursluluk Sınavı (İOKBS) puanınızı hesaplayın.",
    "seo": {
        "meta_title": "PYBS (Bursluluk) Puan Hesaplama 2026",
        "meta_description": "2026 İOKBS Bursluluk sınavı puan hesaplama motoru. 5, 6, 7, 8, 9, 10 ve 11. sınıflar için bursluluk puanı.",
        "meta_keywords": ["bursluluk hesaplama", "pybs puan", "iokbs puanı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "tc_correct", "type": "number", "label": "Türkçe (Doğru)", "default": 0, "min": 0, "max": 25},
        {"name": "mat_correct", "type": "number", "label": "Matematik (Doğru)", "default": 0, "min": 0, "max": 25},
        {"name": "fen_correct", "type": "number", "label": "Fen Bilimleri (Doğru)", "default": 0, "min": 0, "max": 25},
        {"name": "soc_correct", "type": "number", "label": "Sosyal Bilimler (Doğru)", "default": 0, "min": 0, "max": 25}
    ],
    "logic_function": calc_lgs, # Similar 4 subject structure
    "faq": [
        {
            "question": "Bursluluk sınavında kaç puanla kazanılır?",
            "answer": "Kazanma puanı yıla, sınıfa ve kontenjan türüne göre 440 ile 480 puan arasında değişebilmektedir."
        }
    ]
}
