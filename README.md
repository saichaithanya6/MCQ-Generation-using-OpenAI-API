## Project Overview:

The project's goal is to automate the generation of multiple-choice questions using OpenAI's GPT-3.5 Turbo model based on a given input of text.

Here is the detailed step-by-step process done to create the project:

### Downloading Packages and Environments:
* Created this project in VS code to test locally in the computer.
* Created python environment, packages and API keys in the the environment. Connected VSCode to Git HUb to sync the code changes done the environment.

### Experimenting with the Code:
* Developed code to load the model from the OpenAI API:
        * Created a sequential chain to take an input template prompt and load the text into the LLM.
        * Built another chain to evaluate the generated MCQs.
        * Joined the two chains of LLMs using the Sequential Chain code.
* Tested the code using sample text with the LLM model, and the results were promising.

### Source Code:
* Replicated the experimental code in the source folder and deployed it in a Streamlit app.
* Ran the code and successfully tested it within the Streamlit app.
In conclusion, the app successfully generated MCQs based on the provided context using the LLM.

