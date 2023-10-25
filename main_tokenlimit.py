import streamlit as st
import pdfplumber
import openai

# Set your OpenAI API key
openai.api_key = ''

def process_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def query_openai_api(query, text):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"{text}\n\nQuery: {query}\nAnswer:",
      temperature=0,
      max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.title("Medicare Document Interaction")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        text = process_pdf(uploaded_file)
        st.text_area("Extracted Text", text, height=250)
        
        query = st.text_input("Enter your query")
        
        if st.button("Ask"):
            answer = query_openai_api(query, text)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()
