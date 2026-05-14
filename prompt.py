def generate_eda_prompt(df):

    return f"""
    Analyze this dataset.

    Shape:
    {df.shape}

    Columns:
    {list(df.columns)}

    Missing Values:
    {df.isnull().sum().to_string()}

    Sample Data:
    {df.head().to_string()}
    """


def generate_cleaning_prompt(df):

    return f"""
    Suggest cleaning steps for this dataset.

    Missing Values:
    {df.isnull().sum().to_string()}

    Data Types:
    {df.dtypes.to_string()}
    """


def generate_question_prompt(df, user_question):

    return f"""
    Dataset Columns:
    {list(df.columns)}

    User Question:
    {user_question}
    """


def generate_code_prompt(df):

    return f"""
    Write Python EDA code for dataframe df.

    Columns:
    {list(df.columns)}

    Data Types:
    {df.dtypes.to_string()}

    Missing Values:
    {df.isnull().sum().to_string()}

    Return ONLY executable Python code.
    """