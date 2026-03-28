import json
import random
import os
import sys
import hp_art
import st_art

def load_questions(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Could not find the trivia questions file: {filename}")
        sys.exit(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("✨🧙‍♂️ Welcome to the Ultimate Trivia Challenge: HP vs Stranger Things! 🚲🔦\n")
    
    hp_data = load_questions("hp_trivia.json")
    st_data = load_questions("st_trivia.json")
    
    print("Select your difficulty level:")
    print("1. Easy 🟢")
    print("2. Medium 🟡")
    print("3. Hard 🔴")
    
    choice = input("\nEnter 1, 2, or 3: ").strip()
    
    if choice == '1':
        difficulty = 'easy'
        print("\n🟢 Selected: Easy! Let's get started. 🟢\n")
    elif choice == '2':
        difficulty = 'medium'
        print("\n🟡 Selected: Medium! A true challenge. 🟡\n")
    elif choice == '3':
        difficulty = 'hard'
        print("\n🔴 Selected: Hard! Good luck, you'll need it. 🔴\n")
    else:
        print("\n❌ Invalid choice, defaulting to Easy. 🟢\n")
        difficulty = 'easy'

    hp_questions = hp_data.get(difficulty, [])
    st_questions = st_data.get(difficulty, [])
    
    if not hp_questions and not st_questions:
        print("❌ No questions found for this difficulty.")
        sys.exit(1)
        
    # Tag questions with their universe
    all_questions = []
    for q in hp_questions:
        q_copy = q.copy()
        q_copy["universe"] = "HP"
        all_questions.append(q_copy)
        
    for q in st_questions:
        q_copy = q.copy()
        q_copy["universe"] = "ST"
        all_questions.append(q_copy)
        
    # Randomly select 10 questions from the combined pool
    random.shuffle(all_questions)
    round_questions = all_questions[:10]
        
    score = 0
    total_questions = len(round_questions)
    
    hp_available_arts = hp_art.ASCII_ARTS.copy()
    st_available_arts = st_art.ASCII_ARTS.copy()
    random.shuffle(hp_available_arts)
    random.shuffle(st_available_arts)
    
    for i, q_data in enumerate(round_questions, 1):
        universe = q_data["universe"]
        question_text = q_data["question"]
        options = q_data["options"].copy()
        correct_answer = q_data["answer"]
        
        # Shuffle options
        random.shuffle(options)
        
        emoji = "🧙" if universe == "HP" else "🚲"
        print(f"{emoji} Question {i}/{total_questions} ({universe}): {question_text}")
        
        letters = ['A', 'B', 'C', 'D']
        answer_mapping = {}
        for letter, option in zip(letters, options):
            print(f"  {letter}) {option}")
            answer_mapping[letter] = option
            
        while True:
            user_input = input("💡 Your answer (A/B/C/D): ").strip().upper()
            if user_input in letters:
                break
            print("⚠️ Please enter A, B, C, or D.")
            
        selected_answer = answer_mapping[user_input]
        
        if selected_answer == correct_answer:
            if universe == "HP":
                print("✅ Correct! 10 points to Gryffindor! ✨")
                if not hp_available_arts:
                    hp_available_arts = hp_art.ASCII_ARTS.copy()
                    random.shuffle(hp_available_arts)
                print(hp_available_arts.pop())
            else:
                print("✅ Correct! Friends don't lie! 🧇")
                if not st_available_arts:
                    st_available_arts = st_art.ASCII_ARTS.copy()
                    random.shuffle(st_available_arts)
                print(st_available_arts.pop())
                
            print()
            score += 1
        else:
            wrong_emoji = "🐍" if universe == "HP" else "👾"
            print(f"❌ Incorrect! The correct answer was: {correct_answer} {wrong_emoji}\n")
            
    # Final Score
    print("🏆 Game Over! 🏆")
    print(f"Your final score is: {score}/{total_questions}")
    
    if score == total_questions:
        print("🌟 Outstanding! You're a true trivia master! 🌟")
    elif score >= total_questions * 0.7:
        print("✨ Exceeds Expectations! Well done! ✨")
    elif score >= total_questions * 0.5:
        print("📜 Acceptable! Not bad for a beginner. 📜")
    else:
        print("🐉 Poor! You might need to study more. 🐉")

if __name__ == "__main__":
    main()