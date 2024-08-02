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
    frame = BEV.getFrame("tca-tec", "videos/clz6npp6r00055bsy3un6xbe8.mp4")

    BEV.get_homography(frame)

    #TODO (alecoeto): save CSV in bucket
    return jsonify({"result": "Success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)