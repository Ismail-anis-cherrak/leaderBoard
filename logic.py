# from all_results_data import all_results

# # Assuming challenges and coefficients are already defined
# challenges = list(all_results.keys())
# coefficients = [1] * len(challenges)  # default, can change later

# # Step 1: Collect all unique team IDs
# teams = {}
# for challenge in all_results.values():
#     for board_type in ["public", "private"]:
#         for entry in challenge.get(board_type, []):
#             team_id = entry.get("teamId")
#             team_name = entry.get("teamName", f"team_{team_id}")
#             if team_id not in teams:
#                 teams[team_id] = team_name

# # Step 2: Compute combined scores (using public leaderboard)
# combined_scores = {}

# for team_id, team_name in teams.items():
#     total = 0
#     for i, challenge_key in enumerate(challenges):
#         coef = coefficients[i]
#         # Find the team's score in this challenge (public)
#         score = next(
#             (float(entry["displayScore"]) for entry in all_results[challenge_key]["public"]
#              if entry["teamId"] == team_id),
#             0  # default 0 if team didn't participate
#         )
#         total += score * coef
#     # Normalize by sum of coefficients
#     combined_scores[team_name] = total / sum(coefficients)

# # Step 3: Print combined scores
# for team, score in combined_scores.items():
#     print(f"{team}: {score:.5f}")



from all_results_data import all_results

# --------------------------
# VARIABLES
# --------------------------
challenges = list(all_results.keys())
coefficients = [1] * len(challenges)  # default coefficients
sum_coefs = sum(coefficients)

# --------------------------
# GET ALL TEAM IDS AND NAMES
# --------------------------
teams = {}
for chall in challenges:
    for entry in all_results[chall]['public']:
        teams[entry['teamId']] = entry['teamName']
    for entry in all_results[chall]['private']:
        teams[entry['teamId']] = entry.get('teamName', teams.get(entry['teamId'], f"team_{entry['teamId']}"))

# --------------------------
# CALCULATE COMBINED SCORES
# --------------------------
def combined_scores(mode):
    results = {}
    for team_id, team_name in teams.items():
        total = 0.0
        for i, chall in enumerate(challenges):
            # find score in this challenge
            score = 0.0
            for entry in all_results[chall][mode]:
                if entry['teamId'] == team_id:
                    score = float(entry.get('displayScore', 0))
                    break
            total += score * coefficients[i]
        results[team_name] = total / sum_coefs
    return results

# --------------------------
# RUN
# --------------------------
public_scores = combined_scores('public')
private_scores = combined_scores('private')

print("=== PUBLIC COMBINED SCORES ===")
for name, score in public_scores.items():
    print(f"{name}: {score:.5f}")

print("\n=== PRIVATE COMBINED SCORES ===")
for name, score in private_scores.items():
    print(f"{name}: {score:.5f}")
