from dotenv.main import load_dotenv
from langchain.agents import create_agent
from agents.factory import create_store_agent
from services.product_service import ProductService
from tools.search_promotions import search_promotions
from tools.search_store_policies import search_store_policies


def main():
    load_dotenv()

    agent = create_store_agent()

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Meu pedido é 1 e meu e-mail é outro@email.com."
            }
        ]
    })

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
