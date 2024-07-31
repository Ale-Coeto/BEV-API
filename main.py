from flask import Flask, request, jsonify
from BEV.BEV import BEV

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/birdsEyeView', methods=['POST'])
def get_homography_BEV():
    img_id = request.get_json()["id"]
    
    #TODO (alecoeto): download video from bucket, extract first frame and send it to get_homography()

    img = "parque1.jpeg"
    BEV.get_homography(img)

    #TODO (alecoeto): save CSV in bucket
    return jsonify({"result": "Success"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)