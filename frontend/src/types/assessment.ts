export type ProcessingType = 'real-time' | 'batch' | 'either'
export type PlanningLevel = 'low' | 'medium' | 'high'

export interface AssessmentRequest {
  industry: string
  business_challenge: string
  input_data_type: string
  desired_output: string
  intended_users: string
  processing_type: ProcessingType
  data_sensitivity: PlanningLevel
  expected_usage: PlanningLevel
  budget_level: PlanningLevel
  compliance_requirements?: string
  additional_context?: string
}
