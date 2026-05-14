# mw-sites

All MW Development static sites in one repo.

| Directory | Domain | Description |
|-----------|--------|-------------|
| `ryanmilly/` | ryanmilly.com | Personal portfolio — Quiet Conviction brand |
| `helixcode/` | helixcode.app | Helix brand site |
| `build/` | build.helixcode.app | Helix build/pipeline pages |
| `revenuefirst/` | revenuefirst.ai | RevenueFirst.AI landing page |
| `signal/` | signal.millyweb.com | Personal knowledge blog — video summaries |
| `adventures-of-shanghai/` | aos.millyweb.com | Adventures of Shanghai content brand |
| `canvas/` | canvas.millyweb.com | AI chat canvas (FastAPI + OpenRouter) |

## Deploy

All static sites serve via the `helixcode-sites` Nginx container on VPS2.
Canvas runs its own FastAPI container at canvas.millyweb.com.

## Design tokens (shared)

- Portfolio: `#FAF7F2` bg, `#B85C38` terracotta, Newsreader/Playfair/Caveat
- Helix: dark navy + crimson `#c41e3a`
- Signal: `#faf9f7` paper, `#c41e3a` accent, Cormorant Garamond serif
