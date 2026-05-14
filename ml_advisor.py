def detect_ml_problem(df):

    target_column = None
    problem_type = "Unknown"

    # Heuristic approach

    for col in df.columns:

        unique_values = df[col].nunique()

        # Classification heuristic
        if unique_values <= 10:

            target_column = col
            problem_type = "Classification"

        # Regression heuristic
        elif unique_values > 10 and df[col].dtype != "object":

            target_column = col
            problem_type = "Regression"

    return {
        "target_column": target_column,
        "problem_type": problem_type
    }