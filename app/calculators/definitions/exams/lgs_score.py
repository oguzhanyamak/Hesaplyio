from app.calculators.logic.exams.lgs_score import calc_lgs

EXAM_LGS_CONFIG = {
    "id": "lgs-score",
    "slug": "lgs-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "LGS Puan Hesaplama",
    "description": "Milli Eğitim Bakanlığı (MEB) güncel katsayılarına göre Liselere Geçiş Sistemi (LGS) puanınızı hesaplayın.",
    "seo": {
        "meta_title": "LGS Puan Hesaplama 2026 | Güncel MEB Katsayıları",
        "meta_description": "2026 LGS puanı hesaplama aracı. Türkçe, Matematik, Fen, İnkılap, Din ve Yabancı Dil netlerinizle tahmini sınav puanınızı hesaplayın.",
        "meta_keywords": ["lgs hesaplama", "lgs puan", "meb lgs puan hesapla", "lgs katsayıları"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "tc_correct", "type": "number", "label": "Türkçe (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "tc_incorrect", "type": "number", "label": "Türkçe (Yanlış)", "default": 0, "min": 0, "max": 20},
        {"name": "mat_correct", "type": "number", "label": "Matematik (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "mat_incorrect", "type": "number", "label": "Matematik (Yanlış)", "default": 0, "min": 0, "max": 20},
        {"name": "fen_correct", "type": "number", "label": "Fen Bilimleri (Doğru)", "default": 0, "min": 0, "max": 20},
        {"name": "fen_incorrect", "type": "number", "label": "Fen Bilimleri (Yanlış)", "default": 0, "min": 0, "max": 20},
        {"name": "ink_correct", "type": "number", "label": "İnkılap Tarihi (Doğru)", "default": 0, "min": 0, "max": 10},
        {"name": "ink_incorrect", "type": "number", "label": "İnkılap Tarihi (Yanlış)", "default": 0, "min": 0, "max": 10},
        {"name": "din_correct", "type": "number", "label": "Din Kültürü (Doğru)", "default": 0, "min": 0, "max": 10},
        {"name": "din_incorrect", "type": "number", "label": "Din Kültürü (Yanlış)", "default": 0, "min": 0, "max": 10},
        {"name": "yab_correct", "type": "number", "label": "Yabancı Dil (Doğru)", "default": 0, "min": 0, "max": 10},
        {"name": "yab_incorrect", "type": "number", "label": "Yabancı Dil (Yanlış)", "default": 0, "min": 0, "max": 10}
    ],
    "logic_function": calc_lgs,
    "faq": [
        {
            "question": "LGS'de yanlışlar doğruları götürüyor mu?",
            "answer": "Evet, LGS'de 3 yanlış 1 doğruyu götürmektedir."
        },
        {
            "question": "Alt test katsayıları nedir?",
            "answer": "LGS'de Türkçe, Matematik ve Fen Bilimleri testlerinin katsayısı 4; T.C. İnkılap Tarihi ve Atatürkçülük, Din Kültürü ve Ahlak Bilgisi ile Yabancı Dil testlerinin katsayısı 1'dir."
        }
    ]
}
