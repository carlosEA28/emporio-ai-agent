
import csv
from decimal import Decimal, ROUND_HALF_UP

from services.product_service import DATA_DIR, ProductService


class PromotionService:

    def __init__(self):
        self.product_service = ProductService()

        path = DATA_DIR / "desafio_tecnico_ai_eng - promotions.csv"

        with path.open("r", encoding="utf-8-sig", newline="") as file:
            self.promotions = list(csv.DictReader(file))

    def search_promotions(
        self,
        product_name: str | None = None,
        category: str | None = None,
        active_only: bool = True,
    ) -> list[dict]:

        products_by_id = {
            product["product_id"]: product
            for product in self.product_service.products
        }

        categories_by_id = {
            item["category_id"]: item["name"]
            for item in self.product_service.categories
        }

        results = []

        for promotion in self.promotions:
            product = products_by_id.get(promotion["product_id"])

            if product is None:
                continue

            category_name = categories_by_id.get(
                product["category_id"], "Desconhecida"
            )

            if product_name and (
                product_name.casefold() not in product["name"].casefold()
            ):
                continue

            if category and (
                category.casefold() not in category_name.casefold()
            ):
                continue

            is_active = promotion["is_active"] == "1"

            if active_only:
                if not is_active:
                    continue

                if (
                    product["status"].lower() != "active"
                    or int(product["stock_quantity"]) <= 0
                ):
                    continue

            original_price = Decimal(product["price_brl"])
            discount_percent = Decimal(promotion["discount_percent"])

            discounted_price = (
                original_price * (Decimal("1") - discount_percent / 100)
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            results.append({
                "promotion_id": promotion["promotion_id"],
                "product_id": product["product_id"],
                "product_name": product["name"],
                "category": category_name,
                "description": promotion["description"],
                "discount_percent": float(discount_percent),
                "original_price": float(original_price),
                "discounted_price": float(discounted_price),
                "stock_quantity": int(product["stock_quantity"]),
                "is_active": is_active,
            })

        return results
