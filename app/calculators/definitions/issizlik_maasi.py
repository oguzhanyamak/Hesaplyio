from app.calculators.logic.salary import calculate_unemployment_benefit

ISSIZLIK_CONFIG = {
    "id": "unemployment", "slug": "issizlik-maasi-hesaplama", "category": "Maaş Hesaplama", "title": "İşsizlik Maaşı Hesaplama",
    "description": "Son 4 aylık maaş ortalamanıza göre, işsiz kaldığınızda devletten ne kadar süre ve miktarda ödenek alacağınızı öğrenin.",
    "seo": {
        "meta_title": "İşsizlik Maaşı Hesaplama 2026 | Güncel Alt ve Üst Sınır",
        "meta_description": "2026 işsizlik maaşı hesaplama aracı. Brüt maaşınıza göre ne kadar işsizlik ödeneği alacağınızı ve şartlarını anında öğrenin.",
        "meta_keywords": ["işsizlik maaşı hesapla", "işkur işsizlik ödeneği", "maaşın yüzde kaçı"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_unemployment_benefit,
    "inputs": [
        {"name": "avg_gross_4m", "type": "number", "label": "Son 4 Ay Ortalama Brüt Maaş (₺)", "required": True, "placeholder": "Örn: 40000"}
    ],
    "sections": [
        {
            "title": "İşsizlik Maaşı Şartları ve Süreleri",
            "content": """
                <p>İşsizlik ödeneğinden yararlanabilmek için sigortalı olarak çalışırken kendi istek ve kusuru dışında işsiz kalmak gerekir.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Ne Kadar Süre Ödenir?</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li>İşten ayrılmadan önceki son 3 yılda 600 gün primi olanlara <strong>6 ay</strong>,</li>
                    <li>900 gün primi olanlara <strong>8 ay</strong>,</li>
                    <li>1080 gün primi olanlara <strong>10 ay</strong> süreyle ödenir.</li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "İşsizlik maaşı nasıl hesaplanır?", "answer": "Son 4 aylık brüt kazanç ortalamasının %40'ı olarak hesaplanır ancak asgari ücretin brüt tutarının %80'ini geçemez."},
        {"question": "İşsizlik maaşı için nereye başvurulur?", "answer": "İş sözleşmesinin feshinden sonraki 30 gün içinde İŞKUR'a şahsen veya internet üzerinden başvurulmalıdır."},
        {"question": "İstifa eden işsizlik maaşı alabilir mi?", "answer": "Kendi isteğiyle (istifa) ayrılanlar normal şartlarda işsizlik maaşı alamazlar. Ancak haklı bir nedenle fesh etmişlerse alabilirler."},
        {"question": "İşsizlik maaşından kesinti yapılır mı?", "answer": "Sadece damga vergisi kesintisi yapılır."}
    ],
    "related_calculators": [
        {"title": "Kıdem Tazminatı Hesaplama", "slug": "kidem-tazminati-hesaplama", "url": "/kidem-tazminati-hesaplama", "description": "Tazminat alacağınızı detaylıca görün."},
        {"title": "Netten Brüte Maaş", "slug": "netten-brute-maas-hesaplama", "url": "/netten-brute-maas-hesaplama", "description": "Kazancınızı brüt olarak analiz edin."},
        {"title": "Kredi Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Banka borçlarınızı planlayın."}
    ]
}
