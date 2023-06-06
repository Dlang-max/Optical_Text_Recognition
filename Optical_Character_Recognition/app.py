import streamlit as st
import cv2
import tempfile
import numpy as np
import easyocr
from gingerit.gingerit import GingerIt




st.title('Upload Your Image for Text Recognition')
file = st.file_uploader("Upload Your Image Here")

if file:
    print(file.name)

    temp_file = tempfile.NamedTemporaryFile(delete=False)

    # Write the uploaded file data to the temporary file
    temp_file.write(file.getvalue())

    # Get the full path to the temporary file
    file_path = temp_file.name

    # Close the temporary file
    temp_file.close()

    st.write("File saved to:", file_path)

    image = cv2.imread(file_path)

    reader = easyocr.Reader(['en'], gpu=False)
    results_unpolished = reader.readtext(file_path)

    s = ""
    for result in results_unpolished:
        s += result[len(result) - 2] + " "

    print(s)

    text = s

    parser = GingerIt()
    results_polished = parser.parse(text)

    print(results_polished['result'])

    st.write('Text in Image:', results_polished['result'])

    pass