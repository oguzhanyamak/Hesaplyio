from app.calculators.logic.salary import calculate_net_to_gross

NET_TO_GROSS_CONFIG = {
    "id": "net-to-gross",
    "slug": "netten-brute-maas-hesaplama",
    "category": "Maaş Hesaplama",
    "title": "Netten Brüte Maaş Hesaplama",
    "description": "2026 yılı güncel vergi dilimleri ve SGK kesintileri ile net maaşınızdan brüt maaşınızı anında hesaplayın.",
    "seo": {
        "meta_title": "Netten Brüte Maaş Hesaplama 2026 | Anında Kesin Sonuç",
        "meta_description": "2026 güncel SGK ve vergi oranlarıyla netten brüte maaşınızı anında hesaplayın.",
        "meta_keywords": ["netten brüte", "maaş hesaplama", "2026 vergi dilimleri"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "net_salary",
            "type": "number",
            "label": "Aylık Net Maaş (₺)",
            "placeholder": "Örnek: 45000",
            "required": True,
            "min": 17002, 
            "tooltip": "Aylık olarak banka hesabınıza yatan net tutar"
        },
        {
            "name": "calc_year",
            "type": "select",
            "label": "Hesaplama Yılı",
            "options": [{"label": "2026", "value": "2026"}, {"label": "2025", "value": "2025"}],
            "default": "2026"
        }
    ],
    "logic_function": calculate_net_to_gross,
    "sections": [
        {
            "title": "Netten Brüte Maaş Hesaplama Nedir?",
            "content": """
                <p>Netten brüte maaş hesaplama, banka hesabınıza yatan net tutardan yola çıkarak, işvereninizin sizin adınıza ödediği toplam maliyeti (brüt maaş) bulma işlemidir. Bu hesaplama yapılırken SGK işçi payı, işsizlik sigortası, gelir vergisi ve damga vergisi gibi kesintiler tersine işlem yapılarak hesaplanır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Maaş Kesintileri Nelerdir?</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li><strong>SGK İşçi Payı (%14):</strong> Brüt maaş üzerinden hesaplanan sosyal güvenlik primi.</li>
                    <li><strong>İşsizlik Sigortası (%1):</strong> Brüt maaş üzerinden alınan zorunlu kesinti.</li>
                    <li><strong>Gelir Vergisi:</strong> Kümülatif vergi matrahına göre %15'ten başlayıp %40'a kadar çıkan vergi dilimleri.</li>
                    <li><strong>Damga Vergisi:</strong> Belli bir oranda (binde 7,59) alınan maktu vergi.</li>
                </ul>
            """
        },
        {
            "title": "2026 Vergi Dilimleri Hakkında",
            "content": """
                <div class="bg-blue-50 p-6 rounded-2xl border border-blue-100">
                    <p class="text-sm text-blue-800">Türkiye'de gelir vergisi basamaklı bir yapıya sahiptir. Yıl boyunca kazandığınız toplam brüt miktar arttıkça, girdiğiniz vergi dilimi de yükselir. Bu durum, yılın son aylarına doğru net maaşınızın bir miktar azalmasına neden olabilir.</p>
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Netten brüte maaş hesabı nasıl yapılır?", "answer": "Net maaşınıza yasal kesintilerin (SGK, İşsizlik, Vergi) eklenmesiyle brüt maaşa ulaşılır. Vergi dilimleri değişken olduğu için her ay farklılık gösterebilir."},
        {"question": "Brüt maaş neleri kapsar?", "answer": "Brüt maaş; net maaş, SGK primleri ve gelir vergisi toplamını ifade eder. İşverenin cebinden çıkan toplam maliyet ise brüt maaşa ek olarak SGK işveren payını da kapsar."},
        {"question": "Vergi dilimi maaşı nasıl etkiler?", "answer": "Yıllık kümülatif geliriniz vergi sınırlarını aştığında bir üst dilime (%15, %20, %27, %35, %40) geçersiniz. Bu da net maaşınızdan daha fazla vergi kesilmesine yol açar."},
        {"question": "Asgari ücret istisnası nedir?", "answer": "Tüm çalışanların maaşlarının asgari ücrete kadar olan kısmı gelir vergisi ve damga vergisinden muaftır."},
        {"question": "BES kesintisi zorunlu mu?", "answer": "45 yaş altı çalışanlar için Bireysel Emeklilik Sistemi (BES) otomatik katılımı zorunludur ancak çalışanlar dilerse 2 ay içinde sistemden ayrılabilirler."}
    ],
    "related_calculators": [
        {"title": "Brütten Nete Maaş Hesaplama", "slug": "brutten-nete-maas-hesaplama", "url": "/brutten-nete-maas-hesaplama", "description": "Brüt sözleşme tutarınızın elinize ne kadar geçeceğini hesaplayın."},
        {"title": "Kıdem Tazminatı Hesaplama", "slug": "kidem-tazminati-hesaplama", "url": "/kidem-tazminati-hesaplama", "description": "İşten ayrılma durumunda alacağınız tazminat miktarını öğrenin."},
        {"title": "İşsizlik Maaşı Hesaplama", "slug": "issizlik-maasi-hesaplama", "url": "/issizlik-maasi-hesaplama", "description": "İşsiz kalma durumunda devletten alacağınız desteği hesaplayın."}
    ]
}
