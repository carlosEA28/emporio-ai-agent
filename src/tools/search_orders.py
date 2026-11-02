
from langchain_core.tools import tool

from services.order_service import OrderService


order_service = OrderService()


@tool
def search_orders(order_id: str, email: str) -> str:
    """
    Search a customer's order by order number and email.

    Use this tool when customers ask about order status,
    purchased products, payment, tracking or estimated delivery.

    Both order_id and email are required.
    Ask the customer for missing information before calling this tool.

    Never disclose order information without a matching email.
    Email matching is a basic lookup check, not full authentication.
    """

    order = order_service.get_order(
        order_id=order_id,
        email=email,
    )

    if order is None:
        return (
            "Não foi possível localizar o pedido com o número "
            "e e-mail informados. Confira os dados e tente novamente."
        )

    items = "\n".join(
        f"- {item['product_name']} "
        f"(quantidade: {item['quantity']})"
        for item in order["items"]
    )

    return (
        f"Pedido: {order['order_id']}\n"
        f"Data: {order['order_date']}\n"
        f"Status: {order['status']}\n"
        f"Total: R$ {order['total_brl']:.2f}\n"
        f"Pagamento: {order['payment_method']}\n"
        f"Previsão de entrega: "
        f"{order['estimated_delivery'] or 'Não informada'}\n"
        f"Código de rastreamento: "
        f"{order['tracking_code'] or 'Não disponível'}\n"
        f"Observações: {order['notes'] or 'Nenhuma'}\n"
        f"Produtos:\n{items or 'Nenhum item cadastrado'}"
    )
