"""Question bank and validation for Supply Chain Quest."""

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class AnswerChoice:
    id: str
    label: str


@dataclass(frozen=True)
class Question:
    id: str
    category: str
    prompt: str
    choices: tuple[AnswerChoice, AnswerChoice]
    correct_choice_id: str
    explanation: str
    visual: str


questions: tuple[Question, ...] = (
    Question("meaning", "flow", "What does SCM connect?", (AnswerChoice("a", "Products to customers"), AnswerChoice("b", "Only the checkout")), "a", "SCM helps products move from source to customer.", "FLOW"),
    Question("supplier", "roles", "Who provides parts?", (AnswerChoice("a", "A supplier"), AnswerChoice("b", "A customer")), "a", "Suppliers provide materials and parts.", "SUPPLY"),
    Question("warehouse", "warehouse", "Why use a warehouse?", (AnswerChoice("a", "Store products"), AnswerChoice("b", "Make roads")), "a", "Warehouses hold products safely until they are needed.", "STORE"),
    Question("transport", "transport", "Best for an urgent local delivery?", (AnswerChoice("a", "Bike courier"), AnswerChoice("b", "Cargo ship")), "a", "A bike courier is quick and flexible for short trips.", "MOVE"),
    Question("retailer", "roles", "What is a supermarket?", (AnswerChoice("a", "A retailer"), AnswerChoice("b", "A mine")), "a", "Retailers sell products to customers.", "SHOP"),
    Question("inventory", "warehouse", "Too many unsold coats are...", (AnswerChoice("a", "Excess stock"), AnswerChoice("b", "A route")), "a", "Too much stock uses space and money.", "COUNT"),
    Question("green", "sustainability", "What can cut delivery emissions?", (AnswerChoice("a", "Join nearby deliveries"), AnswerChoice("b", "Send empty vans")), "a", "Fewer journeys use less fuel.", "GREEN"),
    Question("robot", "technology", "What can a warehouse robot do?", (AnswerChoice("a", "Sort packages"), AnswerChoice("b", "Write stories")), "a", "Robots can move and sort items.", "ROBOT"),
    Question("customer", "flow", "Who uses the product?", (AnswerChoice("a", "The customer"), AnswerChoice("b", "The loading dock")), "a", "The customer receives and uses the product.", "USE"),
    Question("data", "technology", "Why use supply-chain data?", (AnswerChoice("a", "Make better plans"), AnswerChoice("b", "Make boxes heavy")), "a", "Data helps teams plan stock, routes, and timing.", "DATA"),
    Question("factory", "roles", "Where are products made?", (AnswerChoice("a", "A factory"), AnswerChoice("b", "A checkout")), "a", "Factories turn materials into finished products.", "MAKE"),
    Question("forecast", "technology", "What can a forecast help predict?", (AnswerChoice("a", "Customer demand"), AnswerChoice("b", "The weather only")), "a", "Demand forecasts help businesses prepare the right stock.", "PLAN"),
    Question("ship", "transport", "Which carries goods across oceans?", (AnswerChoice("a", "A delivery bike"), AnswerChoice("b", "A cargo ship")), "b", "Cargo ships move large loads across oceans.", "SHIP"),
    Question("reuse", "sustainability", "Which choice creates less waste?", (AnswerChoice("a", "Reuse boxes"), AnswerChoice("b", "Throw out boxes")), "a", "Reusing boxes keeps useful material in circulation.", "REUSE"),
    Question("quality", "roles", "What checks products work well?", (AnswerChoice("a", "Quality control"), AnswerChoice("b", "A parking sign")), "a", "Quality checks help catch problems before products ship.", "CHECK"),
    Question("lastmile", "transport", "What is the last mile?", (AnswerChoice("a", "Final trip to you"), AnswerChoice("b", "A factory machine")), "a", "The last mile is the final delivery to the customer.", "FINAL"),
    Question("barcode", "technology", "What can a barcode identify?", (AnswerChoice("a", "A product"), AnswerChoice("b", "A road")), "a", "Barcodes help teams identify and track products.", "SCAN"),
    Question("air", "transport", "Which is usually fastest for far-away urgent goods?", (AnswerChoice("a", "Air freight"), AnswerChoice("b", "A slow boat")), "a", "Air freight is fast, though it can use more energy.", "AIR"),
    Question("repair", "sustainability", "What helps products last longer?", (AnswerChoice("a", "Repair them"), AnswerChoice("b", "Replace them fast")), "a", "Repairing products can reduce waste and new materials.", "FIX"),
    Question("truck", "transport", "What moves goods between nearby cities?", (AnswerChoice("a", "A truck"), AnswerChoice("b", "A bookshelf")), "a", "Trucks are flexible for road deliveries.", "TRUCK"),
    Question("safety", "warehouse", "What keeps a warehouse safe?", (AnswerChoice("a", "Clear walkways"), AnswerChoice("b", "Boxes in every path")), "a", "Clear walkways help people and equipment move safely.", "SAFE"),
)


def validate_questions(items: Sequence[Question]) -> None:
    seen_ids: set[str] = set()
    for question in items:
        if question.id in seen_ids:
            raise ValueError(f"Duplicate question id: {question.id}")
        seen_ids.add(question.id)
        if len(question.choices) != 2:
            raise ValueError(f"Question {question.id} must have exactly two choices")
        choice_ids = {choice.id for choice in question.choices}
        if question.correct_choice_id not in choice_ids:
            raise ValueError(f"Question {question.id} has an invalid correct choice")


validate_questions(questions)
