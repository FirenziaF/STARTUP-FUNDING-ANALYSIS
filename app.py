import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Load the pickled model
model_path = 'xgb.pkl'  # Replace with the path to your pickled model

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file '{model_path}' not found.")
    st.stop()

# Load the DataFrame and calculate column value counts
df = pd.read_csv('datattt.csv')  # Replace with the path to your data file

column_value_counts = {}

for column in df.columns:
    column_value_counts[column] = df[column].value_counts()

# Define the input fields
feature_names = ['Founded_year', 'time_to_first_funding', 'city', 'round_D', 'round_C', 'funding_rounds', 'Industry_Group', 'round_F', 'region', 'round_B']

# Create mapping dictionaries for categorical features
city_mapping = {"New York City": 0, "San Francisco": 1, "London": 2, "Austin": 3, "Seattle": 4, "Palo Alto": 5, "Cambridge": 6, "Chicago": 7, "Mountain View": 8}
region_mapping = {"United States": 0, "China": 1, "Great Britain": 2, "India": 3, "Canada": 4, "Germany": 5, "Israel": 6, "France": 7, "Netherlands": 8, "Spain": 9}

# funding_rounds_mapping = {"Round A": 0, "Round B": 1, "Round C": 2, "Round D": 3, "Round E": 4, "Round F": 5, "Round G": 6, "Round H": 7}
industry_group_mapping = {"Software": 0, "Biotechnology": 1, "Healthcare": 2, "Mobile": 3, "Advertising": 4, "E-Commerce": 5, "Curated Web": 6, "Enterprise Software": 7, "Games": 8, "Other": 9}

