
import csv
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "csv"


class ProductService:

    def __init__(self):
        self.products = self._read_csv(
            "desafio_tecnico_ai_eng - products.csv"
        )
        self.categories = self._read_csv(
            "desafio_tecnico_ai_eng - categories.csv"
        )

    def _read_csv(self, filename: str) -> list[dict]:
        path = DATA_DIR / filename

        with path.open("r", encoding="utf-8-sig", newline="") as file:
            return list(csv.DictReader(file))

    def search_products(
        self,
        name: str | None = None,
        category: str | None = None,
        available_only: bool = True,
    ) -> list[dict]:

        category_names = {
            item["category_id"]: item["name"]
            for item in self.categories
        }

        results = []

        for product in self.products:
            product_name = product["name"]
            category_name = category_names.get(
                product["category_id"], "Desconhecida"
            )

            if name and name.casefold() not in product_name.casefold():
                continue

            if category and category.casefold() not in category_name.casefold():
                continue

            stock = int(product["stock_quantity"])
            status = product["status"].lower()

            if available_only and (stock <= 0 or status != "active"):
                continue

            results.append({
                "product_id": product["product_id"],
                "name": product_name,
                "description": product["description"],
                "category": category_name,
                "price_brl": float(product["price_brl"]),
                "stock_quantity": stock,
                "status": status,
                "specs": product["specs"],
            })

        return results
