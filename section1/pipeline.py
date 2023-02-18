import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from hashlib import sha256
import os

# Define input and output paths
## every hour, this script will scan the raw_input_folder for new files. 
## processed input files are placed into the processed_input_folder to avoid double processing
input_folder = "section1/data/input"
processed_input_folder = "section1/data/input_processed"
successful_output_folder = "section1/data/output_successful"
unsuccessful_output_folder = "section1/data/output_unsuccessful"

# Define email provider domains
## actually, email addresses ending with other domains like .biz or .info are also valid
## however question specifies domains ending with .com and .net, hence using this regex instead
email_regex = '^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.(?:com|net)$'



# Define function for data cleaning and validity checks
def clean_and_validate(df):
    # use a temporary flag is_valid to track whether the row is valid
    df["is_valid"] = True
    # Remove any rows without name field
    df.loc[df["name"].isna(),"is_valid"] = False

    # remove spaces in mobile number field
    df["mobile_no"] = df["mobile_no"].str.replace(' ', '', regex=False)
    # Check mobile number is 8 digits
    df.loc[~((df["mobile_no"].astype(str).str.len() == 8)&(df["mobile_no"].str.isdigit())), "is_valid"] = False

    # Convert date_of_birth to datetime 
    ## From inspection, seems like there are 3 different formats: %m/%d/%Y %d-%m-%Y %Y-%m-%d
    ## alternative is to use pd.to_datetime without specifying format, but it may parse wrongly if month/date is flipped, like in the dataset
    ## df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], errors='coerce')
    date1 = pd.to_datetime(df["date_of_birth"], errors='coerce', format='%m/%d/%Y')
    date2 = pd.to_datetime(df["date_of_birth"], errors='coerce', format='%d-%m-%Y')
    date3 = pd.to_datetime(df["date_of_birth"], errors='coerce', format='%Y-%m-%d')
    df["date_of_birth"] = date1.fillna(date2).fillna(date3)

    # Check applicant is above 18. use relativedelta for exact number of years
    df["above_18"] = df["date_of_birth"].apply(lambda x: relativedelta(date(2022, 1, 1), x.date()).years >= 18)

    df.loc[~df["above_18"], "is_valid"] = False

    # Check email has valid domain
    df.loc[df["email"].str.match(email_regex), "is_valid"] = False
    return df

# Define function for data transformation
def transform_data(df):
    # Split name into first_name and last_name
    ## Data assumptions: First name is always before last name
    ## Titles should be removed: Mr., Mrs., Ms., Dr.
    ## Titles should be removed: Jr., PhD, MD, DVM, DDS, Jr., III, II
    ## names might have middle names - the first token is first name, last token is last name
    df["name"] = df["name"].str.replace('^(Mr\.|Mrs\.|Ms\.|Dr\.) ','', regex=True)
    df["name"] = df["name"].str.replace(' (Jr\.|PhD|MD|DVM|DDS|Jr\.|III|II)$','', regex=True)
    df["first_name"] = df["name"].apply(lambda x: x.split(" ")[0])
    df["last_name"] = df["name"].apply(lambda x: x.split(" ")[-1])

    # Format date_of_birth field into YYYYMMDD
    df["date_of_birth"] = df["date_of_birth"].dt.strftime("%Y%m%d")
    return df

# Define function for membership ID creation
def create_membership_id(last_name, date_of_birth):
    # Concatenate last name and date_of_birth
    input_string = last_name + date_of_birth
    # Generate SHA256 hash
    hashed_input = sha256(input_string.encode()).hexdigest()
    # Truncate to first 5 characters
    truncated_hash = hashed_input[:5]
    # Concatenate last name and truncated hash
    membership_id = last_name + "_" + truncated_hash
    return membership_id

# Loop through input files
for filename in os.listdir(input_folder):
    # Read in file as pandas dataframe
    df = pd.read_csv(os.path.join(input_folder, filename))
    # Clean and validate data
    df = clean_and_validate(df)
    # Split, format and create new fields
    df = transform_data(df)
    # Create membership IDs for successful applications
    df.loc[df["is_valid"], "membership_id"] = df.loc[df["is_valid"]].apply(lambda row: create_membership_id(row["last_name"], row["date_of_birth"]), axis=1)
    # Split data into successful and unsuccessful applications
    successful_df = df[df["membership_id"].notnull()].drop(columns=['is_valid'])
    unsuccessful_df = df[df["membership_id"].isnull()].drop(columns=['is_valid'])
    # Output successful applications
    successful_df.to_csv(os.path.join(successful_output_folder, 'successful_' + filename), index=False)
    # Output unsuccessful applications
    unsuccessful_df.to_csv(os.path.join(unsuccessful_output_folder, 'unsuccessful_' + filename), index=False)
    
    # move processed input file into processed folder
    os.rename(os.path.join(input_folder, filename), os.path.join(processed_input_folder, filename))