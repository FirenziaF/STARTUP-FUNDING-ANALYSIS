import streamlit as st
import pickle
import joblib
import numpy as np
import os

# model = pickle.load(open("xgb_model.pkl", "rb"))

# # Create the Streamlit application
# def main():
#     # Set the title and description
#     st.title("Startup Investment Decision Support")
#     st.subheader("Input startup information and investor preferences")


#     # Startup Information Inputs
#     st.sidebar.header("Startup Information")
#     industry = st.sidebar.selectbox("Industry", ["Biotechnology", "Software", "Healthcare", "Advertising", "Games", "Enterprise Software", "Curated Web", "E-commerce", "Mobile", "Unspecified"])
#     funding_stage = st.sidebar.selectbox("Funding Stage", ["Seed", "Round A", "Round B", "Round C", "Round D"])
#     total_investment = st.sidebar.number_input("Total Investment", min_value=0.0)
#     equity_crowdfunding = st.sidebar.checkbox("Equity Crowdfunding")
    
    
#     # Investor Preferences Inputs
#     st.sidebar.header("Investor Preferences")
#     desired_investment = st.sidebar.number_input("Desired Investment Amount", min_value=0.0)
#     investment_timeframe = st.sidebar.selectbox("Investment Timeframe", ["Short-term", "Medium-term", "Long-term"])
#     risk_appetite = st.sidebar.slider("Risk Appetite", min_value=1, max_value=10, step=1)
#     desired_age = st.sidebar.slider("Desired Age", min_value=1, max_value=10, step=1)
    
    
#     # Perform predictions and recommendations
#     if st.button("Generate Recommendations"):
#         # Call your model or recommendation engine to generate predictions and recommendations
#         # Based on the provided startup information and investor preferences
        
#         int_features = [float(x) for x in request.form.values()]
#         features = [np.array(int_features)]
        
#         operating_status = model.predict(features)  # Replace with model prediction
#         recommendations = ["Operational", "Acquired", "Closed"]  # Replace with recommendation engine results


#         # Display the results
#         st.subheader("Predicted Operating Status:")
#         st.write(operating_status)

#         st.subheader("Investment Recommendations:")
#         for recommendation in recommendations:
#             st.write("- " + recommendation)


#     # Display additional information or insights if needed
    
    
#         # Probable Locations
#         st.subheader("Investment Location")
#         probable_locations = ["New York City", "San francisco", 'London', "Austin", "Seattle", "Palo Alto", "Cambridge"]   # Add more locations based on predicted market
#         st.markdown("*Probable Location:* {}".format(", ".join([location for location in probable_locations])))


# if __name__ == "__main__":
#     main()

# ######################################################################

# Set the background image using CSS   

# page_bg_img = """
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-image: url("https://img.freepik.com/premium-photo/ambitious-business-man-climbing-stairs-success_31965-3080.jpg?w=826");
#         background-size: cover;
#         background-position: top left;
#         background-repeat: no-repeat;
#     }
    
#     [data-testid="stHeader"] {
#         background-color: rgba(0,0,0,0);
#     }
    
#     [data-testid="Toolbar"] {
#         right: 2rem;
#     }
#     </style>
#     """     
    
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Create the Streamlit application
# def main():
#     # Call the set_background function
#     # set_background()

#     # Set the title and description
#     st.title("Startup Investment Decision Support")
#     st.subheader("Input startup information and investor preferences")

#     # Startup Information Inputs
#     st.sidebar.header("Startup Information")
#     industry = st.sidebar.selectbox("Industry", ["Biotechnology", "Software", "Healthcare", "Advertising", "Games", "Enterprise Software", "Curated Web", "E-commerce", "Mobile", "Other"])
#     funding_stage = st.sidebar.selectbox("Funding Stage", ["Seed", "Round A", "Round B", "Round C", "Round D"])
#     total_investment = st.sidebar.number_input("Total Investment", min_value=0.0)
#     equity_crowdfunding = st.sidebar.checkbox("Equity Crowdfunding")

