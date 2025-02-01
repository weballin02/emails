import streamlit as st
import random
import pandas as pd
from faker import Faker

def generate_random_emails(num_emails=100):
    """
    Generate a specified number of unique random email addresses.
    
    :param num_emails: Number of unique email addresses to generate.
    :return: A list of dictionaries containing generated email data.
    """
    fake = Faker()
    email_providers = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"]
    
    email_set = set()
    emails_data = []

    while len(email_set) < num_emails:
        first = fake.first_name().lower().replace(' ', '.')
        last = fake.last_name().lower().replace(' ', '.')
        
        # 30% chance to add a random number at the end of the email
        suffix = str(random.randint(1, 9999)) if random.random() < 0.3 else ""
        domain = random.choice(email_providers)
        
        email = f"{first}.{last}{suffix}{domain}"
        if email not in email_set:
            email_set.add(email)
            emails_data.append({"First Name": first.capitalize(), 
                                "Last Name": last.capitalize(), 
                                "Email Address": email})

    return emails_data

# Streamlit App
st.title("📧 Random Email Generator")

# User input for number of emails
num_emails = st.number_input("Enter the number of emails to generate:", min_value=1, max_value=10000, value=100)

# Button to generate emails
if st.button("Generate Emails"):
    emails = generate_random_emails(num_emails)
    
    # Convert to DataFrame
    df = pd.DataFrame(emails)
    
    # Save as CSV
    csv_file = "generated_emails.csv"
    df.to_csv(csv_file, index=False)

    st.success(f"✅ Successfully generated {num_emails} emails! Saved as '{csv_file}'.")
    
    # Show the DataFrame in Streamlit
    st.dataframe(df)

    # Download button for the CSV file
    st.download_button(
        label="📥 Download CSV File",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=csv_file,
        mime="text/csv"
    )
