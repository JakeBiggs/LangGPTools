# Based on https://raw.githubusercontent.com/hwchase17/langchain/master/langchain/utilities/google_search.py

import os
from typing import Any
from llm_agents.tools.base import ToolInterface
from googleapiclient.discovery import build


"""
Adapted from: Instructions adapted from https://stackoverflow.com/questions/
37083058/
programmatically-searching-google-in-python-using-custom-search
-Install the google-api-python-client library by running the command "pip install google-api-python-client" in your terminal. Make sure that you have a Google account, and if you haven't done so already, create a Google APIs Console project.

-Create an API key by going to the APIs & Services → Credentials panel in Cloud Console, and selecting "Create credentials" and then "API key" from the dropdown menu. The newly created key will be displayed in a dialog box.

-Set up a Custom Search Engine that allows you to search the entire web. Go to this link to create a custom search engine, and add any valid URL (e.g. www.stackoverflow.com) to the "Sites to search" field. Then, go to "Edit search engine" → {your search engine name} → "Setup" and turn "Search the entire web" on. Finally, remove the URL you added from the list of "Sites to search" and take note of the search-engine-ID under "Search engine ID".

-Enable the Custom Search API by going to the APIs & Services → Dashboard panel in Cloud Console, clicking "Enable APIs and Services", searching for "Custom Search API", and then clicking "Enable".
URL for it: https://console.cloud.google.com/apis/library/customsearch.googleapis
.com
"""


def _google_search_results(params) -> list[dict[str, Any]]:
    service = build("customsearch", "v1", developerKey=params['api_key'])
    res = service.cse().list(
        q=params['q'], cx=params['cse_id'], num=params['max_results']).execute()
    return res.get('items', [])


def search(query: str) -> str:
    params: dict = {
        "q": query,
        "cse_id": os.environ["GOOGLE_CSE_ID"],
        "api_key": os.environ["GOOGLE_API_KEY"],
        "max_results": 10
    }

    res = _google_search_results(params)
    snippets = []
    if len(res) == 0:
        return "No good Google Search Result was found"
    for result in res:
        if "snippet" in result:
            snippets.append(result["snippet"])

    return " ".join(snippets)


class GoogleSearchTool(ToolInterface):
    """Tool for Google search results."""

    name = "Google Search"
    description = "Get specific information from a search query. Input should be a question like 'How to add number in Clojure?'. Result will be the answer to the question."

    def use(self, input_text: str) -> str:
        return search(input_text)


if __name__ == '__main__':
    s = GoogleSearchTool()
    res = s.use("Who was the pope in 2023?")
    print(res)