from test import leaderboard_1, leaderboard_2, leaderboard_3, leaderboard_4, leaderboard_5, leaderboard_6, leaderboard_7

coefficients = [2, 5, 3, 4, 2, 1, 1]

def calculate_general_leaderboard(leaderboards, coefficients):
    """
    Calculate a general leaderboard by combining multiple leaderboards with corresponding coefficients.
    leaderboards: List of lists (each is a leaderboard dict list)
    coefficients: List of numeric coefficients (1 per leaderboard)
    Returns: List of dicts with 'teamId', 'teams', 'total_score', and optionally other info
    """
    from collections import defaultdict

    # We'll use lower rank as better, so invert weights accordingly
    team_scores = defaultdict(lambda: {"weighted_sum": 0, "score_breakdown": [], "teams": []})
    num_leaderboards = len(leaderboards)
    
    for i, (lb, coef) in enumerate(zip(leaderboards, coefficients)):
        for entry in lb:
            team_id = entry["teamId"]
            rank = entry["rank"]
            # The lower the rank, the higher the contribution (hence use 1/rank), scale by coef
            weighted_score = coef * (1 / rank)
            team_scores[team_id]["weighted_sum"] += weighted_score
            team_scores[team_id]["score_breakdown"].append(weighted_score)
            # Optionally store teams for reference
            team_scores[team_id]["teams"].append(entry)
    
    # Prepare results list
    results = []
    for team_id, info in team_scores.items():
        results.append({
            "teamId": team_id,
            "weighted_sum": info["weighted_sum"],
            "score_breakdown": info["score_breakdown"],
            "teams": info["teams"],
        })
    
    # Sort by weighted_sum descending (higher weighted_sum is better)
    results.sort(key=lambda x: x["weighted_sum"], reverse=True)

    # Assign general rank
    for idx, item in enumerate(results, 1):
        item["general_rank"] = idx
    
    return results

if __name__ == "__main__":
    # List of leaderboards to combine
    leaderboards = [
        leaderboard_1,
        leaderboard_2,
        leaderboard_3,
        leaderboard_4,
        leaderboard_5,
        leaderboard_6,
        leaderboard_7
    ]

    general_leaderboard = calculate_general_leaderboard(leaderboards, coefficients)
    # Print in a readable way
    # Return general leaderboard structure as a list of dicts, just like the single leaderboards
    # Each dict: {teamId, submissionId, rank, displayScore}
    # submissionId will be None (not available), displayScore will be weighted_sum as "float with 5 decimals"
    # rank is the general rank (1 is best)
    general_leaderboard_structured = []
    for entry in general_leaderboard:
        general_leaderboard_structured.append({
            "teamId": entry["teamId"],
            "submissionId": None,
            "rank": entry["general_rank"],
            "displayScore": f"{entry['weighted_sum']:.5f}",
        })
    print("general_leaderboard:", general_leaderboard_structured)
    for entry in general_leaderboard:
        print(f"#{entry['general_rank']} teamId: {entry['teamId']} weighted_sum: {entry['weighted_sum']:.6f} breakdown: {entry['score_breakdown']}")

