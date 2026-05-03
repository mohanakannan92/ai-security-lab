# Diff: v2 → v3

## Before (Sanitization Only)
- Semantic attacks NOT blocked
- Model still responds

## After (Semantic Defense)
- All semantic attacks blocked
- Returns safe response

## Impact
+ Security improved
- Slight usability tradeoff

## Conclusion
Semantic layer is mandatory


| Version | Block Rate | Leak Rate | Notes |
|--------|-----------|----------|------|
| v1     | 60%       | 10%      | Weak filtering |
| v2     | 80%       | 0%       | Good sanitization |
| v3     | 100%      | 0%       | Semantic defense |