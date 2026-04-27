def output_format_viz(model,ID_applicant, api_key, path):
    format_row = {
        "api_key": api_key,
        "ID_applicant": ID_applicant,
        "connaissances financières": model.get("connaissances financières", None)[0],
        "Borne inf IC à 0.95 de CF": model.get("connaissances financières", None)[2][0] if len(model.get("connaissances financières")) == 3 else None,
        "Borne sup IC à 0.95 de CF": model.get("connaissances financières", None)[2][1] if len(model.get("connaissances financières")) == 3 else None,
        "Commentaire CF": model.get("connaissances financières", None)[1],
        "conscienciosité": model.get("conscienciosité", None)[0],
        "Borne inf IC à 0.95 de Consc.": model.get("conscienciosité", None)[2][0] if len(model.get("conscienciosité")) == 3 else None,
        "Borne sup IC à 0.95 de Consc.": model.get("conscienciosité", None)[2][1] if len(model.get("conscienciosité")) == 3 else None,
        "Commentaire conscienciosité": model.get("conscienciosité", None)[1],
        "neuroticisme": model.get("neuroticisme", None)[0],
        "Borne inf IC à 0.95 de Neur.": model.get("neuroticisme", None)[2][0] if len(model.get("neuroticisme")) == 3 else None,
        "Borne sup IC à 0.95 de Neur.": model.get("neuroticisme", None)[2][1] if len(model.get("neuroticisme")) == 3 else None,
        "Commentaire neuroticisme": model.get("neuroticisme", None)[1],
        "nom du fichier": path
    }
    return format_row