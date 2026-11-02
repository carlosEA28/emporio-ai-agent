
from langchain_core.tools import tool

from services.promotion_service import PromotionService


promotion_service = PromotionService()


@tool
def search_promotions(
    product_name: str | None = None,
    category: str | None = None,
    active_only: bool = True,
) -> str:
    """
    Search promotions and discounted prices for musical instruments.

    Use this tool when customers ask about promotions, discounts,
    special offers or whether a specific product is on sale.

    Parameters:
    - product_name: Search by brand or model, such as "Yamaha" or "C40".
    - category: Filter by instrument category, such as "Violões" or "Ukuleles".
    - active_only: Return only active promotions by default.

    When the customer specifies an instrument category, always use
    the category filter. Never include products from other categories.

    If no promotions are found, do not assume that the products
    are unavailable; only report that no matching promotions exist.

    Promotional discounts cannot be combined with the PIX discount.
    """

    promotions = promotion_service.search_promotions(
        product_name=product_name,
        category=category,
        active_only=active_only,
    )

    if not promotions:
        return "Nenhuma promoção encontrada para os filtros informados."

    results = []

    for promotion in promotions:
        status = "Ativa" if promotion["is_active"] else "Inativa"

        results.append(
            f"Produto: {promotion['product_name']}\n"
            f"ID: {promotion['product_id']}\n"
            f"Categoria: {promotion['category']}\n"
            f"Promoção: {promotion['description']}\n"
            f"Desconto: {promotion['discount_percent']:g}%\n"
            f"Preço original: R$ {promotion['original_price']:.2f}\n"
            f"Preço promocional: R$ {promotion['discounted_price']:.2f}\n"
            f"Estoque: {promotion['stock_quantity']}\n"
            f"Status da promoção: {status}"
        )

    return "\n\n".join(results)
