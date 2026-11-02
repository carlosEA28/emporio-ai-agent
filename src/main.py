from dotenv import load_dotenv
from agents.factory import create_store_agent


def main():
    load_dotenv()

    agent = create_store_agent()
    messages = []

    print("Empório da Música — AI Assistant")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            question = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAté logo!")
            break

        if question.lower() in ("sair", "exit", "quit"):
            print("Até logo!")
            break

        if not question:
            continue

        messages.append({
            "role": "user",
            "content": question
        })

        try:
            response = agent.invoke({"messages": messages})

            messages = response["messages"]
            answer = messages[-1].content

            print(f"\nAssistente: {answer}\n")

        except Exception as error:
            messages.pop()
            print(f"\nErro ao processar mensagem: {error}\n")


if __name__ == "__main__":
    main()
