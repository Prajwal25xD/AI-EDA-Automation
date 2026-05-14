import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def safe_execute_code(code, df):

    blocked_keywords = [
        "os.",
        "sys.",
        "subprocess",
        "shutil",
        "open(",
        "__import__",
        "eval(",
        "exec(",
        "rm ",
        "del ",
    ]

    # Safety check
    for keyword in blocked_keywords:

        if keyword in code:

            st.error(f"Blocked unsafe keyword detected: {keyword}")
            return

    local_vars = {
        "df": df,
        "pd": pd,
        "np": np,
        "plt": plt,
        "sns": sns,
        "st": st
    }

    try:

        exec(code, {}, local_vars)

        st.success("AI-generated code executed successfully.")

    except Exception as e:

        st.error(f"Execution Error: {str(e)}")