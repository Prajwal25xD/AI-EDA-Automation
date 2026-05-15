# AI-Powered EDA Automation System

An AI-driven Exploratory Data Analysis (EDA) platform built using **Streamlit** and **Google Gemini API** that automates dataset analysis, generates AI insights, suggests data cleaning steps, creates visualizations, and provides machine learning recommendations.

---

# 🚀 Live Demo

🌐 **Deployed on Streamlit:**  
(Add your Streamlit deployment link here)

Example:

https://ai-eda-automation-llpuaps6gs888stsvsqe9a.streamlit.app/

---

# 📌 Features

✅ Upload CSV datasets interactively  
✅ Automated Exploratory Data Analysis (EDA)  
✅ AI-generated dataset insights using Gemini  
✅ AI-powered data cleaning suggestions  
✅ Automated visualizations and charts  
✅ Ask questions about the dataset using AI  
✅ AI-generated Python EDA code  
✅ Safe execution of generated code  
✅ Machine Learning recommendations  
✅ Interactive Streamlit dashboard  

---

# 🛠 Tech Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit |
| AI/LLM | Google Gemini API |
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Environment Management | Conda |
| Deployment | Streamlit Cloud |

---

# 📂 Project Structure

```text
AI_EDA_AUTOMATION/
│
├── app.py
├── prompts.py
├── eda_agent.py
├── visualizer.py
├── data_handler.py
├── code_executor.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-EDA-Automation.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd AI-EDA-Automation
```

---

## 3️⃣ Create Conda Environment

```bash
conda create -n ai_eda_env python=3.11
```

Activate environment:

```bash
conda activate ai_eda_env
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Gemini API Key

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your Gemini API key from:

https://aistudio.google.com/app/apikey

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 Application Functionalities

## 📌 Dataset Overview
- Dataset shape
- Columns
- Data types
- Missing values
- Statistical summary

---

## 📈 Automated Visualizations
- Correlation heatmap
- Missing value analysis
- Numeric distributions
- Boxplots
- Categorical analysis

---

## 🧠 AI Dataset Insights
Uses Gemini API to:
- Analyze datasets
- Generate insights
- Identify patterns
- Suggest preprocessing steps

---

## 🧹 AI Cleaning Suggestions
Provides recommendations for:
- Missing value handling
- Encoding
- Scaling
- Outlier treatment
- Duplicate removal

---

## ❓ Ask Questions About Dataset
Users can ask natural language questions such as:
- "Which column has highest missing values?"
- "What are the important features?"
- "Is this dataset suitable for classification?"

---

## ⚡ AI Generated Python Code
The system can:
- Generate Python EDA code
- Display generated code
- Execute code safely

---

## 🤖 AI ML Recommendations
Suggests:
- Suitable ML problem type
- Recommended algorithms
- Feature engineering ideas
- Evaluation metrics

# 🔒 Security Notes

- API keys are stored using `.env`
- `.env` is excluded via `.gitignore`
---

# 📦 Requirements

Main dependencies:

```text
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
python-dotenv
google-genai
```

---

# 🌟 Future Improvements

- PDF report generation
- AutoML integration
- Multi-agent architecture
- Advanced dashboard analytics
- Database support
- Docker deployment
- Authentication system

---

# 👨‍💻 Author

**Prajwal Poojary**
---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub.
