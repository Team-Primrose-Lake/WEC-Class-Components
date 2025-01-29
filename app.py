# app.py
import streamlit as st
import matlab.engine
import numpy as np
import pandas as pd
import os
from PIL import Image


# Function to start MATLAB engine and add paths
eng = matlab.engine.start_matlab()
eng.addpath(r"C:\\SHAMM\\github repos\\WEC-Class-Components\\matlab_scripts")

#eng = start_matlab()

# Streamlit App Layout
st.title("Fire Hall Coverage Simulation")

st.sidebar.header("Input Parameters")

# File upload for input file
uploaded_file = st.sidebar.file_uploader("Upload Input File", type=["csv"])

# Output file name
outputfile = st.sidebar.text_input("Output CSV File Name", "output_centers.csv")
output_image = "coverage_plot.png"

# Output image file name
#output_image = st.sidebar.text_input("Output Plot Image", "coverage_plot.png")

# Buffer radius 'r'
r = st.sidebar.number_input("Buffer Radius (r) in km", min_value=0.1, value=2.5, step=0.1)

# Overlap factor
overlap_factor = st.sidebar.number_input("Overlap Factor", min_value=0.0, value=0.85, step=0.05)

# Visualization option
visualize_circles = st.sidebar.checkbox("Visualize Circles", value=True)

# Button to execute MATLAB function
if st.sidebar.button("Run Processing"):
    if uploaded_file:
        # Save the uploaded file to a temporary location
        temp_input_path = r"data\\temp_input.csv"
        with open(temp_input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Call the MATLAB function
            eng.firehall_algorithm(temp_input_path, outputfile, r, overlap_factor, visualize_circles, nargout=0)
            #eng.read_lat_lon(temp_input_path)
            st.success(f"Processing completed! Results saved to `{outputfile}`.")
            
            # Provide a download link for the output CSV
            if os.path.exists(outputfile):
                with open(outputfile, "rb") as f:
                    st.download_button(
                        label="Download Output CSV",
                        data=f,
                        file_name=outputfile,
                        mime="text/csv"
                    )
            else:
                st.warning(f"Output file `{outputfile}` not found.")
            
            # Display the CSV contents
            if os.path.exists(outputfile):
                df = pd.read_csv(outputfile)
                st.write("### Valid Circle Centers:")
                st.dataframe(df)
            
            # Display the plot image if visualization was enabled
            if visualize_circles and os.path.exists(output_image):
                st.write("### Coverage Plot:")
                image = Image.open(output_image)
                st.image(image, caption="Coverage Plot", use_container_width=True)
            elif visualize_circles:
                st.warning("Plot image not found.")
        
        except Exception as e:
            st.error(f"An error occurred during processing: {e}")
        finally:
            # Clean up temporary file
            if os.path.exists(temp_input_path):
                os.remove(temp_input_path)
            if os.path.exists(output_image):
                os.remove(output_image)
    else:
        st.warning("Please upload an input file to proceed.")
        
# Description: Run the app via terminal block
# Author: Mohammad Vohra
# Date: Jan 25, 2025
# URL: https://www.linkedin.com/pulse/transform-your-applications-how-convert-streamlit-app-mohammad-vohra-1qfsf/
# import streamlit.web.cli as stcli
# import os, sys

# def resolve_path(path):
#     return os.path.abspath(os.path.join(os.getcwd(), path))


# if __name__ == "__main__":
#     sys.argv = [
#         "streamlit",
#         "run",
#         resolve_path("app.py"),
#         "--global.developmentMode=false",
#     ]
#     sys.exit(stcli.main())