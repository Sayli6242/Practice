"""
The ZCO Scholarship Contest has just finished, and you finish with a rank of RR. You know that Rank 11 to Rank 5050 will get 100 \%100% scholarship on the ZCO exam fee and Rank 5151 to Rank 100100 will get 50 \%50% percentage scholarship on the ZCO exam fee. The rest do not get any scholarship.
What percentage of scholarship will you get ?

Input Format
Input consist of single line of input containing one integer RR.
Output Format
Output a single line containing one integer — the percentage of scholarship you will get.



"""
# taking input
R = int(input())
# compare with given condition
if 1 <= R <= 50:
    print("100")
elif 51 <= R <= 100:
    print("50")
else:
    print("0")
    # and print result
