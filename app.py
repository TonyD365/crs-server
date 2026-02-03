from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # 只要有人访问你的 Koyeb 网址，就返回这句话
    return "Hello World! Greetings from Canada."

if __name__ == "__main__":
    # Koyeb 默认监听 8080 端口，必须设置为 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
