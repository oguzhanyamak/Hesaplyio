from app.calculators.logic.mortgage_loan import calculate_mortgage_loan

MORTGAGE_LOAN_CONFIG = {
    "id": "mortgage-loan",
    "slug": "konut-kredisi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Konut Kredisi Hesaplama",
    "description": "Ev sahibi olmak isteyenler için %0 BSMV ve KKDF (vergisiz) konut kredisi taksit hesaplama aracı ve ödeme tablosu.",
    "seo": {
        "meta_title": "Konut Kredisi Hesaplama 2026 | Taksit Ödeme Planı",
        "meta_description": "2026 konut kredisi faiz oranlarıyla aylık taksit hesaplama. 120 ay veya 240 ay vadeli ev kredisi ödeme planı ve toplam maliyet hesabı.",
        "meta_keywords": ["konut kredisi hesaplama", "ev kredisi", "kredi ödeme planı", "ev kredisi faizi", "vergisiz kredi"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Kredi Tutarı (₺)",
            "placeholder": "Örnek: 2000000",
            "required": True,
            "min": 10000, 
            "tooltip": "Satın alacağınız evin tutarı değil, çekeceğiniz kredi tutarı"
        },
        {
            "name": "interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Aylık Faiz Oranı (%)",
            "placeholder": "Örnek: 2.80",
            "required": True,
            "min": 0,
            "tooltip": "Bankanın sunduğu konut kredisi aylık faiz oranı"
        },
        {
            "name": "term_months",
            "type": "number",
            "label": "Vade (Ay)",
            "placeholder": "Örnek: 120",
            "required": True,
            "min": 1,
            "max": 240,
            "tooltip": "Genellikle konut kredilerinde 120 veya 240 aya kadar çıkar"
        }
    ],
    "logic_function": calculate_mortgage_loan,
    "faq": [
        {
            "question": "Konut kredisinde vergi kesintisi neden yok?",
            "answer": "Türkiye'de konut alımını desteklemek amacıyla, gerçek kişilerin alacağı konut kredilerinde %15 KKDF ve %5 BSMV vergileri sıfır (0) olarak uygulanır. Bu durum konut kredisini diğer kredilerden daha maliyet-avantajlı kılar."
        },
        {
            "question": "Konut kredisi peşinat oranları nedir?",
            "answer": "BDDK kuralları çerçevesinde, evin enerji sınıfına ve değerine göre değişmekle birlikte genellikle evin ekspertiz değerinin %80'ine kadar kredi kullandırılabilir. %20 peşinat standart kabul edilir."
        },
        {
            "question": "Konut kredisinde hayat sigortası zorunlu mu?",
            "answer": "Yasal olarak zorunlu değildir ancak bankalar kredi riskini minimize etmek için genellikle hayat sigortasını şart koşarlar. Hayat sigortası yaptırmamanız durumunda faiz oranı yükselebilir."
        },
        {
            "question": "Ekspertiz ücretini banka mı öder?",
            "answer": "Hayır, gayrimenkul değerleme (ekspertiz) ücreti bankanın anlaştığı bağımsız firmalara ödenir ve bu masraf kredi kullanıcısı tarafından karşılanır."
        },
        {
            "question": "Konut kredisi yapılandırma avantajlı mıdır?",
            "answer": "Piyasadaki faiz oranları düştüğünde konut kredinizi yapılandırarak (refinansman) aylık taksitlerinizi düşürebilirsiniz. Ancak erken kapatma komisyonlarını da hesaba katmalısınız."
        }
    ]
}
