from flask import Flask, request
import subprocess
import json

app = Flask(__name__)


@app.route('/simulation', methods=['POST'])
def run_simulation():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        jsonfile = request.json 
    else:
        return 'Content-Type not supported!'
    # Extract the three string arguments from the request body
    #avatar_filename = request.form['avatar_filename']
    #garnment_filename = request.form['garment_filename']
    #filename = request.form['filename']
    print(jsonfile)
    json_str = json.dumps(jsonfile)
    jsonobj = json.loads(json_str)
    

    garments = []
    avatar_filename = jsonobj['avatar_filename']

    for garment_filename in jsonobj['garment_filename']:
        garments.append(garment_filename)

    
    filename = jsonobj['filename']

    print("lors de la simulation le fichier aura le nom :")
    print(filename)

    print("Durant la simulation les vetements suivant seront simuler")
    print(garments)

    print("Durant la simulation voici l'avatar utilisé")
    print(avatar_filename)
    # Run the hello.py script as a subprocess
    # process = subprocess.Popen(["python", "openwithpath.py", avatar_filename])
    # process.wait()
    
    # process = subprocess.Popen(["python", "openwithpathgarnment.py", garments[0]])
    # process.wait()
    
    # lenght = len(garments)

    # if (lenght > 1):
    #     process = subprocess.Popen(["python", "openwithpathgarnment2.py", garments[1]])
    #     process.wait()

    # process = subprocess.Popen(["python", "save_export.py", filename])
    # process.wait()

    # process = subprocess.Popen(["python", "blend.py", filename])
    # process.wait()


    # Return the file to the client
    return "OK"

@app.route('/', methods=['GET'])
def hello():

    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)