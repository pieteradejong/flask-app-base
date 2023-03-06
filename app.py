from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = []

@app.route('/')
def index():
    return "Hello, World."

@app.route('/<name>')
def print_name(name):
    return f"Hello, {name}."


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            "Nothing Found", 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        ID = books_list[-1]['id']+1

        new_obj = {
            'id': ID,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }

        books_list.append(new_obj)

        return jsonify(books_list), 201


if __name__ == "__main__":
    app.run()
