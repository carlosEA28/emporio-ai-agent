
import csv

from services.product_service import DATA_DIR, ProductService


class OrderService:

    def __init__(self):
        self.product_service = ProductService()

        self.orders = self._read_csv("orders")
        self.customers = self._read_csv("customers")
        self.order_items = self._read_csv("order_items")

    def _read_csv(self, name: str) -> list[dict]:
        path = DATA_DIR / f"desafio_tecnico_ai_eng - {name}.csv"

        with path.open("r", encoding="utf-8-sig", newline="") as file:
            return list(csv.DictReader(file))

    def get_order(self, order_id: str, email: str) -> dict | None:
        order = next(
            (
                item for item in self.orders
                if item["order_id"] == str(order_id).strip()
            ),
            None,
        )

        if order is None:
            return None

        customer = next(
            (
                item for item in self.customers
                if item["customer_id"] == order["customer_id"]
            ),
            None,
        )

        if customer is None:
            return None

        if customer["email"].strip().casefold() != email.strip().casefold():
            return None

        products_by_id = {
            product["product_id"]: product
            for product in self.product_service.products
        }

        items = []

        for item in self.order_items:
            if item["order_id"] != order["order_id"]:
                continue

            product = products_by_id.get(item["product_id"])

            items.append({
                "product_id": item["product_id"],
                "product_name": (
                    product["name"] if product else "Produto não encontrado"
                ),
                "quantity": int(item["quantity"]),
            })

        return {
            "order_id": order["order_id"],
            "order_date": order["order_date"],
            "status": order["status"],
            "total_brl": float(order["total_brl"]),
            "payment_method": order["payment_method"],
            "tracking_code": order["tracking_code"],
            "estimated_delivery": order["estimated_delivery"],
            "notes": order["notes"],
            "items": items,
        }
