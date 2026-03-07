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
    "sections": [
        {
            "title": "Konut Kredisi Hesaplama ve Ev Sahibi Olma Süreci",
            "content": """
                <p>Konut kredisi (mortgage), hayalinizdeki eve sahip olmanız için bankalar tarafından uzun vadeli ve düşük faizli olarak sunulan bir kredi türüdür. Diğer kredi türlerinden en büyük farkı, KKDF ve BSMV gibi yasal vergilerden muaf olması ve alınan evin banka tarafından teminat (ipotek) olarak kabul edilmesidir.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Neden Konut Kredisi?</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li><strong>Vergi Avantajı:</strong> Bireysel konut kredilerinde %0 vergi uygulanır.</li>
                    <li><strong>Uzun Vade:</strong> 120, 180 hatta 240 aya varan vade seçenekleri mevcuttur.</li>
                    <li><strong>Sermaye Koruma:</strong> Tüm birikiminizi eve yatırmak yerine bir kısmını kredilendirerek nakit akışınızı koruyabilirsiniz.</li>
                </ul>
            """
        },
        {
            "title": "Konut Kredisi Masrafları Nelerdir?",
            "content": """
                <div class="bg-white border border-slate-200 p-6 rounded-2xl shadow-sm space-y-4">
                    <p>Kredi taksitlerinin yanı sıra, ev alırken şu masrafları da bütçenize dahil etmelisiniz:</p>
                    <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 bg-blue-600 rounded-full"></div> Ekspertiz Ücreti</li>
                        <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 bg-blue-600 rounded-full"></div> Tapu Harcı (%4)</li>
                        <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 bg-blue-600 rounded-full"></div> Kredi Tahsis Ücreti (%0.5)</li>
                        <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 bg-blue-600 rounded-full"></div> DASK ve Konut Sigortası</li>
                    </ul>
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Konut kredisinde vergi kesintisi neden yok?", "answer": "Türkiye'de konut alımını desteklemek amacıyla, bireysel konut kredilerinde %15 KKDF ve %5 BSMV vergileri sıfır (0) olarak uygulanır."},
        {"question": "Konut kredisi peşinat oranları nedir?", "answer": "Satın alınacak evin ekspertiz değerine ve enerji sınıfına göre değişmekle birlikte, genellikle %20 peşinat ödenmesi ve %80'ine kadar kredi kullandırılması beklenir."},
        {"question": "Konut kredisinde hayat sigortası zorunlu mu?", "answer": "Yasal olarak bir zorunluluk olmasa da bankalar kredi riskini yönetmek adına hayat sigortasını genellikle şart koşarlar. Sigortasız kredi seçeneklerinde faiz oranları daha yüksek olabilir."},
        {"question": "Ekspertiz ücretini banka mı öder?", "answer": "Değerleme (ekspertiz) hizmeti bağımsız firmalarca verilir ve ücreti kredi başvurusu yapan kişi tarafından karşılanır."},
        {"question": "Kaç yaşına kadar konut kredisi çekilebilir?", "answer": "Çoğu banka, kredi vadesi bittiğinde kişinin yaşının 70 veya 75'i geçmemesini şart koşar."},
        {"question": "İpotek ne zaman kalkar?", "answer": "Kredi borcunun tamamı ödendikten sonra bankadan alınan fek yazısı ile tapu dairesinde ipotek kaldırma işlemi yapılır."}
    ],
    "related_calculators": [
        {"title": "İhtiyaç Kredisi Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Küçük harcamalarınız için genel amaçlı kredi maliyetini bulun."},
        {"title": "Mevduat Getirisi Hesaplama", "slug": "mevduat-faizi-hesaplama", "url": "/mevduat-faizi-hesaplama", "description": "Birikimlerinizi değerlendirirken ne kadar kazanacağınızı görün."},
        {"title": "Kira Artış Oranı Hesaplama", "slug": "kira-artisi-hesaplama", "url": "/kira-artis-orani-hesaplama", "description": "Yasal sınırlara göre yeni kira bedelinizi belirleyin."}
    ]
}
