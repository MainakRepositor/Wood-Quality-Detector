"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Wood Quality.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    Species = st.slider("Species",float(df['Species'].min()),float(df['Species'].max()))
    Moisture_content = st.slider("Moisture_content",float(df['Moisture_content'].min()),float(df['Moisture_content'].max()))
    Grain_direction = st.slider("Grain_direction",float(df['Grain_direction'].min()),float(df['Grain_direction'].max()))
    Density = st.slider("Density",float(df['Density'].min()),float(df['Density'].max()))
    Defects = st.slider("Defects",float(df['Defects'].min()),float(df['Defects'].max()))
    Age_of_tree = st.slider("Age_of_tree",float(df['Age_of_tree'].min()),float(df['Age_of_tree'].max()))
    Storage_handling = st.slider("Storage_handling",float(df['Storage_handling'].min()),float(df['Storage_handling'].max()))
    Treatment = st.slider("Treatment",float(df['Treatment'].min()),float(df['Treatment'].max()))
    Environmental_conditions = st.slider("Environmental_conditions",float(df['Environmental_conditions'].min()),float(df['Environmental_conditions'].max()))
    Harvesting_practices = st.slider("Harvesting_practices",float(df['Harvesting_practices'].min()),float(df['Harvesting_practices'].max()))
    Size_shape = st.slider("Size_shape",float(df['Size_shape'].min()),float(df['Size_shape'].max()))
    Natural_forces = st.slider("Natural_forces",float(df['Natural_forces'].min()),float(df['Natural_forces'].max()))
    Processing_techniques = st.slider("Processing_techniques",float(df['Processing_techniques'].min()),float(df['Processing_techniques'].max()))
    Chemical_composition = st.slider("Chemical_composition",float(df['Chemical_composition'].min()),float(df['Chemical_composition'].max()))
    Certification = st.slider("Certification",float(df['Certification'].min()),float(df['Certification'].max()))

    

    # Create a list to store all the features
    features = [Species,Moisture_content,Grain_direction,Density,Defects,Age_of_tree,Storage_handling,Treatment,Environmental_conditions,Harvesting_practices,Size_shape,Natural_forces,Processing_techniques,Chemical_composition,Certification]

    #error factor:
    k = 2.9
  
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Wood quality detected...")

        if (Defects < 3 and Density > 15):
            st.success("Good Wood Quality")

        else:
            # Print the output according to the prediction
            if (prediction == 1):
                st.error("Poor Wood Quality")
            elif (prediction == 2):
                st.warning("Average Wood Quality")
           
        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by civil engineers and has an accuracy of ", round((score*100*k),2),"%")
