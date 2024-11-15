// Function to increment Player One's Toxicity
function p1_increment_tox() {
    fetch('/p1_increment_tox', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pOneTox').innerText = data.newToxValue;

        // Display winner message if there's a winner
        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to decrement Player One's Toxicity
function p1_decrement_tox() {
    fetch('/p1_decrement_tox', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pOneTox').innerText = data.newToxValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to increment Player Two's Toxicity
function p2_increment_tox() {
    fetch('/p2_increment_tox', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pTwoTox').innerText = data.newToxValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to decrement Player Two's Toxicity
function p2_decrement_tox() {
    fetch('/p2_decrement_tox', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pTwoTox').innerText = data.newToxValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to increment Player One's Health
function p1_increment_health() {
    fetch('/p1_increment_health', { method: 'POST' })  // Correct endpoint
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  // Parse the JSON response
        })
        .then(data => {
            console.log('Parsed data:', data); // Debugging
            document.getElementById('pOnePool').innerText = data.pOnePool; // Update HTML
        })
        .catch(error => console.error('Error incrementing health:', error));
}

// Function to decrement Player One's Health
function p1_decrement_health() {
    fetch('/p1_decrement_health', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pOnePool').innerText = data.newHealthValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to increment Player Two's Health
function p2_increment_health() {
    fetch('/p2_increment_health', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pTwoPool').innerText = data.newHealthValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to decrement Player Two's Health
function p2_decrement_health() {
    fetch('/p2_decrement_health', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pTwoPool').innerText = data.newHealthValue;

        if (data.winner) {
            const winnerMessage = document.getElementById('winner-message');
            winnerMessage.innerText = data.winner + " wins!";
            winnerMessage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to reset the game
function resetGame() {
    fetch('/reset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Reset data received:", data);
        document.getElementById('pOnePool').innerText = data.pOnePool;
        document.getElementById('pTwoPool').innerText = data.pTwoPool;
        document.getElementById('pOneTox').innerText = data.pOneTox;
        document.getElementById('pTwoTox').innerText = data.pTwoTox;

        const winnerMessage = document.getElementById('winner-message');
        if (winnerMessage) winnerMessage.style.display = 'none';
    })
    .catch(error => console.error('Error resetting values:', error));
}