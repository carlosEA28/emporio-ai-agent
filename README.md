
# Empório da Música — AI Customer Support Agent

A Python customer support agent developed for the **Artefact AI Engineer technical challenge**. It assists customers of a fictional musical instrument store in Campo Grande, Brazil, answering questions in Brazilian Portuguese.

## What it does

- **Store policies:** answers questions about returns, warranties, payments, shipping, and opening hours using the store's PDF manual.
- **Products:** finds instruments by name or category and checks prices, specifications, and stock availability.
- **Promotions:** retrieves active discounts and calculates promotional prices using the supplied CSV files.
- **Orders:** provides order status, purchased items, and tracking details after matching the order number with the customer's email.

## Getting started

**Requirements:** Python compatible with `pyproject.toml`, [uv](https://docs.astral.sh/uv/), an OpenAI API key, and internet access for model and embedding requests.

1. Clone the repository and install dependencies:

   ```bash
   git clone https://github.com/carlosEA28/emporio-ai-agent.git
   cd emporio-ai-agent
   uv sync
   ```

2. Create a `.env` file in the project root:

   ```dotenv
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Ensure the provided CSV files are located in `data/csv/` and the policy manual is available at `data/pdf/políticas_da_loja.pdf`. The CSV services use the original filenames (`desafio_tecnico_ai_eng - products.csv`, etc.).

4. Build the local policy index before the first run:

   ```bash
   PYTHONPATH=src uv run python -c "from rag.ingestion import ingest; ingest('data/pdf')"
   ```

5. Run the agent:

   ```bash
   uv run src/main.py
   ```

The application starts an interactive command-line chat. Enter a customer question and press Enter to receive a response. Conversation context is maintained during the session, allowing follow-up questions.

Type `sair`, `exit`, or `quit` to close the application. Conversation history is not persisted between executions. Re-ingest the PDF whenever its contents change.

## Architecture

```text
Customer question
       |
       v
LangChain agent (gpt-5-nano)
       |
       +-- search_store_policies --> PDF retriever --> ChromaDB
       +-- search_products -------> ProductService --> Products + Categories CSVs
       +-- search_promotions -----> PromotionService --> Promotions + Product CSVs
       +-- search_orders ---------> OrderService --> Orders + Customers + Items CSVs
       |
       v
Response in Brazilian Portuguese
```

The agent uses **LangChain `create_agent`** to select tools, execute them, and use their results when preparing a response.

The policy PDF follows a **RAG pipeline**: load and normalize the text, split it into overlapping chunks, generate embeddings with `text-embedding-3-small`, and persist them in ChromaDB. The policy tool retrieves relevant excerpts with source-page information.

Operational CSVs are queried directly by Python services. Products are linked to categories, promotions are matched with products, and orders are associated with customers and order items.

## Tech stack

| Component | Technology | Purpose |
| --- | --- | --- |
| Language | Python | Main implementation |
| Agent orchestration | LangChain (`create_agent`) | Tool selection and execution |
| LLM | OpenAI `gpt-5-nano` | Understand requests and generate answers |
| Embeddings | OpenAI `text-embedding-3-small` | Represent policy passages for semantic search |
| Vector store | ChromaDB (`langchain-chroma`) | Local persistent policy index |
| PDF processing | PyPDFLoader, RecursiveCharacterTextSplitter | PDF loading and chunking |
| Structured data | Python `csv` module | Read-only queries over supplied datasets |
| Dependencies | `uv` | Installation and execution |

## Technical decisions and trade-offs

- **Hybrid retrieval rather than RAG for everything.** Policies are unstructured text, so semantic search is useful. Prices, stock, promotions, and order IDs require exact matches and calculations; direct CSV queries are simpler and more reliable than vector similarity for these fields.

- **A single agent with focused tools.** `create_agent` handles the tool-calling cycle, allowing the model to select and execute tools according to the customer's request. Multiple agents or custom orchestration would introduce unnecessary complexity for this customer-support prototype.

- **Lightweight local storage.** ChromaDB persists the policy index locally, while the original CSVs remain the source of truth for operational data. No database server is required, but changes to the PDF require index maintenance, and CSV updates are not automatically synchronized with external systems.

- **Model and prompt design.** `gpt-5-nano` was selected as a lightweight model for tool calling and response generation. The system prompt establishes the store's tone, tool-use expectations, and response boundaries. Descriptive tool docstrings help distinguish product names, categories, promotions, and policy questions. However, prompting and tool calling do not eliminate reasoning errors.

- **Interactive CLI instead of a web application.** The challenge focuses on agent behavior, so a command-line interface keeps the project simple and easy to execute. It supports multiple questions and preserves conversation context during a session without requiring a frontend, API server, or additional infrastructure.

## Project structure

```text
.
├── data/
│   ├── csv/                  # Original challenge CSVs
│   ├── pdf/                  # Store policy manual
│   └── vector_store/         # Generated index (not committed)
├── src/
│   ├── agents/
│   │   └── factory.py        # Agent configuration and system prompt
│   ├── rag/                  # PDF ingestion, vector store, retrieval
│   ├── services/             # Product, promotion, and order logic
│   ├── tools/                # LangChain tool definitions
│   └── main.py               # Interactive CLI entry point
├── examples/                 # Recorded example interactions
├── pyproject.toml
└── README.md
```

## Known limitations and future improvements

1. **LLM reasoning is not guaranteed.** The agent can select appropriate tools but still misinterpret business rules, such as minimum installment amounts. Deterministic validation of calculations and payment conditions would improve reliability.

2. **Literal product matching.** Product search relies on string matching against names and categories. Requests involving detailed characteristics may require broader searches or additional structured filters.

3. **Static operational data.** Product availability, promotions, and order information come from local CSV files rather than live business systems. Changes made outside these files are not reflected automatically.

4. **Limited identity verification.** Matching an order number with an email does not prove ownership of that email. A production system would require authentication or another verification mechanism.

5. **Session-only conversation history.** The interactive CLI preserves context while the application is running, but conversations are not saved between executions.

6. **Manual document ingestion.** Changes to the policy PDF require updating the vector index. Automated document synchronization is not implemented.

7. **Limited automated evaluation.** Features were manually validated with product, promotion, policy, and order scenarios. Automated unit tests, tool integration tests, and agent regression evaluations would improve confidence in future changes.

8. **External API dependency.** The application requires internet access and an OpenAI API key for language generation and embeddings.

Given more time, the highest-priority improvements would be deterministic validation of payment rules, secure order access, richer product filtering, and automated regression tests.

## Example interactions

See [`examples/`](examples/) for five recorded interactions covering store policies, product recommendations, promotions, PIX discount rules, and order lookup.

The original customer questions and agent responses are in Portuguese, matching the store's audience, while supporting descriptions are in English.
