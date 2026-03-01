from app.calculators.logic.exams.simple_exam import calculate_simple_exam

def calc_ags(correct: int|str=0):
    return calculate_simple_exam(c=correct, i=0, total_q=100, correct_coeff=1.0, penalize=False)

EXAM_AGS_CONFIG = {
    "id": "ags-score",
    "slug": "ags-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "AGS Puan Hesaplama",
    "description": "Akademik ve diğer mesleki Gelişim Sınavları için puanınızı hesaplayın.",
    "seo": {
        "meta_title": "AGS Puan Hesaplama 2026",
        "meta_description": "2026 AGS sınavı puan hesaplama motoru.",
        "meta_keywords": ["ags puanı", "ags hesaplama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "correct", "type": "number", "label": "Doğru Sayısı", "default": 0, "min": 0, "max": 100}
    ],
    "logic_function": calc_ags,
    "faq": [
        {
            "question": "AGS sınavında yanlış doğruyu götürür mü?",
            "answer": "Sınav türüne göre değişmekle birlikte genellikle 100 soru üzerinden değerlendirme yapılır."
        }
    ]
}
