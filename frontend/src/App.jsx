const agents = [
  { name: "Agent Lyra", status: "active", queue: 4 },
  { name: "Agent Nox", status: "active", queue: 2 },
  { name: "Agent Xenia", status: "review", queue: 1 },
  { name: "Agent Sol", status: "active", queue: 5 },
];

const reviews = [
  {
    title: "Caption flagged for brand risk",
    meta: "Confidence 0.41 · Campaign: Aurora",
    reason: "Mentions competitor product explicitly.",
  },
  {
    title: "Budget escalation requested",
    meta: "Spend proposal: $1,500 · Agent Sol",
    reason: "Exceeds daily budget gate.",
  },
  {
    title: "Policy check pending",
    meta: "Platform: TikTok · Tag: sensitive topic",
    reason: "Requires human review before publish.",
  },
];

export default function App() {
  return (
    <div className="app">
      <div className="bg-texture"></div>
      <header className="topbar">
        <div className="brand">
          <span className="brand-mark">C</span>
          <div>
            <div className="brand-title">Project Chimera</div>
            <div className="brand-subtitle">Human Ops Console</div>
          </div>
        </div>
        <div className="top-actions">
          <button className="btn ghost">Switch Role</button>
          <button className="btn">Approve Batch</button>
        </div>
      </header>

      <main className="grid">
        <section className="panel hero">
          <div>
            <h1>Stay in control of the swarm.</h1>
            <p>
              Monitor agents, review risky outputs, and keep a defensible audit trail.
              Human approval gates are enforced where it matters.
            </p>
          </div>
          <div className="hero-metrics">
            <div className="metric">
              <span className="label">Active Agents</span>
              <span className="value">128</span>
            </div>
            <div className="metric">
              <span className="label">Items in Review</span>
              <span className="value">23</span>
            </div>
            <div className="metric">
              <span className="label">Budget Utilization</span>
              <span className="value">62%</span>
            </div>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Operations Dashboard</h2>
            <span className="badge">Live</span>
          </div>
          <div className="agent-grid">
            {agents.map((agent) => (
              <div className="agent-card" key={agent.name}>
                <div>
                  <strong>{agent.name}</strong>
                  <div className="review-meta">Queue: {agent.queue} tasks</div>
                </div>
                <span className={`status ${agent.status === "review" ? "warn" : "ok"}`}>
                  {agent.status}
                </span>
              </div>
            ))}
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Review Queue</h2>
            <div className="filters">
              <button className="pill active">All</button>
              <button className="pill">Policy</button>
              <button className="pill">Brand</button>
              <button className="pill">Budget</button>
            </div>
          </div>
          <div className="review-list">
            {reviews.map((item) => (
              <div className="review-item" key={item.title}>
                <div>
                  <strong>{item.title}</strong>
                </div>
                <div className="review-meta">{item.meta}</div>
                <div>{item.reason}</div>
                <div className="review-actions">
                  <button className="btn">Approve</button>
                  <button className="btn ghost">Reject</button>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Agent Profile</h2>
          </div>
          <div className="profile">
            <div className="profile-card">
              <div className="avatar">AX</div>
              <div>
                <div className="profile-name">Agent Xenia</div>
                <div className="profile-meta">Persona: Tech Futurist</div>
                <div className="chip-row">
                  <span className="chip">reputation 0.86</span>
                  <span className="chip">status: busy</span>
                </div>
              </div>
            </div>
            <div className="profile-body">
              <div className="profile-section">
                <h3>Active Skills</h3>
                <ul className="flat-list">
                  <li>fetch_trends</li>
                  <li>generate_caption</li>
                  <li>publish_content</li>
                </ul>
              </div>
              <div className="profile-section">
                <h3>Recent Outputs</h3>
                <ul className="flat-list">
                  <li>Caption: "AI is now the creative director"</li>
                  <li>Post: Threads / 2 min ago</li>
                  <li>HITL: flagged for brand review</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Task Trace View</h2>
          </div>
          <div className="timeline">
            <div className="event">
              <span className="dot"></span>
              <div>
                <div className="event-title">Task Created</div>
                <div className="event-meta">Planner / 12:45:02</div>
              </div>
            </div>
            <div className="event">
              <span className="dot"></span>
              <div>
                <div className="event-title">Worker Draft Generated</div>
                <div className="event-meta">Worker / 12:45:11</div>
              </div>
            </div>
            <div className="event">
              <span className="dot warn"></span>
              <div>
                <div className="event-title">Judge Escalated</div>
                <div className="event-meta">Confidence 0.41 / 12:45:15</div>
              </div>
            </div>
            <div className="event">
              <span className="dot"></span>
              <div>
                <div className="event-title">HITL Review Pending</div>
                <div className="event-meta">Moderator / 12:45:18</div>
              </div>
            </div>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <h2>Governance & Policies</h2>
          </div>
          <div className="policy-grid">
            <div className="policy">
              <div className="policy-title">HITL Threshold</div>
              <div className="policy-value">0.65</div>
            </div>
            <div className="policy">
              <div className="policy-title">Budget Gate</div>
              <div className="policy-value">$1,000 / day</div>
            </div>
            <div className="policy">
              <div className="policy-title">Brand Safety</div>
              <div className="policy-value">Strict</div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
