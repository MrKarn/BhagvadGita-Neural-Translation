from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

def translate_sanskrit(text):
  """Translates Sanskrit text to Hindi using Google Translate."""
  translator = Translator()
  try:
    translation = translator.translate(text, dest='hi')
    return translation.text
  except:
    # Handle translation errors (e.g., network issues)
    return "An error occurred during translation. Please try again later."

@app.route('/', methods=['GET', 'POST'])
def translate():
  if request.method == 'POST':
    sanskrit_text = request.form['sanskrit_text']
    hindi_translation = translate_sanskrit(sanskrit_text)
  else:
    sanskrit_text = ""
    hindi_translation = ""
  return render_template('index.html', sanskrit_text=sanskrit_text, hindi_translation=hindi_translation)

if __name__ == '__main__':
  app.run(debug=True)
  
