from app.calculators.logic.salary import calculate_gross_to_net

BRUTTEN_NETE_CONFIG = {
    "id": "brutten-nete", "slug": "brutten-nete-maas-hesaplama", "category": "Maaş Hesaplama", "title": "Brütten Nete Maaş Hesaplama",
    "description": "Brüt sözleşme tutarınızın, vergi ve SGK kesintileri sonrası elinize ne kadar geçeceğini 2026 güncel verileriyle hesaplayın.",
    "seo": {
        "meta_title": "Brütten Nete Maaş Hesaplama 2026 | Anında Kesin Sonuç",
        "meta_description": "2026 brüt maaş üzerinden net maaş hesaplama aracı. SGK işçi payı, gelir vergisi ve damga vergisi kesintilerini detaylıca görün.",
        "meta_keywords": ["brütten nete", "maaş hesapla", "vergi kesintisi", "sgk primi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_gross_to_net,
    "inputs": [
        {"name": "gross_salary", "type": "number", "label": "Aylık Brüt Maaş (₺)", "required": True, "placeholder": "Örn: 60000"},
        {"name": "calc_year", "type": "select", "label": "Yıl", "options": [{"label": "2026", "value": "2026"}], "default": "2026"}
    ],
    "sections": [
        {
            "title": "Brütten Nete Maaş Nasıl Hesaplanır?",
            "content": """
                <p>Brüt maaş, işvereninizle anlaştığınız toplam tutardır. Ancak bu tutardan yasal kesintiler yapıldıktan sonra elinize geçen miktar <strong>net maaş</strong> olarak adlandırılır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Yapılan Kesintiler</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li><strong>SGK Primi (%14):</strong> Sosyal Güvenlik Kurumu işçi payı.</li>
                    <li><strong>İşsizlik Sigortası (%1):</strong> Zorunlu işsizlik fonu kesintisi.</li>
                    <li><strong>Gelir Vergisi:</strong> Maaşınızın vergi matrahına göre %15'ten başlayan oranlar.</li>
                    <li><strong>Damga Vergisi:</strong> Maktu oranda alınan devlet vergisi.</li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "Brüt maaş nedir?", "answer": "Brüt maaş, yasal kesintiler (vergi, SGK vb.) düşülmeden önceki toplam maaş tutarıdır."},
        {"question": "Net maaş nasıl hesaplanır?", "answer": "Brüt maaştan; SGK işçi payı, işsizlik sigortası payı, gelir vergisi ve damga vergisi çıkarılarak bulunur."},
        {"question": "Asgari ücret brüt ve net ne kadardır?", "answer": "2026 yılı asgari ücret tutarı resmi rakamla net olarak ifade edilse de, brüt miktar üzerinden tüm kesintiler hesaplanmaktadır."},
        {"question": "BES kesintisi opsiyonel mi?", "answer": "Bireysel Emeklilik Sistemi (BES), otomatik katılım sonrası çalışanın isteğiyle iptal edilebilir bir sitemdir."}
    ],
    "related_calculators": [
        {"title": "Netten Brüte Maaş Hesaplama", "slug": "netten-brute-maas-hesaplama", "url": "/netten-brute-maas-hesaplama", "description": "Net elinize geçen paradan brüt tutarı bulun."},
        {"title": "Kıdem Tazminatı Hesaplama", "slug": "kidem-tazminati-hesaplama", "url": "/kidem-tazminati-hesaplama", "description": "İşten ayrılma durumunda alacağınız tazminatı öğrenin."},
        {"title": "İşsizlik Maaşı Hesaplama", "slug": "issizlik-maasi-hesaplama", "url": "/issizlik-maasi-hesaplama", "description": "İşsiz kalma durumunda devlet desteğini hesaplayın."}
    ]
}
