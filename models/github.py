from dataclasses import dataclass
from typing import List


@dataclass
class RepoActivity:
    repo_name: str
    top_event_types: List[str]
    is_owned_by_user: bool
