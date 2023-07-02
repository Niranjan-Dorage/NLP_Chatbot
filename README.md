# CHATBOT NLP BACKEND

Chatbot in Python using spacy library.

## How does it work?

First of all, it's recommended to create a virtual environment for this chatbot project. So, install all the dependencies - after downloading the project, of course - as follows:

```cmd
mkdir chatbot-nlp-backend
```

The command above creates a directory with the specified name, in this case `chatbot-nlp-backend`. So, just get in the folder and create a Python Virtual Environment. You guys can do it like this:

```
python -m venv env
```

Now, you guys must install all project's the dependencies:

```
pip install -r requirements.txt
```

So, get in the source (src) folder where there's application file and run:

```
uvicorn application:app --reload
```
Ready! API is running! 

Address: `http://localhost:8000/`

## Docker

You guys can run it on Docker. For this you will need to create an image and run a container from it. In the folder where the Dockerfile file is, run the following commands:

```
docker build -t <<name_image>> .
```

Afterwards

```
docker run -d --name <<name_container>> -p 80:80 <<name_image>>
```

The address keep up same.

It's worth mentioning that FastAPI automatically provide the API documentation. For access it, you can go `http://127.0.0.1:8000/docs`.

That's it! Bye!
