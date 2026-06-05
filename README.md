# SML Base-4 Sovereign Harmonic Matrix
### Institutional Signal Engine by ScriptMasterLabs

[![smithery badge](https://smithery.ai/badge/timothy-walton45/sml-base4-signals)](https://smithery.ai/servers/timothy-walton45/sml-base4-signals)

**9-set EMA compression · Self-calibrating CI · Dual-gate signals · AI counsel debate · XRPL micropayment**

> The pre-breakout accumulation signature retail indicators can't see.

---

## What This Does

The SML Base-4 engine detects when a market is mathematically coiling across **every institutional time horizon simultaneously** — the structural signature that precedes high-conviction directional moves.

**9 harmonic EMA sets** measuring compression from intraday scalp all the way through institutional position-building cycles. When all 9 sets compress at once, price is consolidating across every dimension simultaneously.

### Live Validated Results — June 4, 2026

| Ticker | State | Sets Coiled | CI Score | Engine Verdict |
|--------|-------|-------------|----------|----------------|
| **SPY** | **APEX SINGULARITY** | **8/9** | **94.8** | Structural coil — top 5th pct compression |
| **IWM** | **CRITICAL MASS** | **5/9** | **85.9** | Compressed regime confirmed |
| **QQQ** | **CRITICAL MASS** | **5/9** | **91.1** | Tightening vector |
| AMC | SCANNING | 1/9 | 75.8 | ← **Correctly blocked — chop zone** |
| GME | SCANNING | 0/9 | 63.7 | ← **Correctly blocked — zero convergence** |

**Same CI=78 threshold. Five instruments. Zero parameter tuning.** The self-calibrating percentile system correctly separated institutional setups from chop-zone instruments without any adjustment.

---

## Dual-Gate Signal Qualification

```
CI >= 78  (Structural Gate)   →  Top 22nd percentile compression
                                  Eliminates the 50-65 chop zone
                                  where market makers run stop hunts

SQI >= 75 (Execution Gate)    →  4-pillar composite confirmed:
                                  Compression (40pt) + MTF (30pt)
                                  + Volume (15pt) + Regime (15pt)

PRIME Signal = Both gates pass simultaneously
```

**Why 78?** Below CI=78, market makers retain enough EMA dispersion to hunt stops in both directions. Above 78, the multi-week anchor lines are mathematically committed — breaking price requires breaking institutional positions across every time horizon first.

---

## MCP Tools

### Free Tools (no payment required)
| Tool | Description |
|------|-------------|
| `get_signal_preview` | Truncated signal — state, CI, SQI, action, key levels |
| `run_showcase` | Live scan: SPY/IWM/QQQ/AMC/GME/NVDA sorted by quality |
| `get_methodology` | Complete mathematical reference + live validation data |
| `check_health` | Service status |
| `get_institution_catalog` | Full ScriptMasterLabs product catalog |

### Premium Tools (RLUSD via x402)
| Tool | Cost | Description |
|------|------|-------------|
| `get_intelligence_brief` | 0.10 RLUSD | Full institutional narrative with risk factors and agent instruction |
| `get_full_signal` | 0.05 RLUSD | All 9 set metrics + MTF breakdown + SQI pillars |
| `scan_tickers` | 0.05 RLUSD | Multi-ticker scan with CI/prime filters (up to 10 symbols) |
| `get_council_verdict` | 0.25 RLUSD | Full Bull/Bear/Neutral AI debate via TradingAgents + Anthropic Claude |

---

## Quick Start

### Claude Desktop / Cursor (local stdio)
```bash
claude mcp add sml-institutional -- python /path/to/mcp_server_sml.py
```

### Via Smithery (remote HTTP)
Install directly from [Smithery](https://smithery.ai/servers/timothy-walton45/sml-base4-signals).

### Direct MCP connection
```
https://sml-signal-api-production.up.railway.app/mcp
```

---

## Signal Decision Tree for AI Agents

```
1. Call get_signal_preview(ticker)
2. IF ci_gate_passed = false  →  DO NOT ACT (chop zone)
3. IF ci_gate_passed = true AND is_prime = true  →  PRIME — call get_intelligence_brief()
4. IF ci_gate_passed = true AND is_prime = false →  BUILDING — recheck in 1 hour
5. Brief includes agent_instruction with exact action, levels, and invalidation point
6. ALL execution requires human confirmation
```

---

## The Full Institutional Stack

| Engine | Description |
|--------|-------------|
| SML Base-4 (Python + Pine Script v6) | Core compression engine — this MCP server |
| SqueezeOS v5.x | 13+ specialized trading engines |
| Oracle Engine | BUY_PRIME / BUY / HOLD / SHIELD aggregator |
| TradingAgents Counsel | Bull/Bear AI debate via Anthropic Claude |
| Echo Forge | Cross-asset pattern memory |
| IWM 0DTE Desk | Same-day options engine |
| Fee Forge / XRPL | x402 micropayment rail — RLUSD native |
| Robinhood MCP | Paper trading execution (30-day validation in progress) |

---

## Regulatory Context (2026)

- **PDT Rule**: Eliminated June 4, 2026 — no day-trade frequency limit
- **Margin Floor**: $2,000 minimum equity for margin accounts  
- **Hard Stop**: $2,100 circuit breaker — 100-point buffer above the floor
- **Execution**: Human confirmation required on all orders
- **Mode**: Paper mode default

---

## License

**Proprietary — © ScriptMasterLabs 2026. DO NOT REDISTRIBUTE.**

- Website: [scriptmasterlabs.com](https://scriptmasterlabs.com)
- GitHub: [timwal78](https://github.com/timwal78)
- Smithery: [timothy-walton45/sml-base4-signals](https://smithery.ai/servers/timothy-walton45/sml-base4-signals)
