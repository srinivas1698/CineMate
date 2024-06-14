import streamlit as st
from langchain.llms import OpenAI
from neo4j import GraphDatabase, basic_auth

st.title('🎥 🔗 CineMate')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

context_prompt = """
You need to generate a cypher query to satisfy the user's request. 
The Neo4j database contains:
Nodes: Movie, Person
Relationship: 
ACTED_IN
DIRECTED
FOLLOWS
PRODUCED
REVIEWED
WROTE

Only generate the query. DO NOT generate any extra info or other text.
"""

display_prompt = """
This is the result returned from the Neo4j DB. Display the results to the user in an
readable and understandale format. Give the result like a helpful Movie Chatbot Assistant.
"""
def display_results(results):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(str(results) + display_prompt)
    st.info(response)

def queryNeo4jDB(query):
    driver = GraphDatabase.driver(
            "bolt://18.204.203.58:7687",
    auth=basic_auth("neo4j", "respirations-widths-infection"))
    with driver.session(database="neo4j") as session:
        results = session.read_transaction(
                    lambda tx: tx.run(query,
                      favorite="The Matrix").data())
        display_results(results)
    driver.close()

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    query = llm(input_text + context_prompt)
    queryNeo4jDB(query)


with st.form('my_form'):
    text = st.text_area('Enter text:', 'Need a movie suggestion, type here')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)