import type { AssessmentResponse } from '../types/assessment'

type RecommendationResultsProps = {
  recommendation: AssessmentResponse | null
  onNewAssessment: () => void
}

type GuidanceListProps = {
  title: string
  items: string[]
}

function GuidanceList({ title, items }: GuidanceListProps) {
  return (
    <div className="guidance-group">
      <h4>{title}</h4>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  )
}

export function RecommendationResults({
  recommendation,
  onNewAssessment,
}: RecommendationResultsProps) {
  if (!recommendation) {
    return (
      <section
        className="workspace-panel recommendation-panel"
        aria-labelledby="recommendation-results-title"
      >
        <div className="panel-heading">
          <span className="step-number" aria-hidden="true">
            02
          </span>
          <div>
            <p className="eyebrow">Output</p>
            <h2 id="recommendation-results-title" tabIndex={-1}>
              Recommendation results
            </h2>
          </div>
        </div>
        <div className="results-empty-state">
          <strong>Complete the assessment to generate a recommendation.</strong>
          <p>
            Your AWS AI service direction, architecture, controls, and delivery
            guidance will appear here.
          </p>
        </div>
      </section>
    )
  }

  const primaryService = recommendation.recommended_services[0]

  return (
    <section
      className="workspace-panel recommendation-panel"
      aria-labelledby="recommendation-results-title"
    >
      <div className="panel-heading results-heading">
        <div className="results-heading-main">
          <span className="step-number" aria-hidden="true">
            02
          </span>
          <div>
            <p className="eyebrow">Output</p>
            <h2 id="recommendation-results-title" tabIndex={-1}>
              Recommendation results
            </h2>
          </div>
        </div>
        <button className="secondary-button" type="button" onClick={onNewAssessment}>
          New assessment
        </button>
      </div>

      <p className="sr-only" role="status">
        Recommendation generated successfully.
      </p>

      <div className="recommendation-dashboard">
        <section className="recommendation-summary" aria-labelledby="summary-title">
          <div className="summary-primary">
            <p className="section-kicker">Primary AWS AI service</p>
            <h3 id="summary-title">
              {primaryService?.service_name ?? 'Service recommendation unavailable'}
            </h3>
            <p>{recommendation.problem_summary}</p>
          </div>
          <dl className="summary-facts">
            <div>
              <dt>Complexity estimate</dt>
              <dd>
                <span className={`planning-badge level-${recommendation.complexity}`}>
                  {recommendation.complexity}
                </span>
                <span className="fact-detail">
                  Based on workload characteristics and the recommended service.
                </span>
              </dd>
            </div>
            <div>
              <dt>Relative cost estimate</dt>
              <dd>
                <span className={`planning-badge level-${recommendation.cost_level}`}>
                  {recommendation.cost_level}
                </span>
                <span className="fact-detail">
                  A planning level, not an AWS bill or pricing quote.
                </span>
              </dd>
            </div>
          </dl>
        </section>

        <section className="result-section" aria-labelledby="services-title">
          <div className="result-section-heading">
            <p className="section-kicker">Service fit</p>
            <h3 id="services-title">Why this service?</h3>
          </div>
          <div className="service-list">
            {recommendation.recommended_services.map((service) => (
              <article className="service-card" key={service.service_name}>
                <h4>{service.service_name}</h4>
                <dl className="service-details">
                  <div>
                    <dt>Purpose</dt>
                    <dd>{service.purpose}</dd>
                  </div>
                  <div>
                    <dt>Why selected</dt>
                    <dd>{service.reason_selected}</dd>
                  </div>
                  <div>
                    <dt>Implementation role</dt>
                    <dd>{service.implementation_role}</dd>
                  </div>
                </dl>
              </article>
            ))}
          </div>
        </section>

        <section className="result-section" aria-labelledby="architecture-title">
          <div className="result-section-heading">
            <p className="section-kicker">Advisory solution flow</p>
            <h3 id="architecture-title">Proposed target architecture</h3>
            <p className="result-section-description">
              These AWS services are recommendation targets. CloudWise V1 has not
              deployed or connected them.
            </p>
          </div>
          <ol className="architecture-flow">
            {recommendation.architecture.map((component, index) => (
              <li key={`${component.component_name}-${index}`}>
                <span className="flow-index" aria-hidden="true">
                  {String(index + 1).padStart(2, '0')}
                </span>
                <div>
                  <h4>{component.component_name}</h4>
                  <p className="aws-service-label">{component.aws_service}</p>
                  <p>{component.responsibility}</p>
                </div>
              </li>
            ))}
          </ol>
        </section>

        <section className="result-section" aria-labelledby="phases-title">
          <div className="result-section-heading">
            <p className="section-kicker">Delivery path</p>
            <h3 id="phases-title">Proposed implementation plan</h3>
            <p className="result-section-description">
              Suggested future steps if the recommendation is approved for delivery.
            </p>
          </div>
          <ol className="phase-timeline">
            {recommendation.implementation_phases.map((phase) => (
              <li key={phase.phase_number}>
                <span className="phase-number">Phase {phase.phase_number}</span>
                <div>
                  <h4>{phase.title}</h4>
                  <p>{phase.description}</p>
                </div>
              </li>
            ))}
          </ol>
        </section>

        <div className="result-grid">
          <section className="result-section" aria-labelledby="responsible-ai-title">
            <div className="result-section-heading">
              <p className="section-kicker">Review and oversight</p>
              <h3 id="responsible-ai-title">Responsible AI</h3>
            </div>
            {recommendation.responsible_ai.human_review_required && (
              <p className="review-indicator">Human review required</p>
            )}
            <p className="section-explanation">
              {recommendation.responsible_ai.explanation}
            </p>
            <div className="guidance-columns">
              <GuidanceList
                title="Risks"
                items={recommendation.responsible_ai.risks}
              />
              <GuidanceList
                title="Mitigations"
                items={recommendation.responsible_ai.mitigations}
              />
            </div>
          </section>

          <section className="result-section" aria-labelledby="security-title">
            <div className="result-section-heading">
              <p className="section-kicker">Technical controls</p>
              <h3 id="security-title">Recommended future security controls</h3>
              <p className="result-section-description">
                Controls to evaluate and provision during implementation; CloudWise
                V1 has not configured them.
              </p>
            </div>
            <div className="guidance-stack">
              <GuidanceList
                title="Access control"
                items={recommendation.security.iam_controls}
              />
              <GuidanceList
                title="Encryption"
                items={recommendation.security.encryption_controls}
              />
              <GuidanceList
                title="Logging & audit"
                items={recommendation.security.logging_controls}
              />
            </div>
            <div className="advisory-detail">
              <strong>Data protection</strong>
              <p>{recommendation.security.data_protection_notes}</p>
            </div>
          </section>
        </div>

        <section className="result-section" aria-labelledby="privacy-title">
          <div className="result-section-heading">
            <p className="section-kicker">Data governance</p>
            <h3 id="privacy-title">Privacy &amp; compliance</h3>
          </div>
          <div className="guidance-columns">
            <GuidanceList
              title="Privacy considerations"
              items={recommendation.privacy_and_compliance.privacy_considerations}
            />
            <GuidanceList
              title="Compliance considerations"
              items={recommendation.privacy_and_compliance.compliance_considerations}
            />
          </div>
          <div className="advisory-detail">
            <strong>Data retention</strong>
            <p>{recommendation.privacy_and_compliance.data_retention_notes}</p>
          </div>
        </section>

        <div className="result-grid result-grid-compact">
          <section className="result-section" aria-labelledby="limitations-title">
            <div className="result-section-heading">
              <p className="section-kicker">Known constraints</p>
              <h3 id="limitations-title">Limitations</h3>
            </div>
            <ul className="plain-guidance-list">
              {recommendation.limitations.map((limitation) => (
                <li key={limitation}>{limitation}</li>
              ))}
            </ul>
          </section>

          <section className="result-section" aria-labelledby="alternatives-title">
            <div className="result-section-heading">
              <p className="section-kicker">Options to consider</p>
              <h3 id="alternatives-title">Alternatives considered</h3>
            </div>
            <ul className="plain-guidance-list">
              {recommendation.alternatives_considered.map((alternative) => (
                <li key={alternative}>{alternative}</li>
              ))}
            </ul>
          </section>
        </div>

        <aside className="recommendation-disclaimer" aria-label="Recommendation disclaimer">
          <strong>Advisory notice</strong>
          <p>{recommendation.disclaimer}</p>
        </aside>
      </div>
    </section>
  )
}
