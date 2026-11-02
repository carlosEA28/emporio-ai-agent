# Example 2 — Product recommendation under a budget (CSV)

**Scenario:** A customer searches for nylon-string acoustic guitars within a price limit. The agent uses the product catalog and stock information.

**Customer:**

> Quero um violão de nylon por até R$ 600.

**Assistant (actual output):**

> Ótima escolha! Aqui vão violões de nylon até R$ 600 disponíveis no momento:
>
> - Yamaha C40 Nylon Natural (ID 81) — R$ 599,90
>   - Tampo Spruce, laterais/fundo Meranti, strings nylon, escala 650mm, sem eletrônica.
>   - Estoque: 12
>
> - Tagima Memphis AC-39 Nylon Natural (ID 83) — R$ 429,90
>   - Corpo leve, strings nylon, escala 650mm, top Linden, sem eletrônica.
>   - Estoque: 15
>
> - Rozini RC-104 Nylon Estudante (ID 85) — R$ 459,90
>   - Tampo Spruce, back/sides Sapele, neck Nato, strings nylon, escala 650mm, sem eletrônica.
>   - Estoque: 10
>
> Se quiser, posso detalhar mais sobre cada modelo (conforto do braço, tipo de acabamento, sonoridade) ou ajudar a escolher com base no seu estilo de toque. Qual deles você gostaria de conhecer com mais detalhes? Observação: para informações sobre políticas de devolução, garantia, pagamentos ou horários de funcionamento, posso consultar a loja.

**Data source:** `products.csv` and `categories.csv`, accessed through the product-search service/tool. This is an actual response captured during manual validation.
