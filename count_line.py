import argparse
def count_lines(input_file, output_file):
    
    with open(input_file, "r", encoding="utf-8") as text_file: #reading my input file
         lines = sum(1 for line in text_file) # reading each line separately 

      # counting lines 
    print(f"The number of lines in {input_file} is: {lines}")

    with open(output_file, "w", encoding="utf-8") as output_file: # writing to the file
        output_file.write(f"The number of lines in {input_file} is: {lines}\n")
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Count the number of lines in the text file.") # creating an ArgumentParser object with some description.
    parser.add_argument("input_file", type=str, help="Path to the input text file")
    parser.add_argument("output_file", type=str, help="Path to the output text file")
    args = parser.parse_args()

    count_lines(args.input_file, args.output_file)