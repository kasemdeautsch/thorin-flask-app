import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open(os.path.join(app.root_path, 'data', 'company.json'), 'r') as f:
        data = json.load(f)

    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_url>")
def about_member(member_url):
    print("member_url: ", member_url)
    member = {}
    with open(os.path.join("data", "company.json"), "r") as json_data:
        info = json.load(json_data)
        # print("info...", info)
        # print("info_type.", type(info))
        
        for obj in info:
            if obj["url"] == member_url:
                member = obj
                print("member...", member)
    return render_template('member.html', member=member)
    



@app.route("/contactus")
def add():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def work():
    return render_template("careers.html", page_title="Careers")


print("name...", __name__)
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)