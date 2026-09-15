"""Behavior tests for the pure Supply Chain Quest game model."""

import random
import unittest

from python_app.game import (
    QUESTIONS_PER_GAME,
    GameState,
    answer,
    answer_is_correct,
    current_question,
    next_question,
    reset_game,
    start_game,
)
from python_app.questions import AnswerChoice, Question, questions, validate_questions


class QuestionBankTests(unittest.TestCase):
    def test_question_bank_has_valid_two_choice_questions(self) -> None:
        self.assertGreaterEqual(len(questions), QUESTIONS_PER_GAME)
        validate_questions(questions)

    def test_validation_rejects_duplicate_ids(self) -> None:
        duplicate = questions[0]
        with self.assertRaisesRegex(ValueError, "Duplicate question id"):
            validate_questions((duplicate, duplicate))

    def test_validation_rejects_wrong_choice_count(self) -> None:
        invalid = Question(
            "invalid", "flow", "Prompt", (AnswerChoice("a", "A"),), "a", "Explain", "FLOW"  # type: ignore[arg-type]
        )
        with self.assertRaisesRegex(ValueError, "exactly two"):
            validate_questions((invalid,))

    def test_validation_rejects_unknown_correct_choice(self) -> None:
        invalid = Question(
            "invalid", "flow", "Prompt", (AnswerChoice("a", "A"), AnswerChoice("b", "B")), "c", "Explain", "FLOW"
        )
        with self.assertRaisesRegex(ValueError, "invalid correct choice"):
            validate_questions((invalid,))


class GameStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.playing = start_game(rng=random.Random(7))

    def test_start_selects_ten_questions(self) -> None:
        self.assertEqual(self.playing.phase, "question")
        self.assertEqual(len(self.playing.session_questions), QUESTIONS_PER_GAME)
        self.assertEqual(self.playing.question_index, 0)
        self.assertEqual(self.playing.score, 0)

    def test_correct_answer_scores_once(self) -> None:
        correct_id = current_question(self.playing).correct_choice_id
        answered = answer(self.playing, correct_id)
        self.assertEqual(answered.phase, "feedback")
        self.assertEqual(answered.score, 1)
        self.assertTrue(answer_is_correct(answered))
        self.assertEqual(answer(answered, "b"), answered)

    def test_incorrect_answer_does_not_score(self) -> None:
        question = current_question(self.playing)
        wrong_id = next(choice.id for choice in question.choices if choice.id != question.correct_choice_id)
        answered = answer(self.playing, wrong_id)
        self.assertEqual(answered.score, 0)
        self.assertFalse(answer_is_correct(answered))

    def test_answering_invalid_choice_still_locks_question(self) -> None:
        answered = answer(self.playing, "unknown")
        self.assertEqual(answered.phase, "feedback")
        self.assertEqual(answered.score, 0)
        self.assertEqual(answer(answered, "a"), answered)

    def test_next_advances_and_clears_selection(self) -> None:
        answered = answer(self.playing, current_question(self.playing).correct_choice_id)
        next_state = next_question(answered)
        self.assertEqual(next_state.phase, "question")
        self.assertEqual(next_state.question_index, 1)
        self.assertIsNone(next_state.selected_choice_id)
        self.assertEqual(next_state.score, 1)

    def test_next_is_ignored_before_feedback(self) -> None:
        self.assertEqual(next_question(self.playing), self.playing)

    def test_last_next_completes_game(self) -> None:
        state = self.playing
        for _ in range(QUESTIONS_PER_GAME):
            state = answer(state, current_question(state).correct_choice_id)
            state = next_question(state)
        self.assertEqual(state.phase, "complete")
        self.assertEqual(state.score, QUESTIONS_PER_GAME)

    def test_reset_returns_to_welcome(self) -> None:
        self.assertEqual(reset_game(), GameState())
        self.assertEqual(reset_game(), reset_game())


if __name__ == "__main__":
    unittest.main()
