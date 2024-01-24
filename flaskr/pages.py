from flask import render_template, Flask

def make_endpoints(app):
    
    @app.route("/")
    def home():
        return render_template(
            'base.html',
            page_name="Home Page",
            page_content="Base Home Page for Our Website"
        )