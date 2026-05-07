"""
    this file contains all the tests for CI_CD
"""

import json
import pytest
from utils import output_format_viz



# Structure attendue : clés exactes + types attendus
EXPECTED_STRUCTURE = {
        "Api_key": str,
        "Id_applicant": str,
        "Connaissances financières": int,
        "Borne inf IC à 0.95 de CF": (int, float, type(None)),
        "Borne sup IC à 0.95 de CF": (int, float, type(None)),
        "Commentaire CF": str,
        "Conscienciosité": int,
        "Borne inf IC à 0.95 de Consc.": (int, float, type(None)),
        "Borne sup IC à 0.95 de Consc.": (int, float, type(None)),
        "Commentaire conscienciosité": str,
        "Neuroticisme": int,
        "Borne inf IC à 0.95 de Neur.": (int, float, type(None)),
        "Borne sup IC à 0.95 de Neur.": (int, float, type(None)),
        "Commentaire neuroticisme": str,
        "Nom du fichier": str
    }


@pytest.fixture
def sample_inputs():
    """
    creating sample inputs for the tests
    """
    json_file = {
                "Iyb": {
                        "610081": {
                                    "user": "Instruction du User",
                                    "model": (
                                        "{\"connaissances financi\u00e8res\": "
                                        "[78, \"Le commentaire du score\", [65, 88]],"
                                        "\"conscienciosit\u00e9\": [62, \"Le commentaire du score\", [48, 75]],"
                                        "\"neuroticisme\": [25, \"Le commentaire du score\", [12, 40]]}"
                                    )
                                }
                    }
                }
    data = json.dumps(json_file, ensure_ascii=False, indent=4)
    data = json.loads(data)
    for api_key in data.keys():
        for id_applicant in data[api_key]:
            model = json.loads(data[api_key][id_applicant]["model"])
            break
        break

    return model


def test_structure_cles(sample_inputs):
    """Les clés retournées correspondent exactement à la structure attendue."""
    result = output_format_viz(
                            id_applicant="id_applicant",
                            api_key="api_key",
                            path="/path",
                            model=sample_inputs)
    print(result)
    assert set(result.keys()) == set(EXPECTED_STRUCTURE.keys())


def test_structure_types(sample_inputs):
    """Chaque valeur est du bon type."""
    result = output_format_viz(
                            id_applicant="id_applicant",
                            api_key="api_key",
                            path="/path",
                            model=sample_inputs)
    for key, expected_type in EXPECTED_STRUCTURE.items():
        assert isinstance(result[key], expected_type), \
            f"{key!r} : type {type(result[key]).__name__!r} inattendu"


def test_pas_de_cles_inattendues(sample_inputs):
    """Aucune clé supplémentaire ne s'est glissée dans le retour."""
    result = output_format_viz(id_applicant="id_applicant", api_key="api_key", path="/path", model=sample_inputs)
    cles_inattendues = set(result.keys()) - set(EXPECTED_STRUCTURE.keys())
    assert not cles_inattendues, f"Clés inattendues : {cles_inattendues}"
