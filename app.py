from flask import Flask, request, jsonify, session, render_template
import random
import os
import json
import hp_art
import st_art

app = Flask(__name__)
# In production, set a strong secret key. Using a random one here for simplicity.
app.secret_key = os.urandom(24)

# ================================
# ROUTES
# ================================

@app.route('/')
def index():
    return render_template('index.html')

# ================================
# GUESSING GAME API
# ================================

@app.route('/api/guess/start', methods=['POST'])
def guess_start():
    session['guess_secret'] = random.randint(1, 100)
    session['guess_tries'] = 0
    return jsonify({"message": "Game started", "status": "ok"})

@app.route('/api/guess/submit', methods=['POST'])
def guess_submit():
    data = request.json
    guess = data.get('guess')
    
    if 'guess_secret' not in session:
        return jsonify({"error": "Game not started"}), 400
        
    try:
        guess = int(guess)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid guess format"}), 400

    secret = session['guess_secret']
    session['guess_tries'] += 1
    tries = session['guess_tries']

    if guess < secret:
        return jsonify({"result": "higher", "message": "Higher! ↑", "tries": tries})
    elif guess > secret:
        return jsonify({"result": "lower", "message": "Lower! ↓", "tries": tries})
    else:
        # User guessed correctly
        session.pop('guess_secret', None)
        return jsonify({
            "result": "correct", 
            "message": f"YOU GOT IT! It took you {tries} tries.", 
            "tries": tries
        })

# ================================
# TRIVIA GAME API
# ================================

def load_trivia_questions(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_trivia_questions(difficulty):
    hp_data = load_trivia_questions("hp_trivia.json")
    st_data = load_trivia_questions("st_trivia.json")
    
    hp_questions = hp_data.get(difficulty, [])
    st_questions = st_data.get(difficulty, [])
    
    all_questions = []
    for q in hp_questions:
        q_copy = q.copy()
        q_copy["universe"] = "HP"
        all_questions.append(q_copy)
        
    for q in st_questions:
        q_copy = q.copy()
        q_copy["universe"] = "ST"
        all_questions.append(q_copy)
        
    random.shuffle(all_questions)
    return all_questions[:10]

@app.route('/api/trivia/start', methods=['POST'])
def trivia_start():
    data = request.json
    difficulty = data.get('difficulty', 'easy')
    
    questions = get_trivia_questions(difficulty)
    if not questions:
        return jsonify({"error": "No questions found for this difficulty"}), 404
        
    # Prepare ASCII arts to avoid repeating
    hp_arts = hp_art.ASCII_ARTS.copy()
    random.shuffle(hp_arts)
    st_arts = st_art.ASCII_ARTS.copy()
    random.shuffle(st_arts)
        
    session['trivia_state'] = {
        "questions": questions,
        "score": 0,
        "current": 0,
        "hp_arts": hp_arts,
        "st_arts": st_arts
    }
    
    return jsonify({"message": "Trivia started", "total": len(questions)})

@app.route('/api/trivia/question', methods=['GET'])
def trivia_question():
    state = session.get('trivia_state')
    if not state or state['current'] >= len(state['questions']):
        return jsonify({"error": "Game over or not started"}), 400
        
    q_index = state['current']
    q_data = state['questions'][q_index]
    
    # Shuffle options on serving
    options = q_data['options'].copy()
    random.shuffle(options)
    
    return jsonify({
        "question": q_data['question'],
        "universe": q_data['universe'],
        "options": options,
        "current": q_index + 1,
        "total": len(state['questions'])
    })

@app.route('/api/trivia/answer', methods=['POST'])
def trivia_answer():
    data = request.json
    answer = data.get('answer')
    
    state = session.get('trivia_state')
    if not state or state['current'] >= len(state['questions']):
        return jsonify({"error": "Game over or not started"}), 400
        
    q_index = state['current']
    q_data = state['questions'][q_index]
    correct_answer = q_data['answer']
    universe = q_data['universe']
    
    is_correct = (answer == correct_answer)
    art = None
    
    if is_correct:
        state['score'] += 1
        if universe == "HP":
            if not state['hp_arts']:
                state['hp_arts'] = hp_art.ASCII_ARTS.copy()
                random.shuffle(state['hp_arts'])
            art = state['hp_arts'].pop()
        else:
            if not state['st_arts']:
                state['st_arts'] = st_art.ASCII_ARTS.copy()
                random.shuffle(state['st_arts'])
            art = state['st_arts'].pop()
            
    state['current'] += 1
    session.modified = True
    
    game_over = state['current'] >= len(state['questions'])
    
    return jsonify({
        "correct": is_correct,
        "correct_answer": correct_answer,
        "art": art,
        "score": state['score'],
        "game_over": game_over,
        "total_questions": len(state['questions'])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
