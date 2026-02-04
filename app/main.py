from app.agent.dual_agent import run_dual_agent


def main():
    while True:
        user_input = input("Ask SQL Agent (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        output = run_dual_agent(user_input)
        print(output["sql_result"])




if __name__ == "__main__":
    main()
