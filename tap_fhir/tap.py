"""FHIR tap class."""

from __future__ import annotations

import sys

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_fhir import streams

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class TapFHIR(Tap):
    """FHIR tap class."""

    name = "tap-fhir"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType(nullable=False),
            required=True,
            secret=True,  # Flag config as protected.
            title="Client ID",
            description="The Client ID to authenticate against the API service",
        ),
        th.Property(
            "client_secret",
            th.StringType(nullable=False),
            required=True,
            secret=True,  # Flag config as protected.
            title="Client Secret",
            description="The Client Secret to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType(nullable=True),
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType(nullable=False),
            title="API URL",
            default="https://api.mysample.com",
            description="The url for the API service",
        ),
        th.Property(
            "user_agent",
            th.StringType(nullable=True),
            description=(
                "A custom User-Agent header to send with each request. Default is "
                "'<tap_name>/<tap_version>'"
            ),
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[streams.FHIRStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.EncounterStream(self),
        ]


if __name__ == "__main__":
    TapFHIR.cli()
