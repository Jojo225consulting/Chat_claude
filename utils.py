"""
    Annex functions
"""


def output_format_viz(model,id_applicant, api_key, path, **kwargs):
    format_row = {
        "Api_key": api_key,
        "ID_applicant": id_applicant,
        "Proba utilisation IA": model.get("Proba_AI", None),
        "Connaissances financières": model.get("connaissances financières", None)[0],
        "Borne inf IC à 0.95 de CF": model.get("connaissances financières", None)[2][0] if len(model.get("connaissances financières")) == 3 else None,
        "Borne sup IC à 0.95 de CF": model.get("connaissances financières", None)[2][1] if len(model.get("connaissances financières")) == 3 else None,
        "Commentaire CF": model.get("connaissances financières", None)[1],
        "Conscienciosité": model.get("conscienciosité", None)[0],
        "Borne inf IC à 0.95 de Consc.": model.get("conscienciosité", None)[2][0] if len(model.get("conscienciosité")) == 3 else None,
        "Borne sup IC à 0.95 de Consc.": model.get("conscienciosité", None)[2][1] if len(model.get("conscienciosité")) == 3 else None,
        "Commentaire conscienciosité": model.get("conscienciosité", None)[1],
        "Neuroticisme": model.get("neuroticisme", None)[0],
        "Borne inf IC à 0.95 de Neur.": model.get("neuroticisme", None)[2][0] if len(model.get("neuroticisme")) == 3 else None,
        "Borne sup IC à 0.95 de Neur.": model.get("neuroticisme", None)[2][1] if len(model.get("neuroticisme")) == 3 else None,
        "Commentaire neuroticisme": model.get("neuroticisme", None)[1],
        "Nom du fichier": path
    }
    return format_row