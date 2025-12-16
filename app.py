from flask import Flask, request, jsonify, render_template
from groq import Groq

client = Groq(api_key="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")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ================== EXPLAIN ERRORS ==================
@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    code = data["code"]
    language = data["language"]

    prompt = f"""
You are an expert {language} programmer.

Analyze the following code and identify ALL errors.

INSTRUCTIONS (STRICT):
- For EACH error:
  1. Mention the exact LINE NUMBER
  2. Show the exact faulty LINE
  3. Explain the error clearly in simple words
- Use numbered errors
- Do NOT provide fixed code
- Do NOT add suggestions
- Do NOT add extra text

FORMAT EXACTLY LIKE THIS:

Error 1:
Line <number> → <faulty code>

Explanation:
<simple explanation>

Error 2:
Line <number> → <faulty code>

Explanation:
<simple explanation>

Code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "explanation": response.choices[0].message.content
    })

# ================== FIX CODE ONLY ==================
@app.route("/fix", methods=["POST"])
def fix():
    data = request.get_json()
    code = data["code"]
    language = data["language"]

    prompt = f"""
You are an expert {language} developer.

Fix the code below.

RULES (STRICT):
- Return ONLY the fully corrected code
- No explanation
- No markdown
- No comments unless required by syntax
- Code must be ready to copy & run in compiler

Code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "fixed_code": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
