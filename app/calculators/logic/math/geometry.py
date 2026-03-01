import math

def calculate_area_perimeter(shape: str, dimension1: float | str, dimension2: float | str = 0, dimension3: float | str = 0) -> dict:
    try:
        d1 = float(dimension1)
        d2 = float(dimension2)
        d3 = float(dimension3)
    except ValueError:
        raise ValueError("Lütfen geçerli sayısal değerler girin.")

    area = 0
    perimeter = 0
    label = ""
    
    if shape == "square":
        area = d1 * d1
        perimeter = 4 * d1
        label = f"Kare (Kenar: {d1})"
    elif shape == "rectangle":
        area = d1 * d2
        perimeter = 2 * (d1 + d2)
        label = f"Dikdörtgen (Kenarlar: {d1}, {d2})"
    elif shape == "circle":
        area = math.pi * (d1 ** 2)
        perimeter = 2 * math.pi * d1
        label = f"Daire (Yarıçap: {d1})"
    elif shape == "triangle":
        # Using Heron for area if d3 > 0, else base * height / 2 (d2 as height)
        if d3 > 0:
            s = (d1 + d2 + d3) / 2
            if s <= d1 or s <= d2 or s <= d3:
                return {"status": "error", "message": "Geçersiz üçgen kenarları."}
            area = math.sqrt(s * (s - d1) * (s - d2) * (s - d3))
            perimeter = d1 + d2 + d3
            label = f"Üçgen (Kenarlar: {d1}, {d2}, {d3})"
        else:
            area = (d1 * d2) / 2
            # Perimeter not possible with just base/height easily
            perimeter = 0
            label = f"Üçgen (Taban: {d1}, Yükseklik: {d2})"
            
    return {
        "summary": { "label": f"{label} Sonucu", "value": f"Alan: {round(area, 4)}, Çevre: {round(perimeter, 4)}" },
        "breakdown": [
            {"label": "Şekil", "value": label},
            {"label": "Alan", "value": round(area, 4)},
            {"label": "Çevre", "value": round(perimeter, 4)}
        ]
    }

def calculate_volume(shape: str, d1: float | str, d2: float | str = 0, d3: float | str = 0) -> dict:
    try:
        v1 = float(d1)
        v2 = float(d2)
        v3 = float(d3)
    except ValueError:
        raise ValueError("Lütfen geçerli sayısal değerler girin.")
        
    volume = 0
    label = ""
    
    if shape == "cube":
        volume = v1 ** 3
        label = f"Küp (Kenar: {v1})"
    elif shape == "prism":
        volume = v1 * v2 * v3
        label = f"Prizma ({v1}, {v2}, {v3})"
    elif shape == "sphere":
        volume = (4/3) * math.pi * (v1 ** 3)
        label = f"Küre (Yarıçap: {v1})"
    elif shape == "cylinder":
        volume = math.pi * (v1 ** 2) * v2
        label = f"Silindir (r: {v1}, h: {v2})"
        
    return {
        "summary": { "label": f"{label} Hacmi", "value": round(volume, 4) },
        "breakdown": [{"label": "Hacim", "value": round(volume, 4)}]
    }
