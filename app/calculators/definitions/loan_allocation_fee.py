from app.calculators.logic.loan_allocation_fee import calculate_loan_expense

LOAN_FEE_CONFIG = {
    "id": "loan-fee",
    "slug": "kredi-dosya-masrafi-hesaplama",
    "category": "Kredi Hesaplama",
    "title": "Kredi Dosya Masrafı (Tahsis Ücreti) Hesaplama",
    "description": "Çekeceğiniz ihtiyaç, taşıt veya konut kredisi için bankanın en fazla ne kadar dosya masrafı alabileceğini BDDK limitleriyle hesaplayın.",
    "seo": {
        "meta_title": "Kredi Dosya Masrafı ve Tahsis Ücreti Hesaplama",
        "meta_description": "Bankam benden fazla dosya masrafı mı kesti? BDDK 2026 kurallarına göre yasal azami tahsis ücretini ve üzerine eklenen BSMV vergisini hesaplayın.",
        "meta_keywords": ["kredi dosya masrafı", "tahsis ücreti", "dosya masrafı hesaplama", "kredi kesintileri"],
        "schema_type": "SoftwareApplication",
    },
    "inputs": [
        {
            "name": "principal",
            "type": "number",
            "label": "Talep Edilen Kredi Miktarı (₺)",
            "placeholder": "Örnek: 250000",
            "required": True,
            "min": 1000
        }
    ],
    "logic_function": calculate_loan_expense,
    "faq": [
        {
            "question": "Banka yasal olarak en fazla ne kadar dosya masrafı kesebilir?",
            "answer": "Bankalar tüketicilerden 'Kredi Tahsis Ücreti' adı altında en fazla çekilen kredi tutarının binde beşi (%0.5) kadar dosya masrafı kesebilir."
        },
        {
            "question": "Dosya masrafından vergi alınır mı?",
            "answer": "Evet, bankanın aldığı %0.5'lik hizmet bedeli üzerinden %15 Banka ve Sigorta Muameleleri Vergisi (BSMV) tahsil edilerek devlete ödenir."
        }
    ]
}
