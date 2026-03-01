from app.calculators.logic.exams.tyt_score import calculate_yks_tyt

EXAM_TYT_CONFIG = {
    "id": "tyt-score",
    "slug": "tyt-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "TYT Puan Hesaplama",
    "description": "ÖSYM güncel katsayılarına (%33 Türkçe, %33 Mat vs) göre 2026 Üniversite Sınavı (YKS) TYT ham ve yerleştirme puanınızı hesaplayın.",
    "seo": {
        "meta_title": "TYT Puan Hesaplama 2026 | Güncel ÖSYM Katsayıları",
        "meta_description": "2026 TYT (Temel Yeterlilik Testi) puanı hesaplama aracı. Türkçe, Matematik, Sosyal ve Fen netlerinizle ham ve OBP yerleştirme puanınızı hesaplayın.",
        "meta_keywords": ["tyt hesaplama", "tyt puan", "yks puan", "yks hesaplama motoru", "obp"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "tr_correct", "type": "number", "label": "Türkçe (Doğru)", "placeholder": "40", "default": 0, "min": 0, "max": 40
        },
        {
            "name": "tr_incorrect", "type": "number", "label": "Türkçe (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 40
        },
        {
            "name": "math_correct", "type": "number", "label": "Matematik (Doğru)", "placeholder": "40", "default": 0, "min": 0, "max": 40
        },
        {
            "name": "math_incorrect", "type": "number", "label": "Matematik (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 40
        },
        {
            "name": "soc_correct", "type": "number", "label": "Sosyal B. (Doğru)", "placeholder": "20", "default": 0, "min": 0, "max": 20
        },
        {
            "name": "soc_incorrect", "type": "number", "label": "Sosyal B. (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 20
        },
        {
            "name": "sci_correct", "type": "number", "label": "Fen B. (Doğru)", "placeholder": "20", "default": 0, "min": 0, "max": 20
        },
        {
            "name": "sci_incorrect", "type": "number", "label": "Fen B. (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 20
        },
        {
            "name": "diploma", "type": "number", "step": "0.01", "label": "Diploma Notu (OBP İçin)", "placeholder": "Örnek: 85.50", "default": 85.00, "min": 50, "max": 100
        }
    ],
    "logic_function": calculate_yks_tyt,
    "faq": [
        {
            "question": "Dört yanlış bir doğruyu götürüyor mu?",
            "answer": "Evet. ÖSYM sistemi gereği işaretlemediğiniz (boş) sorular netinizi etkilemezken, TYT'de yaptığınız her 4 yanlış 1 doğrunuzu silmektedir."
        },
        {
            "question": "TYT için OBP sınava ne kadar etki eder?",
            "answer": "Diploma notunuz önce 5 ile çarpılarak OBP (Ortaöğretim Başarı Puanı) bulunur. Daha sonra bu puanın %12'si (kısacası Diploma x 0.6) Ham Puanınıza eklenerek Yerleştirme Puanı oluşur."
        }
    ]
}
