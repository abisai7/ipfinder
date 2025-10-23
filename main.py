import datetime

import streamlit as st

import requests
from requests.exceptions import RequestException

st.set_page_config(page_title="Public IP — IP pública", page_icon="🌐")

TRANSLATIONS = {
    "es": {
        "app_title": "Mostrar IP pública",
        "description": "Esta pequeña app consulta tu IP pública usando api.ipify.org",
        "refresh": "Refrescar",
        "spinner": "Obteniendo IP pública...",
        "success": "IP encontrada",
        "last_check": "Última comprobación:",
        "select_copy_info": "Puedes seleccionar la IP (clic sobre ella) y copiarla al portapapeles.",
        "error_fetch": "No se pudo obtener la IP pública. Revisa tu conexión a Internet o prueba de nuevo.",
        "error_hint": "Si el problema persiste, intenta abrir https://api.ipify.org desde el navegador para verificar la accesibilidad.",
        "language_label": "Idioma",
        "language_options": "Español",
    },
    "en": {
        "app_title": "Show public IP",
        "description": "This small app fetches your public IP using api.ipify.org",
        "refresh": "Refresh",
        "spinner": "Getting public IP...",
        "success": "IP found",
        "last_check": "Last check:",
        "select_copy_info": "You can select the IP (click it) and copy it to the clipboard.",
        "error_fetch": "Could not obtain the public IP. Check your internet connection or try again.",
        "error_hint": "If the problem persists, try opening https://api.ipify.org in your browser to verify accessibility.",
        "language_label": "Language",
        "language_options": "English",
    },
    "pt": {
        "app_title": "Mostrar IP pública",
        "description": "Este pequeno app consulta seu IP público usando api.ipify.org",
        "refresh": "Atualizar",
        "spinner": "Obtendo IP público...",
        "success": "IP encontrada",
        "last_check": "Última verificação:",
        "select_copy_info": "Você pode selecionar o IP (clique nele) e copiá-lo para a área de transferência.",
        "error_fetch": "Não foi possível obter o IP público. Verifique sua conexão com a Internet ou tente novamente.",
        "error_hint": "Se o problema persistir, tente abrir https://api.ipify.org no navegador para verificar a acessibilidade.",
        "language_label": "Idioma",
        "language_options": "Português",
    },
}


@st.cache_data(ttl=60)
def fetch_public_ip() -> str | None:
    """ Returns the public IP address as a string,
        or None if it cannot be fetched.
    """
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data.get("ip")
    except RequestException:
        return None


def main() -> None:
    # Language selection
    lang_map = {"Español": "es", "English": "en", "Português": "pt"}

    lang_choice = st.sidebar.selectbox(
        "Idioma / Language / Idioma",
        ("English", "Español", "Português"),
        index=0,
    )
    lang = lang_map.get(lang_choice, "en")

    def t(key: str) -> str:
        return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)

    st.title(t("app_title"))
    st.write(t("description"))

    col1, col2 = st.columns([1, 7])

    with col1:
        if st.button(t("refresh")):
            fetch_public_ip.clear()

    with st.spinner(t("spinner")):
        ip = fetch_public_ip()

    if ip:
        st.success(t("success"))
        st.code(ip, language=None)
        st.markdown(f"**{t('last_check')}** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.info(t("select_copy_info"))
    else:
        st.error(t("error_fetch"))
        st.markdown(t("error_hint"))


if __name__ == '__main__':
    main()
