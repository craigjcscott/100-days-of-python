import numpy as np

def roll_dice():
	print("How many dice?")
	num_dice = int(input())
	
	print("How many sides per dice")
	num_sides = int(input())
	
	return list(np.random.randint(low=1, high=num_sides, size=num_dice))

# Build the function
def yahtzee_max(dice_vals):
	val, freq = np.unique(dice_vals, return_counts=True)
	
	opt_val = val[np.argmax(val*freq)]
	print("Here is the optimum value:", opt_val)
	print("Here is the score:", opt_val * freq[np.argmax(val*freq)])

# Run the function
test_list = roll_dice()
print("Dice values:", test_list)
yahtzee_max(test_list)


