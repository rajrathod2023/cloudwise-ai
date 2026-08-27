export function AppHeader() {
  return (
    <header className="site-header">
      <div className="container header-content">
        <a className="brand" href="#top" aria-label="CloudWise AI home">
          <span className="brand-mark" aria-hidden="true">
            CW
          </span>
          <span>
            <strong>CloudWise AI</strong>
            <small>AWS AI Solution Advisor</small>
          </span>
        </a>

        <span className="status-badge">
          <span className="status-dot" aria-hidden="true" />
          Advisory workspace
        </span>
      </div>
    </header>
  )
}
