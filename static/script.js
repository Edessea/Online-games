const app = {
    // STATE
    views: ['main-menu', 'guessing-game', 'trivia-menu', 'trivia-game', 'trivia-end'],
    guessLog: [],
    
    // NAVIGATION
    showView(viewId) {
        this.views.forEach(v => {
            document.getElementById(v).classList.remove('active');
        });
        document.getElementById(viewId).classList.add('active');
    },

    // ------------------------------------
    // GUESSING GAME
    // ------------------------------------
    async startGame(gameType) {
        if (gameType === 'guess') {
            try {
                const res = await fetch('/api/guess/start', { method: 'POST' });
                if (res.ok) {
                    document.getElementById('start-guess-btn').classList.add('hidden');
                    document.getElementById('guess-play-area').classList.remove('hidden');
                    this.guessLog = ["--- WELCOME TO THE GUESSING GAME ---", "I'm thinking of a number between 1 and 100."];
                    this.updateGuessLog();
                    document.getElementById('guess-input').focus();
                }
            } catch (e) {
                console.error("Failed to start game", e);
            }
        }
    },

    updateGuessLog() {
        const logHtml = this.guessLog.map(line => `<div>${line}</div>`).join('');
        const logEl = document.getElementById('guess-log');
        logEl.innerHTML = logHtml;
        logEl.scrollTop = logEl.scrollHeight;
    },

    handleGuessEnter(e) {
        if (e.key === 'Enter') {
            this.submitGuess();
        }
    },

    async submitGuess() {
        const inputEl = document.getElementById('guess-input');
        const guess = inputEl.value;
        if (!guess) return;

        this.guessLog.push(`> ${guess}`);
        inputEl.value = '';
        inputEl.focus();

        try {
            const res = await fetch('/api/guess/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ guess: parseInt(guess) })
            });
            const data = await res.json();
            if (data.error) {
                this.guessLog.push(`Error: ${data.error}`);
            } else {
                this.guessLog.push(data.message);
                if (data.result === 'correct') {
                    this.guessLog.push("--- GAME OVER ---");
                    document.getElementById('guess-input').disabled = true;
                    setTimeout(() => {
                        document.getElementById('start-guess-btn').classList.remove('hidden');
                        document.getElementById('start-guess-btn').innerText = "Play Again";
                        document.getElementById('guess-play-area').classList.add('hidden');
                        document.getElementById('guess-input').disabled = false;
                    }, 3000);
                }
            }
            this.updateGuessLog();
        } catch (e) {
            console.error(e);
        }
    },

    // ------------------------------------
    // TRIVIA GAME
    // ------------------------------------
    async startTrivia(difficulty) {
        try {
            const res = await fetch('/api/trivia/start', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ difficulty })
            });
            if (res.ok) {
                this.showView('trivia-game');
                this.loadNextTriviaQuestion();
            }
        } catch (e) {
            console.error("Failed to start trivia", e);
        }
    },

    async loadNextTriviaQuestion() {
        document.getElementById('trivia-next-btn').classList.add('hidden');
        document.getElementById('trivia-art-box').classList.add('hidden');
        document.getElementById('trivia-art-box').innerHTML = "";
        
        try {
            const res = await fetch('/api/trivia/question');
            if (!res.ok) {
                 this.showView('trivia-end');
                 return;
            }
            const data = await res.json();
            
            if (data.error) {
                console.error(data.error);
                return;
            }

            document.getElementById('trivia-progress').innerText = `Question ${data.current}/${data.total}`;
            const emoji = data.universe === "HP" ? "🧙" : "🚲";
            document.getElementById('trivia-q-box').innerHTML = `${emoji} ${data.question}`;
            
            const optionsGroup = document.getElementById('trivia-options');
            optionsGroup.innerHTML = '';
            
            data.options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'option-btn';
                btn.innerText = opt;
                btn.onclick = () => this.submitTriviaAnswer(opt, btn);
                optionsGroup.appendChild(btn);
            });

        } catch (e) {
             console.error(e);
        }
    },

    async submitTriviaAnswer(answer, btnEl) {
        const buttons = document.querySelectorAll('.option-btn');
        buttons.forEach(b => b.disabled = true); // Disable all once answered

        try {
            const res = await fetch('/api/trivia/answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ answer })
            });
            const data = await res.json();
            
            document.getElementById('trivia-score').innerText = `Score: ${data.score}`;

            if (data.correct) {
                btnEl.classList.add('correct');
                if (data.art) {
                    const artBox = document.getElementById('trivia-art-box');
                    artBox.innerText = data.art;
                    artBox.classList.remove('hidden');
                }
            } else {
                btnEl.classList.add('incorrect');
                // find correct button and highlight green
                buttons.forEach(b => {
                    if (b.innerText === data.correct_answer) {
                        b.classList.add('correct');
                    }
                });
            }

            if (data.game_over) {
                document.getElementById('trivia-next-btn').innerText = "See Results →";
                document.getElementById('trivia-next-btn').onclick = () => this.showTriviaResults(data.score, data.total_questions);
            } else {
                document.getElementById('trivia-next-btn').innerText = "Next Question →";
                document.getElementById('trivia-next-btn').onclick = () => this.loadNextTriviaQuestion();
            }
            document.getElementById('trivia-next-btn').classList.remove('hidden');

        } catch (e) {
            console.error(e);
        }
    },

    showTriviaResults(score, total) {
        document.getElementById('trivia-final-score').innerText = `${score}/${total}`;
        let msg = "";
        if (score === total) msg = "🌟 Outstanding! You're a true trivia master! 🌟";
        else if (score >= total * 0.7) msg = "✨ Exceeds Expectations! Well done! ✨";
        else if (score >= total * 0.5) msg = "📜 Acceptable! Not bad for a beginner. 📜";
        else msg = "🐉 Poor! You might need to study more. 🐉";
        
        document.getElementById('trivia-final-msg').innerText = msg;
        this.showView('trivia-end');
    }
};
