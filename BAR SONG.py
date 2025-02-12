print("Welcome!")
print()
print("This is the Online Text Scanning Tool (OTST)")
print("Used for verifying the authenticity of work provided by a student.")
print()
Source = input("What source is the information from?: ")
TextCheck = input("Enter the original line of text from the source:")
TextSample = input("Enter a response by student 1:")

if TextSample == TextCheck:
    print("This student has plagiarized! The text they provided perfectly matches what " + str(Source) + " says.")
elif TextSample != TextCheck:
    print("No evidence of direct plagiarism found. This student is all clear for this question!")
