import wolframalpha
import wikipedia
from translate import Translator

# Taking input from user
question = 'What is the capital of England'
  
# App id obtained by the above steps
app_id = 'A8Y4J6-WPRPYAYXXX'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)
  
# Stores the response from 
# wolf ram alpha
res = client.query(question)
  
try:
    answer = next(res.results).text
    print(answer)
except:
    print('error')

# print(wikipedia.summary("Donald Trump"))

# class clsTranslate():

#     def translateText(self, strString, strTolang):
#         self.strString = strString
#         self.strTolang = strTolang
#         translator = Translator(to_lang=self.strTolang)
#         translation = translator.translate(self.strString)
#         return (str(translation))

# # Create a Class object and call the Translate function

# objTrans=clsTranslate()
# strTranslatedText= objTrans.translateText('How are you', 'fr')

# print(strTranslatedText)