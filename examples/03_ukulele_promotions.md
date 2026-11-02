# Example 3 — Active promotions by category (CSV)

**Scenario:** A customer asks for promotions in one category. The agent must select active promotions for ukuleles rather than mixing instrument categories.

**Customer:**

> Vocês têm alguma promoção de ukulele?

**Assistant (actual output):**

> Sim! Temos promoções ativas para ukuleles. São as seguintes:
>
> - Kalani KAL-700T Tenor Natural — Oferta Especial — 10% de desconto
>   - De R$ 359,00 por R$ 323,10
>   - Estoque: 11 unidades
>
> - Ohana CK-20 Concert Natural — Desconto Exclusivo — 20% de desconto
>   - De R$ 549,00 por R$ 439,20
>   - Estoque: 6 unidades
>
> Observação: descontos promocionais não podem ser combinados com o desconto PIX.
>
> Se quiser, posso ajudar a buscar outras opções de ukulele dentro de um determinado tamanho, faixa de preço ou características.

**Data source:** `promotions.csv`, `products.csv`, and `categories.csv`, through the promotions tool. The answer above is the actual agent response, excluding additional raw debug prints that followed it in the terminal.
