def remove_duplicates(input_file, output_file):
    # Read the URLs from the input file
    with open(input_file, 'r') as file:
        urls = file.readlines()
    
    # Remove any trailing whitespace characters from each URL
    urls = [url.strip() for url in urls]
    
    # Use a set to remove duplicates
    unique_urls = set(urls)
    
    # Write the unique URLs to the output file
    with open(output_file, 'w') as file:
        for url in unique_urls:
            file.write(url + '\n')

# Define input and output file names using raw strings
input_file = r'C:\Users\ASUS\Desktop\New folder\porn.txt'  # Raw string for the input file path
output_file = r'C:\Users\ASUS\Desktop\New folder\output.txt'  # Raw string for the output file path

# Call the function to remove duplicates
remove_duplicates(input_file, output_file)
