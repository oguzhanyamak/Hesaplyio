def calculate_target_nets(target_score: float|str=0, base_score: float=100, coefficient: float=3.4):
    ts = float(target_score)
    needed_points = ts - base_score
    if needed_points <= 0:
        needed_nets = 0
    else:
        needed_nets = needed_points / coefficient
        
    return {
        "summary": {
            "label": "Gereken Toplam Net",
            "value": round(needed_nets, 2)
        },
        "breakdown": [
            {"label": "Hedeflenen Puan", "value": ts},
            {"label": "Taban Puan (Offset)", "value": base_score},
            {"label": "Ortalama Soru Katsayısı", "value": coefficient},
            {"label": "Çıkarılması Gereken Net", "value": round(needed_nets, 2)}
        ]
    }

EXAM_UNIV_TABAN_CONFIG = {
    "id": "univ-target",
    "slug": "universite-yks-taban-puanlari-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "Üniversite Hedef Net Hesaplama",
    "description": "Girmeyi hedeflediğiniz üniversite bölümünün puanına ulaşmak için kaç net yapmanız gerektiğini hesaplayın.",
    "seo": {
        "meta_title": "Hedef Puan İçin Kaç Net Gerekli? | YKS 2026",
        "meta_description": "Hedeflediğiniz üniversite taban puanına ulaşmak için TYT ve AYT'de yapmanız gereken tahmini net sayılarını hesaplayın.",
        "meta_keywords": ["üniversite taban puanları", "kaçı netle kazanırım", "yks hedef puan"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "target_score", "type": "number", "label": "Hedeflenen Bölüm Puanı", "default": 400, "min": 100, "max": 560}
    ],
    "logic_function": calculate_target_nets,
    "faq": [
        {
            "question": "Bu hesaplama kesin sonuç verir mi?",
            "answer": "Hayır, bu bir simülasyondur. Standart sapmalar sınavın zorluğuna göre katsayıları değiştirebilir."
        }
    ]
}
