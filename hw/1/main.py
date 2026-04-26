from groq import generate_response
from utils import print_header, save_output
import time

def handle_temperature(cmd):
    prompt = cmd.replace("temp ", "").strip()

    temps = [0.1, 0.5, 0.9]
    results = []

    print("\n[Temperature Experiment]")
    for t in temps:
        print(f"\n--- TEMP {t} ---")
        response = generate_response(prompt, temperature=t, max_tokens=512)
        print(response)
        results.append(f"\nTEMP {t}:\n{response}")
        time.sleep(1)

    save_output("\n".join(results))


def handle_instruction(cmd):
    topic = cmd.replace("inst ", "").strip()

    instructions = [
        f"Summarize {topic} in 3 bullet points.",
        f"Explain {topic} like I'm 10 years old.",
        f"Give pros and cons of {topic}.",
        f"Write a futuristic 2050 scenario about {topic}.",
    ]

    results = []

    print("\n[Instruction Mode]")
    for inst in instructions:
        print(f"\n--- {inst} ---")
        response = generate_response(inst, temperature=0.7, max_tokens=512)
        print(response)
        results.append(f"\nPROMPT: {inst}\n{response}")
        time.sleep(1)

    save_output("\n".join(results))


def handle_custom(cmd):
    try:
        parts = cmd.replace("custom ", "").split("|")
        prompt = parts[0].strip()
        temp = 0.7
        tokens = 512

        for p in parts[1:]:
            if "temp=" in p:
                temp = float(p.split("=")[1])
            elif "tokens=" in p:
                tokens = int(p.split("=")[1])

        print(f"\n[Custom Prompt | temp={temp}, tokens={tokens}]")
        response = generate_response(prompt, temperature=temp, max_tokens=tokens)
        print(response)

        save_output(f"\nCUSTOM:\n{prompt}\n\n{response}")

    except Exception as e:
        print("Invalid custom command format.")
        print("Example: custom Explain AI | temp=1.2 | tokens=600")


def show_help():
    print("\nAvailable Commands:")
    print(" temp <prompt>        → Compare temperatures")
    print(" inst <topic>         → Instruction-based prompts")
    print(" custom <prompt> | temp=0.7 | tokens=512")
    print(" help                 → Show commands")
    print(" exit                 → Quit\n")


def main():
    print_header("AI PROMPT ENGINEERING TERMINAL")

    show_help()

    while True:
        cmd = input(">>> ").strip()

        if cmd.startswith("temp "):
            handle_temperature(cmd)

        elif cmd.startswith("inst "):
            handle_instruction(cmd)

        elif cmd.startswith("custom "):
            handle_custom(cmd)

        elif cmd == "help":
            show_help()

        elif cmd == "exit":
            print("Goodbye.")
            break

        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()