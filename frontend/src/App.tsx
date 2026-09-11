import { useEffect, useReducer } from 'react'
import { IconBadge, answerIcon, questionIcon } from './components/IconBadge'
import { gameReducer, initialGameState, isAnswerCorrect, QUESTIONS_PER_GAME } from './game/reducer'

function App() {
  const [state, dispatch] = useReducer(gameReducer, initialGameState)
  const question = state.sessionQuestions[state.questionIndex]

  useEffect(() => {
    if (state.phase !== 'complete') return
    const timeout = window.setTimeout(() => dispatch({ type: 'RESET' }), 15000)
    return () => window.clearTimeout(timeout)
  }, [state.phase])

  if (state.phase === 'welcome') {
    return <main className="screen welcome-screen"><div className="brand-mark" aria-hidden="true"><span>SC</span></div><p className="eyebrow">OPEN HOUSE GAME</p><h1>Supply Chain<br /><strong>Quest</strong></h1><p className="intro">Move it. Make it. Deliver it.</p><button className="primary-button start-button" onClick={() => dispatch({ type: 'START' })}>PLAY <span aria-hidden="true">-&gt;</span></button><p className="microcopy">10 questions | Tap to start</p></main>
  }

  if (state.phase === 'complete') {
    return <main className="screen complete-screen"><p className="eyebrow">DONE!</p><div className="score-ring"><span>{state.score}</span><small>of {QUESTIONS_PER_GAME}</small></div><h1>Nice work!</h1><p className="completion-copy">You kept it moving.</p><button className="primary-button" onClick={() => dispatch({ type: 'RESET' })}>PLAY AGAIN <span aria-hidden="true">-&gt;</span></button><p className="microcopy">Resetting soon</p></main>
  }

  const correct = state.phase === 'feedback' && isAnswerCorrect(state)
  return <main className={`screen game-screen category-${question.category}`}><header className="game-header"><div><p className="eyebrow">QUESTION {state.questionIndex + 1}/{QUESTIONS_PER_GAME}</p><p className="progress">{state.score} <span>points</span></p></div><div className="score-pill"><span>SC</span><strong>{state.score}</strong></div></header><div className="progress-track" aria-label={`Question ${state.questionIndex + 1} of ${QUESTIONS_PER_GAME}`}><span style={{ width: `${((state.questionIndex + 1) / QUESTIONS_PER_GAME) * 100}%` }} /></div><section className="question-panel"><div className="visual-tile" aria-hidden="true"><IconBadge name={questionIcon(question.visual)} size={30} /></div><p className="category-label">{question.category}</p><h1>{question.prompt}</h1><div className="answers" role="group" aria-label="Answer choices">{question.choices.map((choice, index) => { const isSelected = state.selectedChoiceId === choice.id; const isCorrectChoice = question.correctChoiceId === choice.id; const answerClass = state.phase === 'feedback' ? (isCorrectChoice ? 'correct' : isSelected ? 'incorrect' : 'muted') : ''; return <button key={choice.id} className={`answer-button ${answerClass}`} disabled={state.phase === 'feedback'} onClick={() => dispatch({ type: 'ANSWER', choiceId: choice.id })}><span className="answer-icon"><IconBadge name={answerIcon(question.visual, index)} size={20} /></span><span>{choice.label}</span>{state.phase === 'feedback' && isCorrectChoice && <b aria-label="correct">OK</b>}{state.phase === 'feedback' && isSelected && !isCorrectChoice && <b aria-label="incorrect">X</b>}</button> })}</div>{state.phase === 'feedback' && <div className={`feedback ${correct ? 'feedback-correct' : 'feedback-incorrect'}`} role="status"><strong>{correct ? 'YES!' : 'TRY AGAIN'}</strong><span>{question.explanation}</span><button className="next-button" onClick={() => dispatch({ type: 'NEXT' })}>{state.questionIndex === QUESTIONS_PER_GAME - 1 ? 'SCORE' : 'NEXT'} <span aria-hidden="true">-&gt;</span></button></div>}</section></main>
}

export default App
