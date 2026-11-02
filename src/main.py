from dotenv.main import load_dotenv
from langchain.agents import create_agent
from agents.factory import create_store_agent
from tools.search_store_policies import search_store_policies


def main():
    load_dotenv()

    agent = create_store_agent()

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Moro em São Paulo. Quais opções de entrega vocês oferecem e quanto demoram?"
            }
        ]
    })

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
