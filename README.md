# COSC 310 Individual Project

![Cute lil robot!](https://upload.wikimedia.org/wikipedia/commons/7/75/Kawaii_robot_power_clipart.svg)

<sub><sup>**IMAGE CREDIT**</sub></sup><br>
<sub><sup>"File:Kawaii robot power clipart.svg" by Mvolz is marked under CC0 1.0.</sub></sup>

**CHATBOT PROGRAM**

This program is meant to be a simple chatbot capable of 30 rounds of semi-natural speech. This was initally done via simple phrase recognition but has been upgraded to use python's natural language toolkit, and then further upgraded to include a few basic APIs. 

## Toolkits added for Group A3

- Misspelling handling via Porter Stemmer.
> Program stems user input and checks against stemmed sentences on the backend, allowing the system to handle minor gramatical errors.

- Part of Speech recognition.
> In order to make sure the user is giving a valid name or food item, the system checks for a noun when asking for user input for stored values.

- Named entity recognition.
> Similar to the POS recognition, the program uses NER to isolate the name of an organization from a string when the user inputs a response to a question like 'What is your favorite hockey team?"

- A simple GUI via Python's Tkinter functionality.
> The title explains it pretty well, this allows the user to input conversation in a more standard setting. This also allows the user to look back through chat history.

- More varried responses when the agent doesn't understand.
> In order to make the program a bit more dynamic, it can now randomly pick from one of five error sentences instead of just the one.

POS Tagging<br/>
![POS](https://github.com/COSC-310-Group-24/Assignment-2/blob/main/Images/pos.png?raw=true "Demonstration of POS tagging")

Named Entity Recognition<br/>
![NER](https://github.com/COSC-310-Group-24/Assignment-2/blob/main/Images/ner.png?raw=true "Demonstration of Named Entity Recognition")

Stemming<br/>
![STEM](https://github.com/COSC-310-Group-24/Assignment-2/blob/main/Images/stem.png?raw=true "Demonstration of Porter Stemmer")

GUI<br/>
![GUI](https://github.com/COSC-310-Group-24/Assignment-2/blob/main/Images/gui.png?raw=true "Demonstration of GUI")

More varried responses (some not shown, bad RNG)<br/>
![RANDOM](https://github.com/COSC-310-Group-24/Assignment-2/blob/main/Images/random.png?raw=true "Demonstration of Responses")

## APIs added for Individual Project

- Wolfram API.
> Program can send "What is" "How much/many" or math problems to Wolfram and return the response.

- Wikipedia API.
> Program can return the first sentence of any wikipedia article to give a general summary of a topic.

- Microsoft Translate API.
> Program can parrot back a sentence the user inputs in another language.

Wolfram API<br/>
![WOLF](https://github.com/MasonPles/COSC310FinalProject/blob/main/Images/wolf.png?raw=true "Wolfram API")

Wikipedia API<br/>
![WIKI](https://github.com/MasonPles/COSC310FinalProject/blob/main/Images/wiki.png?raw=true "Wikipedia API")

Microsoft Translate API<br/>
![TRANSLATE](https://github.com/MasonPles/COSC310FinalProject/blob/main/Images/translate.png?raw=true "Microsoft Translate API")
