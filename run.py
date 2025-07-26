import os
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env  # noqa: E402

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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

# Contact Us route
@app.route("/contactus", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        print("request...", request)
        print("request.form...", request.form)
        print("Name...", request.form["email"])
        
        flash("Thanks {}, we have received your message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def work():
    return render_template("careers.html", page_title="Careers")


print("name...", __name__)

# Check if the script is run directly
# and not imported as a module
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
