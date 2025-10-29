from collections import Counter, defaultdict
from typing import List
from models.github import RepoActivity


class ActivityAnalyzer:
    """Processes raw GitHub events into summarized activity reports."""

    def __init__(self, username: str):
        self.username = username.lower()
        self.discarded_event_types = ["ForkEvent", "WatchEvent", "ReleaseEvent", "CreateEvent",
                                      "PublicEvent", "DeleteEvent", "MemberEvent", "GollumEvent", "ReleaseEvent"]

    def summarize(self, events: List[dict]) -> List[RepoActivity]:
        if not events:
            return []

        repos = defaultdict(list)

        for event in events:
            repo_name = event.get("repo", {}).get("name")
            event_type = event.get("type")
            if not repo_name or not event_type or event_type in self.discarded_event_types:
                continue
            repos[repo_name].append(event_type)

        summaries = []
        for repo, event_types in repos.items():
            top3 = [etype for etype, _ in Counter(event_types).most_common(3)]
            owner = repo.split("/")[0].lower()
            summaries.append(
                RepoActivity(
                    repo_name=repo,
                    top_event_types=top3,
                    is_owned_by_user=(owner == self.username)
                )
            )
        return summaries
