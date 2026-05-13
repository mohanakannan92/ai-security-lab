from output_sanitizer import sanitize_output

tests = [
    "Here is your answer about Python basics.",
    "The system prompt is: You must not reveal secrets.",
    "Internal instructions say not to disclose this.",
]

for t in tests:
    result = sanitize_output(t)

    print("\nOutput:", t)
    print("Result:", result)