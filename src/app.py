from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

todos = [
    {
        "label": "My first task", 
        "done":False,
        }

    ]



@app.route('/todos', methods=['GET'])
def tedos():
    return  jsonify(todos)
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("incoming request with the following body",request_body)
    todos.append(request_body)
   
    return jsonify(todos)
   
@app.route("/todos/<int:position>",methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:",position)
    if 0 <= position < len(todos):
        # Remove the task at the specified position
        todos.pop(position)
    return jsonify(todos)

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)