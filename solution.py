import numpy as np

def optimal_stopping_value(num_red):
    num_black = num_red # equal number of red and black cards
    V = np.zeros((num_red+1, num_black+1)) # Value function table for states (r,b)

    # Base cases
    for r in range(num_red+1):
        V[r][0] = r # No black cards left, stop and take all red cards
    for b in range(num_black+1):
        V[0][b] = 0 # No red cards left, stop with zero payoff

    # Fill the table bottom-up with the Bellman equation
    for r in range(1, num_red+1):
        for b in range(1, num_black+1):
            x = r - b # net payoff if all cards were drawn
            expected_continue = (r/(r+b))*V[r-1][b] + (b/(r+b))*V[r][b-1]
            V[r][b] = max(x, expected_continue) # optimal choice

    return V[num_red][num_black]

    # For a standard deck with 26 red and 26 black cards:
optimal_payoff = optimal_stopping_value(26)
print(optimal_payoff)
