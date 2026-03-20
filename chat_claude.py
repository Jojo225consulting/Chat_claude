import streamlit as st
import anthropic
import json
import os

def main():

    password = st.text_input("Entrez votre clé API Claude", type="password")

    uploaded_file = st.file_uploader("Choisissez un fichier JSON contenant les conversations", type=["json"])
    if uploaded_file is not None:
        st.write("Fichier uploadé :", uploaded_file.name)
    context = st.text_area("Entrez votre contexte ici", height=100)
    user_text = st.text_area("Entrez votre prompt ici", height=100)
    
    if st.button("Envoyer le prompt à Claude"):
        try:
            client = anthropic.Anthropic(api_key=password)
            if "new_historic" not in st.session_state:
                st.session_state["new_historic"] = {}
            if uploaded_file is not None:
                old_historic = []
                st.session_state["ID"] = []
                for conversation in json.load(uploaded_file):
                    current_chat = []
                    for message in conversation:
                        try:
                            st.session_state["ID"].append(message)
                            for mono in conversation[list(conversation.keys())[0]]:
                                role = mono["role"]
                                texte = mono["content"]
                                current_chat.append({f"{role}": f"{texte}"})
                                st.session_state["ID"].append(list(conversation.keys())[0])
                            
                        except KeyError:
                            pass
                            

                    old_historic.append(current_chat)
                for i,conv in enumerate(old_historic):
                    def_profil = """Le meilleur profil est celui d'un emprunteur discipliné, éclairé et émotionnellement stable. 
                    Il sait ce qu'il signe, honore ses échéances naturellement, et ne laisse pas un événement stressant (perte d'emploi, dépense imprévue) dérailler ses finances.
                    Le pire profil cumule trois fragilités qui se renforcent mutuellement : l'ignorance financière lui fait sous-estimer ses engagements, la faible conscienciosité l'empêche de les honorer même quand il le pourrait, et le névrosisme élevé amplifie les comportements contre-productifs dès qu'un choc survient. 
                    C'est la combinaison de ces trois facteurs — et non l'un d'eux isolément — qui rend le profil véritablement à risque."""
                    response = client.messages.create(
                        model = "claude-opus-4-6",
                        max_tokens = 4000,
                        system = context, #Tu est un analyste de profil client pour l'octroi de prêt bancaire. Tu as posé des questions à un client pour évaluer des scores sur 100 de 3 critères: \n" \
                        #"1. le niveau de connaissance financière du client \n" \
                        #"2. la consciencosité du client \n" \
                        #"3. le neuvrosisme du client" \
                        messages=[
                            {"role": "user", "content" : f"""{user_text} \n
                            Discussion ci-dessous: \n
                            {conv}!"""}
                        ]

                    )

                    
                    st.session_state["new_historic"][st.session_state["ID"][i]] =  {"user" : user_text ,
                                                           "model" : response.content[0].text} 
                st.write("Réponse de Claude :")
                st.write("Ce que contient votre historique :")
                st.write(st.session_state["new_historic"])
            
        except Exception as e:
            st.warning("Veuillez entrer votre clé API et un prompt avant d'envoyer.")
            st.error(f"Une erreur est survenue : {e}")

    try:
        json_string = json.dumps(dict(st.session_state["new_historic"]), ensure_ascii=False, indent=4)
        st.download_button(
            label="📥 Télécharger les réponses de Claude Ici",
            data=json_string,
            file_name="session_answers.json",
            mime="application/json"
        )
    except:
        pass
    # if st.button("Enregistrer l'historique du prompt"):


if __name__ == "__main__":
    main()
