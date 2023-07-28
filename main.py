
'''
“Deal or No Deal” (TM) is a game show on NBC.
In the this version of the game, there are 10 possible dollar amounts: $100, $500, $1 000, $5
000, $10 000, $25 000, $50 000, $100 000, $500 000, $1 000 000 sealed in imaginary briefcases.
These dollar amounts are numbered 1 – 10 (i.e. 1 ! $100, 2 ! $500, 3 ! $1 000, ..., 10 ! $1
000 000). Before the game starts the contestant will have chosen one of the briefcases as his/hers
to possibly keep. During the game, some of the ten possible dollar amounts have been eliminated
from the game because the contestant has selected some of the other briefcases and revealed the
amounts inside.
At some point, the contestant will stop opening briefcases, and a “Banker” will offer the contestant
cash in exchange for what might be contained in his/her chosen briefcase. Then the contestant is
asked: “Deal or No Deal?”.
This is a program that helps a player decide if he/she should choose “deal” or “no deal”, by calculating the average of the remaining amounts (i.e., all unopened briefcases, including his/her “own”
briefcase), and comparing that value to the “Banker’s” offer. If the offer is higher than the average,
then the player should ”deal” otherwise, the player should say “no deal”.
Input Specifications
The user must input a number n (1 <= n < 10) which indicates how many cases have been opened
so far, followed by a list of n integers between 1 and 10 representing the values in the game that
have been eliminated, followed by the “Banker’s” offer, all seperated by a single space. For example: 3 2 5 10 300 indicates
that briefcases containing $500, $10 000, and $1 000 000 have been eliminated and the Banker’s
offer is $300. Please ensure that no duplicate case numbers are entered for the eliminated
values, and that the “Banker’s” offer is an integer greater than 10.

'''


def deal_or_no_deal(input_string):
    inputs = input_string.split()
    num_opened = int(inputs[0])
    eliminated = inputs[1:num_opened+1]
    banker_offer = int(inputs[num_opened+1])

    values = [None, 100, 500, 1000, 5000, 10000, 250000, 50000, 100000, 500000, 1000000]
    elim_values = []
    for i in eliminated:
        elim_values.append(values[int(i)])
    total_sum = 1691600  # Sum of all possible amounts (1 + 2 + ... + 10)
    remaining_sum = total_sum - sum(elim_values)  # Sum of the remaining amounts
    average = remaining_sum / (10 - num_opened)  # Average of the remaining amounts

    if banker_offer > average:
        return "deal"
    else:
        return "no deal"

# Read input from the user
input_str = input()

# Call the function and print the result
result = deal_or_no_deal(input_str)
print(result)
