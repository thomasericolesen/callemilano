# CalleMilano: instructions for Claude

All project rules live in `AGENTS.md`, imported here so every Claude Code session loads them, on the Mac, on the web, in the cloud and on the phone. Do not write rules in this file; a rule applies only when it stands in `AGENTS.md`.

@AGENTS.md

## Where to start

- `docs/project-state.md`: what exists, what is open, what to do next.
- The newest `docs/status-*.md`: the latest handover. Older ones are in `docs/history/`.
- `docs/change-log.md`: decisions and changes, newest first.
- `docs/README.md`: map of the documentation.

Report in Danish (see "Language" in `AGENTS.md`).

## Sessions away from the owner's Mac

The repository holds everything needed for record work, fact checks, validation, the catalogue and the app export. A few things exist only on the Mac:

- The import token `~/.callemilano-import-token`. Never commit it. Without it, import into the app is done later from the Mac, or through `callemilano.dk/admin`.
- Claude in Chrome, signed in, for the Facebook/Instagram and Google Maps checks. Without it, leave those checks for a Mac session and say so.
- `trips/`, which holds guest data and is never committed. Deliver trip plans from a cloud session to the owner directly, not through git.

When one of these is missing, do the rest of the task and list what is left for a Mac session in the report and in the status file.
