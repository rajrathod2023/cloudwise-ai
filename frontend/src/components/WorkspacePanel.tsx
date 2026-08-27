type WorkspacePanelProps = {
  eyebrow: string
  title: string
  description: string
  step: string
}

export function WorkspacePanel({
  eyebrow,
  title,
  description,
  step,
}: WorkspacePanelProps) {
  return (
    <section className="workspace-panel" aria-labelledby={`${step}-title`}>
      <div className="panel-heading">
        <span className="step-number" aria-hidden="true">
          {step}
        </span>
        <div>
          <p className="eyebrow">{eyebrow}</p>
          <h2 id={`${step}-title`}>{title}</h2>
        </div>
      </div>
      <p>{description}</p>
      <div className="placeholder-state" aria-label={`${title} coming soon`}>
        <span className="placeholder-line placeholder-line-long" />
        <span className="placeholder-line" />
        <span className="placeholder-label">Coming in the next milestone</span>
      </div>
    </section>
  )
}
