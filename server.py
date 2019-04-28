"""
Written By Ari Bornstein
"""
import io, time, requests, argparse
from flask import Flask, jsonify
from flask import request
import matplotlib.font_manager
import matplotlib.pyplot as plt

app = Flask(__name__)

def text2img(text):
    """
    Takes a string of under 200 characters and 
    returns an image buffer represenation of the string
    using matplotlib 
    """
    fig = plt.figure()
    plt.axis([0, 10, 0, 10])
    plt.text(5, 10, text, fontsize=12,  ha='center', va='top', wrap=True)
    plt.axis('off')
    image_data = io.BytesIO()
    plt.savefig(image_data, format='png')
    image_data.seek(0)
    return image_data

def ocr(img_data):
    """
    Apply OCR to text 
    """
    # Read the image into a byte array
    headers = {'Ocp-Apim-Subscription-Key': args.key,
                'Content-Type': 'application/octet-stream'}
    params = {'mode': 'Handwritten'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=img_data)
    response.raise_for_status()
    img_data.close()

    # The recognized text isn't immediately available, so poll to wait for completion.
    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        time.sleep(.5)
        if ("recognitionResults" in analysis):
            return " ".join([line["text"] for line in analysis["recognitionResults"][0]["lines"]])

        if ("status" in analysis and analysis['status'] == 'Failed'):
            return "Failed"
    else:
        return "Failed"

@app.route('/',methods=['GET'])
def clean_homoglyphs():
    if request.method == 'GET': 
        query = request.args.get('q')
        if (not query) or len(query) > 200:
            return "Demo service only supports requests of less than 200 characters."
        image_data = text2img(query)
        clean_text = ocr(image_data)
        if clean_text != "Failed":
            return jsonify({"Query":query,
                    "Clean_Text": clean_text})
        else:
            return clean_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", action="store", default="westeurope")
    parser.add_argument("-k", "--key", action="store")
    args = parser.parse_args()
    analyze_url = "https://{}.api.cognitive.microsoft.com/vision/v2.0/read/core/asyncBatchAnalyze".format(args.region)
    app.run(host='0.0.0.0')

    