import itertools

def generate_pathways(interventions, n_steps):
    results = []
    for r in range(len(interventions)):  # for each length of interventions
        for perm in itertools.permutations(interventions[1:], r): # Exclude '0', generate permutations
            for indices in itertools.combinations(range(n_steps), len(perm)): # Indices to insert interventions
                result = [0] * n_steps # Initial pathway with all '0's
                for index, intervention in zip(indices, perm): # Insert interventions
                    result[index] = intervention
                results.append(result)
    return results
