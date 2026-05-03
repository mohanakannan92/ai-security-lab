# report.py

def generate_report(summary, metrics, weaknesses):
    print("\n📊 SECURITY REPORT\n")

    print(f"Total Tests: {summary['total']}")
    print(f"Blocked: {summary['blocked']}")
    print(f"Bypass: {summary['bypass']}")
    print(f"Leaks: {summary['leaks']}")

    print("\n🎯 Metrics:")
    print(f"Block Rate: {metrics['block_rate']}%")
    print(f"Bypass Rate: {metrics['bypass_rate']}%")
    print(f"Leak Rate: {metrics['leak_rate']}%")
    print(f"Security Score: {metrics['security_score']}%")

    print("\n⚠️ Weak Categories:")
    if not weaknesses:
        print("None 🎉")
    else:
        for w in weaknesses:
            print(f"- {w['attack_type']} ({w['failure_rate']}% failure)")