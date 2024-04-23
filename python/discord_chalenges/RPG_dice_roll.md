Dice Roll
In role-playing games, the standard notation for dice rolls is nds, where n is the number of die to roll and s is how many sides each die has. For example 2d6 means roll two six-sided dice, 1d12 means roll one 12-sided die. 

Write a function to simulate a role-playing game dice roll. The function should accept a parameter which must conform to the standard notation. Return None if the format is invalid. The function should generate a random roll for each die and return a list containing the results.

Example:

```py
roll('2d6')     # [5, 2]
roll('3d10')    # [1, 9, 7]
```


ADVANCED
Modify the function so that, in addition to the list of rolls, it also returns the sum of the rolled dice and the highest roll in a dictionary.

For example, if the call was roll('2d6') and it rolled a 6 and a 3, then roll should return this:

```py
{
  'dice': [6, 3],
  'total': 9,
  'highest': 6
}
```