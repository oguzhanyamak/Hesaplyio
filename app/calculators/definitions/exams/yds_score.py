from app.calculators.logic.exams.simple_exam import calculate_simple_exam

# Wrapper for YDS
def calc_yds(correct: int|str=0, incorrect: int|str=0):
    return calculate_simple_exam(c=correct, i=incorrect, total_q=80, correct_coeff=1.25, penalize=False)

EXAM_YDS_CONFIG = {
    "id": "yds-score",
    "slug": "yds-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "YDS Puan Hesaplama",
    "description": "Yabancı Dil Bilgisi Seviye Tespit Sınavı netlerinizi girerek 1.25 katsayılı YDS puanınızı hesaplayın.",
    "seo": {
        "meta_title": "YDS Puan Hesaplama (%1.25 Katsayı)",
        "meta_description": "ÖSYM YDS Sınavı puanı hesaplama. Yanlışlar doğruları götürmez, her soru 1.25 puandır.",
        "meta_keywords": ["yds puan hesapla", "yökdil hesaplama", "yabancı dil sınavı"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "correct", "type": "number", "label": "Doğru Sayısı", "placeholder": "80", "default": 0, "min": 0, "max": 80
        },
        {
            "name": "incorrect", "type": "number", "label": "Yanlış Sayısı", "placeholder": "0", "default": 0, "min": 0, "max": 80,
            "tooltip": "YDS'de yanlışlar doğruları götürmez. Ancak toplam sayının 80'i aşmamasına dikkat edin."
        }
    ],
    "logic_function": calc_yds,
    "faq": [
        {
            "question": "YDS'de yanlış doğruyu götürür mü?",
            "answer": "YDS ve YÖKDİL gibi dil sınavlarında 4 yanlış 1 doğruyu götürme uygulaması YOKTUR. Boş bırakmak yerine işaretleme yapmanız avantajınızadır."
        },
        {
            "question": "YDS 1 soru kaç puan?",
            "answer": "YDS sınavı 80 sorudan oluşur ve taban puanı 100'dür. Dolayısıyla sistem her doğru yanıtı sabit 1.25 katsayısı ile çarpmaktadır."
        }
    ]
}
