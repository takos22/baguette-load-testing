from quart import Quart

app = Quart(__name__)


@app.route("/quart", methods=["GET"])
async def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8004)
