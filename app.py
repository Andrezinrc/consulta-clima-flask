from flask import Flask
from flask import url_for, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  
  data = {}

  if request.method == "POST":
    API_KEY = "" #coloque sua chave
    cidade = request.form.get("cidade")
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
    
    try:
      response = requests.get(link)
      data = response.json()
      print(data)
    except Exception as erro:
      return f"Nao foi possivel acessar a api {erro}"

  return render_template("index.html", data=data)
if __name__ == "__main__":
  app.run(debug=True)
