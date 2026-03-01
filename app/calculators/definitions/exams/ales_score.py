from app.calculators.logic.exams.ales_score import calc_ales

EXAM_ALES_CONFIG = {
    "id": "ales-score",
    "slug": "ales-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "ALES Puan Hesaplama",
    "description": "Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı netlerinize göre SAY, EA ve SÖZ puanlarınızı öğrenin.",
    "seo": {
        "meta_title": "ALES Puan Hesaplama Modülü - 50 Sayısal 50 Sözel",
        "meta_description": "2026 ALES Puanı nasıl hesaplanır? 50 Matematik ve 50 Türkçe katsayılarıyla Sözel, Eşit Ağırlık ve Sayısal ALES skorunuzu görün.",
        "meta_keywords": ["ales hesaplama", "akademik personel sınavı", "ales ea puanı", "ales standart sapma"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "say1_c", "type": "number", "label": "Sayısal (Doğru)", "placeholder": "50", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "say1_i", "type": "number", "label": "Sayısal (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "soz1_c", "type": "number", "label": "Sözel (Doğru)", "placeholder": "50", "default": 0, "min": 0, "max": 50
        },
        {
            "name": "soz1_i", "type": "number", "label": "Sözel (Yanlış)", "placeholder": "0", "default": 0, "min": 0, "max": 50
        }
    ],
    "logic_function": calc_ales,
    "faq": [
        {
            "question": "ALES katsayıları nedir?",
            "answer": "ALES Sayısal testinde Matematik %75, Türkçe %25; Eşit Ağırlıkta her ikisi de %50; Sözelde ise Matematik %25, Türkçe %75 etkilidir. Taban puan 50'den başlar."
        }
    ]
}
