tnoffsin: without using outside libraries or sources. Write a function that looks at customer age ranges contained in the dataset and determines the top two most common reasons for seeking a loan for each and write these values to a new CSV file.

GitHub Copilot: Sure, here's a step-by-step plan and the corresponding code to achieve this:

1. Read the CSV file and parse the data.
2. Group the data by age ranges.
3. Count the occurrences of each reason for seeking a loan within each age range.
4. Determine the top two most common reasons for each age range.
5. Write the results to a new CSV file.

Here's the Python code to accomplish this:

```python
import csv
from collections import defaultdict, Counter

def analyze_loan_reasons(input_file, output_file):
    # Step 1: Read the CSV file and parse the data
    data = []
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    # Step 2: Group the data by age ranges
    age_ranges = defaultdict(list)
    for row in data:
        age_range = row['Age Range']
        reason = row['Reason']
        age_ranges[age_range].append(reason)
    
    # Step 3: Count the occurrences of each reason for seeking a loan within each age range
    top_reasons = {}
    for age_range, reasons in age_ranges.items():
        reason_counts = Counter(reasons)
        # Step 4: Determine the top two most common reasons for each age range
        top_two_reasons = reason_counts.most_common(2)
        top_reasons[age_range] = top_two_reasons
    
    # Step 5: Write the results to a new CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Age Range', 'Top Reason 1', 'Count 1', 'Top Reason 2', 'Count 2'])
        for age_range, reasons in top_reasons.items():
            row = [age_range]
            for reason, count in reasons:
                row.extend([reason, count])
            writer.writerow(row)

# Example usage
input_file = 'data_use.csv'
output_file = 'top_loan_reasons.csv'
analyze_loan_reasons(input_file, output_file)
```

This code assumes that your CSV file has columns named "Age Range" and "Reason". Adjust the column names if they are different in your dataset.