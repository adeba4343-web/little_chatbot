import responses
import try_math, random_joke

def get_response(user_input):
    user_input = user_input.lower()

    # check predefined responses first
    for key in responses:
        if key in user_input:
            # special case for joke
            if key == "joke":
                return random_joke()
            return responses[key]

    # check if it's a math question
    math_result = try_math(user_input)
    if math_result:
        return math_result

    # fallback answer
    return "I don't understand that yet 🤔"

def main():
    print("Hi! I'm Chatty. Type 'quit' to exit.")
    conversation = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatty: Bye! 👋")
            break

        response = get_response(user_input)
        print("Chatty:", response)

        # log conversation
        conversation.append(f"You: {user_input}")
        conversation.append(f"Chatty: {response}")

    # save conversation to a file
    with open("conversation_log.txt", "w") as f:
        for line in conversation:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
