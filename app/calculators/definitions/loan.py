from app.calculators.logic.loan import calculate_loan_repayment

LOAN_CONFIG = {
    "id": "consumer-loan",
    "slug": "kredi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "İhtiyaç Kredisi Hesaplama",
    "description": "Güncel faiz oranları, KKDF ve BSMV vergileri dahil olarak ihtiyaç kredisi ve aylık taksit tutarlarınızı anında hesaplayın.",
    "seo": {
        "meta_title": "İhtiyaç Kredisi Hesaplama 2026 | Taksit Ödeme Planı",
        "meta_description": "Ne kadar kredi çekebilirim? Güncel banka faiz oranlarıyla ihtiyaç kredisi hesaplama, aylık taksit tutarı ve ödeme planı çıkarın.",
        "meta_keywords": ["kredi hesaplama", "ihtiyaç kredisi", "kredi ödeme planı", "kredi faizi hesaplama", "aylık taksit"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 1000, 
            "tooltip": "Çekmek istediğiniz toplam tutar"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 3.50",
            "required": True,
            "min": 0,
            "tooltip": "Bankanın belirlediği aylık baz faiz oranı"
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 24",
            "required": True,
            "min": 1,
            "max": 36,
            "tooltip": "Aylık taksit sayınız"
        }
    ],
    "logic_function": calculate_loan_repayment,
    "sections": [
        {
            "title": "İhtiyaç Kredisi Hesaplama Nasıl Yapılır?",
            "content": """
                <p>İhtiyaç kredisi hesaplama, bankadan alacağınız anapara tutarının üzerine aylık faiz ve yasal vergilerin (KKDF, BSMV) eklenmesiyle oluşan toplam borcun, vade süresine (ay sayısına) bölünmesi işlemidir. Türkiye'de taksitli krediler genellikle <strong>Eşit Taksitli Ödeme Planı</strong> (Anüite) sistemine göre hesaplanır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Kredi Maliyetini Etkileyen Faktörler</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li><strong>Anapara:</strong> Bankadan talep ettiğiniz kredi tutarı.</li>
                    <li><strong>Faiz Oranı:</strong> Bankanın sunduğu aylık baz faiz.</li>
                    <li><strong>KKDF (%15):</strong> Kaynak Kullanımını Destekleme Fonu, faiz üzerinden alınır.</li>
                    <li><strong>BSMV (%10):</strong> Banka ve Sigorta Muameleleri Vergisi, faiz üzerinden alınır.</li>
                    <li><strong>Vade:</strong> Geri ödeme süresidir; vade uzadıkça aylık taksit düşer ancak toplam faiz maliyeti artar.</li>
                </ul>
            """
        },
        {
            "title": "Kredi Hesaplama Örnekleri",
            "content": """
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">50.000 TL Kredi Örneği</h4>
                        <p class="text-sm">24 ay vade ve %3,50 faizle: Aylık taksit yaklaşık 3.500 TL civarında olur. Toplam geri ödeme ise anaparadan yüksek olacaktır.</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">100.000 TL Kredi Örneği</h4>
                        <p class="text-sm">12 ay vade ve %3,50 faizle: Aylık taksit yaklaşık 11.000 TL bandında seyreder. Kısa vadede toplam maliyet daha düşük kalır.</p>
                    </div>
                </div>
            """
        }
    ],
    "faq": [
        {"question": "İhtiyaç kredisi taksitleri nasıl hesaplanır?", "answer": "İhtiyaç kredisi taksitleri, ana para üzerine banka faizi, %15 KKDF ve %10 BSMV vergileri eklenerek bulunan toplam faiz oranı üzerinden her ay kalan ana paraya işletilerek hesaplanır."},
        {"question": "En uygun kredi vadesi ne kadardır?", "answer": "En uygun vade, aylık gelirinize göre belirlenmelidir. Vade uzadıkça aylık taksitler düşer ancak toplam faiz maliyeti artar. Genellikle 24 veya 36 ay ideal dengedir."},
        {"question": "Kredi hesaplamasında KKDF ve BSMV nedir?", "answer": "KKDF (%15) ve BSMV (%10), bireysel ihtiyaç kredilerinde faiz tutarı üzerinden alınan devlet vergileridir. Emekli ve ticari kredilerde oranlar değişebilir."},
        {"question": "Dosya masrafı kredi taksitini etkiler mi?", "answer": "Dosya masrafı genellikle kredi başında peşin (veya kredi tutarından düşülerek) alınır. Aylık taksiti doğrudan değiştirmez ancak projenin toplam maliyetini etkiler."},
        {"question": "Kredi erken kapatma cezası var mıdır?", "answer": "İhtiyaç kredilerinde erken kapatma cezası uygulanmaz. Kalan anapara üzerinden borcunuzu kapatarak gelecek ayların faizinden tasarruf edebilirsiniz."},
        {"question": "Yıllık Maliyet Oranı (YMO) nedir?", "answer": "Faiz, vergiler ve tüm masrafların birleşmesiyle oluşan yıllık efektif faiz oranıdır. Bankalar arası karşılaştırma yapmak için en sağlıklı veridir."}
    ],
    "related_calculators": [
        {"title": "Konut Kredisi Hesaplama", "slug": "konut-kredisi-hesaplama", "url": "/konut-kredisi-hesaplama", "description": "Ev alırken kullanacağınız düşük vergi avantajlı krediyi hesaplayın."},
        {"title": "Mevduat Faizi Hesaplama", "slug": "mevduat-faizi-hesaplama", "url": "/mevduat-faizi-hesaplama", "description": "Paranızı bankaya yatırdığınızda ne kadar getiri alacağınızı öğrenin."},
        {"title": "Kredi Kartı Taksit Hesaplama", "slug": "kredi-karti-taksit-hesaplama", "url": "/kredi-karti-taksit-hesaplama", "description": "Kredi kartı harcamalarınızı taksitlendirmenin maliyetini bulun."}
    ]
}
