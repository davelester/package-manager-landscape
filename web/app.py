from flask import Flask, render_template, redirect
import toml
import os
import sys

app = Flask(__name__)

web_dir = os.path.dirname(os.path.realpath(__file__))
landscape_file_path = os.path.join(web_dir, '..', 'landscape.toml')

with open(landscape_file_path, 'r') as f:
    landscape = toml.load(f)

# Count Package Managers included in landscape
pmcount=0
for category in landscape:
    for ecosystems in landscape[category]:
        for item in landscape[category][ecosystems]:
            pmcount+=1

@app.route("/")
def index():
    return render_template('index.html', landscape=landscape, pmcount=pmcount)

@app.route("/contribute/")
def contribute():
    return redirect('https://github.com/davelester/package-manager-landscape/blob/main/CONTRIBUTING.md', code=302)

if __name__ == '__main__':
    app.run(debug=False)