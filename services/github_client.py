import requests
import os
import json
import logging

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class GitHubClient:
    """Client to interact with GitHub API, with caching for stale data."""

    def __init__(self, session=None, allow_stale=False):
        self.session = session or requests.Session()
        self.allow_stale = allow_stale

    def get_user_events(self, username):
        try:
            response = self.session.get(
                f"https://api.github.com/users/{username}/events/public", timeout=10)
            response.raise_for_status()
            response_data = response.json()
            self._write_to_cache(username, response_data)
            return response_data
        except requests.RequestException as e:
            if self.allow_stale:
                logger.warning(
                    "Network issue. Returning stale cached data if available.")
                return self._read_from_cache(username)
            raise e

    def _read_from_cache(self, username):
        """Read from cache incase of network issues."""

        cache_path = f"/tmp/github_events_{username}.json"
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def _write_to_cache(self, username, data):
        """Write data to cache for future use."""

        cache_path = f"/tmp/github_events_{username}.json"
        try:
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(data, f)
        except Exception:
            pass