#     # Investor Preferences Inputs
#     st.sidebar.header("Investor Preferences")
#     desired_investment = st.sidebar.number_input("Desired Investment Amount", min_value=0.0)
#     investment_timeframe = st.sidebar.selectbox("Investment Timeframe", ["Short-term", "Medium-term", "Long-term"])
#     risk_appetite = st.sidebar.slider("Risk Appetite", min_value=1, max_value=10, step=1)
#     desired_age = st.sidebar.slider("Desired Age", min_value=0, max_value=10, step=1)

#     # Perform predictions and recommendations
#     if st.button("Generate Recommendations"):
#         # Call your model or recommendation engine to generate predictions and recommendations
#         # Based on the provided startup information and investor preferences

#         features = [total_investment, equity_crowdfunding, desired_investment, investment_timeframe, risk_appetite, desired_age]
#         operating_status = "operational/ non-operational" # model.predict([features])  # Replace with model prediction
#         recommendations = ["Operational", "Acquired", "Closed"]  # Replace with recommendation engine results

#         # Display the results
#         st.subheader("Predicted Operating Status:")
#         st.write(operating_status)

#         st.subheader("Investment Recommendations:")
#         for recommendation in recommendations:
#             st.write("- " + recommendation)

#     # Display additional information or insights if needed
#     # Probable Locations
#     st.subheader("Investment Location")
#     probable_locations = ["New York City", "San Francisco", "London", "Austin", "Seattle", "Palo Alto", "Cambridge"]   # Add more locations based on predicted market
#     st.markdown("*Probable Location:* {}".format(", ".join([location for location in probable_locations])))
#     st.markdown(
#         f"""
#         <p>
#         Phone: +254 712-254-856 / +254 712-254-857
#         <br>
#         Email Address: data.<EMAIL>@gmail.com/info@examplecompany.com
#         <br>
#         <a href="data.badger@hotmail.com">
#         You can get in touch with us at the links provided
#         </p>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()

#  #####################################################

# Set the background image using CSS   
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

# Create the Streamlit application

def page_home():
    st.title("Data Badgers Homepage")
    st.markdown("""
                <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px;">
                <h3><em>Welcome to the Startup Investment Decision Support app!</em></h3>
                <p><h6>Welcome, dear reader, to the Startup Investment Decision Support app! Get ready to embark on a transformative journey as we unveil our groundbreaking platform that connects investors and startup founders, revolutionizing the investment landscape. Discover a world of tailored recommendations and personalized insights that will supercharge your investment strategy. With our innovative tools and empowering recommendations, you'll be poised to seize the most promising opportunities and unlock your path to investment success. Embrace the future of investing and join us on this thrilling adventure!<h6></p>
                </div>
                """,
        unsafe_allow_html=True
        )

def page_about():
    st.title("More about us")
    st.markdown(
        """
        <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px;">            
            <p>With our compelling "Call to Action" feature, investors can seamlessly transition to an external system where they can access comprehensive data and delve deeper into intriguing startups. Our platform also showcases insightful graphs and visualizations that highlight the performance of startups across different categories, enabling investors to gain a deeper understanding of industry trends and make data-driven investment decisions.</p>
            <p>To get started, simply click the "Get Started" button and let our user-friendly sidebar guide you through the process. Input your investment preferences and desired funding amounts to refine your recommendations and discover the perfect investment opportunities. Join our platform today and unlock a world of investment possibilities, driving innovation and fostering growth in the startup ecosystem.</p>
        
        </div>
        """,
        unsafe_allow_html=True
    )


    
def page_startup_info():
    st.title("Startup Investment Decision Support")
    st.subheader("We are here for you")
    st.write("Input startup information here...")

