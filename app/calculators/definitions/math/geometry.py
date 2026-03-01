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
    "faq": [
        {"question": "Dairenin alanı nasıl hesaplanır?", "answer": "pi * r^2 formülü ile hesaplanır."}
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
