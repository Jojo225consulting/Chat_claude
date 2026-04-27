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
                ID_applicant = []
                for conversation in json.load(uploaded_file):
                    current_chat = []
                    for key in conversation:# key correspond à l'ID de la conversation
                        try:
                            st.session_state["ID"].append(key)
                            for mono in conversation[key]:
                                role = mono["role"]
                                texte = mono["content"]
                                current_chat.append({f"{role}": f"{texte}"})

                            
                        except KeyError:
                            pass
                            
                    old_historic.append(current_chat)

                for i,conv in enumerate(old_historic):
                    response = client.messages.create(
                        model = "claude-opus-4-6",
                        max_tokens = 4000,
                        system = context, 
                        messages=[
                            {"role": "user", "content" : f"""{user_text} \n
                            Historique de la discussion: \n
                            {conv}!"""}
                        ]

                    )          
                    st.session_state["new_historic"][st.session_state["ID"][i]] =  {"user" : context + " \n \n " + user_text ,
                                                           "model" : response.content[0].text} 
                st.write("Réponse de Claude :")
                st.write("Ce que contient votre historique :")
                st.write(st.session_state["new_historic"])
            
        except Exception as e:
            st.warning("Veuillez entrer votre clé API et un prompt avant d'envoyer.")
            st.error(f"Une erreur est survenue : {e}")

    try:
        json_string = json.dumps(dict( {str(password)[-7:] : st.session_state["new_historic"]} ), ensure_ascii=False, indent=4)
        st.download_button(
            label="📥 Télécharger les réponses de Claude Ici",
            data=json_string,
            file_name="session_answers.json",
            mime="application/json"
        )
    except:
        pass


if __name__ == "__main__":
    main()
