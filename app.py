from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    num = request.args.get('number')
    return jsonify({
        "status": "success",
        "developer": "ANISH EXPLOITS",
        "result": {
            "number": num,
            "info": "API is working for " + str(num),
            "owner": "Shubham"
        }
    })

if __name__ == '__main__':
    app.run()
  
