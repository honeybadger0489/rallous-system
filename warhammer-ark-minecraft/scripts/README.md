# Pack scripts

```bash
# Refresh Modrinth version pins (needs network)
python3 scripts/generate-pack.py

# Verify pipeline with a handful of official files
./scripts/download-pack.sh --starter

# Download the full default set into downloads/ (gitignored binaries)
./scripts/download-pack.sh
```

Downloads use Modrinth CDN URLs and SHA-1 hashes from `pack/modrinth.index.json`. No CurseForge API key is required for the default set. Magistu’s Epic Knights is CurseForge-only — add it in the CurseForge/Prism UI.
