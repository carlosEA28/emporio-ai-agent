# Example 1 — Store return policies (RAG)

**Scenario:** A customer asks about returns. The agent retrieves passages from the store's PDF policy manual using `search_store_policies` and answers based on those passages.

**Customer:**

> Qual é a política de devolução?

**Assistant (actual output):**

> Aqui está o resumo da Política de Devoluções da Empório da Música:
>
> - Direito de Arrependimento (compras online)
>   - Você pode solicitar a devolução em até 7 dias corridos após o recebimento, sem necessidade de justificar.
>   - O produto deve estar na embalagem original, sem sinais de uso, com todos os acessórios e manuais.
>   - O reembolso é feito na mesma forma de pagamento original, em até 10 dias úteis.
>   - O frete de devolução é por conta da loja em caso de arrependimento.
>
> - Trocas por Defeito
>   - Defeitos de fabricação podem ser trocados em até 30 dias corridos após a compra.
>   - Após 30 dias, o cliente deve acionar a garantia com o fabricante (a Empório da Música pode intermediar se solicitado).
>   - Danos por mau uso, quedas ou modificações não autorizadas não são cobertos.
>
> - Trocas por Preferência
>   - Trocas por preferência (cor, modelo, tamanho) são permitidas em até 7 dias, mediante disponibilidade do produto desejado.
>   - O produto deve estar em perfeito estado e na embalagem original.
>   - Diferenças de valor serão cobradas ou reembolsadas conforme o caso.
>
> - Itens Não Elegíveis para Troca
>   - Instrumentos com personalização ou ajustes sob encomenda (setup, regulagens especiais).
>   - Produtos adquiridos em promoções de liquidação com aviso de “venda final”.
>   - Boquilhas de instrumentos de sopro, por questões de higiene.
>
> - Garantia
>   - Além da garantia legal de 90 dias contra defeitos de fabricação (a contar do recebimento), muitos fabricantes oferecem garantia adicional (6 meses a 2 anos). Consulte o certificado de garantia que acompanha o produto para os detalhes.
>
> Se quiser, posso adaptar essas informações para o seu caso específico (por exemplo, se o produto já foi recebido há X dias, se é defeito, etc.) ou indicar onde encontrar a política completa.

**Observed tool use:** `search_store_policies(query="política de devolução")`; retrieved pages 4 and 7 of the store manual. The tool invocation and response were present in the captured agent trace.
