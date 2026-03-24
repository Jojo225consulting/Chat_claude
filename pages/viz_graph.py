import pygwalker as pyg
import streamlit.components.v1 as components
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm, get_streamlit_html
import streamlit as st
import pandas as pd
import numpy as np
import json

st.set_page_config(
    layout="wide"
)

uploaded_file = st.file_uploader("Ajouter des données supplémentaires", type=["json"])
text_detail = st.text_area("Saisissez un détail pour caractériser ce fichier, les résultats/prompts, de façon unique(par exemple: prompt_v1_23_03_2026)", height=30)

rows = []

def adding_rows(path: str, detail: str):
    global rows
    with open(path, "r", encoding="utf-8") as f: # path du dossier contenant tout le projet
        data = json.load(f)
    for api_key in data.keys():
        for ID_applicant in data[api_key]:
            rows.append({
                    "api_key": api_key,
                    "ID_applicant": ID_applicant,
                    "connaissances financières": json.loads(data[api_key][ID_applicant]["model"])["connaissances financières"][0],
                    "conscienciosité": json.loads(data[api_key][ID_applicant]["model"])["conscienciosité"][0],
                    "neuroticisme": json.loads(data[api_key][ID_applicant]["model"])["neuroticisme"][0],
                    "Commentaire CF": json.loads(data[api_key][ID_applicant]["model"])["connaissances financières"][1],
                    "Commentaire conscienciosité": json.loads(data[api_key][ID_applicant]["model"])["conscienciosité"][1],
                    "Commentaire neuroticisme": json.loads(data[api_key][ID_applicant]["model"])["neuroticisme"][1],
                    "détails": detail
                })

try:
    if st.button("Ajouter le fichier"):
        if uploaded_file is not None:
            st.write("Fichier uploadé :", uploaded_file.name)
            if text_detail is in [None, ""," ", "  ", "    " ]:
                st.write("Associez un détail au fichier à ajouter (par exemple: prompt_v1_23_03_2026)")
            else:
                data = json.load(uploaded_file)
                for api_key in data.keys():
                    for ID_applicant in data[api_key]:
                        rows.append({
                                "api_key": api_key,
                                "ID_applicant": ID_applicant,
                                "connaissances financières": json.loads(data[api_key][ID_applicant]["model"])["connaissances financières"][0],
                                "conscienciosité": json.loads(data[api_key][ID_applicant]["model"])["conscienciosité"][0],
                                "neuroticisme": json.loads(data[api_key][ID_applicant]["model"])["neuroticisme"][0],
                                "Commentaire CF": json.loads(data[api_key][ID_applicant]["model"])["connaissances financières"][1],
                                "Commentaire conscienciosité": json.loads(data[api_key][ID_applicant]["model"])["conscienciosité"][1],
                                "Commentaire neuroticisme": json.loads(data[api_key][ID_applicant]["model"])["neuroticisme"][1],
                                "détails": detail
                            })
                
except KeyError:
    st.write("Le format de votre fichier json n'est pas le format adéquat")
    


adding_rows(path = "session_answers_bank_conversation.json", detail="prompt_v1_22032026")
# adding_rows(path = "session_answers_bank_conversation.json", detail="prompt_v2_22032026_test")

df = pd.DataFrame(rows)

# init_streamlit_comm()

vis_spec = vis_spec = vis_spec = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["line"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"connaissances financières","name":"connaissances financières","basename":"connaissances financières","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"conscienciosité","name":"conscienciosité","basename":"conscienciosité","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"neuroticisme","name":"neuroticisme","basename":"neuroticisme","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"Commentaire CF","name":"Commentaire CF","basename":"Commentaire CF","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire conscienciosité","name":"Commentaire conscienciosité","basename":"Commentaire conscienciosité","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire neuroticisme","name":"Commentaire neuroticisme","basename":"Commentaire neuroticisme","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"connaissances financières","name":"connaissances financières","basename":"connaissances financières","semanticType":"quantitative","analyticType":"dimension","offset":0}],"columns":[{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0}],"color":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"renderer":"vega-lite"},"visId":"gw_mB7U","name":"Connaissances financières"},{"config":{"defaultAggregated":true,"geoms":["line"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"connaissances financières","name":"connaissances financières","basename":"connaissances financières","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"conscienciosité","name":"conscienciosité","basename":"conscienciosité","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"neuroticisme","name":"neuroticisme","basename":"neuroticisme","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"Commentaire CF","name":"Commentaire CF","basename":"Commentaire CF","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire conscienciosité","name":"Commentaire conscienciosité","basename":"Commentaire conscienciosité","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire neuroticisme","name":"Commentaire neuroticisme","basename":"Commentaire neuroticisme","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"conscienciosité","name":"conscienciosité","basename":"conscienciosité","semanticType":"quantitative","analyticType":"dimension","offset":0}],"columns":[{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0}],"color":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"renderer":"vega-lite"},"visId":"gw_bhnU","name":"Conscienciosité"},{"config":{"defaultAggregated":true,"geoms":["line"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"connaissances financières","name":"connaissances financières","basename":"connaissances financières","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"conscienciosité","name":"conscienciosité","basename":"conscienciosité","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"neuroticisme","name":"neuroticisme","basename":"neuroticisme","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"Commentaire CF","name":"Commentaire CF","basename":"Commentaire CF","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire conscienciosité","name":"Commentaire conscienciosité","basename":"Commentaire conscienciosité","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Commentaire neuroticisme","name":"Commentaire neuroticisme","basename":"Commentaire neuroticisme","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"neuroticisme","name":"neuroticisme","basename":"neuroticisme","semanticType":"quantitative","analyticType":"dimension","offset":0}],"columns":[{"fid":"ID_applicant","name":"ID_applicant","basename":"ID_applicant","semanticType":"nominal","analyticType":"dimension","offset":0}],"color":[{"fid":"api_key","name":"api_key","basename":"api_key","semanticType":"nominal","analyticType":"dimension","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"renderer":"vega-lite"},"visId":"gw_29LZ","name":"Neuroticisme"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["ID_applicant","connaissances financières","api_key"],"measures":[]}]}]},{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["ID_applicant","conscienciosité","api_key"],"measures":[]}]}]},{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["ID_applicant","neuroticisme","api_key"],"measures":[]}]}]}],"version":"0.5.0.0"}"""

# vis_spec_dict = json.loads(vis_spec)

html = get_streamlit_html(df, spec=vis_spec)

components.html(html, height=1000)
