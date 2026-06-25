"""
agent.py
COMMIT 2: Wires in the Memory module so the agent now remembers
the conversation for the session.
"""


from memory import Memory




def greet():
    print("=" * 50)
    print("  Simple AI Agent  (v0.2 - with memory)")
    print("=" * 50)
    print("Type 'exit' to quit.\n")




def run():
    greet()
    memory = Memory()


    while True:
        user_input = input("You: ").strip()
        memory.add("user", user_input)


        if user_input.lower() in ("exit", "quit"):
            print(f"Agent: Goodbye! We had {memory.turn_count()} turns this session.")
            break


        response = "(not implemented yet)"
        memory.add("agent", response)
        print(f"Agent: {response}")




if __name__ == "__main__":
    run()




