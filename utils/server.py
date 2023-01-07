from flask import Flask

from main import port
from utils.general import read_file

server = Flask("HTTP-Server")
file_cash = {}


@server.route("/css/<path:css>", methods=["GET"])
def get_css_file(css):
    if css not in file_cash:
        file_content = read_file("/web-content/css/" + css)
        file_cash[css] = file_content
        return file_content
    else:
        return file_cash[css]


@server.route("/js/<path:js>", methods=["GET"])
def get_js_file(js):
    if js not in file_cash:
        file_content = read_file("/web-content/js/" + js)
        file_cash[js] = file_content
        return file_content
    else:
        return file_cash[js]


@server.route("/", methods=["GET"])
def root():
    return read_file("./web-content/html/index.html")


server.run("localhost", port)
