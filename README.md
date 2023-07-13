<h1 style="text-align: center;"><span style="color: #FF0000;">STARTUP FUNDING ANALYSIS:</span> <strong><span style="color: #0000FF;">Exploring Venture Capital Investments in Various Industries</span></strong></h1>
![Alt text](./startupimage1.jpg)

## Project Overview
This data science project aims to predict the operating status of startups using machine learning techniques. The project involves analyzing a dataset containing information about startups, performing data preprocessing, conducting exploratory data analysis (EDA), feature engineering, model training, and deploying a predictive model using Streamlit.

## Dataset
The dataset used in this project consists of features related to startups, including funding details, investment amounts, funding rounds, and industry groups. The target variable is the operating status of the startups, which can be categorized as "closed," "operating," or "acquired." The dataset contains a combination of numerical and categorical features.

## Data Preprocessing:
During the data preprocessing phase, several preprocessing steps were performed to prepare the data for analysis and modeling. These steps included handling missing values, transforming categorical variables into numerical representations, and creating new categorical features based on descriptive summaries. The dataset was then split into feature matrix X and target variable y.

## Exploratory Data Analysis:
Exploratory data analysis was conducted to gain insights into the dataset and understand the relationships between different variables. Visualizations such as histograms, bar plots, and correlation matrices were used to explore the distribution of variables, identify patterns, and detect any potential correlations.

## Feature Engineering:
Feature engineering techniques were applied to enhance the predictive power of the model. New categorical features were created based on the values of certain numerical features, allowing for a more nuanced representation of the data. This step aimed to capture relevant information and improve the model's ability to predict the operating status of startups accurately.

## Model Training and Evaluation:
In this project, four different machine learning models were trained and evaluated for the prediction of startup operating status: Decision Tree, Random Forest, XGBoost, and AdaBoost. Each model was trained on the preprocessed dataset and underwent hyperparameter tuning to optimize its performance.

After evaluating the models based on metrics such as accuracy, F1-score, precision, and recall, the Decision Tree model was chosen as the best-performing model. It demonstrated superior performance on the test set, achieving high accuracy, F1-score, precision, and recall. The Decision Tree model was selected for its ability to capture complex relationships within the data and provide transparent decision-making processes.

The chosen Decision Tree model was further improved through hyperparameter tuning, utilizing techniques such as sequential feature selection(SFS). This process involved systematically exploring different combinations of hyperparameters to identify the optimal configuration that maximizes the model's performance.

## Deployment and Interactive Interface:
The trained model was deployed using the Streamlit framework to create an interactive web application. The application allows users to input their investor preferences, such as desired investment amount, investment timeframe, and risk appetite. Based on these preferences and the selected features, the model generates predictions for the operating status of startups. Additionally, investment recommendations and additional information about recommended startups are provided to assist users in making informed investment decisions.


## Project Structure
The project is structured into several main components:

1. **Data Preprocessing**: The dataset is preprocessed to handle missing values, transform categorical variables into numerical representations, and create new categorical features based on descriptive summaries.

2. **Exploratory Data Analysis (EDA)**: EDA is performed to gain insights into the dataset, identify patterns, and detect potential correlations between variables. Visualizations such as histograms, bar plots, and correlation matrices are used to explore the data.

3. **Feature Engineering**: Feature engineering techniques are applied to enhance the predictive power of the model. New categorical features are created based on the values of certain numerical features to capture relevant information and improve the model's performance.

4. **Model Training**: The Decision Tree classifier is selected as the model for predicting the operating status of startups. The model is trained on the preprocessed data using a combination of selected features and the corresponding target variable.

5. **Model Evaluation**: The trained model is evaluated using various metrics such as accuracy, precision, recall, and F1-score to assess its performance and determine its predictive capabilities.

6. **Model Deployment**: The trained model is deployed using the Streamlit framework to create an interactive web application. The application allows users to input their investor preferences, such as desired investment amount, investment timeframe, and risk appetite. Based on these preferences and the selected features, the model generates predictions for the operating status of startups. Investment recommendations and additional information about recommended startups are also provided.

## Dependencies
The project has the following dependencies:

* Python (version 3.7+)
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
*Mlxtend
* Streamlit
## Installation and Usage
1. Clone the repository to your local machine.

2. Install the necessary dependencies using pip or conda package manager.

"""
bash
Copy code
pip install -r requirements.txt
3. Run the Streamlit application to launch the web interface.
""'

"""
bash
Copy code
streamlit run app.py
"""
4. Follow the instructions on the web interface to input your investor preferences and generate predictions for startup operating status.

## How to Use
1. Open the web application in your browser after running the Streamlit application.

2. On the sidebar, you will find the "Investor Preferences" section. Fill in the desired investment amount, investment timeframe, and risk appetite.

3. Click the "Generate Recommendations" button to generate predictions and recommendations based on your preferences.

4. The application will display the predicted operating status of startups based on the selected features and preferences. It will also provide investment recommendations and additional information about the recommended startups.

5. Explore the visualization and insights section to gain further understanding of the data and the factors influencing startup operating status.

6 You can modify your investor preferences and click the "Generate Recommendations" button again to obtain updated predictions and recommendations.

## Project Documentation
For a detailed overview of the project, including the data preprocessing steps, EDA findings, feature engineering techniques, model training, and evaluation, please refer to the Project Documentation.

## Conclusion and Recommendations
1. Based on the analysis conducted in this project, several key findings and recommendations can be made to assist investors in making informed decisions:

2. Investment-related variables such as total investment and funding rounds (e.g., round A, round B) have a significant impact on the operating status of startups. Investors should consider the overall investment levels and strategically plan and secure funding during critical funding rounds.

3. Equity crowdfunding presents an attractive opportunity for startups to raise funds and attract potential investors. Investors should explore equity crowdfunding platforms to diversify their investment portfolio.

Seed funding plays a crucial role in kick-starting startup operations and increasing their chances of success. Investors should pay attention to startups that have successfully secured seed funding.

4. Industry-specific factors and dynamics significantly influence the operating status of startups. Investors should consider the industry group of startups and analyze its potential for growth and success.

5. Venture funding and angel funding can provide valuable resources and expertise to fuel startup growth and expansion. Investors should actively seek opportunities to invest in startups that have secured venture capital or angel funding.

These recommendations serve as a guide for investors to navigate the startup landscape and optimize their investment strategies.

## Future Enhancements
Future enhancements to this project could include:

- Incorporating real-time data feeds to keep the model up-to-date and improve its predictive capabilities.
Expanding the feature set by incorporating additional external data sources to provide a more comprehensive analysis.
- Refining the model using advanced techniques such as ensemble learning or neural networks to enhance prediction accuracy.
- Conducting further analysis on the impact of specific features on startup operating status.


## License
This project is licensed under the MIT License.

## Acknowledgments
The dataset used in this project is provided by Crunchbase. Special thanks to the open-source community for their valuable contributions to the libraries and tools used in this project.

## Contributors
This project was developed by  as part of [Data Science Bootcamp] at [Moringa School]. Contributions and suggestions are welcome. Feel free to submit a pull request or open an issue.

Special thanks to our Moringa School Data Science Technical Mentors for their guidance throughout the project. We would also like to acknowledge the contributions of the Elites team members:

1. Florence Nguuni

2. Joel Omondi.

3. [Isaac Muturi](https://github.com/Isaac-Ndirangu-Muturi-749)

4. Brian Chabari.

5. Diana Mwaura. 

6. Kennedy Juma. 
