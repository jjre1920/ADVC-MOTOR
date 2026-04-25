from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sistema_status = {
    "comandante": "Jesús Javier Rubio Escutia",
    "proyecto": "Advance Global 2027",
    "nodos_activos": 20,
    "educacion": {"mateo": "Pendiente", "juan_diego": "Pendiente"}
}

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>ADVANCE CORE - 2027</title>
            <style>
                body { background: #0a0a0a; color: #00f2ff; font-family: sans-serif; 
                       display: flex; flex-direction: column; align-items: center; 
                       justify-content: center; height: 100vh; margin: 0; }
                .panel { border: 2px solid #00f2ff; padding: 40px; border-radius: 10px;
                         background: rgba(0, 242, 255, 0.05); text-align: center; }
                .pulse { width: 15px; height: 15px; background: #00f2ff; 
                         border-radius: 50%; display: inline-block; animation: p 2s infinite; }
                @keyframes p { 0% { box-shadow: 0 0 0 0 rgba(0,242,255,0.7); } 
                               70% { box-shadow: 0 0 0 10px rgba(0,242,255,0); } }
            </style>
        </head>
        <body>
            <div class="panel">
                <div class="pulse"></div>
                <h1>ADVANCE GLOBAL CORE</h1>
                <p>Arquitecto: Rubio Escutia</p>
                <p style="font-size: 0.8em; color: #00f2ff;">PROTOCOL 2027 - ACTIVE</p>
            </div>
        </body>
    </html>
    """

@app.route('/status')
def get_status():
    return jsonify(sistema_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
