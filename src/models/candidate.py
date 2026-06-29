"""
candidate.py

Defines the canonical Candidate model used across the TalentFusion pipeline.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Candidate:
    """
    Canonical Candidate Profile
    """

    candidate_id: str = ""

    full_name: str = ""

    emails: List[str] = field(default_factory=list)

    phones: List[str] = field(default_factory=list)

    location: str = ""

    links: List[str] = field(default_factory=list)

    headline: str = ""

    years_experience: float = 0.0

    skills: List[str] = field(default_factory=list)

    experience: List[Dict[str, Any]] = field(default_factory=list)

    education: List[Dict[str, Any]] = field(default_factory=list)

    provenance: Dict[str, Any] = field(default_factory=dict)

    overall_confidence: float = 0.0