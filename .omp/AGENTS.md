# Project Context

This repository uses the deterministic chapter controller described in the
root `AGENTS.md`. `python tools/run_next.py` is the preferred clean-worktree
entry point for the next chapter. Inside a requested chapter, begin and resume
by running `python tools/workflow.py status N`; execute only its reported next
action through `ACCEPTED`; the wrapper owns the accept commit. Mastering is
`python tools/run_next_mastering.py`.
