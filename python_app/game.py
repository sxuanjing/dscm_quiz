"""Pure game state transitions for Supply Chain Quest."""

from dataclasses import dataclass
import random
from typing import Sequence

try:
    from .questions import Question, questions
except ImportError:
    from questions import Question, questions

QUESTIONS_PER_GAME = 10


@dataclass(frozen=True)
class GameState:
    phase: str = "welcome"
    session_questions: tuple[Question, ...] = ()
    question_index: int = 0
    score: int = 0
    selected_choice_id: str | None = None


def start_game(question_bank: Sequence[Question] = questions, rng: random.Random | None = None) -> GameState:
    if len(question_bank) < QUESTIONS_PER_GAME:
        raise ValueError("The question bank must contain at least 10 questions")
    generator = rng or random
    selected = tuple(generator.sample(list(question_bank), QUESTIONS_PER_GAME))
    return GameState(phase="question", session_questions=selected)


def answer(state: GameState, choice_id: str) -> GameState:
    if state.phase != "question" or state.selected_choice_id is not None:
        return state
    question = state.session_questions[state.question_index]
    score = state.score + int(choice_id == question.correct_choice_id)
    return GameState("feedback", state.session_questions, state.question_index, score, choice_id)


def next_question(state: GameState) -> GameState:
    if state.phase != "feedback":
        return state
    if state.question_index == len(state.session_questions) - 1:
        return GameState("complete", state.session_questions, state.question_index, state.score, state.selected_choice_id)
    return GameState("question", state.session_questions, state.question_index + 1, state.score, None)


def reset_game() -> GameState:
    return GameState()


def current_question(state: GameState) -> Question:
    return state.session_questions[state.question_index]


def answer_is_correct(state: GameState) -> bool:
    return state.selected_choice_id == current_question(state).correct_choice_id
