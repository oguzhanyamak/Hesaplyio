from app.calculators.logic.salary import calculate_notice_pay

IHBAR_CONFIG = {
    "id": "notice_pay", "slug": "ihbar-tazminati-hesaplama", "category": "Maaş Hesaplama", "title": "İhbar Tazminatı Hesaplama",
    "description": "İşten ayrılma sürecinde ihbar süresine uyulmaması durumunda ödenecek tazminatı çalışma sürenize göre hesaplayın.",
    "seo": {
        "meta_title": "İhbar Tazminatı Hesaplama 2026 | Süreler ve Net Hesapla",
        "meta_description": "2026 güncel ihbar tazminatı hesaplama aracı. Çalışma sürenize göre 2, 4, 6 veya 8 haftalık brüt ve net ihbar tutarlarını öğrenin.",
        "meta_keywords": ["ihbar tazminatı", "ihbar süresi hesapla", "ihbar tazminatı kesintileri"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_notice_pay,
    "inputs": [
        {"name": "gross_salary", "type": "number", "label": "Aylık Brüt Maaş (₺)", "required": True, "placeholder": "Örn: 45000"},
        {"name": "duration_months", "type": "number", "label": "Toplam Çalışma (Ay)", "required": True, "placeholder": "Örn: 24"}
    ],
    "sections": [
        {
            "title": "İhbar Tazminatı ve Süreleri Hakkında",
            "content": """
                <p>İhbar tazminatı, iş sözleşmesini feshetmek isteyen tarafın, karşı tarafa vermesi gereken yasal bildirim süresine (ihbar süresi) uymaması halinde ödediği tazminattır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Yasal İhbar Süreleri</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li>6 aydan az çalışanlar için: <strong>2 hafta</strong></li>
                    <li>6 ay - 1,5 yıl arası çalışanlar için: <strong>4 hafta</strong></li>
                    <li>1,5 yıl - 3 yıl arası çalışanlar için: <strong>6 hafta</strong></li>
                    <li>3 yıldan fazla çalışanlar için: <strong>8 hafta</strong></li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "İhbar tazminatı nedir?", "answer": "Bildirim sürelerine uymadan işten ayrılan işçinin işverene veya işten çıkaran işverenin işçiye ödediği paradır."},
        {"question": "İhbar tazminatından vergi kesilir mi?", "answer": "Evet, kıdem tazminatından farklı olarak ihbar tazminatından hem Gelir Vergisi hem de Damga Vergisi kesilir."},
        {"question": "İstifa eden ihbar tazminatı alabilir mi?", "answer": "Hayır, istifa eden işçi ihbar tazminatı alamaz; aksine bildirim süresine uymazsa işverene ihbar tazminatı ödemek zorunda kalabilir."},
        {"question": "Kendi isteğiyle ayrılan ihbar süresinde çalışmalı mı?", "answer": "Evet, istifa eden çalışan ihbar süresi boyunca çalışmaya devam etmelidir. Aksi takdirde tazminat yükümlülüğü doğar."}
    ],
    "related_calculators": [
        {"title": "Kıdem Tazminatı Hesaplama", "slug": "kidem-tazminati-hesaplama", "url": "/kidem-tazminati-hesaplama", "description": "Toplam çalışma sürenize göre tazminatınızı bulun."},
        {"title": "İşsizlik Maaşı Hesaplama", "slug": "issizlik-maasi-hesaplama", "url": "/issizlik-maasi-hesaplama", "description": "İşten ayrılma sonrası devlet desteğini hesaplayın."},
        {"title": "Netten Brüte Maaş", "slug": "netten-brute-maas-hesaplama", "url": "/netten-brute-maas-hesaplama", "description": "Brüt kazancınızı analiz edin."}
    ]
}
