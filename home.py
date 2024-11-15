from flask import Flask, jsonify, render_template


app = Flask(__name__)

pOnePool=20
pTwoPool=20

pOneTox=0
pTwoTox=0

@app.route('/p1_increment_tox', methods=['POST'])
def p1_increment_tox():
    global pOneTox

    pOneTox += 1


    # Return the updated value of pOneTox and winner status
    return jsonify(newToxValue=pOneTox)

@app.route('/p1_decrement_tox', methods=['POST'])
def p1_decrement_tox():
    global pOneTox

    pOneTox -= 1


    # Return the updated value of pOneTox and winner status
    return jsonify(newToxValue=pOneTox)

@app.route('/p2_increment_tox', methods=['POST'])
def p2_increment_tox():
    global pTwoTox

    pTwoTox += 1

    return jsonify(newToxValue=pTwoTox)

@app.route('/p2_decrement_tox', methods=['POST'])
def p2_decrement_tox():
    global pTwoTox

    pTwoTox -= 1

    return jsonify(newToxValue=pTwoTox)


@app.route('/p1_decrement_health', methods=['POST'])
def p1_decrement_health():
    global pOnePool

    pOnePool -= 1

    return jsonify(newToxValue=pOnePool)

@app.route('/p1_increment_health', methods=['POST'])
def p1_increment_health():
    global pOnePool

    pOnePool += 1


    return jsonify({"pOnePool": pOnePool})

@app.route('/p2_increment_health', methods=['POST'])
def p2_increment_health():
    global pTwoPool
    
    pTwoPool += 1


    return jsonify(newToxValue=pTwoPool)


@app.route('/p2_decrement_health', methods=['POST'])
def p2_decrement_health():
    global pTwoPool
    
    pTwoPool -= 1

    return jsonify(newToxValue=pTwoPool)

@app.route("/")
def home():
    return render_template("index.html", pOnePool=pOnePool, pTwoPool=pTwoPool, pOneTox=pOneTox, pTwoTox=pTwoTox)

# Route to handle reset requests
@app.route("/reset", methods=["POST"])
def reset():
    global pOnePool, pTwoPool, pOneTox, pTwoTox

    pOnePool = 20
    pTwoPool = 20
    pOneTox = 0
    pTwoTox = 0

    # Return the reset values as a JSON response
    return jsonify({
        "pOnePool": pOnePool,
        "pTwoPool": pTwoPool,
        "pOneTox": pOneTox,
        "pTwoTox": pTwoTox
    })

if __name__ == "__main__":
    app.run(debug=True)
