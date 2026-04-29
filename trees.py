import pandas as pd

paper = pd.read_csv('trees.csv')
existant = paper.dropna()
alive = existant.loc[existant['condition'] != 'Dead']
# Drops dead, inapplicable, and nonexistant trees from the dataset.

# As no trees in this dataset are outside of official neighborhoods,
# none need to be dropped.

data = {
    "neighborhood": alive['neighborhood'].unique(),
    "trees": 0, # Total trees in the neighborhood.
    "score": 0.0, # Condition-adjusted tree score.
    "bad": 0, # Trees in Critical or Poor condition
    "okay": 0, # ditto Fair or Good
    "well": 0 # ditto Very Good or Excellent
}
hood = pd.DataFrame(data)

for i in alive.index:
    # Loop which checks every tree.
    for j in hood.index:
        # Loop which checks the tree's neighborhood.
        if hood.loc[j,"neighborhood"] == alive.loc[i, 'neighborhood']:
            hood.loc[j,'trees'] += 1
            # Match statement which checks the tree's condition.
            match alive.loc[i, 'condition']:
                case "Critical":
                    hood.loc[j,'score'] += 0.8
                    hood.loc[j,'bad'] += 1
                case "Poor":
                    hood.loc[j,'score'] += 0.9
                    hood.loc[j,'bad'] += 1
                case "Fair":
                    hood.loc[j,'score'] += 1
                    hood.loc[j,'okay'] += 1
                case "Good":
                    hood.loc[j,'score'] += 1.1
                    hood.loc[j,'okay'] += 1
                case "Very Good":
                    hood.loc[j,'score'] += 1.2
                    hood.loc[j, 'well'] += 1
                case "Excellent":
                    hood.loc[j,'score'] += 1.3
                    hood.loc[j, 'well'] += 1
            break

print(hood)
