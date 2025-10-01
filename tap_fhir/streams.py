"""Stream type classes for tap-fhir."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_fhir.client import FHIRStream

class EncounterStream(FHIRStream):
    """Define custom stream."""

    name = "Encounter"
    path = "/s2s/Encounter"
    schema = {}

class GroupsStream(FHIRStream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
