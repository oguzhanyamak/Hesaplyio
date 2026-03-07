from app.calculators.logic.salary import calculate_severance_pay

KIDEM_CONFIG = {
    "id": "severance", "slug": "kidem-tazminati-hesaplama", "category": "Maaş Hesaplama", "title": "Kıdem ve İhbar Tazminatı",
    "description": "İşten ayrılma veya çıkarılma durumunda hak ettiğiniz kıdem ve ihbar tazminatını 2026 tavan fiyatlarıyla hesaplayın.",
    "seo": {
        "meta_title": "Kıdem Tazminatı Hesaplama 2026 | İhbar ve Brüt Kazanç",
        "meta_description": "2026 kıdem tazminatı tavanı üzerinden ne kadar tazminat alacağınızı hesaplayın. İhbar süresi ve damga vergisi dahil net tutar bulma.",
        "meta_keywords": ["kıdem tazminatı hesabı", "ihbar tazminatı", "tazminat tavanı 2026"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_severance_pay,
    "inputs": [
        {"name": "gross_salary", "type": "number", "label": "Son Brüt Maaş (₺)", "required": True, "placeholder": "Örn: 50000"},
        {"name": "years", "type": "number", "label": "Çalışılan Yıl", "default": 1},
        {"name": "months", "type": "number", "label": "Ay", "default": 0},
        {"name": "days", "type": "number", "label": "Gün", "default": 0}
    ],
    "sections": [
        {
            "title": "Kıdem Tazminatı Alma Şartları",
            "content": """
                <p>Kıdem tazminatı, çalışanların iş yerinde geçirdikleri her bir yıl için ödenen bir toplu ödemedir. Hak kazanmak için şu şartlar gereklidir:</p>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li>İş yerinde en az <strong>1 tam yıl</strong> çalışmış olmak.</li>
                    <li>İşveren tarafından haklı bir neden olmaksızın işten çıkarılmak veya işçi tarafından haklı nedenle istifa etmek.</li>
                    <li>Emeklilik, askerlik veya kadın çalışanlar için evlilik nedeniyle ayrılmak.</li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "Kıdem tazminatı nasıl hesaplanır?", "answer": "Her tam yıl için bir aylık brüt maaş ödenir. 1 yıldan artan süreler ise gün bazında orantılanır."},
        {"question": "Kıdem tazminatı tavanı nedir?", "answer": "Devletin belirlediği ve brüt maaşınız ne kadar yüksek olursa olsun, bir yıl için ödenebilecek en yüksek tutarı ifade eder."},
        {"question": "İstifa eden kıdem tazminatı alabilir mi?", "answer": "Normal şartlarda hayır. Ancak askerlik, emeklilik, sağlık sorunları veya haklı fesih durumlarında istifa edilse dahi alınabilir."},
        {"question": "Tazminattan vergi kesilir mi?", "answer": "Kıdem tazminatından sadece damga vergisi kesilir, gelir vergisi kesilmez."}
    ],
    "related_calculators": [
        {"title": "İşsizlik Maaşı Hesaplama", "slug": "issizlik-maasi-hesaplama", "url": "/issizlik-maasi-hesaplama", "description": "İşten çıktıktan sonra devletten alacağınız ödeneği bulun."},
        {"title": "Netten Brüte Maaş", "slug": "netten-brute-maas-hesaplama", "url": "/netten-brute-maas-hesaplama", "description": "Net maaşınızdan brüt kazancınızı bulun."},
        {"title": "İhbar Tazminatı", "slug": "ihbar-tazminati-hesaplama", "url": "/ihbar-tazminati-hesaplama", "description": "İhbar süresi bildirilmediğinde ödenecek tutarı bulun."}
    ]
}
