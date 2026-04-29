from pt import generate_response

def print_section(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")


def safe_generate(prompt, temperature=0.3, max_tokens=1024):
    try:
        response = generate_response(
            prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"


def run_activity():
    print("\n🎯 Prompt Engineering Activity\n")

    category = input("Enter a category (e.g., fruit, city, animal): ").strip()
    item = input(f"Enter a specific {category}: ").strip()

    if not category or not item:
        print("❌ Category and item cannot be empty.")
        return

    print_section("ZERO-SHOT")

    zero_prompt = f"Is '{item}' a '{category}'? Answer only Yes or No."
    print("Prompt:", zero_prompt)

    zero_response = safe_generate(zero_prompt, temperature=0.2)
    print("Response:", zero_response)

    print_section("ONE-SHOT")

    one_prompt = f"""Determine if the item belongs to the category.

Example:
Category: fruit
Item: apple
Answer: Yes

Now:
Category: {category}
Item: {item}
Answer:"""

    one_response = safe_generate(one_prompt, temperature=0.2)
    print("Response:", one_response)

    print_section("FEW-SHOT")

    few_prompt = f"""Determine if the item belongs to the category.

Example 1:
Category: fruit
Item: apple
Answer: Yes

Example 2:
Category: fruit
Item: carrot
Answer: No

Example 3:
Category: vehicle
Item: bicycle
Answer: Yes

Now:
Category: {category}
Item: {item}
Answer:"""

    few_response = safe_generate(few_prompt, temperature=0.2)
    print("Response:", few_response)

    print_section("CREATIVE FEW-SHOT")

    creative_prompt = f"""Write a one-sentence imaginative story about the given word.

Example 1:
Word: moon
Story: The moon winked as the night whispered secrets.

Example 2:
Word: computer
Story: The computer dreamed of escaping into the internet.

Word: {item}
Story:"""

    creative_response = safe_generate(creative_prompt, temperature=0.7)
    print("Response:", creative_response)

    print_section("REFLECTION")

    print("1. How did the responses differ between each approach?")
    print("2. Which approach gave the most accurate answer?")
    print("3. Which approach was most creative?")
    print("4. How did examples influence the AI's output?")
    print("5. Where could you use this in real life?")

    print_section("SUMMARY")

    print(f"Zero-shot: {zero_response}")
    print(f"One-shot: {one_response}")
    print(f"Few-shot: {few_response}")
    print(f"Creative: {creative_response}")


if __name__ == "__main__":
    run_activity()