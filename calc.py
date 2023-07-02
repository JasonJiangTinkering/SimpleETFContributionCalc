import os
return_on_investment_estimate = float(os.environ.get('return_on_investment_estimate', 0)) # None
desired_capital = float(os.environ.get('desired_capital', 0)) # None
years_to_reach_goal = int(os.environ.get('years_to_reach_goal', 0)) # KeyError: key does not exist.
starting_capital = float(os.environ.get('starting_capital', 0)) # 0

print(f'return_on_investment_estimate, {return_on_investment_estimate}' )
print(f'desired_capital, {desired_capital}' )
print(f'years_to_reach_goal, {years_to_reach_goal}' )
print(f'starting_capital, {starting_capital}' )
print('STARTING ALGORITHM')
print("-------------------")
# return the # of money needed per year to reach desired capital given return_on_investment_estimate, desired_capital, and years_to_reach_goal
def money_won(yearly_contribution, answer_check=0):
    print("testing yearly contribution: " + str(yearly_contribution))
    cur_assets = starting_capital
    for i in range(years_to_reach_goal):
        if (answer_check == 1):
            print("year " + str(i) + " assets: " + str(cur_assets))          
        cur_assets = (cur_assets + yearly_contribution) * (1 + return_on_investment_estimate)
    print("cur_assets diff from goal: " + str(abs(desired_capital - cur_assets)))
    return cur_assets

def binarySearchCorrectYearlyContribution():
    if years_to_reach_goal==0:
        raise Exception("years_to_reach_goal cannot be 0")
    yearly_contribution_guess = desired_capital
    minguess = 0
    maxguess = desired_capital
    found_answer = 0
    while not abs(found_answer - desired_capital) < 0.01:
        found_answer = money_won(yearly_contribution_guess)
        if found_answer > desired_capital:
            maxguess = yearly_contribution_guess
            yearly_contribution_guess = (minguess + maxguess) / 2
        elif found_answer < desired_capital:
            minguess = yearly_contribution_guess
            yearly_contribution_guess = (minguess + maxguess) / 2
    if not abs(found_answer - desired_capital) < 0.01:
        raise ValueError("binary search failed")
    money_won(yearly_contribution_guess, answer_check=1)
    return yearly_contribution_guess
            
print("target average yearly contribution goal: " + str(binarySearchCorrectYearlyContribution()))