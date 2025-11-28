import requests
import json

URL = "https://www.kaggle.com/api/i/competitions.LeaderboardService/GetLeaderboard"
DIGITALOCEAN_API_URL = "https://squid-app-7q77b.ondigitalocean.app/api/api/public/leaderboard/v2"

HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.kaggle.com",
    "priority": "u=1, i",
    "sec-ch-ua": '"Not_A Brand";v="99", "Chromium";v="142"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-kaggle-build-version": "c2ee156b9524b01de987e886dce7d8ba63bd2bda",
    "x-xsrf-token": "CfDJ8Ksq__M8KNdOsrtGDpOZ52UMWj8GrGN2iv-kwzzKuHojxq9Yw4nMZNj34xAVqRBjmpIv6NmNww5poWudeHU17-qJCECeorRh6uMfOMqNKXXZXu_2e1cKFbwfA5qo87y0auv5w67DFZJNzPOyRUIDoUs",
}

COOKIES = {
    "ka_sessionid": "3ea8f4f675a51e37fe7ff620c7d93d7b",
    "_ga": "GA1.1.718538698.1764000276",
    "__Host-KAGGLEID": "CfDJ8Ksq__M8KNdOsrtGDpOZ52WTWuq9ZZw4xfSqsP3yIDSuR6gqw4zLPnUI10ORWFEzN-v8I4xrdPJpX_-LedpWgyNsvBMEdMP-oAm101ju8VcPVvpHnmdPZxfd",
    "CSRF-TOKEN": "CfDJ8Ksq__M8KNdOsrtGDpOZ52UGfnNs_R2SJpWuP_g4p9gUA-zWuZErpYzRAMI13BPAYIK8X0p6ke9xqUNSvCO4AWDk_hVWdRxzG81eqo47MA",
    "GCLB": "CL_HuY2Kub-LdxAD",
    "build-hash": "c2ee156b9524b01de987e886dce7d8ba63bd2bda",
    "XSRF-TOKEN": "CfDJ8Ksq__M8KNdOsrtGDpOZ52UMWj8GrGN2iv-kwzzKuHojxq9Yw4nMZNj34xAVqRBjmpIv6NmNww5poWudeHU17-qJCECeorRh6uMfOMqNKXXZXu_2e1cKFbwfA5qo87y0auv5w67DFZJNzPOyRUIDoUs",
    "CLIENT-TOKEN": "your_long_token_here",
    "ph_phc_6WRm2N9FRiCMAgNh0mS138RpLNhSv80s47Jl5IGdOqi_posthog": '{"distinct_id":"019ab69c-1d62-7b58-a3bc-d30e2f0f15a7"}',
    "ka_db": "CfDJ8Ksq__M8KNdOsrtGDpOZ52XTScdIZ3fhW6jUK3pz24vumw9RqHb9Al2JTx7fVCU-6oohcN-fDwFLZJtuDHmjasOSedbxGE52XsESNb_60SjhxLo83SfDlsdiYLI",
    "_ga_T7QHS60L4Q": "GS2.1.s1764078114$j5$l0$h0",
}

CHALLENGES = [
    {
        "key": "node_classification",
        "name": "Node Classification in a Citation Network",
        "competitionId": 119402,
        "referer": "https://www.kaggle.com/competitions/node-classification-in-a-citation-network/leaderboard",
    },
    {
        "key": "masked_xray",
        "name": "Masked_Xray_Challenge",
        "competitionId": 119863,
        "referer": "https://www.kaggle.com/competitions/masked-xray-challenge/leaderboard",
    },
    {
        "key": "aitsp",
        "name": "AI-Based Task Scheduling Problem (AITSP)",
        "competitionId": 118838,
        "referer": "https://www.kaggle.com/competitions/ai-based-task-scheduling-problem-aitsp/leaderboard",
    },
    {
        "key": "molecular_features",
        "name": "Molecular Features Classification",
        "competitionId": 119833,
        "referer": "https://www.kaggle.com/competitions/molecular-features-classification/leaderboard",
    },
    {
        "key": "aism",
        "name": "AI Sentence Meaning Similarity Challenge (AISM)",
        "competitionId": 120995,
        "referer": "https://www.kaggle.com/competitions/ai-paraphrase-understanding-challenge-aipuc/leaderboard",
    },
    {
        "key": "find_the_water",
        "name": "Find the Water",
        "competitionId": 120514,
        "referer": "https://www.kaggle.com/competitions/find-the-water/leaderboard",
    },
    {
        "key": "Histopathology",
        "name": "Histopathology 7-Class Tissue Classification Chall",
        "competitionId": 124609,
        "referer": "https://www.kaggle.com/competitions/Histopathology-classification-alpha-ai-2-k-25/leaderboard",
    },
]


# --------------------------
# NORMALIZE TEAM NAME
# --------------------------
def normalize_name(name: str) -> str:
    if not name:
        return "unknown"
    return name.lower().replace(" ", "_")


# --------------------------
# EXTRACT LEADERBOARD
# --------------------------
def extract_leaderboard(leaderboard, teams_map):
    if not leaderboard:
        return []

    return [
        {
            "teamId": entry.get("teamId"),
            "teamName": normalize_name(teams_map.get(entry.get("teamId"), "UNKNOWN")),
            "displayScore": entry.get("displayScore"),
        }
        for entry in leaderboard
    ]


