from app.calculators.logic.math.util import calculate_random, calculate_number_to_words

RANDOM_CONFIG = {
    "id": "random_num", "slug": "rastgele-sayi-hesaplama", "category": "Matematik", "title": "Rastgele Sayı Üretici",
    "description": "İstenen aralıkta tamamen rastgele tamsayılar üretin.",
    "seo": {
        "meta_title": "Rastgele Sayı Üretici | Online Random Number Generator",
        "meta_description": "Belirlediğiniz aralıkta rastgele sayılar üreten ücretsiz online araç.",
        "meta_keywords": ["rastgele sayı", "random sayı üret"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_random,
    "inputs": [
        {"name": "min_val", "type": "number", "label": "Alt Sınır", "default": 1},
        {"name": "max_val", "type": "number", "label": "Üst Sınır", "default": 100},
        {"name": "count", "type": "number", "label": "Üretilecek Adet", "default": 1}
    ],
    "faq": [
        {"question": "Sayılar gerçekten rastgele mi?", "answer": "Evet, Python'un güvenli rastgele sayı üreticisi kullanılmaktadır."}
    ]
}

WORDS_CONFIG = {
    "id": "num_to_words", "slug": "sayi-okunusu-hesaplama", "category": "Matematik", "title": "Sayı Okunuşu",
    "description": "Rakamla yazılan bir sayının yazı ile okunuşunu anında öğrenin.",
    "seo": {
        "meta_title": "Sayıyı Yazıya Çevirme | Sayı Okunuşu Hesapla",
        "meta_description": "Rakamla girilen sayıların Türkçe okunuşunu ve yazı ile yazılışını gösteren araç.",
        "meta_keywords": ["sayı okunuşu", "rakamı yazıya çevir"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_number_to_words,
    "inputs": [
        {"name": "n", "type": "number", "label": "Sayı", "required": True}
    ],
    "sections": [
        {
            "title": "Sayıları Yazıya Çevirme Nerede Kullanılır?",
            "content": """
                <p>Rakamların yazı ile ifade edilmesi (sayı okunuşu), özellikle resmi belgelerde, çek ve senet işlemlerinde veya fatura keserken büyük önem taşır. Hatalı yazılan bir rakam maddi kayıplara yol açabileceği için bu işlem titizlikle yapılmalıdır.</p>
                <h3 class="text-xl font-bold text-slate-800 mt-6 mb-3">Türkçe Sayı Yazım Kuralları</h3>
                <ul class="list-disc ml-6 space-y-2 mt-4">
                    <li>Sayılar genellikle ayrı yazılır (Örn: On beş).</li>
                    <li>Çek, senet gibi ticari belgelerde bitişik yazılır (Örn: Onbeş).</li>
                    <li>Parasal değerlerde kuruş kısımları da belirtilmelidir.</li>
                </ul>
            """
        }
    ],
    "faq": [
        {"question": "Sayıları yazıya çevirirken nelere dikkat edilmeli?", "answer": "Özellikle bankacılık ve muhasebe işlemlerinde, sayının sonuna 'Yalnız' ibaresi eklenmesi ve bitişik yazılması güvenlik sağlar."},
        {"question": "Kaç basamağa kadar destekliyor?", "answer": "Sistemimiz şu an için 1 trilyon (12 basamak) sınırına kadar tüm sayıların Türkçe okunuşunu desteklemektedir."},
        {"question": "Ondalıklı sayıları yazıya çevirebilir mi?", "answer": "Evet, virgüllü kısımları 'nokta' veya 'virgül' olarak ayırarak okunuşunu öğrenebilirsiniz."},
        {"question": "Sayıların yazımı ayrı mı olmalı?", "answer": "TDK kurallarına göre oyun adları ve çek/senet işlemleri hariç sayılar daima ayrı yazılmalıdır."},
        {"question": "Çek senet kapama işlemi nedir?", "answer": "Yazılan sayının başına ve sonuna '#' veya '*' gibi işaretler konularak araya rakam eklenmesini önleme işlemidir."}
    ],
    "related_calculators": [
        {"title": "Yüzde Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Oransal hesaplamalarınızı hızlandırın."},
        {"title": "Kredi Hesaplama", "slug": "kredi-hesaplama", "url": "/kredi-hesaplama", "description": "Taksit tutarlarını yazı ile kontrol edin."},
        {"title": "KDV Hesaplama", "slug": "yuzde-hesaplama", "url": "/yuzde-hesaplama", "description": "Faturalarınız için KDV dâhil ve hariç tutarları bulun."}
    ]
}
