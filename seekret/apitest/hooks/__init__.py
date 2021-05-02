from box import Box
from requests import Response


def pytest_tavern_beta_before_every_request(request_args: Box):
    """
    Log the outgoing request.

    :note: This is a hook function intended to be imported in a conftest.py file in the tavern test directory.
    """

    print(f'---> Making request to {request_args.url}')


def pytest_tavern_beta_after_every_response(expected, response: Response):
    """
    Log the incoming response.

    :note: This is a hook function intended to be imported in a conftest.py file in the tavern test directory.
    """

    print(f'<--- Got response {response.status_code} from {response.url}: {response.reason}')