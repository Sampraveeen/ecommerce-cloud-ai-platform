# Security Group: Basic Firewall Rules (AWS EC2)

**Inbound rules (allow):**
- SSH — TCP 22 — Source: *My IP* (tighten later)
- HTTP — TCP 80 — Source: 0.0.0.0/0, ::/0
- HTTPS — TCP 443 — Source: 0.0.0.0/0, ::/0

**Outbound rules:** allow all (default) or restrict to required ports.

**Why this matters:** Matches Scenario‑1 requirements to configure basic firewall rules for the cloud instance.