# --------------------------
# FETCH KAGGLE CHALLENGES
# --------------------------
def fetch_kaggle_challenges():
    raw_results = {}
    clean_results = {}

    for chall in CHALLENGES:
        print(f"Fetching {chall['name']}...")

        HEADERS["referer"] = chall["referer"]

        payload = {
            "competitionId": chall["competitionId"],
            "leaderboardMode": "LEADERBOARD_MODE_DEFAULT"
        }

        response = requests.post(
            URL,
            headers=HEADERS,
            cookies=COOKIES,
            json=payload
        )

        try:
            data = response.json()
        except:
            data = {}

        raw_results[chall["key"]] = data

        # map teamId -> teamName
        teams_map = {t.get("teamId"): t.get("teamName") for t in data.get("teams", [])}

        # public leaderboard
        leaderboard = extract_leaderboard(data.get("publicLeaderboard"), teams_map)

        # store in clean_results dictionary
        clean_results[chall["key"] + "_leaderboard"] = leaderboard

    return raw_results, clean_results


# --------------------------
# FETCH DIGITALOCEAN CHALLENGES
# --------------------------
def fetch_digitalocean_challenges():
    print("Fetching FactCheck Challenge...")
    print("Fetching Legal Challenge...")
    
    try:
        response = requests.get(DIGITALOCEAN_API_URL)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching DigitalOcean challenges: {e}")
        return {"factcheck": {"public": [], "private": []}, "legal": {"public": [], "private": []}}


# --------------------------
# FETCH ALL CHALLENGES
# --------------------------
def fetch_all_challenges():
    # Fetch Kaggle challenges
    raw_results, clean_results = fetch_kaggle_challenges()
    
    # Fetch DigitalOcean challenges
    digitalocean_data = fetch_digitalocean_challenges()
    
    # Build the big object
    all_results = {}
    
    # Add Kaggle challenges
    for chall in CHALLENGES:
        key = chall["key"]
        all_results[key] = {
            "public": clean_results.get(f"{key}_leaderboard", []),
            "private": raw_results.get(key, {}).get("privateLeaderboard", []) or []
        }
    
    # Add DigitalOcean challenges (factcheck and legal)
    all_results["factcheck"] = digitalocean_data.get("factcheck", {"public": [], "private": []})
    all_results["legal"] = digitalocean_data.get("legal", {"public": [], "private": []})
    
    return raw_results, clean_results, all_results


# --------------------------
# RUN
# --------------------------
raw_results, clean_results, all_results = fetch_all_challenges()

print("\n===== ALL RESULTS (BIG OBJECT) =====")
print(json.dumps(all_results, indent=4))


# Invert aitsp scores
for mode in ['public', 'private']:
    for entry in all_results['aitsp'][mode]:
        original_score = float(entry['displayScore'])
        # entry['displayScore'] = str(1 / original_score if original_score != 0 else 0)
        baseline = 2400 
        entry['displayScore'] = max(0, (baseline - original_score) / baseline)


for mode in ['public', 'private']:
    for entry in all_results['factcheck'][mode]:
        original_score = float(entry['displayScore'])
        entry['displayScore'] = str(original_score / 10 )



for mode in ['public', 'private']:
    for entry in all_results['legal'][mode]:
        original_score = float(entry['displayScore'])
        entry['displayScore'] = str(original_score / 10 )



print("\nAfter inversion of  scores:")
print(json.dumps(all_results, indent=4))


# --------------------------
# VARIABLES
# --------------------------
challenges = list(all_results.keys())
print (len(challenges))
coefficients = [0.12,0.12,0.12,0.12,0.08,0.12,0.12,0.12,0.08]  
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
# ENSURE PRIVATE LEADERBOARD HAS TEAM NAMES
# --------------------------
for chall in challenges:
    for entry in all_results[chall]['private']:
        if 'teamName' not in entry or not entry['teamName']:
            entry['teamName'] = teams.get(entry['teamId'], f"team_{entry['teamId']}")


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
        results[team_name] = total 
    return results

# --------------------------
# RUN
# --------------------------
public_scores = combined_scores('public')
private_scores = combined_scores('private')

print("\n=== PUBLIC COMBINED SCORES ===")
for name, score in sorted(public_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score:.5f}")

print("\n=== PRIVATE COMBINED SCORES ===")
for name, score in sorted(private_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score:.5f}")






# --------------------------
# SEND SCORES TO SUPABASE (FIXED)
# --------------------------
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://saputdsxcuweyfinmvfy.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNhcHV0ZHN4Y3V3ZXlmaW5tdmZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE2NjY4MzAsImV4cCI6MjA3NzI0MjgzMH0.LWusCh2g2yK_y8xGtrcRgDK62Ai65ATKO-4pSyxpYx0")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

from time import time

# --------------------------
# INSERT LEADERBOARD SNAPSHOT
# --------------------------

# Generate a unique snapshot ID (using current timestamp)
leaderboard_id = int(time())

def send_leaderboard_to_supabase(scores_dict, table_name):
    """
    Insert leaderboard snapshot into Supabase.
    """
    rows = [
        {
            "leaderboard_id": leaderboard_id,
            "team_name": team_name,
            "score": float(score)
        }
        for team_name, score in scores_dict.items()
    ]
    
    # Batch insert all rows at once (much faster)
    response = supabase.table(table_name).insert(rows).execute()
    
    
    

    
    

# Send public and private scores
send_leaderboard_to_supabase(public_scores, "public_leaderboards")
#send_leaderboard_to_supabase(private_scores, "private_leaderboards")

print("✅ Leaderboard snapshot inserted and old snapshots cleaned.")
