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

const agentGrid = document.getElementById("agentGrid");
const reviewList = document.getElementById("reviewList");

agents.forEach((agent) => {
  const card = document.createElement("div");
  card.className = "agent-card";
  card.innerHTML = `
    <div>
      <strong>${agent.name}</strong>
      <div class="review-meta">Queue: ${agent.queue} tasks</div>
    </div>
    <span class="status ${agent.status === "review" ? "warn" : "ok"}">${agent.status}</span>
  `;
  agentGrid.appendChild(card);
});

reviews.forEach((item) => {
  const row = document.createElement("div");
  row.className = "review-item";
  row.innerHTML = `
    <div><strong>${item.title}</strong></div>
    <div class="review-meta">${item.meta}</div>
    <div>${item.reason}</div>
    <div class="review-actions">
      <button class="btn">Approve</button>
      <button class="btn ghost">Reject</button>
    </div>
  `;
  reviewList.appendChild(row);
});
