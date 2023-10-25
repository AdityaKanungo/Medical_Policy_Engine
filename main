import streamlit as st
import pdfplumber
import openai

# Set your OpenAI API key
openai.api_key = ''

def process_pdf(file):
    with pdfplumber.open(file) as pdf:
        text_pages = [page.extract_text() for page in pdf.pages]
    return text_pages

def query_openai_api(query, text):
    prompt = (
        f"Please read the following document and answer the query based on its content:\n\n"
        f"Document:\n{text}\n\n"
        f"Query: {query}\n"
        f"Answer:"
    )
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.2,
        max_tokens=2500  # Adjust as needed
    )
    
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.title("Medicare Document Interaction")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        text_pages = process_pdf(uploaded_file)
        
        query = st.text_input("Enter your query")
        
        if st.button("Ask"):
            # Here you would implement a search algorithm to find the most relevant text chunk
            # For simplicity, this example just uses the first chunk
            most_relevant_chunk = text_pages[0] if text_pages else ""
            answer = query_openai_api(query, most_relevant_chunk)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()
