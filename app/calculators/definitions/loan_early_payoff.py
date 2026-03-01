from app.calculators.logic.loan_early_payoff import calculate_loan_early_payoff

LOAN_EARLY_PAYOFF_CONFIG = {
    "id": "early-payoff",
    "slug": "kredi-erken-kapatma-cezasi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Kredi Erken Kapatma Cezası ve İndirimi",
    "description": "Kredinizi erken veya toplu kapatırsanız ne kadar faiz indirimi alacağınızı ve olası kapama cezalarını anında görün.",
    "seo": {
        "meta_title": "Kredi Erken Kapatma Cezası ve İndirimi Hesaplama 2026",
        "meta_description": "İhtiyaç veya konut kredimi erken kapatırsam ne kadar kâr ederim? Tüketici kredisi erken kapama indirimi hesaplama ve ceza hesabı.",
        "meta_keywords": ["kredi erken kapatma", "erken kapama cezası", "faiz indirimi hesaplama", "konut kredisi kapama"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Tüm Kredinin Başlangıç Tutarı (₺)",
            "placeholder": "Örnek: 100000",
            "required": True,
            "min": 1000, 
            "tooltip": "Krediyi çekerken elinize geçen asli rakam."
        },
        {
            "name": "total_installments",
            "type": "number",
            "label": "Toplam Çekilen Vade",
            "placeholder": "Örnek: 36",
            "required": True,
            "min": 1
        },
        {
            "name": "remaining_months",
            "type": "number",
            "label": "Ödenmemiş (Kalan) Vade Ayı",
            "placeholder": "Örnek: 24",
            "required": True,
            "min": 1,
            "tooltip": "Ödeyip kurtulmak istediğiniz aylar"
        },
        {
            "name": "current_interest_rate",
            "type": "number",
            "step": "0.01",
            "label": "Kredi Faiz Oranı (%)",
            "placeholder": "Örnek: 2.50",
            "required": True,
            "min": 0,
        }
    ],
    "logic_function": calculate_loan_early_payoff,
    "faq": [
        {
            "question": "İhtiyaç kredisini erken kapatınca ceza ödenir mi?",
            "answer": "Hayır. Tüketici Kanununa göre, bireysel ihtiyaç ta taşıt kredilerini vadesinden önce ödeyen müşteriden banka erken kapama cezası, tazminatı veya komisyonu talep edemez."
        },
        {
            "question": "Konut kredisi erken ödeme cezası yüzde kaç?",
            "answer": "Konut finansmanında banka size yasal sınır olan kalan vadesi 36 ayın altına düşenlerde %1, kalan vadesi 36 ayı aşanlarda ise %2 erken ödeme ücreti (cezası) yansıtabilir."
        }
    ]
}
