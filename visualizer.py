import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def show_missing_values(df):

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) > 0:

        st.subheader("Missing Values")

        fig, ax = plt.subplots(figsize=(10, 4))

        missing.sort_values().plot(
            kind="barh",
            ax=ax
        )

        ax.set_title("Missing Values by Column")

        st.pyplot(fig)


def show_correlation(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] > 1:

        st.subheader("Correlation Heatmap")

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(12, 6))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)


def show_numeric_distributions(df):

    numeric_cols = df.select_dtypes(include="number").columns

    st.subheader("Numeric Feature Distributions")

    for col in numeric_cols[:5]:

        fig, ax = plt.subplots(figsize=(7, 4))

        sns.histplot(
            df[col].dropna(),
            kde=True,
            ax=ax
        )

        ax.set_title(f"Distribution of {col}")

        st.pyplot(fig)


def show_boxplots(df):

    numeric_cols = df.select_dtypes(include="number").columns

    st.subheader("Outlier Detection Boxplots")

    for col in numeric_cols[:5]:

        fig, ax = plt.subplots(figsize=(7, 4))

        sns.boxplot(
            x=df[col],
            ax=ax
        )

        ax.set_title(f"Boxplot of {col}")

        st.pyplot(fig)


def show_categorical_counts(df):

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    st.subheader("Categorical Features")

    for col in categorical_cols[:5]:

        fig, ax = plt.subplots(figsize=(8, 4))

        df[col].value_counts().head(10).plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(f"Top Categories in {col}")

        st.pyplot(fig)