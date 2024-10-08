import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from source.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from source.mcqgenerator.MCQgenerator import generate_evaluate_chain
from source.mcqgenerator.logger import logging

#loading json file
with open(r"D:\ai-pro\project\response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#Create a form using st.form
with st.form("user_inputs"):
    #File Upload
    file= st.file_uploader("Update a PDF or txt file")
    
    #Input Fields
    Number_of_MCQ= st.number_input("No. of MCQs", min_value=3, max_value=50)
    
    #Subject
    Topic= st.text_input("Insert Subject", max_chars=20)
    
    #Quiz tone
    Difficulty = st.text_input("Complexity Level of Questions", max_chars=20, placeholder="Simple")
    
    #Add Button
    submit_button= st.form_submit_button("Create MCQs")
    
    #Check if the button is Clicked and all fields have input
    
    if submit_button and file is not None and Number_of_MCQ and Topic and Difficulty:
        with st.spinner("loading..."):
            try:
                text= read_file(file)
                
                #Count tokens and cost of API call
                with get_openai_callback() as cb:
                    response= generate_evaluate_chain(
                        {
                            "text": text,
                            "number": Number_of_MCQ,
                            "subject": Topic,
                            "tone": Difficulty,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
                #st.write(response)
            
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Complete Tokens:{cb.completion_tokens}")
                if isinstance(response, dict):
                    #Extract the quiz data from response
                    quiz= response.get("quiz", None)
                    if quiz is not None:
                        table_data= get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in a text box as well
                            st.text_area(label= "Review", value= response["review"])
                        else:
                            st.error("Error in the table data")
                            
                else:
                    st.write(response)
                
                    
                