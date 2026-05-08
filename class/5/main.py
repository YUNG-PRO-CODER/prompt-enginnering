from groq import generate_response

def bias_mitigation_activity():
    print("Bias Mitigation Activity")
    prompt = input("Enter a prompt to check for bias: ")
    if not prompt.strip():
        print("Please enter a valid prompt")
        return
    initial_response = generate_response(prompt, temperature=0.5, max_tokens=500)
    print("\nInitial Response:")
    print(initial_response)
    
    modified_prompt = input("Modify the prompt to make it more neutral: ").strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.5, max_tokens=500)
        print("\nModified Response: ")
        print(modified_response)
    else:
        print("No modifications made to the prompt")

def token_limit_activity():
    print("Token Limit Activity")
    long_prompt = input("Enter a long prompt to test token limits: ").strip()
    
    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.5, max_tokens=500)
        preview = long_response[:100] + "..." if len(long_response) > 100 else long_response
        print("\nPreview of Long Response:")
        print(preview)
    else:
        print("No prompt entered therefore skipping it")
        
    short_prompt = input("Enter a short prompt to test token limits: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.5, max_tokens=500)
        print("\nShort Response:")
        print(short_response)
    else:
        print("No prompt entered therefore skipping it")
        
def run_activity():
    print("Welcome to the Bias Mitigation and Token Limit Activity")
    print("1. Bias Mitigation")
    print("2. Token Limit")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        
if __name__ == "__main__":
    run_activity()