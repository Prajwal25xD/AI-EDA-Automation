import streamlit as st

from code_executor import safe_execute_code
from data_handler import load_data
from eda_agent import ask_gemini
from ml_advisor import detect_ml_problem

from prompt import (
    generate_eda_prompt,
    generate_cleaning_prompt,
    generate_question_prompt,
    generate_code_prompt
)

from visualizer import (
    show_missing_values,
    show_correlation,
    show_numeric_distributions,
    show_boxplots,
    show_categorical_counts
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI EDA Agent",
    layout="wide"
)

st.title("🤖 AI EDA Agent using Gemini")

st.write(
    "Upload a dataset and let AI perform automated exploratory data analysis."
)

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ==========================================
# MAIN APP
# ==========================================

if uploaded_file:

    # Load Dataset
    df = load_data(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # ==========================================
    # DATASET OVERVIEW
    # ==========================================

    st.header("📌 Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Dataset Shape")

        st.write(df.shape)

        st.subheader("Columns")

        st.write(df.columns.tolist())

    with col2:

        st.subheader("Data Types")

        st.write(df.dtypes)

        st.subheader("Missing Values")

        st.write(df.isnull().sum())

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Statistical Summary")

    st.write(df.describe(include="all"))

    # ==========================================
    # VISUALIZATIONS
    # ==========================================

    st.header("📊 Automated Visualizations")

    show_missing_values(df)

    show_correlation(df)

    show_numeric_distributions(df)

    show_boxplots(df)

    show_categorical_counts(df)

    # ==========================================
    # AI DATASET INSIGHTS
    # ==========================================

    st.header("🧠 AI Dataset Insights")

    if st.button("Generate AI Insights"):

        with st.spinner("Gemini analyzing dataset..."):

            eda_prompt = generate_eda_prompt(df)

            eda_result = ask_gemini(eda_prompt)

        st.subheader("AI Insights")

        st.write(eda_result)

    # ==========================================
    # AI CLEANING SUGGESTIONS
    # ==========================================

    st.header("🧹 AI Cleaning Suggestions")

    if st.button("Suggest Data Cleaning"):

        with st.spinner("Analyzing data quality..."):

            cleaning_prompt = generate_cleaning_prompt(df)

            cleaning_result = ask_gemini(cleaning_prompt)

        st.subheader("Cleaning Suggestions")

        st.write(cleaning_result)

    # ==========================================
    # ASK QUESTIONS ABOUT DATASET
    # ==========================================

    st.header("❓ Ask Questions About Dataset")

    user_question = st.text_input(
        "Ask anything about the dataset"
    )

    if st.button("Ask AI"):

        if user_question:

            with st.spinner("Thinking..."):

                question_prompt = generate_question_prompt(
                    df,
                    user_question
                )

                answer = ask_gemini(question_prompt)

            st.subheader("AI Answer")

            st.write(answer)

    # ==========================================
    # AI GENERATED PYTHON EDA CODE
    # ==========================================

    st.header("⚡ AI Generated Python EDA Code")

    if st.button("Generate EDA Code"):

        with st.spinner("Generating Python EDA code..."):

            code_prompt = generate_code_prompt(df)

            generated_code = ask_gemini(code_prompt)

            # Remove markdown formatting
            generated_code = generated_code.replace(
                "```python",
                ""
            )

            generated_code = generated_code.replace(
                "```",
                ""
            )

            # Store code in session
            st.session_state.generated_code = generated_code

        st.subheader("Generated Python Code")

        st.code(
            generated_code,
            language="python"
        )

    # ==========================================
    # EXECUTE AI GENERATED CODE
    # ==========================================

    if "generated_code" in st.session_state:

        if st.button("Run Generated Code"):

            with st.spinner("Executing AI-generated code..."):

                safe_execute_code(
                    st.session_state.generated_code,
                    df
                )
    # =========================
    # ML PROBLEM DETECTION
    # =========================

    st.header("🤖 ML Problem Detection")

    ml_info = detect_ml_problem(df)

    st.write(f"Detected Problem Type: {ml_info['problem_type']}")

    st.write(f"Possible Target Column: {ml_info['target_column']}")

    # ==========================================
    # AI ML RECOMMENDATIONS
    # ==========================================

    st.header("🤖 AI ML Recommendations")

    if st.button("Generate ML Suggestions"):

        with st.spinner("Analyzing ML possibilities..."):

            ml_prompt = f"""
            Analyze this dataset and suggest:

            1. Suitable ML problem type
            2. Best ML algorithms
            3. Recommended preprocessing
            4. Feature engineering ideas
            5. Evaluation metrics

            Dataset Shape:
            {df.shape}

            Columns:
            {list(df.columns)}

            Data Types:
            {df.dtypes.to_string()}
            """

            ml_result = ask_gemini(ml_prompt)

        # Save result in session state
        st.session_state.ml_result = ml_result


    # Show result safely
    if "ml_result" in st.session_state:

        st.subheader("AI ML Recommendations")

        st.write(st.session_state.ml_result)
    # ==========================================
    # FOOTER
    # ==========================================

    st.markdown("---")

    st.caption(
        "🚀 Built using Streamlit + Gemini API + Python"
    )