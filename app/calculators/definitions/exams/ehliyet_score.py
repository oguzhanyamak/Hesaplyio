from app.calculators.logic.exams.simple_exam import calculate_simple_exam

def calc_ehliyet(correct: int|str=0, incorrect: int|str=0):
    return calculate_simple_exam(c=correct, i=incorrect, total_q=50, correct_coeff=2.0, penalize=False)

EXAM_EHLIYET_CONFIG = {
    "id": "ehliyet-score",
    "slug": "ehliyet-sinavi-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "Ehliyet Sınavı Puan Hesaplama",
    "description": "Ehliyet sınavı (E-Sınav) doğru sayılarınıza göre puanınızı hesaplayın.",
    "seo": {
        "meta_title": "Ehliyet Sınavı Puan Hesaplama 2026",
        "meta_description": "2026 ehliyet sınavı puan hesaplama aracı. Kaç doğruyla geçeceğinizi öğrenin. Her soru 2 puandır.",
        "meta_keywords": ["ehliyet puanı", "ehliyet hesaplama", "direksiyon sınavı puanı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "correct", "type": "number", "label": "Doğru Sayısı", "default": 0, "min": 0, "max": 50
        }
    ],
    "logic_function": calc_ehliyet,
    "faq": [
        {
            "question": "Ehliyet sınavında yanlışlar doğruları götürür mü?",
            "answer": "Hayır, ehliyet sınavında yanlışlar doğruları götürmez."
        },
        {
            "question": "Ehliyet sınavından geçmek için kaç puan almak gerekir?",
            "answer": "Sınavdan başarılı sayılmak için en az 70 puan almanız gerekmektedir (35 Doğru)."
        }
    ]
}
