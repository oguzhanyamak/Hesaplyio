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
    "faq": [
        {
            "question": "İhtiyaç kredisi taksitleri nasıl hesaplanır?",
            "answer": "İhtiyaç kredisi taksitleri, ana para üzerine banka faizi, %15 KKDF ve %5 BSMV vergileri eklenerek bulunan 'toplam faiz oranı' üzerinden her ay kalan ana paraya işletilerek hesaplanır."
        },
        {
            "question": "En uygun kredi vadesi ne kadardır?",
            "answer": "En uygun vade, aylık gelirinize göre belirlenmelidir. Vade uzadıkça aylık taksitler düşer ancak bankaya ödeyeceğiniz toplam faiz maliyeti artar. Genellikle 24 veya 36 ay ideal dengedir."
        },
        {
            "question": "Kredi hesaplamasında KKDF ve BSMV nedir?",
            "answer": "KKDF (Kaynak Kullanımını Destekleme Fonu) %15, BSMV (Banka ve Sigorta Muameleleri Vergisi) %10 (ihtiyaç kredilerinde) oranında faiz üzerinden alınan devlet vergileridir."
        },
        {
            "question": "Dosya masrafı kredi taksitini etkiler mi?",
            "answer": "Dosya masrafı genellikle kredi başında peşin (veya kredi tutarından düşülerek) alınır. Aylık taksit tutarlarını doğrudan değiştirmez ancak projenin toplam maliyetini (Yıllık Maliyet Oranı) etkiler."
        },
        {
            "question": "Kredi erken kapatma cezası var mıdır?",
            "answer": "İhtiyaç kredilerinde erken kapatma veya ara ödeme cezası (erken ödeme tazminatı) bulunmamaktadır. Kalan anapara üzerinden borcunuzu kapatarak faizden tasarruf edebilirsiniz."
        }
    ]
}
