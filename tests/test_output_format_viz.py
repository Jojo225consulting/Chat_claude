import pytest
from utils import output_format_viz
import json

# Structure attendue : clés exactes + types attendus
EXPECTED_STRUCTURE = {
        "api_key": str,
        "ID_applicant": str,
        "connaissances financières": int,
        "Borne inf IC à 0.95 de CF": (int,float, type(None)),
        "Borne sup IC à 0.95 de CF": (int,float, type(None)),
        "Commentaire CF" : str,
        "conscienciosité": int,
        "Borne inf IC à 0.95 de Consc.": (int,float, type(None)),
        "Borne sup IC à 0.95 de Consc.": (int,float, type(None)),
        "Commentaire conscienciosité": str,
        "neuroticisme": int,
        "Borne inf IC à 0.95 de Neur.": (int,float, type(None)),
        "Borne sup IC à 0.95 de Neur.": (int,float, type(None)),
        "Commentaire neuroticisme": str,
        "nom du fichier": str
    }

@pytest.fixture
def sample_inputs():
    json_file = {"Iyb": 
                    {"610081": 
                        {"user": "Instruction du User",
                        "model": "{\"connaissances financi\u00e8res\": [78, \"Le commentaire du score\", [65, 88]], \"conscienciosit\u00e9\": [62, \"Le commentaire du score\", [48, 75]], \"neuroticisme\": [25, \"Le commentaire du score\", [12, 40]]}"
                        }
                    }
                }
    data = json.dumps(json_file, ensure_ascii=False, indent=4)
    data = json.loads(data)
    for api_key in data.keys():
        for ID_applicant in data[api_key]:
            model = json.loads(data[api_key][ID_applicant]["model"])
            break
        break

    return model

def test_structure_clés(sample_inputs):
    """Les clés retournées correspondent exactement à la structure attendue."""
    result = output_format_viz(ID_applicant="ID_applicant", api_key="api_key", path="/path", model=sample_inputs)
    print(result)
    assert set(result.keys()) == set(EXPECTED_STRUCTURE.keys())

def test_structure_types(sample_inputs):
    """Chaque valeur est du bon type."""
    result = output_format_viz(ID_applicant="ID_applicant", api_key="api_key", path="/path", model=sample_inputs)
    for key, expected_type in EXPECTED_STRUCTURE.items():
        assert isinstance(result[key], expected_type), \
            f"{key!r} : type {type(result[key]).__name__!r} inattendu"

def test_pas_de_clés_inattendues(sample_inputs):
    """Aucune clé supplémentaire ne s'est glissée dans le retour."""
    result = output_format_viz(ID_applicant="ID_applicant", api_key="api_key", path="/path", model=sample_inputs)
    clés_inattendues = set(result.keys()) - set(EXPECTED_STRUCTURE.keys())
    assert not clés_inattendues, f"Clés inattendues : {clés_inattendues}"