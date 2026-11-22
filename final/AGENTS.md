# Agent operating instructions
Purpose: maintain a small local Python task tracker. Entry point and business logic: `main.py`; tests: `test_main.py`. No external dependencies.

## Allowed
- Read repository files and suggest a minimal patch.
- Run `python -m unittest discover -v` and `python -m compileall -q main.py test_main.py` in an isolated local workspace.
- Edit `main.py`, `test_main.py`, and documentation only after human review of the proposed scope.
- Keep public function names and acceptance criteria stable; add tests for behavior changes.

## Forbidden without explicit human approval
- Access, print, store, or upload credentials, secrets, private data, or environment variables.
- Run destructive commands or delete files outside the workspace.
- Install or upgrade dependencies; make network requests; deploy to production.
- Merge, push, commit on behalf of the user, or silently approve own changes.

## Review gate
Provide a change summary, unified diff, test command/output, remaining risks, and rollback instructions. Human must inspect and approve before merge or release.
