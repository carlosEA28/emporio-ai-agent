from langchain.agents import create_agent
from tools.search_store_policies import search_store_policies



def main():
    response = search_store_policies.invoke({
        "query": "Qual é a política de devolução?"
    })

    print(response)


if __name__ == "__main__":
    main()
