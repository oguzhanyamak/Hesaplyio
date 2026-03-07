from app.calculators.logic.math.geometry import calculate_area_perimeter, calculate_volume

ALAN_CONFIG = {
    "id": "alan", "slug": "alan-hesaplama", "category": "Matematik", "title": "Alan Hesaplama",
    "description": "Kare, dikdörtgen, daire ve üçgen alanını hızlıca hesaplayın.",
    "seo": {
        "meta_title": "Alan Hesaplama | Kare, Dikdörtgen, Daire ve Üçgen",
        "meta_description": "Geometrik şekillerin alanını hesaplayan online araç. Kare, daire, üçgen ve dikdörtgen alan formülleri.",
        "meta_keywords": ["alan hesabı", "kare alanı", "daire alanı hesapla"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_area_perimeter,
    "inputs": [
        {"name": "shape", "type": "select", "label": "Şekil Seçin", "options": [
            {"label": "Kare", "value": "square"},
            {"label": "Dikdörtgen", "value": "rectangle"},
            {"label": "Daire", "value": "circle"},
            {"label": "Üçgen", "value": "triangle"}
        ], "default": "square"},
        {"name": "dimension1", "type": "number", "label": "Boyut 1 (Kenar / r / Taban)", "required": True},
        {"name": "dimension2", "type": "number", "label": "Boyut 2 (Eksikse 0)", "default": 0},
        {"name": "dimension3", "type": "number", "label": "Boyut 3 (Eksikse 0)", "default": 0}
    ],
    "sections": [
        {
            "title": "Alan Hesaplama Nasıl Yapılır?",
            "content": """
                <p>Alan hesaplama, iki boyutlu bir şeklin yüzeyinin ne kadar yer kapladığını ölçme işlemidir. Her geometrik şeklin kendine has bir alan formülü vardır. En temel birim <strong>metrekare (m²)</strong> olarak kabul edilir.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <strong class="text-blue-600">Kare:</strong> Kenar &times; Kenar
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <strong class="text-blue-600">Dikdörtgen:</strong> Uzun Kenar &times; Kısa Kenar
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <strong class="text-blue-600">Daire:</strong> &pi; &times; r<sup>2</sup>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <strong class="text-blue-600">Üçgen:</strong> (Taban &times; Yükseklik) / 2
                    </div>
                </div>
            """
        }
    ],
    "faq": [
        {"question": "Dairenin alanı nasıl hesaplanır?", "answer": "Dairenin alanı, Pi sayısı (yaklaşık 3,14) ile yarıçapın karesinin çarpılmasıyla bulunur. Formül: π.r²"},
        {"question": "Üçgenin alanı için yükseklik şart mı?", "answer": "Evet, temel formül (taban * yükseklik / 2) yüksekliği gerektirir. Ancak kenar uzunlukları biliniyorsa 'Heron Formülü' ile de hesaplanabilir."},
        {"question": "Alan birimleri arası dönüşüm nasıl yapılır?", "answer": "Birimler karesel olduğu için her basamakta 100 ile çarpılır veya bölünür. Örn: 1 m² = 10.000 cm²."},
        {"question": "Yamuk alanı nasıl hesaplanır?", "answer": "Alt taban ile üst taban toplanır, yükseklik ile çarpılır ve ikiye bölünür."},
        {"question": "Dikdörtgen alanı ile çevresi arasındaki fark nedir?", "answer": "Alan yüzeyi (iç kısmı), çevre ise şekli çevreleyen çizgilerin toplam uzunluğunu (dış sınırı) ifade eder."}
    ],
    "related_calculators": [
        {"title": "Çevre Hesaplama", "slug": "cevre-hesaplama", "url": "/cevre-hesaplama", "description": "Şekillerin çevre uzunluklarını hesaplayın."},
        {"title": "Hacim Hesaplama", "slug": "hacim-hesaplama", "url": "/hacim-hesaplama", "description": "Üç boyutlu nesnelerin hacmini bulun."},
        {"title": "Pisagor Hesaplama", "slug": "pisagor-hesaplama", "url": "/pisagor-hesaplama", "description": "Dik üçgen kenar bağıntılarını hesaplayın."}
    ]
}

CEVRE_CONFIG = {
    "id": "cevre", "slug": "cevre-hesaplama", "category": "Matematik", "title": "Çevre Hesaplama",
    "description": "Her türlü geometrik şeklin çevre uzunluğunu anında bulun.",
    "seo": {
        "meta_title": "Çevre Hesaplama | Geometrik Şekiller",
        "meta_description": "Online çevre hesaplama motoru. Kare, dikdörtgen, daire ve üçgenlerin çevre uzunluklarını bulun.",
        "meta_keywords": ["çevre hesabı", "daire çevresi", "üçgen çevresi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_area_perimeter,
    "inputs": [
        {"name": "shape", "type": "select", "label": "Şekil Seçin", "options": [
            {"label": "Kare", "value": "square"},
            {"label": "Dikdörtgen", "value": "rectangle"},
            {"label": "Daire", "value": "circle"},
            {"label": "Üçgen", "value": "triangle"}
        ], "default": "square"},
        {"name": "dimension1", "type": "number", "label": "Kenar / r / Taban", "required": True},
        {"name": "dimension2", "type": "number", "label": "Kenar 2 (Üçgen İçin)", "default": 0},
        {"name": "dimension3", "type": "number", "label": "Kenar 3 (Üçgen İçin)", "default": 0}
    ],
    "faq": [
        {"question": "Karenin çevresi nasıl bulunur?", "answer": "Bir kenar uzunluğunun 4 ile çarpılması ile bulunur."}
    ]
}

HACIM_CONFIG = {
    "id": "hacim", "slug": "hacim-hesaplama", "category": "Matematik", "title": "Hacim Hesaplama",
    "description": "Küp, prizma, küre ve silindir hacimlerini formüle gerek duymadan bulun.",
    "seo": {
        "meta_title": "Hacim Hesaplama | Küp, Küre ve Silindir",
        "meta_description": "Üç boyutlu nesnelerin hacmini hesaplayan online motor. Küp, silindir ve küre hacim formülleri.",
        "meta_keywords": ["hacim hesabı", "silindir hacmi", "küre hacmi"],
        "schema_type": "SoftwareApplication"
    },
    "logic_function": calculate_volume,
    "inputs": [
        {"name": "shape", "type": "select", "label": "Şekil Seçin", "options": [
            {"label": "Küp", "value": "cube"},
            {"label": "Dikdörtgen Prizma", "value": "prism"},
            {"label": "Küre", "value": "sphere"},
            {"label": "Silindir", "value": "cylinder"}
        ], "default": "cube"},
        {"name": "d1", "type": "number", "label": "Yarıçap / Kenar 1", "required": True},
        {"name": "d2", "type": "number", "label": "Yükseklik / Kenar 2", "default": 0},
        {"name": "d3", "type": "number", "label": "Derinlik / Kenar 3", "default": 0}
    ],
    "faq": [
        {"question": "Hacim birimi nedir?", "answer": "Genellikle metreküp (m³) veya santimetreküp (cm³) olarak ifade edilir."}
    ]
}
