def calculate_yks_full(tyt_net: float|str=0, ayt_mat: float|str=0, ayt_fen: float|str=0, ayt_edb: float|str=0, ayt_soc: float|str=0, diploma: float|str=0) -> dict:
    t_net = float(tyt_net)
    a_mat = float(ayt_mat)
    a_fen = float(ayt_fen)
    a_edb = float(ayt_edb)
    a_soc = float(ayt_soc)
    dip = float(diploma)
    
    # YKS Puanı = (TYT Net * 1.33) + (AYT Netler * 3.0) + Base + OBP
    # Simplified weights
    tyt_contribution = t_net * 1.32
    ayt_contribution = (a_mat + a_fen + a_edb + a_soc) * 3.0
    
    base = 100
    raw_score = base + tyt_contribution + ayt_contribution
    
    # OBP
    placement = dip * 0.6
    
    return {
        "summary": {
            "label": "YKS Yerleştirme Puanı (Tahmini)",
            "value": round(raw_score + placement, 3)
        },
        "breakdown": [
            {"label": "TYT Katkısı", "value": round(tyt_contribution, 2)},
            {"label": "AYT Netler Toplamı", "value": round(a_mat + a_fen + a_edb + a_soc, 2)},
            {"label": "AYT Katkısı", "value": round(ayt_contribution, 2)},
            {"label": "Ham Puan", "value": round(raw_score, 3)},
            {"label": "OBP Yerleştirme Katkısı", "value": round(placement, 2)},
        ]
    }

EXAM_YKS_FULL_CONFIG = {
    "id": "yks-score",
    "slug": "yks-puan-hesaplama",
    "category": "Sınav Puanı Hesaplama",
    "title": "YKS (TYT + AYT) Puan Hesaplama",
    "description": "Hem TYT hem de AYT netlerinizi girerek 4 yıllık üniversite bölümleri için yerleştirme puanınızı hesaplayın.",
    "seo": {
        "meta_title": "YKS Puan Hesaplama 2026 | TYT-AYT Net Hesapla",
        "meta_description": "2026 YKS puanı hesaplama. Sayısal, Sözel ve Eşit Ağırlık puan türlerine göre yerleştirme puanınızı hesaplayın.",
        "meta_keywords": ["yks hesaplama", "ayt puan", "tyt ayt hesapla", "yks yerleştirme"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {"name": "tyt_net", "type": "number", "step": "0.25", "label": "Toplam TYT Netiniz", "default": 0, "min": 0, "max": 120},
        {"name": "ayt_mat", "type": "number", "step": "0.25", "label": "AYT Matematik Net", "default": 0, "min": 0, "max": 40},
        {"name": "ayt_fen", "type": "number", "step": "0.25", "label": "AYT Fen Bilimleri Net", "default": 0, "min": 0, "max": 40},
        {"name": "ayt_edb", "type": "number", "step": "0.25", "label": "AYT Edebiyat-Sos1 Net", "default": 0, "min": 0, "max": 40},
        {"name": "diploma", "type": "number", "step": "0.01", "label": "Diploma Notu", "default": 80, "min": 50, "max": 100}
    ],
    "logic_function": calculate_yks_full,
    "faq": [
        {
            "question": "YKS puanında TYT yüzde kaç etkili?",
            "answer": "YKS genel puanınızın hesaplanmasında TYT %40, AYT ise %60 oranında etkilidir."
        }
    ]
}
