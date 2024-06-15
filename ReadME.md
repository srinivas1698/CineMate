# CineMate Movie Wizard Chatbot

Welcome to CineMate, your helpful Movie Chatbot Assistant! CineMate leverages advanced AI and graph database technologies to provide insightful movie suggestions and information. This README file will guide you through the setup and usage of the CineMate Movie Wizard Chatbot.

## Features

- **Movie Suggestions**: Get personalized movie recommendations based on your input.
- **Graph Database Integration**: Utilizes Neo4j for an enriched database of movies and relationships.
- **AI-Powered Responses**: Uses OpenAI's language model to generate natural and helpful responses.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- OpenAI
- Neo4j

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/cinemate.git
   cd cinemate
   ```

2. **Install Dependencies**

   Ensure you have Python 3.7 or higher installed. Then, install the required packages:

   ```sh
   pip install streamlit langchain neo4j openai
   ```

3. **Set Up Neo4j Database**

   Make sure your Neo4j database is up and running. Update the connection details in the code if necessary.

## Running the Application

1. **Start the Streamlit App**

   Run the following command to start the Streamlit application:

   ```sh
   streamlit run app.py
   ```

2. **Enter Your OpenAI API Key**

   In the sidebar, enter your OpenAI API key. This key is required to generate responses.

3. **Use the Chatbot**

   Enter your query in the text area provided and submit it. The chatbot will process your request, generate a Cypher query, retrieve results from the Neo4j database, and display them in a readable format.

## Code Overview

Here’s a brief overview of the main components of the CineMate Movie Wizard Chatbot:

- **Input Form**: A form for user input where users can type their movie-related queries.
- **Query Generation**: Uses OpenAI’s language model to generate Cypher queries based on user input.
- **Database Interaction**: Connects to the Neo4j database, executes the Cypher query, and retrieves the results.
- **Result Display**: Formats and displays the results using OpenAI’s language model to ensure they are user-friendly.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your improvements.


Enjoy using CineMate, your personal movie wizard! If you encounter any issues or have any suggestions, feel free to open an issue on GitHub.