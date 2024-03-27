
# Gemini Characters Interaction

This REST API was developed for a simple computer science college project. The objective is to use the Gemini (Google LLM) for impersonating any character as if it was the character itself.

## Description
The main endoint (api/v1/interaction) does the objective. The API return the character response given a character name and question.

The other endpoints allow you to:
* Add a new character by sending its name and context in payload.
* List the existing characters names in database.
* Get a specific character context given a name.
* Get or update prompt template which is formatted and sent to the LLM

## Getting Started

### Dependencies

* [Python 3.8+](https://www.python.org/downloads/)
* [Gcloud CLI](https://cloud.google.com/sdk/docs/install)
* [Firestore Database](https://console.firebase.google.com/)
* [Prompts and Characters Firestore Collections](https://console.firebase.google.com/)
* [Gemini API Key](https://aistudio.google.com/app/apikey)

### Installing

* Create a GCP Project through the Firebase console.
* Create a Firestore database.
* Create the collections "characters" and "prompts".
* Generate a Gemini API Key.
* Authenticate and set Firebase project ID through Gcloud CLI.
* Clone the repository
* Create and activate python virtual env.
* Run "pip install requirements.txt".

### Executing program

* Create a environment variable and assign the Gemini API Key value to it.
* Run "cd src && uvicorn main:app"
* Open "localhost:8000/docs" in the browser.
* Create a prompt using /api/v1/prompt/ endpoint.
* Add a new character using /api/v1/characters endpoint.
* Ask any character a question using /api/v1/interaction endpoint.

### Prompt

You need to use the variables {char_name}, {char_context} and {question} in the prompt. These variables are replaced at runtime according to the char_name and question sent through request payload.

Simple example of prompt:
"You must answer the user's question by impersonating a character called '{char_name}' and fully following its context. This is the character's context: ### context ### {char_context} ### end context ###. User question: '{question}'"

## Authors

Carlos Takeshi Sato - [Linkedin](https://linkedin.com/in/carlostak/)

## Version History

* 0.1
    * Initial Release
