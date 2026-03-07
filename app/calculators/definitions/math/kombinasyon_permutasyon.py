from app.calculators.logic.math.combinatorics import calculate_comb_perm

COMB_PERM_CONFIG = {
    "id": "combinatorics", "slug": "kombinasyon-hesaplama", "category": "Matematik", "title": "Kombinasyon ve Permütasyon",
    "description": "Öğeler arasından seçim yapma (Kombinasyon) ve sıralama (Permütasyon) olasılıklarını anında hesaplayın.",
    "seo": {
        "meta_title": "Kombinasyon ve Permütasyon Hesaplama | n'in r'lisi Bul",
        "meta_description": "Online kombinasyon ve permütasyon hesaplayıcı. n ve r değerleriyle seçim ve sıralama olasılıklarını bulun.",
        "meta_keywords": ["kombinasyon hesapla", "permütasyon hesapla", "n'in r'lisi", "sıralama olasılığı"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_comb_perm,
    "inputs": [
        {"name": "n", "type": "number", "label": "Toplam Öğe Sayısı (n)", "required": True, "placeholder": "Örn: 10"},
        {"name": "r", "type": "number", "label": "Seçilen Öğe Sayısı (r)", "required": True, "placeholder": "Örn: 3"},
        {"name": "mode", "type": "select", "label": "İşlem Türü", "options": [
            {"label": "Kombinasyon C(n,r) - Seçme", "value": "combination"},
            {"label": "Permütasyon P(n,r) - Sıralama", "value": "permutation"}
        ], "default": "combination"}
    ],
    "sections": [
        {
            "title": "Kombinasyon ve Permütasyon Nedir?",
            "content": """
                <p>Matematikte olasılık ve veri analizi işlemlerinde sıklıkla karşımıza çıkan iki kavramdır. Temel farkları, **sıralamanın önemli olup olmadığıdır**.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Kombinasyon (Seçme)</h3>
                <p>Sıralamanın önemsiz olduğu gruplama işlemidir. Örn: Bir torbadan 3 top çekmek.</p>
                <div class="bg-blue-50 p-4 rounded-xl font-mono text-blue-800 my-4 text-center">
                    C(n, r) = n! / [r! &times; (n - r)!]
                </div>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Permütasyon (Sıralama)</h3>
                <p>Sıralamanın önemli olduğu dizilim işlemidir. Örn: 3 kişinin bir bankta yan yana oturması.</p>
                <div class="bg-blue-50 p-4 rounded-xl font-mono text-blue-800 my-4 text-center">
                    P(n, r) = n! / (n - r)!
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Kombinasyon ve Permütasyon farkı nedir?", "answer": "Kombinasyonda sıralama önemli değildir (gruplama), permütasyonda ise öğelerin dizilim sırası önemlidir (sıralama)."},
        {"question": "n'in r'lisi ne demektir?", "answer": "n elemanlı bir kümeden r kadar elemanın kaç farklı şekilde seçilebileceğini ifade eden kısımdır."},
        {"question": "C(n, n) ve C(n, 0) kaçtır?", "answer": "Her ikisi de 1'e eşittir. n eleman arasından n elaman seçmenin de, hiçbir şey seçmemenin de tek bir yolu vardır."},
        {"question": "P(n, n) kaçtır?", "answer": "n! (faktöriyel) değerine eşittir. n kişinin n koltuğa kaç farklı şekilde sıralanacağını gösterir."}
    ],
    "related_calculators": [
        {"title": "Faktöriyel Hesaplama", "slug": "faktoryel-hesaplama", "url": "/faktoryel-hesaplama", "description": "Bir sayının faktöriyelini (n!) bulun."},
        {"title": "Yüzde Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Genel artış ve oran hesaplamaları yapın."},
        {"title": "Olasılık Hesaplama", "slug": "istatistik-hesaplama", "url": "/istatistik-hesaplama", "description": "İstatistiki verileri analiz edin."}
    ]
}
