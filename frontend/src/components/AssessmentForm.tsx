import { useState } from 'react'
import type { ChangeEvent, FormEvent } from 'react'

import type { AssessmentRequest } from '../types/assessment'

type FormErrors = Partial<Record<keyof AssessmentRequest, string>>

const initialAssessment: AssessmentRequest = {
  industry: '',
  business_challenge: '',
  input_data_type: '',
  desired_output: '',
  intended_users: '',
  processing_type: 'either',
  data_sensitivity: 'medium',
  expected_usage: 'medium',
  budget_level: 'medium',
  compliance_requirements: '',
  additional_context: '',
}

const fieldRules = {
  industry: { min: 2, max: 100, label: 'Industry' },
  business_challenge: { min: 10, max: 2000, label: 'Business challenge' },
  input_data_type: { min: 2, max: 200, label: 'Input data type' },
  desired_output: { min: 2, max: 500, label: 'Desired output' },
  intended_users: { min: 2, max: 300, label: 'Intended users' },
} as const

const optionalFieldRules = {
  compliance_requirements: { max: 500, label: 'Compliance requirements' },
  additional_context: { max: 2000, label: 'Additional context' },
} as const

function validateAssessment(values: AssessmentRequest): FormErrors {
  const errors: FormErrors = {}

  for (const [field, rule] of Object.entries(fieldRules) as [
    keyof typeof fieldRules,
    (typeof fieldRules)[keyof typeof fieldRules],
  ][]) {
    const value = values[field].trim()
    if (value.length < rule.min) {
      errors[field] = `${rule.label} must be at least ${rule.min} characters.`
    } else if (value.length > rule.max) {
      errors[field] = `${rule.label} must be ${rule.max} characters or fewer.`
    }
  }

  for (const [field, rule] of Object.entries(optionalFieldRules) as [
    keyof typeof optionalFieldRules,
    (typeof optionalFieldRules)[keyof typeof optionalFieldRules],
  ][]) {
    if ((values[field]?.length ?? 0) > rule.max) {
      errors[field] = `${rule.label} must be ${rule.max} characters or fewer.`
    }
  }

  return errors
}

type FieldErrorProps = {
  field: keyof AssessmentRequest
  errors: FormErrors
}

function FieldError({ field, errors }: FieldErrorProps) {
  const message = errors[field]
  if (!message) return null

  return (
    <span className="field-error" id={`${field}-error`} role="alert">
      {message}
    </span>
  )
}

