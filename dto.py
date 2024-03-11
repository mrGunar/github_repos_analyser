import dataclasses


@dataclasses.dataclass(frozen=True)
class CommitStat:
    additions: int = 0
    deletions: int = 0

    def __add__(self, other: "CommitStat"):
        return CommitStat(
            self.additions + other.additions, self.deletions + other.deletions
        )

    def __str__(self):
        return f"Total additionals:{self.additions}.\nTotal deletions: {self.deletions}"
