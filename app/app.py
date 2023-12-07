from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['query']
    # Process the query, search in Milvus, etc.
    results = process_query(user_query)  # Implement this function
    return render_template('results.html', results=results)  # Create a results template

if __name__ == '__main__':
    app.run(debug=True)
