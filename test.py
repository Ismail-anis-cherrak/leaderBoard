from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "file.txt"


def _parse_leaderboards(path: Path, max_rank: int = 15) -> List[List[Dict[str, Any]]]:
    """
    Stream-parse file.txt and return a list with one list of team dicts per curl.

    Each team dict has only basic leaderboard fields (no member details):
    teamId, submissionId, rank, displayScore.
    """
    leaderboards: List[List[Dict[str, Any]]] = []

    current_json_lines: List[str] = []
    in_section = False

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            # New section header: "✅ titanic (3136)"
            if line.startswith("✅ "):
                # Flush previous section if any
                if in_section and current_json_lines:
                    _append_section(current_json_lines, leaderboards, max_rank)
                    current_json_lines = []

                in_section = True
                # We don't store the header; next lines are the JSON payload
                continue

            if in_section:
                current_json_lines.append(line)

        # Flush the last section
        if in_section and current_json_lines:
            _append_section(current_json_lines, leaderboards, max_rank)

    return leaderboards


def _append_section(
    json_lines: List[str],
    leaderboards: List[List[Dict[str, Any]]],
    max_rank: int,
) -> None:
    """Helper to convert a section's JSON to top-ranked team dicts."""
    try:
        data = json.loads("".join(json_lines))
    except json.JSONDecodeError:
        # Skip malformed sections gracefully
        return

    entries = data.get("publicLeaderboard", [])
    top_teams: List[Dict[str, Any]] = []

    for entry in entries:
        if not isinstance(entry, dict):
            continue

        rank = entry.get("rank")
        if not isinstance(rank, int):
            continue
        if not (1 <= rank <= max_rank):
            continue

        team = {
            "teamId": entry.get("teamId"),
            "submissionId": entry.get("submissionId"),
            "rank": rank,
            "displayScore": entry.get("displayScore"),
        }
        top_teams.append(team)

    if top_teams:
        leaderboards.append(top_teams)


# Parse once at import time so other scripts can import these arrays directly
_all_leaderboards = _parse_leaderboards(FILE_PATH, max_rank=15)

# Export up to seven arrays (one per curl); if fewer exist, remaining are empty.
leaderboard_1 = _all_leaderboards[0] if len(_all_leaderboards) > 0 else []
leaderboard_2 = _all_leaderboards[1] if len(_all_leaderboards) > 1 else []
leaderboard_3 = _all_leaderboards[2] if len(_all_leaderboards) > 2 else []
leaderboard_4 = _all_leaderboards[3] if len(_all_leaderboards) > 3 else []
leaderboard_5 = _all_leaderboards[4] if len(_all_leaderboards) > 4 else []
leaderboard_6 = _all_leaderboards[5] if len(_all_leaderboards) > 5 else []
leaderboard_7 = _all_leaderboards[6] if len(_all_leaderboards) > 6 else []

# Convenience export: all arrays in a single list
leaderboards = _all_leaderboards

