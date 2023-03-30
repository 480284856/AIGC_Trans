from flask import Flask, render_template, request

app = Flask(__name__)

def GetResponse(sentence, word):
    import http.client
    import json

    conn = http.client.HTTPConnection("52.53.227.127", 8000)
    payload = json.dumps({
        "prompt": '''Context: I need to throw a dinner party for three vegetarians.\nQuestion: What does "throw" mean here?\nExplanation: In this context, "throw" means to host or organize a dinner party. The phrase "throw a dinner party" is a colloquial expression that means to host a dinner event in one's home or at a restaurant. In the given context, the individual needs to organize a dinner party for three vegetarians.\n\nContext: {}\nQuestion: What does "{}" mean here?\nExplanation:'''.format(
            sentence, word),
        "max_tokens": 200,
        "n": 2,
        "top_p": 0.8,
        "temperature": 0.8
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': '52.53.227.127:8000',
        'Connection': 'keep-alive'
    }
    conn.request("POST",
                 "/v1/engines/text-davinci-003/completions",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    response:str = data.decode("utf-8")
    response:dict = json.loads(response)
    return response['choices'][0]['text']

@app.route('/trans', methods=['POST','GET'])
def test():
    if request.method == 'POST':
        sentence = request.form['sentence'].strip()
        word = request.form['word'].strip()
        explanation = GetResponse(sentence, word)
        return render_template("index.html", sentence=sentence,word=word,explanation=explanation)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)