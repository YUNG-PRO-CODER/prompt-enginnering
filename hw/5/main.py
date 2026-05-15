from groq import generate_response


def get_essay_details():
    print("\n=== AI Writing Assistant ===\n")
    topic = input("What is the topic of your essay? ").strip()
    essay_type = input(
        "What type of essay are you writing? "
    ).strip()
    lengths = [
        "300 words",
        "900 words",
        "1200 words",
        "2000 words"
    ]
    print("\nSelect essay word count:")
    for i, l in enumerate(lengths, 1):
        print(f"{i}) {l}")
        
    try:
        idx = int(input("> ").strip())

        if 1 <= idx <= len(lengths):
            length = lengths[idx - 1]
        else:
            length = "300 words"
    except ValueError:
        length = "300 words"

    target_audience = input(
        "Target audience: "
    ).strip()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience
    }


def generate_essay_content(details):
    try:
        temp = float(
            input(
                "\nEnter temperature "
                "(0.1 structured, 0.7 creative): "
            ).strip()
        )
        if not (0 <= temp <= 1):
            raise ValueError
    except ValueError:
        print("Invalid temperature. Using 0.3")
        temp = 0.3

    intro_prompt = f"""
Write a strong introduction for a
{details['essay_type']} essay.
Topic:
{details['topic']}
Length:
{details['length']}
Audience:
{details['target_audience']}
"""
    introduction = generate_response(
        intro_prompt,
        temperature=temp,
        max_tokens=500
    )

    print("\n=== INTRODUCTION ===\n")
    print(introduction)
    print("\nHow should the body be written?")
    print("1) Full draft")
    print("2) Step-by-step arguments")
    choice = input("> ").strip()

    if choice == "1":
        body_prompt = f"""
Write the full body of a
{details['essay_type']} essay.
Topic:
{details['topic']}
Audience:
{details['target_audience']}
Length:
{details['length']}
"""
        body = generate_response(
            body_prompt,
            temperature=temp,
            max_tokens=1200
            )
        print("\n=== FULL BODY ===\n")
        print(body)

    else:
        step_prompt = f"""
Write step-by-step arguments
for an essay on:

{details['topic']}
Include:
- reasoning
- examples
- evidence
"""
        body_step = generate_response(
            step_prompt,
            temperature=temp,
            max_tokens=1200
        )
        print("\n=== STEP-BY-STEP BODY ===\n")
        print(body_step)

    conclusion_prompt = f"""
Write a conclusion for a
{details['essay_type']} essay.
Topic:
{details['topic']}
Audience:
{details['target_audience']}
"""
    conclusion = generate_response(
        conclusion_prompt,
        temperature=temp,
        max_tokens=500
    )
    print("\n=== CONCLUSION ===\n")
    print(conclusion)


def feedback_and_refinement():
    try:
        rating = int(
            input(
                "\nRate satisfaction (1-5): "
            ).strip()
        )
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        rating = 3

    if rating != 5:
        feedback = input(
            "\nProvide feedback: "
        ).strip()
        refine_prompt = f"""
Refine the essay based on this feedback:
{feedback}

Improve:
- structure
- tone
- clarity
- quality
"""
        refined = generate_response(
            refine_prompt,
            temperature=0.4,
            max_tokens=1000
        )
        print("\n=== REFINED RESPONSE ===\n")
        print(refined)

    else:
        print("\nGreat! Glad you liked it.")


def run_activity():
    print("\nWelcome to the AI Writing Assistant!")
    details = get_essay_details()
    if not details["topic"] or not details["essay_type"]:
        print(
            "\nPlease provide a topic "
            "and essay type."
        )
        return
    generate_essay_content(details)
    feedback_and_refinement()
    
if __name__ == "__main__":
    run_activity()