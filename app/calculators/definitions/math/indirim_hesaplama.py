from app.calculators.logic.math.basic_ops import calculate_discount

INDIRIM_CONFIG = {
    "id": "indirim", "slug": "indirim-hesaplama", "category": "Matematik", "title": "İndirim Hesaplama",
    "description": "Alışverişlerde tasarrufunuzu anında görün. İkinci ürüne %50 indirim veya nakit indirim oranlarını hemen hesaplayın.",
    "seo": {
        "meta_title": "İndirim Hesaplama | Tasarruf ve Son Fiyat Hesapla",
        "meta_description": "Mağaza indirimleri, %50, %25 ve nakit indirim oranlarıyla alışveriş hesaplama aracı. Kaç TL tasarruf edeceğinizi öğrenin.",
        "meta_keywords": ["indirim hesapla", "yüzde kaç indirim", "indirimli fiyat", "mağaza indirimleri"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_discount,
    "inputs": [
        {"name": "price", "type": "number", "label": "Etiket Fiyatı (₺)", "required": True, "placeholder": "Örn: 2000"},
        {"name": "rate", "type": "number", "label": "İndirim Oranı (%)", "required": True, "placeholder": "Örn: 30"}
    ],
    "sections": [
        {
            "title": "İndirim Hesaplama Nasıl Yapılır?",
            "content": """
                <p>İndirim hesaplama işlemi, bir ürünün satış fiyatı üzerinden belli bir oranda tutarın düşülmesiyle yapılır. Bu sayede alışverişinizde ne kadar tasarruf ettiğinizi görebilirsiniz.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">İndirim Formülü</h3>
                <div class="bg-blue-50 p-4 rounded-xl font-mono text-blue-800 my-4 text-center">
                    İndirim Tutarı = (Fiyat &times; İndirim Oranı) / 100
                </div>
                <p><strong>Örnek:</strong> 1.000 TL'lik bir üründe %25 indirim yapılıyorsa (1000 &times; 25) / 100 = 250 TL indirim yapılır. Ürünün indirimli fiyatı 750 TL olur.</p>
            """
        }
    ],
    "faq": [
        {"question": "İndirimli fiyat nasıl hesaplanır?", "answer": "Etiket fiyatından, indirim tutarını (fiyat * oran / 100) çıkararak indirimli fiyatı bulabilirsiniz."},
        {"question": "İkinci ürüne %50 indirim ne demektir?", "answer": "Sepetinizdeki daha ucuz olan ürünün fiyatının yarısının toplam fiyattan düşülmesi anlamına gelir."},
        {"question": "3 al 2 öde kampanyası yüzde kaç indirim sağlar?", "answer": "3 al 2 öde kampanyası, fiyatların aynı olması durumunda yaklaşık %33,3 oranında bir indirim sağlar."},
        {"question": "KDV dahil fiyata mı indirim yapılır?", "answer": "Genellikle mağazalarda gördüğünüz etiket fiyatı KDV dahil fiyattır ve indirim bu fiyat üzerinden hesaplanır."}
    ],
    "related_calculators": [
        {"title": "KDV Hesaplama", "slug": "kdv-hesaplama", "url": "/kdv-hesaplama", "description": "Vergi dâhil faturayı hesaplayın."},
        {"title": "Yüzde Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Genel artış ve oran hesaplamaları yapın."},
        {"title": "Kredi Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Taksitlerinizin detaylarını öğrenin."}
    ]
}
