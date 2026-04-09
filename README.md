📊 Tirumala Pilgrim Footfall Prediction

📌 Overview  
This project focuses on predicting the daily number of pilgrims visiting the Tirumala Tirupati Temple using Machine Learning. The model helps in understanding crowd patterns and supports better planning and management.

🎯 Objective  
- Predict daily pilgrim count using historical data  
- Analyze the impact of festivals 🎉, weekends 📅, and special events  
- Build a regression model for forecasting  

📁 Dataset  
The dataset contains daily records of pilgrim visits along with influencing factors.

Key Features:  
- date – Date of record  
- darshans – Number of pilgrims (target variable)  
- weekend – Weekend indicator 📅  
- is_festival – Festival indicator 🎉  
- is_brahmostavam – Special event indicator 🔥  
- rolling_avg_7 – 7-day rolling average  
- google_trend_score – Trend popularity score 📈  

🧹 Data Preprocessing  
- Converted date column to datetime format  
- Sorted data chronologically  
- Removed duplicate records  
- Checked for missing values  

🤖 Model  
- Algorithm: Linear Regression  
- Selected relevant features  
- Split data into training and testing sets  
- Trained model on historical data  

📈 Model Performance  
- R² Score: 0.47  
- MAE: ~5000  

📊 Visualizations  
- Actual vs Predicted plot 📉  
- Festival impact analysis 🎉  
- Brahmotsavam distribution 🔥  
- Scatter plots 🔵  
- Comparison chart 📊  
- Pairplot / Heatmap 🧠  

🔍 Key Insights  
- Festivals increase pilgrim count 🎉  
- Weekends show higher footfall 📅  
- Brahmotsavam causes variation 🔥  
- Rolling average is an important predictor 📈  

🛠 Tools Used  
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  

🚀 Applications  
- Crowd management  
- Resource planning  
- Event management  

🔮 Future Scope  
- Use advanced models like Random Forest  
- Add more features such as weather  
- Develop real-time prediction system  

▶️ How to Run  
Install required libraries and run the script:

pip install pandas matplotlib seaborn scikit-learn  
python main.py  

📄 License  
This project is for academic purposes.
