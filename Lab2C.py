# Zachary Stickler and Kevin Glosson
# Lab 2 Part C
# We used our knowledge of output formatting to change the output of a movie advertisement as requested.


# Task 5: Formatted output

movie_one = "Star Wars: The Force Awakens"
lead_one = "Daisy Ridley"
lead_two = "John Boyega"
movie_two = "Dirty Grandpa"
lead_three = "Robert DeNiro"
lead_four = "Zac Efron"
# Change the code after this point
print("Today we have a great double feature at WCUmovies:")
print("Today’s leading movie is: ", movie_one, "Starring:",
lead_one, "and", lead_two)
print("Followed by: " + movie_two + " Starring: " + lead_three
+ " and " + lead_four)

# Today we have a great double feature at WCUmovies:
# Today’s leading movie is: Star Wars: The Force Awakens Starring: Daisy Ridley and John Boyega
# Followed by: Dirty Grandpa Starring: Robert DeNiro and Zac Efron


print("Today we have a great double feature at WCUmovies:", "\n")

print("Today’s leading movie is: ", movie_one)
print("\tStarring:", lead_one[0] + ".", lead_one[6:len(lead_one)], "and", lead_two[0] + ".", lead_two[5:len(lead_two)], "\n")
print("Followed by: " + movie_two + "\n\tStarring: " + lead_four[0] + ".", lead_four[4:len(lead_four)] + " and " + "\n" + "\t" + "The Great " + lead_three + "!")

# Today we have a great double feature at WCUmovies:

# Today’s Leading movie is: Star Wars: The Force Awakens
#   Starring: D. Ridley and J. Boyega

# Followed by: Dirty Grandpa
#   Starring: Z. Efron and
#   The Great Robert DeNiro!

