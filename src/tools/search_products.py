
from langchain_core.tools import tool

from services.product_service import ProductService


product_service = ProductService()


@tool
def search_products(
    name: str | None = None,
    category: str | None = None,
    available_only: bool = True,
) -> str:
    """
    Search musical instruments in the store catalog.

    Use this tool to check product prices, specifications and stock.

    Parameters:
    - name: Use only for brand or model names, such as "Yamaha" or "C40".
    - category: Use for instrument categories, such as "Violões" or "Guitarras".
    - available_only: Set to False to include unavailable or discontinued products.

    For requests involving characteristics such as nylon strings, electric
    instruments or beginner-friendly models, search by category and analyze
    the returned descriptions and specifications.

    If a specific search returns no products, try a broader search before
    concluding that the store does not have suitable options.
    """

    products = product_service.search_products(
        name=name,
        category=category,
        available_only=available_only,
    )

    if not products:
        return "Nenhum instrumento encontrado com os filtros informados."

    results = []

    for product in products:
        results.append(
            f"Produto: {product['name']}\n"
            f"ID: {product['product_id']}\n"
            f"Categoria: {product['category']}\n"
            f"Descrição: {product['description']}\n"
            f"Preço: R$ {product['price_brl']:.2f}\n"
            f"Estoque: {product['stock_quantity']}\n"
            f"Status: {product['status']}\n"
            f"Especificações: {product['specs']}"
        )

    return "\n\n".join(results)
