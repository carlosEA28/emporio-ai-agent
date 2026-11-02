# Example 4 — Applying discount rules (RAG)

**Scenario:** A customer asks if a promotional price can receive an additional PIX discount. The agent must consult the store's discount policy rather than guessing.

**Customer:**

> Se eu pagar um instrumento promocional com PIX, ganho mais 5%?

**Assistant (actual output):**

> Resumo direto: não é acumulativo.
>
> - PIX tem desconto de 5% sobre o preço de tabela (pagamento à vista).
> - Esse desconto não se aplica a itens já com preço promocional.
> - Promoções não são cumulativas com o desconto PIX.
> - Compras acima de R$ 2.000,00 podem usar combinação de formas de pagamento (por exemplo, PIX + cartão), conforme a política.
>
> Se você tiver um produto específico em mente, posso verificar se ele está em promoção e qual seria o preço com o PIX, quando aplicável. Pode me dizer o nome do instrumento?

**Reference:** The manual's payment rules (page 3) and promotion rules (page 6). This is an actual agent response captured during manual validation.
