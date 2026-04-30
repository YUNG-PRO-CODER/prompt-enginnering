from groq import generate_response
from matplotlib import category
from matplotlib.pylab import choice

def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Enter the prompt for the AI to generate a response based on your input: ").strip()
    if not prompt:
        print("prompt cannot be empty. Please try again. ")
        return
    
    initial_response = generate_response(prompt, temperature=0.7, max_tokens=400)
    print(f"Initial AI response: {initial_response}")
    
    try:
        rating = int(input("Rate the response from 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            rating = 3
    except ValueError:
            rating = 3
            
    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    
def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    
    category = input("Enter a category (e.g., sciecne, history, teachnology): ").strip()
    item = input("Enter a specific {category} topic (e.g., quantum physics, WW2, AI): ").strip()
    
    if not category or not item:
        print('Category and item cannot be empty. Please try again')
        return
        
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    
    teacher_prompt = generate_response(teacher_prompt, temperature=0.7, max_tokens=400)
    expert_prompt = generate_response(expert_prompt, temperature=0.7, max_tokens=400)

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1. Reinforcement Learning")
    print("2. Role-Based Prompts")
    
    choice = input("Enter your choice (1 or 2): ").strip()
        
    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")
            
if __name__ == "__main__":
    run_activity()