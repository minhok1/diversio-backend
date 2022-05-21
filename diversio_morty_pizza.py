"""The purpose of this exercise is to find how many Pizzas Morty can buy for a given combination of ingredients. 

A Pizza consists of the following ingredients: Crust, Seasoning, Sauce, Veggies, and Cheese

Morty's favourite combination and in this preference order(Crust is more important than Seasoning and so on):

Crust → Pan
Seasoning → Yes
Sauce → Tomato
Veggies → Broccoli
Cheese → No


It’s also possible that multiple Pizza combinations are available in the same quantity, in that case, we resolve it by picking the group
that’s "closest" to Morty's preference.

The definition of closest here being:
1. Count of Pizzas available with a given combination of ingredients. If a combination has a higher count even if it isn't Morty's preference, it will be picked.
2. The ingredients are matched in the preference order mentioned above(Crust → Seasoning → Sauce → Veggies → Cheese),
   and one that has the first mismatching item from Morty's preference is rejected.
3. If the items still match, pick the one that was seen first.


Let’s say we got:

A. (C: Pan,       Se: Yes, Sa: Tomato,  V: Broccoli, C: No)  → 3
B. (C: Thin-Crust Se: No,  Sa: Mayo,    V: Broccoli, C: No)  → 3
C. (C: Pan,       Se: Yes, Sa: Tomato,  V: Onion,    C: Yes) → 3

In the above example, A has the same count as B and C, but as A is also the same as Morty's preference, it’s picked over others.

Let’s take a more complicated example:

A. (C: Thin-Crust, Se: Yes, Sa: Mayo,   V: Broccoli, C: No)  → 3
B. (C: Pan,        Se: Yes, Sa: Tomato, V: Onion,    C: Yes) → 3
C. (C: Pan,        Se: Yes, Sa: Mayo,   V: Broccoli, C: No)  → 4
D. (C: Pan,        Se: Yes, Sa: Tomato, V: Broccoli, C: Yes) → 4 (winner)


Here A and B are already out of the race because of their lower counts(point 1 above),
the tiebreaker between C and D is broken by picking D as when Sauce(Se) is compared,
D has Tomato that matches Morty's preferred Sauce and C has Mayo, hence it’s rejected.

def find_pizza_combination(combinations: List[Tuple[Dict[str, str], int]]) →Dict[str, str]:
   ...
   
`groups` will be a List of tuples, where the first item in tuple will be the dictionary containing the group and the second item will be count.

[
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 4),
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 2),
]

For the above input the output should be:

{'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}

The solution will be evaluated for:

1. Correctness
2. Readability
3. Performance
"""

from typing import Dict, List, Tuple

ideal_pizza = {'crust': 'Pan', 'seasoning': 'Yes', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}

def find_pizza_combination(combinations: List[Tuple[Dict[str, str], int]]) -> Dict[str, str]:
    max_point = 0
    max_index = 0 #index for the current best option
    max_number = 0

    for i in range(len(combinations)):

        if combinations[i][1] > max_number:
            max_index = i
            max_number = combinations[i][1]

        elif combinations[i][1] == max_number:
            pizza = combinations[i][0]
            curr_point = 0

            for index, key in enumerate(pizza):
                if pizza[key] == ideal_pizza[key]:
                    curr_point += 10**(4-index)

            if curr_point > max_point:
                max_point = curr_point
                max_index = i
    
    return combinations[max_index][0]
    







  
groups_1 = [
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 4),
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 2),
]
groups_2 = [
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'Yes', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]
groups_3 = [
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Cucumber', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]
groups_4 = [
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Cucumber', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]

assert find_pizza_combination(groups_1) == groups_1[0][0]
assert find_pizza_combination(groups_2) == groups_2[1][0]
assert find_pizza_combination(groups_3) == groups_3[3][0]
assert find_pizza_combination(groups_4) == groups_4[2][0] and id(find_pizza_combination(groups_4)) == id(groups_4[2][0])
