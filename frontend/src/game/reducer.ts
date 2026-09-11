import type { GameAction, GameState } from './types'
import { questions } from './questions'

export const QUESTIONS_PER_GAME = 10

function shuffledQuestions(): typeof questions {
  return [...questions].sort(() => Math.random() - 0.5).slice(0, QUESTIONS_PER_GAME)
}

export const initialGameState: GameState = { phase: 'welcome', sessionQuestions: [], questionIndex: 0, score: 0, selectedChoiceId: null }

export function gameReducer(state: GameState, action: GameAction): GameState {
  switch (action.type) {
    case 'START':
      return { ...initialGameState, phase: 'question', sessionQuestions: shuffledQuestions() }
    case 'ANSWER': {
      if (state.phase !== 'question' || state.selectedChoiceId !== null) return state
      const question = state.sessionQuestions[state.questionIndex]
      return { ...state, phase: 'feedback', selectedChoiceId: action.choiceId, score: state.score + (action.choiceId === question.correctChoiceId ? 1 : 0) }
    }
    case 'NEXT':
      if (state.phase !== 'feedback') return state
      if (state.questionIndex === state.sessionQuestions.length - 1) return { ...state, phase: 'complete' }
      return { ...state, phase: 'question', questionIndex: state.questionIndex + 1, selectedChoiceId: null }
    case 'RESET':
      return initialGameState
    default:
      return state
  }
}

export function isAnswerCorrect(state: GameState): boolean {
  return state.selectedChoiceId === state.sessionQuestions[state.questionIndex].correctChoiceId
}
