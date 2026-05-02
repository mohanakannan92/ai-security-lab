# analyzer.py

def analyze_results(results):
    summary = {
        "total": len(results),
        "blocked": 0,
        "leaks": 0,
        "bypass": 0,
        "by_type": {}
    }

    for r in results:
        attack_type = r["attack_type"]
        status = r["status"]

        # Initialize category if not exists
        if attack_type not in summary["by_type"]:
            summary["by_type"][attack_type] = {
                "total": 0,
                "blocked": 0,
                "leaks": 0,
                "bypass": 0
            }

        summary["by_type"][attack_type]["total"] += 1

        # -------------------------------
        # Correct status handling
        # -------------------------------
        if status == "blocked":
            summary["blocked"] += 1
            summary["by_type"][attack_type]["blocked"] += 1

        elif status == "leak":
            summary["leaks"] += 1
            summary["by_type"][attack_type]["leaks"] += 1

        elif status == "bypass":
            summary["bypass"] += 1
            summary["by_type"][attack_type]["bypass"] += 1

        else:
            # Safety fallback (should not happen)
            summary["bypass"] += 1
            summary["by_type"][attack_type]["bypass"] += 1

    return summary


def calculate_metrics(summary):
    total = summary["total"]

    # Avoid division by zero
    if total == 0:
        return {
            "block_rate": 0,
            "leak_rate": 0,
            "bypass_rate": 0,
            "security_score": 0
        }

    block_rate = (summary["blocked"] / total) * 100
    leak_rate = (summary["leaks"] / total) * 100
    bypass_rate = (summary["bypass"] / total) * 100

    return {
        "block_rate": round(block_rate, 2),
        "leak_rate": round(leak_rate, 2),
        "bypass_rate": round(bypass_rate, 2),
        "security_score": round(block_rate, 2)  # simple scoring
    }


def detect_weakness(summary):
    weak_categories = []

    for attack_type, data in summary["by_type"].items():
        total = data["total"]
        failures = data["leaks"] + data["bypass"]

        if total == 0:
            continue

        failure_rate = (failures / total) * 100

        if failure_rate > 20:  # threshold
            weak_categories.append({
                "attack_type": attack_type,
                "failure_rate": round(failure_rate, 2)
            })

    return weak_categories