import pandas as pd

# Data for the table
data = {
    "Company": ["Microsoft", "Microsoft", "Microsoft", "Tesla", "Tesla", "Tesla", "Apple", "Apple", "Apple"],
    "Fiscal Year": [2024, 2023, 2022, 2024, 2023, 2022, 2024, 2023, 2022],
    "Total Revenue": [58842, 48059, 43586, 62873, 66389, 51108, 390000, 365000, 350000],
    "Net Income": [88136, 72361, 72738, 7000, 8500, 6000, 92000, 87000, 83000],
    "Total Assets": [159734, 184257, 145345, 122070, 106618, 95345, 400000, 375000, 350000],
    "Total Liabilities": [243686, 205753, 185763, 48390, 43009, 40674, 160000, 150000, 140000],
    "Cash Flow from Operating Activities": [18315, 34704, 13931, 8000, 10000, 7500, 80000, 75000, 70000],
    "Revenue YoY Change": [22.97, 10.23, None, -5.44, 29.91, None, 6.85, 5.48, None],
    "Net Income YoY Change": [21.71, -0.52, None, None, 41.67, None, 5.75, 4.60, None],
    "Assets YoY Change": [-13.30, 26.82, None, 15.40, 12.56, None, 6.67, 6.67, None],
    "Liabilities YoY Change": [18.11, 10.86, None, 11.91, 5.34, None, 6.67, 6.67, None],
    "Cash Flow YoY Change": [-47.23, 149.86, None, 33.33, None, None, 6.67, 6.67, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define function to handle chatbot queries
def simple_chatbot(user_query):
    # Ask for company and year input for dynamic queries
    company = input("Enter the company (Microsoft, Tesla, Apple): ")
    year = int(input("Enter the fiscal year (2022, 2023, 2024): "))
    
    # Filter the DataFrame for the specified company and year
    company_data = df[(df["Company"] == company) & (df["Fiscal Year"] == year)]
    
    if company_data.empty:
        return "Data not found for the specified company or year."
    
    company_data = company_data.iloc[0]  # Extract the first row of the filtered data
    
    if user_query == "What is the total revenue?":
        return f"The total revenue for {company} in {year} is ${company_data['Total Revenue']} million."
    
    elif user_query == "How has net income changed over the last year?":
        if pd.isna(company_data['Net Income YoY Change']):
            return f"Net income change data is not available for {company} in {year}."
        return f"The net income of {company} changed by {company_data['Net Income YoY Change']}% in {year} compared to the previous year."
    
    elif user_query == "What is the total asset value?":
        return f"The total asset value for {company} in {year} is ${company_data['Total Assets']} million."
    
    elif user_query == "What is the cash flow from operating activities?":
        return f"The cash flow from operating activities for {company} in {year} is ${company_data['Cash Flow from Operating Activities']} million."
    
    elif user_query == "What is the YoY change in revenue?":
        if pd.isna(company_data['Revenue YoY Change']):
            return f"Revenue YoY change data is not available for {company} in {year}."
        return f"The YoY change in revenue for {company} in {year} is {company_data['Revenue YoY Change']}%."
    
    else:
        return "Sorry, I can only provide information on predefined queries."

# Test the chatbot function with a query
print("Welcome to the Financial Chatbot!")
while True:
    user_query = input("Ask me a question (or type 'exit' to quit): ").strip()
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
    else:
        response = simple_chatbot(user_query)
        print(response)
