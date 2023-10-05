"""Основные классы и сущности."""

import json


class Valute:
    def __init__(self, name: str, symbol: str, priceUSD: str, capitalize: float):
        self.name = name
        self.symbol = symbol
        self.priceUSD = float(str(priceUSD)[1:].replace(",", ""))
        self.capitalize = capitalize

    def __repr__(self):
        return f"<Valute {self.name} {self.priceUSD}>"

    def to_json(self):
        return json.dumps({"name": self.name, "symbol": self.symbol, "price": self.priceUSD, "active": True})
