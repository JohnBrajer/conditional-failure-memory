"""Reference implementation for John Brajer's Conditional Failure Memory."""
from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class FailureRecord:
    possibility_id: str
    state: Mapping[str, Any]
    conditions: Mapping[str, Any]
    outcome: str
    causes: tuple[str, ...] = field(default_factory=tuple)
    reactivation_conditions: Mapping[str, Any] = field(default_factory=dict)


class FailureMemory:
    def __init__(self) -> None:
        self._records: list[FailureRecord] = []

    def remember(self, record: FailureRecord) -> None:
        self._records.append(record)

    def history(self, possibility_id: str) -> list[FailureRecord]:
        return [r for r in self._records if r.possibility_id == possibility_id]


if __name__ == "__main__":
    memory = FailureMemory()
    memory.remember(FailureRecord(
        possibility_id="launch",
        state={"budget": 200},
        conditions={"required_budget": 500},
        outcome="blocked",
        causes=("insufficient_budget",),
        reactivation_conditions={"budget_gte": 500},
    ))
    print(memory.history("launch"))
