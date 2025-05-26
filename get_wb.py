import requests
from typing import Optional, Dict


def get_wb_info(article: str) -> Optional[Dict[str, str]]:

    url = f"https://card.wb.ru/cards/detail"
    params = {
        "appType": 1,
        "curr": "rub",
        "dest": "-1257786",
        "spp": 30,
        "nm": article
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        products = data.get("data", {}).get("products")
        if not products:
            return None

        product = products[0]
        name = product.get("name")
        price = product.get("salePriceU") or product.get("priceU")
        price_rub = price / 100 if price else None

        return {"name": name, "price": f"{price_rub:.2f} ₽"} if name and price else None

    except (requests.RequestException, ValueError, KeyError):
        return None


