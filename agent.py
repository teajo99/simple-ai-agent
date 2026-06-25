"""
agent.py
The main entry point for our simple AI agent.


COMMIT 1: Just the skeleton. The agent can start, greet the user,
and exit cleanly. No real intelligence yet -- that comes in later commits.
"""




def greet():
    print("=" * 50)
    print("  Simple AI Agent  (v0.1 - skeleton)")
    print("=" * 50)
    print("Type 'exit' to quit.\n")




def run():
    greet()
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Agent: Goodbye!")
            break
        # Placeholder response -- will be replaced with real logic later
        print("Agent: (not implemented yet)")




if __name__ == "__main__":
    run()


