import logging
import socket
from typing import Any

import aiohttp
import async_timeout

# Konfiguracja logowania
_LOGGER = logging.getLogger(__name__)

class IntegrationInstaApiClientError(Exception):
    """Exception to indicate a general API error."""


class IntegrationInstaApiClientCommunicationError(
    IntegrationInstaApiClientError,
):
    """Exception to indicate a communication error."""


class IntegrationInstaApiClientAuthenticationError(
    IntegrationInstaApiClientError,
):
    """Exception to indicate an authentication error."""


def _verify_response_or_raise(response: aiohttp.ClientResponse) -> None:
    """Verify that the response is valid."""
    if response.status in (401, 403):
        msg = "Invalid credentials"
        _LOGGER.error("Authentication failed: %s", msg)  # Log error
        raise IntegrationInstaApiClientAuthenticationError(
            msg,
        )
    response.raise_for_status()


class IntegrationInstaApiClient:
    """Sample API Client."""

    def __init__(
        self,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
    ) -> None:
        """Sample API Client."""
        self._username = username
        self._password = password
        self._session = session
        _LOGGER.info("API Client initialized for user: %s", username)  # Log

    async def async_get_data(self) -> Any:
        """Get data from the API."""
        _LOGGER.info("Fetching data from the API...")  # Logowanie try get data
        return await self._api_wrapper(
            method="get",
            url="https://jsonplaceholder.typicode.com/posts/1",
        )

    async def async_set_title(self, value: str) -> Any: # NOT USED
        """Set title in the API."""
        _LOGGER.info("Setting new title: %s", value)  
        return await self._api_wrapper(
            method="patch",
            url="https://jsonplaceholder.typicode.com/posts/1",
            data={"title": value},
            headers={"Content-type": "application/json; charset=UTF-8"},
        )
        
    async def async_get_followers(self) -> Any:
        """Get number of followers from Instagram."""
        _LOGGER.info("Fetching followers for user: %s", self._username)
        url = f"https://instagram-scraper-api2.p.rapidapi.com/v1/info?username_or_id_or_url={self._username}"

        headers = {
            'x-rapidapi-key': self._password,
            'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
        }

        # Call API method
        response_data = await self._api_wrapper(
            method="get",
            url=url,
            headers=headers,
        )

        # Get numbers
        follower_count = response_data["data"]["follower_count"]
        _LOGGER.info("User %s has %d followers", self._username, follower_count)
        return response_data        

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        """Get information from the API."""
        try:
            _LOGGER.info("Making %s request to %s", method.upper(), url)  # Log request
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                _verify_response_or_raise(response)
                _LOGGER.info("Received response: %s", response.status)  # Log answer
                response_data = await response.json()
                _LOGGER.info("Received response: %s", response_data)  # Log whole answer
                return response_data

        except TimeoutError as exception:
            msg = f"Timeout error fetching information - {exception}"
            _LOGGER.error(msg)  
            raise IntegrationInstaApiClientCommunicationError(
                msg,
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            msg = f"Error fetching information - {exception}"
            _LOGGER.error(msg)  
            raise IntegrationInstaApiClientCommunicationError(
                msg,
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            msg = f"Something really wrong happened! - {exception}"
            _LOGGER.error(msg)  
            raise IntegrationInstaApiClientError(
                msg,
            ) from exception
