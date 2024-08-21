import streamlit as st
from parsera_pieces import Parsera
import pandas as pd
import asyncio

async def fetch_data(url, elements):
    scraper = Parsera(None)
    result = await scraper.arun(url=url, elements=elements)
    return result

def main():
    st.title("AI powered Web Scraper - Integrating Pieces with Parsera")

    st.header("If you wish to try out Parsera: https://parsera.org/app")


    # User input for URL
    url = st.text_input("Enter the URL:", "https://raw.githubusercontent.com/pieces-app/plugin_sublime/main/README.md")

    # Initialize session state for feature names and descriptions
    if 'feature_names' not in st.session_state:
        st.session_state.feature_names = []
    if 'feature_descriptions' not in st.session_state:
        st.session_state.feature_descriptions = []
    if 'num_features' not in st.session_state:
        st.session_state.num_features = 1

    # Number of features input
    num_features = st.number_input("Number of Features", min_value=1, value=st.session_state.num_features, step=1, key='num_features')

    # Update session state based on the number of features
    if len(st.session_state.feature_names) < num_features:
        st.session_state.feature_names.extend([''] * (num_features - len(st.session_state.feature_names)))
    elif len(st.session_state.feature_names) > num_features:
        st.session_state.feature_names = st.session_state.feature_names[:num_features]

    if len(st.session_state.feature_descriptions) < num_features:
        st.session_state.feature_descriptions.extend([''] * (num_features - len(st.session_state.feature_descriptions)))
    elif len(st.session_state.feature_descriptions) > num_features:
        st.session_state.feature_descriptions = st.session_state.feature_descriptions[:num_features]

    # Form for adding multiple feature entries
    with st.form(key='feature_form'):
        st.subheader("Add Features")

        # Input fields for feature names and descriptions
        for i in range(num_features):
            st.session_state.feature_names[i] = st.text_input(f"Feature Name {i + 1}", st.session_state.feature_names[i])
            st.session_state.feature_descriptions[i] = st.text_input(f"Feature Description {i + 1}", st.session_state.feature_descriptions[i])

        submit_button = st.form_submit_button("Add Features")

    # Button to trigger the scraping
    if submit_button:
        # Create elements dynamically based on user input
        elements = {
            "Features": [
                {name: desc for name, desc in zip(st.session_state.feature_names, st.session_state.feature_descriptions)}
            ]
        }

        # Run the async function
        result = asyncio.run(fetch_data(url, elements))
        
        # Render the result in a table
        if result:
            # Create a DataFrame from the result
            df = pd.DataFrame(result)

            # Check if the DataFrame is not empty
            if not df.empty:
                # Display the DataFrame in a table format
                st.table(df)
            else:
                st.write("No results found.")

if __name__ == "__main__":
    main()
