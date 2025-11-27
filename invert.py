from all_results_data import all_results
print (all_results)


# invert aitsp scores
for mode in ['public', 'private']:
    for entry in all_results['aitsp'][mode]:
        original_score = float(entry['displayScore'])
        # avoid division by zero just in case
        entry['displayScore'] = str(1 / original_score if original_score != 0 else 0)

# now all_results['aitsp'] scores are inverted

print("After inversion of aitsp scores:")
 
print (all_results)

# now lets export it 