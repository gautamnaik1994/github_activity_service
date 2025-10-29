import sys
import json
from services.github_client import GitHubClient
from services.activity_analyzer import ActivityAnalyzer
import logging


logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main():
    if len(sys.argv) < 2:
        logger.error("Usage: python main.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    client = GitHubClient(allow_stale=True)
    analyzer = ActivityAnalyzer(username)

    try:
        events = client.get_user_events(username)
        summaries = analyzer.summarize(events)

        if not summaries:
            logger.warning(
                f"No recent public activity found for user '{username}'.")
            return

        print(json.dumps(
            [s.__dict__ for s in summaries],
            indent=2
        ))

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
