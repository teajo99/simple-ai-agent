"""
agent.py
COMMIT 3 (on feature/tools branch): Adds simple tool-calling.
"""


from memory import Memory
from tools import calculate, get_time




def greet():
    print("=" * 50)
    print("  Simple AI Agent  (v0.3 - with tools)")
    print("=" * 50)
    print("Try: 'calc 4 + 5'  or  'what time is it'")
    print("Type 'exit' to quit.\n")

def generate_response(user_input):
    """Route the input to a tool, or fall back to a placeholder."""
    lowered = user_input.lower().strip()


    if lowered.startswith("calc "):
        expression = user_input[5:]
        return calculate(expression)


    if "time" in lowered:
        return get_time()


    return "(not implemented yet -- try 'calc 4 + 5' or 'what time is it')"


def run():
    greet()
    memory = Memory()


    while True:
        user_input = input("You: ").strip()
        memory.add("user", user_input)


        if user_input.lower() in ("exit", "quit"):
            print(f"Agent: Goodbye! We had {memory.turn_count()} turns this session.")
            break


        response = generate_response(user_input)
        memory.add("agent", response)
        print(f"Agent: {response}")




if __name__ == "__main__":
    run()

