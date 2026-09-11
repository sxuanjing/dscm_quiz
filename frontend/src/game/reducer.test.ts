import { describe, expect, it } from 'vitest'
import { questions, validateQuestions } from './questions'
import { gameReducer, initialGameState, QUESTIONS_PER_GAME } from './reducer'

describe('question bank', () => {
  it('contains valid two-choice questions', () => {
    expect(questions.length).toBeGreaterThanOrEqual(10)
    expect(() => validateQuestions(questions)).not.toThrow()
  })
})

describe('game reducer', () => {
  it('starts and scores a correct answer once', () => {
    const playing = gameReducer(initialGameState, { type: 'START' })
    expect(playing.sessionQuestions).toHaveLength(QUESTIONS_PER_GAME)
    const correctChoiceId = playing.sessionQuestions[0].correctChoiceId
    const answered = gameReducer(playing, { type: 'ANSWER', choiceId: correctChoiceId })
    expect(answered.phase).toBe('feedback')
    expect(answered.score).toBe(1)
    expect(gameReducer(answered, { type: 'ANSWER', choiceId: 'b' })).toEqual(answered)
  })

  it('does not score an incorrect answer', () => {
    const playing = gameReducer(initialGameState, { type: 'START' })
    const question = playing.sessionQuestions[0]
    const wrongChoiceId = question.choices.find((choice) => choice.id !== question.correctChoiceId)!.id
    expect(gameReducer(playing, { type: 'ANSWER', choiceId: wrongChoiceId }).score).toBe(0)
  })

  it('advances and resets completely', () => {
    const playing = gameReducer(initialGameState, { type: 'START' })
    const answered = gameReducer(playing, { type: 'ANSWER', choiceId: playing.sessionQuestions[0].correctChoiceId })
    const next = gameReducer(answered, { type: 'NEXT' })
    expect(next.questionIndex).toBe(1)
    expect(next.selectedChoiceId).toBeNull()
    expect(gameReducer(next, { type: 'RESET' })).toEqual(initialGameState)
  })
})
