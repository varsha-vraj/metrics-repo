def calculate_churn_rate(df):
    """
    Calculate churn rate as churned / total_customers.
    Expects a DataFrame with a 'status' column whose churned customers are labeled 'churned'.
    Returns 0.0 if there are no customers to avoid ZeroDivisionError.
    """
    total_customers = len(df)
    if total_customers == 0:
        return 0.0
    churned = len(df[df['status'] == 'churned'])
    return churned / total_customers
