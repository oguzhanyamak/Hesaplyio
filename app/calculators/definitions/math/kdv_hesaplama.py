from app.calculators.logic.math.basic_ops import calculate_vat

KDV_CONFIG = {
    "id": "kdv", "slug": "kdv-hesaplama", "category": "Matematik", "title": "KDV Hesaplama",
    "description": "Katma Değer Vergisi (KDV) dâhil ve hariç tutarlarını %1, %10 ve %20 oranlarıyla anında hesaplayın.",
    "seo": {
        "meta_title": "KDV Hesaplama 2026 | KDV Dahil ve Hariç Hesapla",
        "meta_description": "Güncel %20, %10 ve %1 KDV oranlarıyla hızlı hesaplama. KDV dahil fiyat bulma ve KDV hariç matrah hesaplama aracı.",
        "meta_keywords": ["kdv hesapla", "kdv dahil", "kdv hariç", "yüzde 20 kdv"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_vat,
    "inputs": [
        {"name": "value", "type": "number", "label": "Tutar (₺)", "required": True, "placeholder": "Örn: 1000"},
        {"name": "rate", "type": "select", "label": "KDV Oranı (%)", "options": [
            {"label": "%20 (Genel)", "value": 20},
            {"label": "%10 (Gıda/Tekstil)", "value": 10},
            {"label": "%1 (Temel Gıda)", "value": 1}
        ], "default": 20},
        {"name": "mode", "type": "select", "label": "İşlem", "options": [
            {"label": "KDV Hariç -> KDV Dahil Bul", "value": "add"},
            {"label": "KDV Dahil -> KDV Hariç Bul", "value": "subtract"}
        ], "default": "add"}
    ],
    "sections": [
        {
            "title": "KDV Hesaplama Nasıl Yapılır?",
            "content": """
                <p>KDV (Katma Değer Vergisi), tüketilen her mal ve hizmet üzerinden alınan dolaylı bir vergidir. Türkiye'de genellikle %1, %10 ve %20 oranlarında uygulanır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">KDV Dahil Hesaplama Formülü</h3>
                <p>KDV Hariç tutarı KDV Dahil hale getirmek için: <strong>Tutar &times; (1 + KDV Oranı/100)</strong></p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">KDV Hariç (Matrah) Hesaplama Formülü</h3>
                <p>KDV Dahil tutardan KDV'siz (matrah) tutarı bulmak için: <strong>Tutar / (1 + KDV Oranı/100)</strong></p>
            """
        }
    ],
    "faq": [
        {"question": "KDV oranı kaçtır?", "answer": "Türkiye'de genel KDV oranı %20'dir. Ancak gıda, eğitim ve tekstil gibi kalemlerde %10 ve %1 oranları uygulanmaktadır."},
        {"question": "KDV dahil ve hariç ne demektir?", "answer": "KDV dahil, verginin fiyata eklenmiş halidir. KDV hariç ise verginin henüz eklenmediği saf fiyattır."},
        {"question": "KDV tevkifatı nedir?", "answer": "Verginin satıcı yerine alıcı tarafından vergi dairesine ödenmesi işlemine tevkifat denir."},
        {"question": "Faturada KDV nasıl gösterilir?", "answer": "Faturada malın matrah fiyatı, KDV oranı, KDV tutarı ve Genel Toplam ayrı ayrı belirtilmelidir."}
    ],
    "related_calculators": [
        {"title": "Yüzde Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Genel artış ve oran hesaplamaları yapın."},
        {"title": "İndirim Hesaplama", "slug": "indirim-hesaplama", "url": "/indirim-hesaplama", "description": "Mağaza indirimlerini ve tasarruf miktarınızı görün."},
        {"title": "Kredi Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Banka taksitlerinizi hızlıca hesaplayın."}
    ]
}
