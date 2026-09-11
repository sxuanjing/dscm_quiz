export type GamePhase = 'welcome' | 'question' | 'feedback' | 'complete'

export type QuestionCategory = 'flow' | 'roles' | 'warehouse' | 'transport' | 'sustainability' | 'technology'

export interface AnswerChoice {
  id: string
  label: string
}

export interface Question {
  id: string
  category: QuestionCategory
  prompt: string
  choices: [AnswerChoice, AnswerChoice]
  correctChoiceId: string
  explanation: string
  visual: string
}

export interface GameState {
  phase: GamePhase
  sessionQuestions: Question[]
  questionIndex: number
  score: number
  selectedChoiceId: string | null
}

export type GameAction =
  | { type: 'START' }
  | { type: 'ANSWER'; choiceId: string }
  | { type: 'NEXT' }
  | { type: 'RESET' }
