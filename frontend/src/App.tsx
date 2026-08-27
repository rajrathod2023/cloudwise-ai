import { useState } from 'react'

import { AppHeader } from './components/AppHeader'
import { AssessmentForm } from './components/AssessmentForm'
import { WorkspacePanel } from './components/WorkspacePanel'
import type { AssessmentResponse } from './types/assessment'

const advisoryAreas = [
  'AWS AI service fit',
  'Architecture guidance',
  'Security and privacy',
  'Responsible AI review',
]

export default function App() {
  const [assessmentResponse, setAssessmentResponse] =
    useState<AssessmentResponse | null>(null)

  return (
    <div id="top" className="app-shell">
      <AppHeader />

      <main>
        <section className="hero-section">
          <div className="container hero-grid">
            <div className="hero-copy">
              <p className="eyebrow">Plan with clarity</p>
              <h1>Turn a business challenge into an AWS AI solution direction.</h1>
              <p className="hero-intro">
                CloudWise AI is an advisory workspace that helps teams explore a
                structured, responsible starting point for AWS AI implementation.
              </p>
              <p className="advisory-note">
                Recommendations are indicative and require qualified human review
                before implementation.
              </p>
            </div>

            <aside className="capability-card" aria-labelledby="coverage-title">
              <p className="eyebrow">Recommendation coverage</p>
              <h2 id="coverage-title">A practical view of the whole solution</h2>
              <ul>
                {advisoryAreas.map((area) => (
                  <li key={area}>
                    <span aria-hidden="true">✓</span>
                    {area}
                  </li>
                ))}
              </ul>
            </aside>
          </div>
        </section>

        <section className="workspace-section" aria-labelledby="workspace-title">
          <div className="container">
            <div className="section-heading">
              <p className="eyebrow">Advisor workflow</p>
              <h2 id="workspace-title">From context to recommendation</h2>
              <p>
                The workspace will guide you through describing the problem and
                reviewing a structured solution proposal.
              </p>
            </div>

            <div className="workspace-grid">
              <section
                className="workspace-panel assessment-panel"
                aria-labelledby="assessment-title"
              >
                <div className="panel-heading">
                  <span className="step-number" aria-hidden="true">
                    01
                  </span>
                  <div>
                    <p className="eyebrow">Input</p>
                    <h2 id="assessment-title">Assessment</h2>
                  </div>
                </div>
                <p>
                  Describe the business need, data, users, constraints, and expected
                  scale.
                </p>
                <AssessmentForm onAssessmentCreated={setAssessmentResponse} />
              </section>
              {assessmentResponse ? (
                <section
                  className="workspace-panel result-confirmation-panel"
                  aria-labelledby="recommendation-results-title"
                >
                  <div className="panel-heading">
                    <span className="step-number" aria-hidden="true">
                      02
                    </span>
                    <div>
                      <p className="eyebrow">Output</p>
                      <h2 id="recommendation-results-title">
                        Recommendation results
                      </h2>
                    </div>
                  </div>
                  <p>
                    The local CloudWise API returned a valid recommendation.
                  </p>
                  <div className="integration-success" role="status">
                    <span className="success-mark" aria-hidden="true">
                      ✓
                    </span>
                    <div>
                      <strong>Recommendation generated successfully.</strong>
                      <span>
                        Primary service:{' '}
                        {assessmentResponse.recommended_services[0]?.service_name}
                      </span>
                    </div>
                  </div>
                  <p className="results-note">
                    The complete recommendation dashboard will be added in a future
                    milestone.
                  </p>
                </section>
              ) : (
                <WorkspacePanel
                  step="02"
                  eyebrow="Output"
                  title="Recommendation results"
                  description="Review the proposed AWS AI service, architecture, controls, tradeoffs, and delivery plan."
                />
              )}
            </div>
          </div>
        </section>
      </main>

      <footer>
        <div className="container footer-content">
          <span>CloudWise AI</span>
          <span>Local advisory experience · No AWS resources connected</span>
        </div>
      </footer>
    </div>
  )
}
