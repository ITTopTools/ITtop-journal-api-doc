# Code Review

## Before Submitting

Run through this checklist yourself before asking for review:

- [ ] Does the code do what the spec says?
- [ ] Are all tests passing?
- [ ] Is the linter clean?
- [ ] Are there any new warnings?
- [ ] Are there hardcoded values that should be constants?
- [ ] Is error handling present where failures are possible?
- [ ] Are comments explaining *why*, not *what*?
- [ ] Is anything left that you wouldn't want a teammate to see?

## When Receiving Review

- Treat every comment as a question, not a personal attack
- For each comment: fix it, or explain why you disagree
- Don't silently ignore comments
- If you disagree, discuss — don't just revert and resubmit

## Common Issues to Watch For

| Issue | Red flag |
|-------|----------|
| Function does too much | >30 lines, multiple `and` in its description |
| Naming is unclear | You need a comment to explain a variable name |
| Magic numbers | Literals in logic that aren't 0 or 1 |
| Error ignored | `catch` block that's empty or just logs |
| Test missing | New function with no corresponding test |