def main():
    # Set the title and description
    st.sidebar.title("***Navigation***")
    pages = ["Home", "Startup Information", "About"]
    selected_page = st.sidebar.selectbox("Go to", pages)
    
    if selected_page == "Home":
        page_home()
           
    elif selected_page == "About":
        page_about()

    elif selected_page == "Startup Information":
        page_startup_info()
        
        
        # Startup Information Inputs
        st.sidebar.header("Startup Information")
        industry = st.sidebar.selectbox("Industry", ["Biotechnology", "Software", "Healthcare", "Advertising", "Games", "Enterprise Software", "Curated Web", "E-commerce", "Mobile", "Other"])
        funding_stage = st.sidebar.selectbox("Funding Stage", ["Seed", "Round A", "Round B", "Round C", "Round D"])
        total_investment = st.sidebar.number_input("Total Investment", min_value=0.0)
        equity_crowdfunding = st.sidebar.checkbox("Equity Crowdfunding")

        # Investor Preferences Inputs
        st.sidebar.header("Investor Preferences")
        desired_investment = st.sidebar.number_input("Desired Investment Amount", min_value=0.0)
        investment_timeframe = st.sidebar.selectbox("Investment Timeframe", ["Short-term", "Medium-term", "Long-term"])
        risk_appetite = st.sidebar.slider("Risk Appetite", min_value=1, max_value=10, step=1)
        desired_age = st.sidebar.slider("Desired Age", min_value=0, max_value=10, step=1)
        #operating_status = ""  # placeholder variable until we get actual data from our database/model
        
        # Perform predictions and recommendations
        if st.button("Generate Recommendations"):
            # Call your model or recommendation engine to generate predictions and recommendations
            # Based on the provided startup information and investor preferences

            features = [total_investment, equity_crowdfunding, desired_investment, investment_timeframe, risk_appetite, desired_age]
            operating_status = "operational/ non-operational" # model.predict([features])  # Replace with model prediction
            recommendations = ["Operational", "Acquired", "Closed"]  # Replace with recommendation engine results

            # Display the results
            st.subheader("Predicted Operating Status:")
            st.write(f"**{operating_status}**")

            st.subheader("Investment Recommendations:")
            for recommendation in recommendations:
                st.write("- " + f"**{recommendation}**")
                
            st.markdown("""
                    <br><div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px;">
            <p>
                <div style="max-height: 200px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;">
                    <h3 style="font-weight: bold; color: #333;">List of Countries</h3>
                    <ul style="list-style-type: none; padding: 0;">
                        <ol>
                        <li>United States</li>
                        <li>China</li>
                        <li>Great Britain</li>
                        <li>India</li>
                        <li>Canada</li>
                        <li>Germany</li>
                        <li>Israel</li>
                        <li>France</li>
                        <li>Netherlands</li>
                        <li>Spain</li>
                        </ol>
                    </ul>
                </div>
                <div style="text-align: center; font-size: 24px;">
                    <img src="https://img.freepik.com/premium-vector/political-map-world_23-2147511327.jpg?8&w=740" alt="A map of the top ten countries" width="600">
                </div>
            </p>
        </div>
                    """, unsafe_allow_html=True
                    )

        # Display additional information or insights if needed
        # Probable Locations
        st.subheader("Investment Location")
        probable_locations = ["New York City", "San Francisco", "London", "Austin", "Seattle", "Palo Alto", "Cambridge"]   # Add more locations based on predicted market
        st.markdown("**Probable Location:** " + ", ".join([f"**{location}**" for location in probable_locations]))

        # Placeholder div with image and increased font size
        st.subheader("Levels")
        st.markdown('<div style="text-align: center; font-size: 24px;"><img src="https://img.freepik.com/premium-photo/businessman-holding-tablet-showing-growing-virtual-hologram-statistics-graph-chart-with-arrow-up_34200-307.jpg?w=900" alt="A photo" width="600"></div>', unsafe_allow_html=True)
        
           
if __name__ == "__main__":
    main()