# Create a dictionary for available cities based on regions
region_cities_mapping = {
    "United States": ["New York City", "San Francisco", "Austin", "Seattle", "Chicago", "Mountain View"],
    "China": ["Beijing", "Shanghai", "Hangzhou", "Shenzhen"],
    "Great Britain": ["London", "Cambridge"],
    "India": ["Bangalore", "Mumbai", "New Delhi"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "Israel": ["Tel Aviv", "Jerusalem", "Haifa"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Netherlands": ["Amsterdam", "Rotterdam", "Utrecht"],
    "Spain": ["Barcelona", "Madrid", "Valencia"]
}

def predict_total_investment(features):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame([features], columns=feature_names)

    # Map categorical features to encoded values
    input_data["city"] = input_data["city"].map(city_mapping)
    input_data["region"] = input_data["region"].map(region_mapping)
    input_data["Industry_Group"] = input_data["Industry_Group"].map(industry_group_mapping)

    # Make predictions using the pre-trained model
    prediction = model.predict(input_data)[0]

    return prediction

def load_model():
    with open('xgb.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def page_home():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/premium-photo/ambitious-business-man-climbing-stairs-success_31965-3080.jpg?w=826");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    
    [data-testid="Toolbar"] {
        right: 2rem;
    }
    </style>
    """     
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown("<h1 style='color: rgba(0, 0, 0, 1)'>InvestMatch</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: rgba(0, 0, 0, 1)'>Data Badgers Homepage</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px;">
            <h3><em style="color: rgba(0, 0, 0, 1)">Welcome to the Startup Investment Decision Support app!</em></h3>
            <p><h6 style="color: rgba(0, 0, 0, 1)">Welcome, dear reader, to the Startup Investment Decision Support app! Get ready to embark on a transformative journey as we unveil our groundbreaking platform that connects investors and startup founders, revolutionizing the investment landscape. Discover a world of tailored recommendations and personalized insights that will supercharge your investment strategy. With our innovative tools and empowering recommendations, you'll be poised to seize the most promising opportunities and unlock your path to investment success. Embrace the future of investing and join us on this thrilling adventure!</h6></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def page_about():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/premium-photo/ambitious-business-man-climbing-stairs-success_31965-3080.jpg?w=826");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    
    [data-testid="Toolbar"] {
        right: 2rem;
    }
    </style>
    """     
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown("<h1 style='color: rgba(0, 0, 0, 1)'>InvestMatch</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: rgba(0, 0, 0, 1)'>More about us</h2>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px;">
            <p style="color: rgba(0, 0, 0, 1)">Introducing InvestMatch, the platform that connects investors and startup founders for seamless investment opportunities. With personalized recommendations, in-depth data analysis, and a user-friendly interface, InvestMatch revolutionizes the investment landscape.</p>
            <p style="color: rgba(0, 0, 0, 1)">Investors can discover curated startups that align with their preferences and criteria, enabling them to make informed decisions and seize promising opportunities. Startup founders can showcase their ideas and connect with interested investors, gaining exposure to funding opportunities.</p>
            <p style="color: rgba(0, 0, 0, 1)">InvestMatch's intuitive interface and "Get Started" button streamline navigation, while a call to action seamlessly connects investors to an external system for further data exploration and due diligence. Join InvestMatch today to unlock a world of investment possibilities, driving innovation and fostering growth in the startup ecosystem.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Button for GitHub link
    st.markdown(
        """
        <div style="margin-top: 20px;">
            <a href="https://github.com/FirenziaF/THE-BAGDGERS-CAPSTONE-PROJECT" target="_blank">
                <button style="padding: 10px 20px; background-color: rgba(0, 123, 255, 1); color: white; border: none; border-radius: 5px;">
                    Visit our GitHub
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


def page_startup_info():
    
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/premium-photo/male-hand-holding-question-mark-icon-neon-redbluepurple-backgroundbanner-with-copy-space-place-text_150455-21042.jpg?w=996");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }
    
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    
    [data-testid="Toolbar"] {
        right: 2rem;
    }
    </style>
    """     
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown("<h1 style='color: rgba(3, 3, 3, 6`)'>InvestMatch</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: rgba(256, 256, 256, 1)'><em>StartUp Investment Decision Support</em></h2>", unsafe_allow_html=True)
    st.write("View your predictions here.")

def main():
    # Create a topbar
    with st.container():
        pages = ["Home", "Startup Information", "About"]
        selected_page = st.selectbox("Go to", pages)
    
    if selected_page == "Home":
        page_home()
           
    elif selected_page == "About":
        page_about()

    elif selected_page == "Startup Information":
        page_startup_info()
        
        # Load the model
        model = load_model()

        # Startup Information Inputs
        st.sidebar.header("Startup Information")
        
        # Dropdown for Founded Year
        founded_year = st.sidebar.selectbox("Founded Year", list(range(1980, 2024)))
        
        # Input for funding year
        time_to_first_funding = st.sidebar.number_input("Time to First Funding", min_value=0)
                      
        # Dropdown for Funding Rounds
        funding_rounds = st.sidebar.slider("Funding Rounds", min_value=1, max_value=18, value=1)

        round_B = st.sidebar.checkbox("Round B")
        round_C = st.sidebar.checkbox("Round C")
        round_D = st.sidebar.checkbox("Round D")
        round_F = st.sidebar.checkbox("Round F")
        
        # Dropdown for Region
        region = st.sidebar.selectbox("Region", list(region_cities_mapping.keys()))

        # Dropdown for City based on selected Region
        cities = region_cities_mapping.get(region, [])
        city = st.sidebar.selectbox("City", cities)

        # Dropdown for Industry Group
        industry_group = st.sidebar.selectbox("Industry Group", ["Software", "Biotechnology", "Healthcare", "Mobile", "Advertising", "E-Commerce", "Curated Web", "Enterprise Software", "Games", "Other"])
        

        # Perform predictions and recommendations
        if st.button("Generate Recommendations"):
            # Update the features with user inputs
            features = [founded_year, time_to_first_funding, city, round_D, round_C, funding_rounds, industry_group, round_F, region, round_B]

            # Perform prediction
            prediction = predict_total_investment(features)

            # Display the prediction
            st.subheader("Investment Prediction:")
            st.write(f"**{prediction}**")

            # Reverting back to no data
            st.button("Revert")
            
        
if __name__ == "__main__":
    main()



