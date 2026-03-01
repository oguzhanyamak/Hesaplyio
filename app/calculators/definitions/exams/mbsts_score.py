from app.calculators.logic.exams.simple_exam import calculate_simple_exam

def calc_mbsts(correct: int|str=0, incorrect: int|str=0):
    return calculate_simple_exam(c=correct, i=incorrect, total_q=60, correct_coeff=1.66, penalize=True)

EXAM_MBSTS_CONFIG = {
    "id": "mbsts-score",
    "slug": "dib-mbsts-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "DİB MBSTS Puan Hesaplama",
    "description": "Diyanet İşleri Başkanlığı Mesleki Bilgiler Seviye Tespit Sınavı puanınızı hesaplayın.",
    "seo": {
        "meta_title": "DİB MBSTS Puan Hesaplama 2026",
        "meta_description": "2026 MBSTS puan hesaplama motoru. Diyanet personeli için seviye tespit sınavı puanı.",
        "meta_keywords": ["mbsts puanı", "mbsts hesaplama", "diyanet sınavı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "correct", "type": "number", "label": "Doğru Sayısı", "default": 0, "min": 0, "max": 60},
        {"name": "incorrect", "type": "number", "label": "Yanlış Sayısı", "default": 0, "min": 0, "max": 60}
    ],
    "logic_function": calc_mbsts,
    "faq": [
        {
            "question": "MBSTS'de yanlış doğruyu götürür mü?",
            "answer": "Evet, MBSTS sınavında 4 yanlış 1 doğruyu götürmektedir."
        }
    ]
}
