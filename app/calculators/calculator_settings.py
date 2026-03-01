
# HESAPLA.COM MERKEZİ KONTROL PANELİ
# ---------------------------------
# Bu dosya üzerinden istediğiniz hesaplamayı anında pasif (False) veya aktif (True) yapabilirsiniz.
# Bir hesaplama burada tanımlı değilse, varsayılan olarak AKTİF (True) kabul edilir.

CALCULATOR_STATUS = {
    # Örnek Kullanım:
    # "yuzde-hesaplama": False,          # Yüzde hesaplama artık anasayfada ve API'de görünmez.
    # "kredi-hesaplama": True,
    "ekpss-puan-hesaplama": False,
    "pomem-puan-hesaplama": False,
    "dgs-taban-puanlari-hesaplama": False,
    "ehliyet-sinavi-puan-hesaplama": False,
    "dib-mbsts-puan-hesaplama": False,   
    # Pasif yapmak istediğiniz hesaplamaları buraya ekleyin:
    
}

# KATEGORİ BAZLI KONTROL (Opsiyonel)
# ---------------------------------
# Bir kategoriyi komple kapatmak isterseniz burayı kullanabilirsiniz.
CATEGORY_STATUS = {
    # "Matematik": False,
    # "Sınav Puanı Hesaplama": True,
}
