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

export interface RecommendedService {
  service_name: string
  purpose: string
  reason_selected: string
  implementation_role: string
}

export interface ArchitectureComponent {
  component_name: string
  aws_service: string
  responsibility: string
}

export interface ImplementationPhase {
  phase_number: number
  title: string
  description: string
}

export interface ResponsibleAI {
  risks: string[]
  mitigations: string[]
  human_review_required: boolean
  explanation: string
}

export interface SecurityAssessment {
  iam_controls: string[]
  encryption_controls: string[]
  logging_controls: string[]
  data_protection_notes: string
}

export interface PrivacyComplianceAssessment {
  privacy_considerations: string[]
  compliance_considerations: string[]
  data_retention_notes: string
}

export interface AssessmentResponse {
  assessment_id: string
  status: 'completed'
  problem_summary: string
  use_case_category: string
  recommended_services: RecommendedService[]
  architecture: ArchitectureComponent[]
  implementation_phases: ImplementationPhase[]
  responsible_ai: ResponsibleAI
  security: SecurityAssessment
  privacy_and_compliance: PrivacyComplianceAssessment
  limitations: string[]
  alternatives_considered: string[]
  complexity: PlanningLevel
  cost_level: PlanningLevel
  disclaimer: string
}
