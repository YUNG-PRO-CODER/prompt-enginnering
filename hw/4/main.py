from groq import generate_response


def reflection(activity_name):

    print("\n" + "=" * 50)
    print("REFLECTION")
    print("=" * 50)

    print(f"\nActivity Completed: {activity_name}")

    print("\nHow did it work?")
    print("""
The program takes user prompts and sends them
to an AI model using the OpenRouter API.

The AI generates responses based on:
- the prompt
- temperature
- token limit

The response is then displayed back to the user.
""")

    print("How well did it work?")
    print("""
The activity worked well if:
- responses were generated successfully
- prompts produced meaningful outputs
- users understood the differences in prompts

Bias Mitigation helps users learn:
- how wording changes AI responses
- how to create neutral prompts

Token Limit Activity helps users understand:
- long prompts create larger responses
- shorter prompts are more focused
- token limits affect response size
""")

    print("Possible Improvements:")
    print("""
- Add GUI support
- Save results to a file
- Add multiple AI models
- Add response ratings
- Add conversation memory
""")


def bias_mitigation_activity():

    print("\nBias Mitigation Activity")

    prompt = input("Enter a prompt to check for bias: ").strip()

    if not prompt:
        print("Please enter a valid prompt")
        return

    initial_response = generate_response(
        prompt,
        temperature=0.5,
        max_tokens=500
    )

    print("\nInitial Response:")
    print(initial_response)

    modified_prompt = input(
        "\nModify the prompt to make it more neutral: "
    ).strip()

    if modified_prompt:

        modified_response = generate_response(
            modified_prompt,
            temperature=0.5,
            max_tokens=500
        )

        print("\nModified Response:")
        print(modified_response)

    else:
        print("No modifications made to the prompt")

    reflection("Bias Mitigation Activity")


def token_limit_activity():

    print("\nToken Limit Activity")

    long_prompt = input(
        "Enter a long prompt to test token limits: "
    ).strip()

    if long_prompt:

        long_response = generate_response(
            long_prompt,
            temperature=0.5,
            max_tokens=500
        )

        preview = (
            long_response[:100] + "..."
            if len(long_response) > 100
            else long_response
        )

        print("\nPreview of Long Response:")
        print(preview)

    else:
        print("No prompt entered therefore skipping it")

    short_prompt = input(
        "\nEnter a short prompt to test token limits: "
    ).strip()

    if short_prompt:

        short_response = generate_response(
            short_prompt,
            temperature=0.5,
            max_tokens=500
        )

        print("\nShort Response:")
        print(short_response)

    else:
        print("No prompt entered therefore skipping it")

    reflection("Token Limit Activity")


def run_activity():

    while True:

        print("\n" + "=" * 50)
        print("Bias Mitigation and Token Limit Activity")
        print("=" * 50)

        print("1. Bias Mitigation")
        print("2. Token Limit")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            bias_mitigation_activity()

        elif choice == "2":
            token_limit_activity()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_activity()