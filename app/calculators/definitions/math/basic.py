from app.calculators.logic.math.basic_ops import calculate_percentage, calculate_power, calculate_root, calculate_factorial

YUZDE_CONFIG = {
    "id": "yuzde", "slug": "yuzde-hesaplama", "category": "Matematik", "title": "Yüzde Hesaplama",
    "description": "Her türlü yüzde artış, azalış ve oran hesaplamalarını anında yapın. Pratik, hızlı ve ücretsiz yüzde hesaplama motoru.",
    "seo": {
        "meta_title": "Yüzde Hesaplama | 2026 Pratik Yüzde Hesaplama Motoru",
        "meta_description": "Yüzde hesaplama aracı ile bir sayının yüzdesini bulma, yüzde artış ve azalış işlemlerini kolayca yapın. Formüller ve pratik örneklerle yüzde hesapla.",
        "meta_keywords": ["yüzde hesaplama", "yüzde hesapla", "yüzde kaçı", "yüzde artış hesaplama", "indirim hesaplama"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_percentage,
    "inputs": [
        {"name": "val", "type": "number", "label": "Sayı", "required": True, "placeholder": "Örn: 500"},
        {"name": "pct", "type": "number", "label": "Yüzde Oranı (%)", "required": True, "placeholder": "Örn: 20"},
        {"name": "operation", "type": "select", "label": "İşlem Türü", "options": [
            {"label": "Sayının yüzde %X'ini hesapla", "value": "calculate"},
            {"label": "Sayıyı yüzde %X artır", "value": "add"},
            {"label": "Sayıyı yüzde %X azalt", "value": "subtract"},
            {"label": "A sayısı B sayısının yüzde kaçıdır?", "value": "change"}
        ], "default": "calculate"}
    ],
    "sections": [
        {
            "title": "Yüzde Hesaplama Nasıl Yapılır?",
            "content": """
                <p>Yüzde hesaplama, bir bütünün 100 eş parçaya bölündüğünü varsayarak bu parçalardan ne kadarına sahip olduğumuzu ifade etme yöntemidir. Matematiksel olarak sembolü <strong>%</strong> olan bu işlem, hayatın her alanında karşımıza çıkar.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Temel Yüzde Formülü</h3>
                <p>Bir <strong>A</strong> sayısının <strong>%B</strong>'sini bulmak için şu formül kullanılır:</p>
                <div class="bg-blue-50 p-4 rounded-xl font-mono text-blue-800 my-4 text-center">
                    Sonuç = (A &times; B) / 100
                </div>
                <p>Örneğin; 500 sayısının %20'sini hesaplamak için 500 ile 20 çarpılır (10.000) ve sonuç 100'e bölünür (100). Bu işlem, 500'ü 5'e bölmekle aynı mantığa sahiptir.</p>
            """
        },
        {
            "title": "Pratik Yüzde Hesaplama Örnekleri",
            "content": """
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">%10 İndirim Hesaplama</h4>
                        <p class="text-sm">1.000 TL'lik bir üründe %10 indirim varsa: (1000 &times; 10) / 100 = 100 TL indirim yapılır. Ödenecek tutar 900 TL olur.</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">Maaş Artışı Hesaplama</h4>
                        <p class="text-sm">40.000 TL maaş alan birine %25 zam yapılırsa: (40000 &times; 25) / 100 = 10.000 TL zam gelir. Yeni maaş 50.000 TL olur.</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">%20 KDV Hesaplama</h4>
                        <p class="text-sm">500 TL + KDV olan bir faturada: (500 &times; 20) / 100 = 100 TL KDV eklenir. Toplam 600 TL olur.</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-5 rounded-2xl shadow-sm">
                        <h4 class="font-bold text-blue-600 mb-2">Oran Bulma (Yüzde Kaçıdır?)</h4>
                        <p class="text-sm">200 sayısı 800'ün yüzde kaçıdır? (200 / 800) &times; 100 = %25.</p>
                    </div>
                </div>
            """
        },
        {
            "title": "Yüzde Hesaplamanın Günlük Hayattaki Kullanım Alanları",
            "content": """
                <p>Yüzde hesaplamaları sadece matematik derslerinde değil, günlük kararlarımızda da kritik rol oynar:</p>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li><strong>Alışveriş:</strong> Mağazalardaki "ikinci ürüne %50 indirim" gibi kampanyaları değerlendirirken.</li>
                    <li><strong>Ekonomi:</strong> Enflasyon oranları, maaş zamları ve döviz değişimlerini takip ederken.</li>
                    <li><strong>Vergiler:</strong> KDV, ÖTV, MTV gibi vergi dilimlerini hesaplarken.</li>
                    <li><strong>Yatırım:</strong> Banka mevduat faizleri veya borsa kağıtlarının getiri oranlarını analiz ederken.</li>
                    <li><strong>Mutfak:</strong> Yemek tariflerinde malzeme oranlarını ayarlarken.</li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "Yüzde nasıl hesaplanır?", "answer": "Bir sayının yüzdesini hesaplamak için o sayıyı yüzde oranı ile çarpıp ardından 100'e bölmeniz gerekir. Örn: 200'ün %10'u için 200*10/100 = 20."},
        {"question": "Bir sayının yüzde kaçı olduğunu nasıl bulurum?", "answer": "Küçük sayıyı büyük sayıya bölün ve sonucu 100 ile çarpın. Örn: 50, 200'ün yüzde kaçıdır? (50/200)*100 = %25."},
        {"question": "Yüzde artış nasıl hesaplanır?", "answer": "Mevcut sayıya, sayının belirlenen yüzde kadar eklenmesiyle bulunur. Örn: 100'ü %20 artırmak demek 100 + (100*0.20) = 120 demektir."},
        {"question": "İndirim yüzdesi nasıl hesaplanır?", "answer": "İndirim miktarını ürünün eski fiyatına bölün ve 100 ile çarpın. Böylece ürünün yüzde kaç indirimle satıldığını bulabilirsiniz."},
        {"question": "Hesap makinesinde yüzde nasıl yapılır?", "answer": "Hesap makinelerinde genellikle '%' tuşu bulunur. Sayıyı girip, çarpı tuşuna basıp, yüzde miktarını girdikten sonra % tuşuna basarsanız sonucu verir."},
        {"question": "KDV dahil hesaplama formülü nedir?", "answer": "KDV dahil fiyatı bulmak için; Ürün Fiyatı * (1 + KDV Oranı/100) işlemini yapabilirsiniz. Örn: 100 TL + %20 KDV için 100 * 1.20 = 120 TL."},
        {"question": "Tersten yüzde hesaplama (Yüzdeden sayıyı bulma) nasıl yapılır?", "answer": "Yüzdesi verilen bir sayının tamamını bulmak için; Elinizdeki sayıyı 100 ile çarpıp yüzde oranına bölmelisiniz. Örn: %20'si 40 olan sayı: 40 * 100 / 20 = 200."}
    ],
    "related_calculators": [
        {"title": "KDV Hesaplama", "slug": "kdv-hesaplama", "url": "/kdv-hesaplama", "description": "Katma Değer Vergisi dâhil ve hariç tutarlarını hızlıca hesaplayın."},
        {"title": "Kredi Faiz Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Banka kredi faizlerini ve aylık ödeme planınızı detaylıca inceleyin."},
        {"title": "İndirim Hesaplama", "slug": "indirim-hesaplama", "url": "/indirim-hesaplama", "description": "Mağaza indirimlerini ve tasarruf edeceğiniz tutarı anında öğrenin."}
    ]
}

USLU_CONFIG = {
    "id": "uslu", "slug": "uslu-sayi-hesaplama", "category": "Matematik", "title": "Üslü Sayı Hesaplama",
    "description": "Bir sayının kuvvetini (ünsünü) hızlıca hesaplayın.",
    "seo": {
        "meta_title": "Üslü Sayı Hesaplama | Sayıların Kuvvetini Bul",
        "meta_description": "Herhangi bir sayının üssünü (kuvvetini) hesaplayan online araç.",
        "meta_keywords": ["üslü sayılar", "kuvvet hesaplama", "taban üs"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_power,
    "inputs": [
        {"name": "base", "type": "number", "label": "Taban", "required": True},
        {"name": "exponent", "type": "number", "label": "Üs (Kuvvet)", "required": True}
    ],
    "sections": [
        {
            "title": "Üslü Sayı Hesaplama Nasıl Yapılır?",
            "content": """
                <p>Üslü sayılar, bir sayının kendisiyle kaç kez çarpılacağını kısa yoldan göstermeye yarar. Bir sayının (taban) üzerine yazılan sayı (üs) kadar çarpılmasıdır. Örneğin <strong>2<sup>3</sup></strong> işlemi, 2 sayısının 3 kez çarpılması (2 &times; 2 &times; 2) anlamına gelir ve sonuç <strong>8</strong>'dir.</p>
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 font-serif text-lg text-center my-6">
                    A<sup>n</sup> = A &times; A &times; ... &times; A (n tane)
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Üslü sayılarda taban ve üs nedir?", "answer": "Taban, çarpılan sayıdır. Üs (kuvvet) ise tabanın kendisiyle kaç kere çarpılacağını ifade eder."},
        {"question": "Üslü sayıların günlük hayatta kullanımı nedir?", "answer": "Nüfus artış hızı, bileşik faiz hesapları, bilgisayar kapasite birimleri (Byte, KB, MB) gibi hızla büyüyen verilerde üslü sayılar kullanılır."},
        {"question": "Negatif sayıların üssü nasıl hesaplanır?", "answer": "Negatif bir sayının çift kuvveti pozitif, tek kuvveti ise negatiftir. Örn: (-2)^2 = 4, (-2)^3 = -8."},
        {"question": "0 üzeri 0 (0^0) kaçtır?", "answer": "Matematikte bu bir belirsizliktir, ancak birçok uygulama ve yazılımda işlem kolaylığı açısından 1 olarak kabul edilebilir."},
        {"question": "Üssün üssü nasıl hesaplanır?", "answer": "Bir üslü sayının tekrar üssü alınıyorsa üsler çarpılır. Örn: (2^3)^2 = 2^(3*2) = 2^6."}
    ],
    "related_calculators": [
        {"title": "Köklü Sayı Hesaplama", "slug": "koklu-sayi-hesaplama", "url": "/koklu-sayi-hesaplama", "description": "Üslü sayıların tersi olan kök alma işlemlerini yapın."},
        {"title": "Faktöriyel Hesaplama", "slug": "faktoryel-hesaplama", "url": "/faktoryel-hesaplama", "description": "Bir sayının faktöriyel değerini hızlıca bulun."},
        {"title": "Yüzde Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Her türlü yüzde ve artış hesaplamasını yapın."}
    ]
}

KOKLU_CONFIG = {
    "id": "koklu", "slug": "koklu-sayi-hesaplama", "category": "Matematik", "title": "Köklü Sayı Hesaplama",
    "description": "Karekök, küp kök veya herhangi bir dereceden kök hesaplayın.",
    "seo": {
        "meta_title": "Köklü Sayı Hesaplama | Karekök ve Küp Kök",
        "meta_description": "Online köklü sayı hesaplama motoru. Tüm derecelerden kök alma.",
        "meta_keywords": ["karekök hesapla", "küp kök", "kök derecesi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_root,
    "inputs": [
        {"name": "val", "type": "number", "label": "Sayı", "required": True},
        {"name": "degree", "type": "number", "label": "Kök Derecesi", "default": 2}
    ],
    "sections": [
        {
            "title": "Köklü Sayı Hesaplama Mantığı",
            "content": """
                <p>Köklü sayılar, üslü sayıların tersi olarak düşünülebilir. Bir sayının hangi sayının karesi, küpü veya n. kuvveti olduğunu bulma işlemine <strong>kök alma</strong> denir. En yaygın kullanılanı, derecesi 2 olan <strong>karekök</strong> işlemidir.</p>
                <div class="bg-blue-50 p-6 rounded-2xl border border-blue-100 text-center my-6">
                    <p class="text-2xl">&radic;X = Y ise Y<sup>2</sup> = X'tir.</p>
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Karekök dışına çıkarma işlemi nasıl yapılır?", "answer": "Bir sayıyı tam kare çarpanlarına ayırarak dışarı çıkarabilirsiniz. Örn: √20 = √(4*5) = 2√5."},
        {"question": "Küp kök ve dördüncü derece kök ne anlama gelir?", "answer": "Küp kök, hangi sayının kendisiyle 3 kere çarpımının bu sonucu verdiğini bulmaktır. Derece arttıkça çarpım sayısı artar."},
        {"question": "Negatif sayıların kökü alınabilir mi?", "answer": "Reel sayılarda çift dereceli köklerin içi negatif olamaz; ancak tek dereceli köklerin (küp kök gibi) içi negatif olabilir."},
        {"question": "İrrasyonel kök nedir?", "answer": "√2 veya √3 gibi tam sayı olarak dışarı çıkamayan sayılara irrasyonel köklü sayılar denir."},
        {"question": "Köklerin derecesi nasıl toplanır?", "answer": "Kök dereceleri ancak kök içleri ve dereceleri aynı ise (katsayılar toplanarak) toplanabilir."}
    ],
    "related_calculators": [
        {"title": "Üslü Sayı Hesaplama", "slug": "uslu-sayi-hesaplama", "url": "/uslu-sayi-hesaplama", "description": "Bir sayının kuvvetlerini hesaplayın."},
        {"title": "Faktöriyel Hesaplama", "slug": "faktoryel-hesaplama", "url": "/faktoryel-hesaplama", "description": "n! değerini tek tıkla bulun."},
        {"title": "Pisagor Hesaplama", "slug": "pisagor-hesaplama", "url": "/pisagor-hesaplama", "description": "Dik üçgende kenar uzunluklarını kolayca hesaplayın."}
    ]
}

FAKTORIYEL_CONFIG = {
    "id": "faktoryel", "slug": "faktoryel-hesaplama", "category": "Matematik", "title": "Faktöriyel Hesaplama",
    "description": "Bir sayının faktöriyelini (n!) tek tıkla bulun.",
    "seo": {
        "meta_title": "Faktöriyel Hesapla (n!) | Online Matematik Araçları",
        "meta_description": "0-1000 arası sayıların faktöriyelini anında hesaplayan online araç.",
        "meta_keywords": ["faktöriyel", "n faktöriyel", "matematik araçları"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_factorial,
    "inputs": [
        {"name": "n", "type": "number", "label": "Sayı (n)", "required": True, "min": 0, "max": 1000}
    ],
    "sections": [
        {
            "title": "Faktöriyel Hesaplama ve Kullanım Alanları",
            "content": """
                <p>Faktöriyel, 1'den n'ye kadar olan tüm pozitif tam sayıların çarpımıdır ve <strong>n!</strong> sembolüyle gösterilir. Faktöriyel değerleri, n arttıkça çok hızlı büyür. Matematikte olasılık ve istatistik hesaplamalarının temelidir.</p>
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 font-mono text-center my-6">
                    5! = 5 &times; 4 &times; 3 &times; 2 &times; 1 = 120
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Faktöriyel nerede kullanılır?", "answer": "Kombinasyon, permütasyon ve olasılık hesaplamalarında, bir grup nesnenin kaç farklı şekilde sıralanabileceğini bulmak için kullanılır."},
        {"question": "0 faktöriyel (0!) neden 1'dir?", "answer": "Matematiksel tutarlılık ve Boş Küme'nin tek bir dizilimi (hiçbir şey seçmeme) olduğu kabul edildiği için 0! = 1 olarak tanımlanmıştır."},
        {"question": "1000! neden hesaplanamıyor?", "answer": "1000! çok devasa bir sayıdır ve standart sayı türlerine sığmaz. Bilgisayar belleğinde yüzlerce basamak yer kaplar."},
        {"question": "Faktöriyel toplama ve çıkarma nasıl yapılır?", "answer": "Faktöriyel ifadeler genellikle küçük olanın parantezine alınarak ortak hale getirildikten sonra dört işlem yapılır."},
        {"question": "Gama fonksiyonu nedir?", "answer": "Gama fonksiyonu, faktöriyel kavramını tam sayılar dışındaki (ondalıklı ve karmaşık) sayılara genelleyen özel bir fonksiyondur."}
    ],
    "related_calculators": [
        {"title": "Kombinasyon Hesaplama", "slug": "kombinasyon-hesaplama", "url": "/kombinasyon-hesaplama", "description": "Öğeler arasından seçim yapma olasılıklarını bulun."},
        {"title": "Permütasyon Hesaplama", "slug": "permutasyon-hesaplama", "url": "/permutasyon-hesaplama", "description": "Sıralama dizilimlerini hesaplayın."},
        {"title": "Üslü Sayı Hesaplama", "slug": "uslu-sayi-hesaplama", "url": "/uslu-sayi-hesaplama", "description": "Üst alma işlemlerini yapın."}
    ]
}