export function AssessmentForm() {
  const [values, setValues] = useState<AssessmentRequest>(initialAssessment)
  const [errors, setErrors] = useState<FormErrors>({})
  const [isReady, setIsReady] = useState(false)

  function handleChange(
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>,
  ) {
    const field = event.target.name as keyof AssessmentRequest
    const value = event.target.value

    setValues((current) => ({ ...current, [field]: value }))
    setErrors((current) => ({ ...current, [field]: undefined }))
    setIsReady(false)
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const nextErrors = validateAssessment(values)
    setErrors(nextErrors)
    setIsReady(Object.keys(nextErrors).length === 0)

    if (Object.keys(nextErrors).length > 0) {
      const firstInvalidField = Object.keys(nextErrors)[0]
      document.getElementById(firstInvalidField)?.focus()
    }
  }

  function errorProps(field: keyof AssessmentRequest) {
    return {
      'aria-invalid': Boolean(errors[field]),
      'aria-describedby': errors[field] ? `${field}-error` : undefined,
    }
  }

  return (
    <form className="assessment-form" noValidate onSubmit={handleSubmit}>
      <fieldset>
        <legend>Business context</legend>
        <p className="group-description">
          Tell us what the organisation needs and what information is available.
        </p>

        <div className="form-grid">
          <div className="form-field">
            <label htmlFor="industry">Industry</label>
            <input
              id="industry"
              name="industry"
              type="text"
              minLength={2}
              maxLength={100}
              autoComplete="organization-title"
              placeholder="e.g. Retail, healthcare, finance"
              value={values.industry}
              onChange={handleChange}
              {...errorProps('industry')}
            />
            <FieldError field="industry" errors={errors} />
          </div>

          <div className="form-field form-field-wide form-field-prominent">
            <label htmlFor="business_challenge">Business challenge</label>
            <span className="field-hint" id="business-challenge-hint">
              Describe the problem, current process, and outcome you want to improve.
            </span>
            <textarea
              id="business_challenge"
              name="business_challenge"
              minLength={10}
              maxLength={2000}
              rows={5}
              placeholder="e.g. Our support team needs to understand recurring themes and sentiment across customer feedback."
              value={values.business_challenge}
              onChange={handleChange}
              aria-describedby={
                errors.business_challenge
                  ? 'business-challenge-hint business_challenge-error'
                  : 'business-challenge-hint'
              }
              aria-invalid={Boolean(errors.business_challenge)}
            />
            <FieldError field="business_challenge" errors={errors} />
          </div>

          <div className="form-field">
            <label htmlFor="input_data_type">Input data type</label>
            <input
              id="input_data_type"
              name="input_data_type"
              type="text"
              minLength={2}
              maxLength={200}
              placeholder="e.g. Customer review text"
              value={values.input_data_type}
              onChange={handleChange}
              {...errorProps('input_data_type')}
            />
            <FieldError field="input_data_type" errors={errors} />
          </div>

          <div className="form-field">
            <label htmlFor="desired_output">Desired output</label>
            <input
              id="desired_output"
              name="desired_output"
              type="text"
              minLength={2}
              maxLength={500}
              placeholder="e.g. A structured sentiment summary"
              value={values.desired_output}
              onChange={handleChange}
              {...errorProps('desired_output')}
            />
            <FieldError field="desired_output" errors={errors} />
          </div>

          <div className="form-field form-field-wide">
            <label htmlFor="intended_users">Intended users</label>
            <input
              id="intended_users"
              name="intended_users"
              type="text"
              minLength={2}
              maxLength={300}
              placeholder="e.g. Customer experience and product teams"
              value={values.intended_users}
              onChange={handleChange}
              {...errorProps('intended_users')}
            />
            <FieldError field="intended_users" errors={errors} />
          </div>
        </div>
      </fieldset>

      <fieldset>
        <legend>Solution characteristics</legend>
        <p className="group-description">
          Set the operational characteristics used to shape the recommendation.
        </p>

        <div className="form-grid form-grid-selects">
          <div className="form-field">
            <label htmlFor="processing_type">Processing type</label>
            <select
              id="processing_type"
              name="processing_type"
              value={values.processing_type}
              onChange={handleChange}
            >
              <option value="either">Either</option>
              <option value="batch">Batch</option>
              <option value="real-time">Real-time</option>
            </select>
          </div>

          <div className="form-field">
            <label htmlFor="data_sensitivity">Data sensitivity</label>
            <select
              id="data_sensitivity"
              name="data_sensitivity"
              value={values.data_sensitivity}
              onChange={handleChange}
            >
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>

          <div className="form-field">
            <label htmlFor="expected_usage">Expected usage</label>
            <select
              id="expected_usage"
              name="expected_usage"
              value={values.expected_usage}
              onChange={handleChange}
            >
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>

          <div className="form-field">
            <label htmlFor="budget_level">Budget constraint</label>
            <select
              id="budget_level"
              name="budget_level"
              value={values.budget_level}
              onChange={handleChange}
            >
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>
        </div>
      </fieldset>

      <fieldset>
        <legend>Governance context</legend>
        <p className="group-description">
          Add optional requirements that may influence security and review guidance.
        </p>

        <div className="form-grid">
          <div className="form-field">
            <label htmlFor="compliance_requirements">
              Compliance requirements <span className="optional-label">Optional</span>
            </label>
            <textarea
              id="compliance_requirements"
              name="compliance_requirements"
              maxLength={500}
              rows={4}
              placeholder="e.g. Industry regulations or internal policies"
              value={values.compliance_requirements}
              onChange={handleChange}
              {...errorProps('compliance_requirements')}
            />
            <FieldError field="compliance_requirements" errors={errors} />
          </div>

          <div className="form-field">
            <label htmlFor="additional_context">
              Additional context <span className="optional-label">Optional</span>
            </label>
            <textarea
              id="additional_context"
              name="additional_context"
              maxLength={2000}
              rows={4}
              placeholder="Share any constraints, dependencies, or review needs."
              value={values.additional_context}
              onChange={handleChange}
              {...errorProps('additional_context')}
            />
            <FieldError field="additional_context" errors={errors} />
          </div>
        </div>
      </fieldset>

      <div className="form-actions">
        <button className="primary-button" type="submit">
          Generate recommendation
        </button>
        <p className="submission-explainer">
          This step validates the assessment locally. No data is sent yet.
        </p>
      </div>

      {isReady && (
        <div className="readiness-message" role="status">
          <strong>Assessment ready.</strong>
          <span>API integration is the next step.</span>
        </div>
      )}
    </form>
  )
}
