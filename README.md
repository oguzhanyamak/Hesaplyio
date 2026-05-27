# Hesaply.io

Hesaply.io; finans, kredi, kredi kartı, maaş, sınav puanı ve matematik alanlarında hızlı, sade ve SEO odaklı hesaplama araçları sunan FastAPI tabanlı bir web uygulamasıdır.

Canlı site: [https://www.hesaply.io/](https://www.hesaply.io/)

## Proje Özeti

Bu proje, kullanıcıların farklı alanlardaki hesaplama ihtiyaçlarını tek bir çatı altında karşılamak için geliştirilmiştir. Uygulama, sunucu tarafında render edilen sayfalar, dinamik hesaplayıcı kayıt sistemi, JSON tabanlı hesaplama API endpointleri ve arama motoru görünürlüğünü destekleyen teknik SEO çıktılarıyla yapılandırılmıştır.

Aktif hesaplayıcılar modüler dosya yapısıyla yönetilir. Her hesaplayıcı için ayrı tanım dosyası, giriş alanları, SEO meta bilgileri, açıklama bölümleri, SSS içerikleri ve hesaplama fonksiyonu bulunur.

## Öne Çıkan Özellikler

- 54 aktif hesaplama aracı
- FastAPI ile yüksek performanslı backend
- Jinja2 ile server-side rendered sayfalar
- Alpine.js ile hafif ve hızlı frontend etkileşimleri
- Tailwind CSS tabanlı responsive kullanıcı arayüzü
- Dinamik hesaplayıcı kayıt sistemi
- JSON API üzerinden anlık hesaplama
- Dinamik `sitemap.xml` ve `robots.txt`
- SEO meta tag, canonical URL, Open Graph ve Twitter Card desteği
- FAQPage JSON-LD structured data çıktısı
- GZip sıkıştırma ve statik dosyalar için cache header optimizasyonu
- Docker ile production deployment desteği


## Kullanılan Teknolojiler

| Katman | Teknoloji |
| --- | --- |
| Backend | Python, FastAPI |
| ASGI Server | Uvicorn |
| Production Server | Gunicorn + Uvicorn Worker |
| Template Engine | Jinja2 |
| Frontend Etkileşim | Alpine.js |
| Stil | Tailwind CSS |
| Validasyon / Ayar Yönetimi | Pydantic, Pydantic Settings |
| Deployment | Docker |

## Proje Yapısı

```text
.
├── app
│   ├── api
│   │   └── routes.py
│   ├── calculators
│   │   ├── definitions
│   │   ├── logic
│   │   ├── calculator_settings.py
│   │   └── registry.py
│   ├── static
│   │   └── robots.txt
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── calculator_page.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── privacy.html
│   ├── config.py
│   └── main.py
├── Dockerfile
├── requirements.txt
└── run.py
```

## Mimari Yaklaşım

### Dinamik Hesaplayıcı Sistemi

`app/calculators/registry.py`, `app/calculators/definitions` klasörünü tarayarak sonu `_CONFIG` ile biten hesaplayıcı konfigürasyonlarını otomatik olarak yükler. Bu sayede yeni bir hesaplayıcı eklemek için mevcut yapıya uygun yeni bir tanım dosyası oluşturmak yeterlidir.

Her hesaplayıcı konfigürasyonu genel olarak şu bilgileri içerir:

- `id`
- `slug`
- `category`
- `title`
- `description`
- `seo`
- `inputs`
- `logic_function`
- `sections`
- `faq`
- `related_calculators`

### Hesaplama Mantığı

Hesaplama fonksiyonları `app/calculators/logic` altında tutulur. Tanım dosyaları doğrudan ilgili logic fonksiyonunu referans alır. Böylece arayüz konfigürasyonu ile iş mantığı birbirinden ayrılmış olur.

### Sayfa Render Süreci

- Ana sayfa `/` route'u üzerinden tüm aktif hesaplayıcıları listeler.
- Hesaplayıcı sayfaları `/{calculator_slug}` route'u ile dinamik olarak oluşturulur.
- Form gönderimleri `/api/calculate/{calculator_slug}` endpointine JSON olarak yapılır.
- Sonuçlar sayfa yenilenmeden Alpine.js ile kullanıcıya gösterilir.

## Kurulum

### Gereksinimler

- Python 3.13 veya uyumlu güncel Python sürümü
- `pip`
- İsteğe bağlı olarak Docker

### Lokal Ortamda Çalıştırma

1. Sanal ortam oluşturun:

```bash
python -m venv venv
```

2. Sanal ortamı aktifleştirin:

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

3. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

4. Ortam değişkenlerini hazırlayın:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

5. Geliştirme sunucusunu başlatın:

```bash
python run.py
```

Uygulama varsayılan olarak şu adreste çalışır:

```text
http://127.0.0.1:8000
```

Alternatif olarak:

```bash
uvicorn app.main:app --reload
```

## Ortam Değişkenleri

`.env.example` dosyasında temel ortam değişkenleri yer alır:

```env
APP_NAME="Hesaply.io"
ENVIRONMENT="production"
DOMAIN="https://hesaply.io"
PORT=8080
DEBUG=False
```

| Değişken | Açıklama |
| --- | --- |
| `APP_NAME` | Uygulama adı |
| `ENVIRONMENT` | Çalışma ortamı |
| `DOMAIN` | Canonical URL, sitemap ve robots çıktılarında kullanılan domain |
| `PORT` | Production ortamında kullanılacak port |
| `DEBUG` | Debug durumu |

## API Kullanımı

Hesaplama işlemleri aşağıdaki endpoint üzerinden yapılır:

```http
POST /api/calculate/{calculator_slug}
```

Örnek istek:

```bash
curl -X POST http://127.0.0.1:8000/api/calculate/kredi-hesaplama \
  -H "Content-Type: application/json" \
  -d '{"principal":100000,"interest_rate":3.5,"term_months":24}'
```

Örnek cevap yapısı:

```json
{
  "status": "success",
  "data": {
    "summary": {
      "label": "Aylık Taksit",
      "value": 7050.25
    },
    "breakdown": [],
    "payment_plan": []
  }
}
```

## Yeni Hesaplayıcı Ekleme

1. `app/calculators/logic` altında hesaplama fonksiyonunu oluşturun.
2. `app/calculators/definitions` altında yeni bir tanım dosyası ekleyin.
3. Tanım dosyasında `_CONFIG` ile biten bir sözlük oluşturun.
4. `slug`, `category`, `title`, `inputs` ve `logic_function` alanlarını doldurun.
5. Gerekirse `seo`, `sections`, `faq` ve `related_calculators` alanlarını ekleyin.
6. Hesaplayıcının aktif/pasif durumunu `app/calculators/calculator_settings.py` üzerinden yönetin.

Örnek konfigürasyon iskeleti:

```python
from app.calculators.logic.example import calculate_example

EXAMPLE_CONFIG = {
    "id": "example",
    "slug": "ornek-hesaplama",
    "category": "Matematik",
    "title": "Örnek Hesaplama",
    "description": "Kısa açıklama.",
    "inputs": [
        {
            "name": "value",
            "type": "number",
            "label": "Değer",
            "required": True
        }
    ],
    "logic_function": calculate_example,
    "faq": []
}
```

## Docker ile Çalıştırma

Docker imajını oluşturun:

```bash
docker build -t hesaply .
```

Container'ı başlatın:

```bash
docker run -p 8080:8080 --env-file .env hesaply
```

Production komutu Dockerfile içinde Gunicorn ve Uvicorn worker ile tanımlıdır:

```bash
gunicorn --bind 0.0.0.0:$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker app.main:app
```

## SEO ve Performans Çalışmaları

Projede arama motoru görünürlüğü ve sayfa performansı için aşağıdaki çalışmalar yapılmıştır:

- Dinamik `sitemap.xml` üretimi
- Arama motorları için `robots.txt` çıktısı
- Canonical URL kullanımı
- Sayfa bazlı meta title ve meta description
- Open Graph ve Twitter Card meta etiketleri
- FAQ içerikleri için JSON-LD structured data
- Statik dosyalar için uzun süreli cache header
- GZip sıkıştırma
- Google Analytics'in gecikmeli yüklenmesi
- Font, CDN ve Google Tag Manager için preconnect / dns-prefetch optimizasyonları
- Mobil uyumlu responsive arayüz

## Kazanımlar

Bu proje kapsamında aşağıdaki konularda pratik deneyim kazanılmıştır:

- FastAPI ile üretime uygun web uygulaması geliştirme
- Jinja2 template yapısıyla SEO dostu sayfa üretimi
- Alpine.js ile sade ve hızlı frontend etkileşimleri oluşturma
- Modüler hesaplayıcı mimarisi tasarlama
- Finans, sınav, maaş ve matematik alanlarında hesaplama algoritmaları geliştirme
- Dinamik sitemap ve robots çıktılarıyla teknik SEO uygulamaları
- Google Analytics entegrasyonu ve ölçümleme mantığı
- Google Search Console üzerinden indeksleme, sitemap gönderimi ve arama performansı takibi
- PageSpeed Insights ile performans, erişilebilirlik, SEO ve best practices analizleri
- Core Web Vitals odaklı frontend optimizasyonları
- Docker ile deployment süreci hazırlama
- Production ortamında Gunicorn + Uvicorn worker kullanımı

