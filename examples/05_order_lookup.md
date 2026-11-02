# Example 5 — Order tracking and customer email check (CSV)

**Scenario:** The customer asks for an order update. The agent requests the required fields when missing and looks up a specific order only when an order number and matching email are provided.

The following are **three separate test invocations**, not a single persisted multi-turn session. All assistant outputs were captured from the running application.

## A. Missing information

**Customer:**

> Quero saber onde está meu pedido.

**Assistant (actual output):**

> Claro! Vou te ajudar a verificar o status do seu pedido.
>
> Para eu consultar, por favor me informe:
> - Número do pedido
> - E-mail associado à compra
>
> Assim que eu tiver esses dados, posso buscar o status do pedido. Observação: não divulgarei informações sem o e-mail correspondente.

## B. Matching order and email

**Customer:**

> Meu pedido é 1 e meu e-mail é pedro.oliveira@jmail.com. Qual o status?

**Assistant (actual output):**

> Pedido 1
> - Data do pedido: 15/10/2025
> - Produto: Martin D-28 Dreadnought Natural (1)
> - Total: R$ 11.499,00
> - Pagamento: PIX
> - Status: Entregue
> - Previsão de entrega (original): 25/10/2025
> - Código de rastreamento: BRAB1234567BR
> - Observações: Nenhuma
>
> Precisa de algum comprovante ou nota fiscal? Posso ajudar com isso.

## C. Nonmatching email

**Customer:**

> Meu pedido é 1 e meu e-mail é outro@email.com.

**Assistant (actual output):**

> Não consegui localizar esse pedido com os dados informados (número 1 e e-mail outro@email.com).
>
> Pode confirmar:
> - O número correto do pedido (às vezes pode incluir símbolos como # ou ter mais dígitos)?
> - O e-mail cadastrado na compra?
>
> Se tiver o ID completo ou outro e-mail que possa ter sido usado na compra, envie para eu tentar localizar novamente. Também posso ajudar com outras informações caso precise.

**Data source:** `orders.csv`, `order_items.csv`, `customers.csv` and `products.csv`, through the order-search service/tool.

**Limitations:** Email matching is not strong customer authentication; this is a prototype using fictional test data. The assistant's offer to provide invoices/receipts is not backed by an implemented tool.
