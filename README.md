# CHATBOT NLP BACKEND

Chatbot in Python using spacy library.

## How does it work?

First of all, it's recommended to create a virtual environment for this chatbot project. So, install all the dependencies - after downloading the project, of course -, as follows:

```cmd
mkdir chatbot-nlp-backend
```

The command above creates a directory with the specified name, in this case `chatbot-nlp-backend`. So, just get in the folder and create a Python Virtual Environment. You can do it like this:

```
python -m venv env
```

Now, you must install all the dependencies:

```
pip install -r requirements.txt
```

So, get in the src folder where there's application file and run:

```
uvicorn application:app --reload
```
Ready! API is running! 

Address: `http://localhost:8000/`
