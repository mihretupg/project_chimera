# Chimera Agent Research Notes

## Chimera & OpenClaw

- Chimera agents are **nodes in an Agent Social Network**.
- Each agent publishes:
  - **Availability** (idle, busy, degraded)
  - **Skills** (capabilities and supported tasks)
  - **Reputation** (historical performance, reliability)
- Other agents can discover Chimera nodes **without a human marketplace**.
- This models a **peer-to-peer agent economy** where humans are optional governors.

## Social Protocols Agents Require

1. **Capability advertisement**
   - Agents broadcast what they can do.
2. **Rate negotiation**
   - Agents negotiate costs/effort autonomously.
3. **Trust / reputation exchange**
   - Maintain confidence in collaborative workflows.
4. **Status broadcasting**
   - Communicate busy, idle, or degraded states to the network.

## Mapping to OpenClaw Presence & MCP Resources

- Availability → OpenClaw presence system
- Skill catalog → MCP skill registry
- Reputation → MCP scoring & trust system
- Status → Resource-aware scheduling
