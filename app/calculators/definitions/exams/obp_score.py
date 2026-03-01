from app.calculators.logic.salary import calculate_net_to_gross # We can create a simple one for OBP

def calculate_obp_score(diploma: float|str=0):
    dip = float(diploma)
    obp = dip * 5
    return {
        "summary": {
            "label": "Ortaöğretim Başarı Puanı (OBP)",
            "value": round(obp, 2)
        },
        "breakdown": [
            {"label": "Diploma Notu", "value": dip},
            {"label": "OBP Katsayısı", "value": 5},
            {"label": "Yerleştirme Katkısı (x 0.12)", "value": round(obp * 0.12, 2)}
        ]
    }

EXAM_OBP_CONFIG = {
    "id": "obp-score",
    "slug": "obp-okul-puani-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "OBP Okul Puanı Hesaplama",
    "description": "Lise diploma notunuzun üniversite sınavı (YKS) puanınıza ne kadar etki edeceğini hesaplayın.",
    "seo": {
        "meta_title": "OBP Hesaplama 2026 | Okul Puanı Sınava Ne Kadar Ekler?",
        "meta_description": "OBP (Ortaöğretim Başarı Puanı) hesaplama aracı. Diploma notuna göre YKS yerleştirme puanına gelecek ek puanı bulun.",
        "meta_keywords": ["obp hesaplama", "okul puanı", "diploma notu hesaplama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "diploma", "type": "number", "step": "0.01", "label": "Lise Diploma Notu", "default": 85, "min": 50, "max": 100}
    ],
    "logic_function": calculate_obp_score,
    "faq": [
        {
            "question": "OBP puanı sınav puanına nasıl eklenir?",
            "answer": "Diploma notunuz 5 ile çarpılarak OBP oluşturulur. Bu puanın %12'si (OBP x 0.12) ham puanınıza yerleştirme puanı olarak eklenir."
        }
    ]
}
