import type { AssessmentRequest, AssessmentResponse } from '../types/assessment'

const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000'
).replace(/\/$/, '')

export type AssessmentApiErrorKind = 'validation' | 'server' | 'unavailable'

export class AssessmentApiError extends Error {
  kind: AssessmentApiErrorKind

  constructor(kind: AssessmentApiErrorKind) {
    super(kind)
    this.name = 'AssessmentApiError'
    this.kind = kind
  }
}

export async function createAssessment(
  request: AssessmentRequest,
): Promise<AssessmentResponse> {
  let response: Response

  try {
    response = await fetch(`${API_BASE_URL}/api/v1/assessments`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    })
  } catch {
    throw new AssessmentApiError('unavailable')
  }

  if (response.status === 422) {
    throw new AssessmentApiError('validation')
  }

  if (!response.ok) {
    throw new AssessmentApiError('server')
  }

  return (await response.json()) as AssessmentResponse
}
