def custom_in(value, l1):
    return any(check_if_names_are_equal(value, x) for x in l1)


def check_if_names_are_equal(name_source1, name_source2):
    if SCI_CLUBS_NAMES_ALIASES.get(name_source2.lower().strip(), None) == name_source1.lower():
        return True

    def remove_substrings(string):
        for substring in substrings:
            string = string.replace(substring, "")
        return string.strip()

    substrings = [
        "studenckie koło naukowe technologów chemicznych",
        "koło naukowe projektantów chemicznych ",
        "stowarzyszenie naukowe studentów ",
        "studenckie koło naukowe ",
        "koło naukowe studentów ",
        "knpc ",
        "skntch ",
        "koło naukowe ",
        "skn ",
        "sns ",
        "kn ",
        '"',
    ]

    n1 = remove_substrings(name_source1.lower())
    n2 = remove_substrings(name_source2.lower())
    return n1 == n2


SCI_CLUBS_NAMES_ALIASES = {
    "biomedical ai": "biomedical al",
    "projekt scorpio": "koło naukowe pojazdów niekonwencjonalnych off-road",
    "pmg (project management group)": "project management group - pmgroup",
    "ase pwr": "akademickie stowarzyszenie e-sportowe",
    "gdsc google developer student club": "google developers student club",
    "kn kredek": "kredek - creation and development group",
    "akademicki chór politechniki wrocławskiej (achpwr)": "akademicki chór politechniki wrocławskiej",
    "iaeste politechnika wrocławska": "komitet lokalny iaeste przy politechnice wrocławskiej",
    "aquae ductus": "koło naukowe aque ductus",
    "przewrotka": "klub kajakowy przewrotka",
    "rekiny jakości": "studenckie koło naukowe zarządzania jakością rekiny jakości",
    "allin": "koło naukowe studentów chemii „allin”",
    "telewizja studencka styk": "telewizja studencka politechniki wrocławskiej styk",
    "m3": 'koło naukowe mikroinżynierii, mikroelektroniki i mikrosystemów "m3"',
    "konar": "koło naukowe robotyków konar",
    "habitat now studenckie koło naukowe": "koło naukowe habitat now!",
    "ks giuoco piano": "koło szachowe giuoco piano",
    "koło naukowe newway": 'koło naukowe inżynierii materiałów i procesów budowlanych "newway"',
    "thermores": "studenckie kolo naukowe thermores",
    "sknu cardo": "studenckie koło naukowe urbanistyki cardo",
    "debatelab": "koło naukowe debate lab",
    "esn politechnika wrocławska (esn pwr)": "esn politechnika wrocławska",
    'koło naukowe mechatroniki i robotyki "synergia"': "koło naukowe mechatroniki i robotyki „synergia”",
    "photonics and bionanotechnology association 'phobia'": "międzywydziałowe koło naukowe photonics and bionanotechnology association phobia",
    "spaf": "stowarzyszenie para artystycznej fotografii spaf",
    "humanizacja środowiska miejskiego (hśm)": "koło naukowe humanizacja środowiska miejskiego",
    "lem wrocław motorsport": "koło naukowe pojazdów i robotów mobilnych",
    "sktt iskra pwr": "studencki klub tańca towarzyskiego iskra",
    "akademickie stowarzyszenie informatyczne - asi": "akademickie stowarzyszenie informatyczne (asi)",
    "skt": "studencki klub turystyczny",
    "audio engineering society wrocław student section": "studenckie koło naukowe polskiej sekcji audio engineering society",
    "koło naukowe obrabiarek sterowanych numerycznie": "koło naukowe obrabiarek sterowanych numerycznie (osn)",
    "koło naukowo-badawcze gis im. dr józefa woźniaka": "koło naukowo-badawcze gis",
    "sns automatyk pwr": "stowarzyszenie naukowe studentów automatyk",
}
