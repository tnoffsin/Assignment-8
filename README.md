# Assignment-8
#This is the objective of the code I had.
Write a function that looks at customer age ranges contained in the dataset and determines the top two most common reasons for seeking a loan for each and write these values to a new CSV file.

#This is what the dataset headers consisted of
customer_id: Unique identifier for each custome, customer_age: Age of the customer customer_income: Annual income of the customer home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE) employment_duration: Duration of employment in months loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE) loan_grade: Grade assigned to the loan loan_amnt: Loan amount requested loan_int_rate: Interest rate of the loan term_years: Loan term in years historical_default: Indicates if the customer has a history of default (Y/N) cred_hist_length: Length of the customer's credit history in years Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)

#What does the code do?
The code first imports the CSV file. 
It then takes two arguments, input file and output file.
It continues to go on and create an empty data list to store rows from the CSV file. Each row containing a new customer data.
Then reads the CSB file and converts each row (or customer) into a dictionary where the keys are the column names (or headers). 
It then continues to append each row dictionary to the empty data list.
Then creates age_ranges where each key maps to a list of reasons for seeking a loan.
it then gets the value associated with the loan_intent key and appends the loan reason to the corresponding age range list.
It then goes on to create an empty dictionary to store the top two reasons for each age range.
It counts the occurances of each reason to determine the top two most common reasons to take out a loan,
It then returns and stores the top two reasons in the dictionary.
It then opens a new CSV file and writes in the information starting with the header row.
Then goes into writing age range and adds each reason and its count to the row as well. The writes the row to the output CSV file. 
The last three code lines should be the input_file which is the data set it analyzed.
The output_file is what you named the new file with the two most common reasons to take out loan along with the age_range and how many times it occured. 
The last line is just to specify the file paths to process the loan data and write in the results.

#Are there any Tuples or Sets?
#Returns a list of tuples, where each tuples contains a reason and a count.
top_two_reasons = reason_counts.most_common(2)
        top_reasons[age_range] = top_two_reasons
        
#Writing results to CSV file, each row contains a list where reasons and counts are added as tuples
for age_range, reasons in top_reasons.items():
            row = [age_range]
            for reason, count in reasons:
                row.extend([reason, count])
            writer.writerow(row)

#There are no examples of Sets in my code
            


        
