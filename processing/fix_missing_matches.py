def custom_in(value, l1):
    return any(check_if_names_are_equal(value, x) for x in l1)


def check_if_names_are_equal(name_source1, name_source2):
    def remove_substrings(string):
        for substring in substrings:
            string = string.replace(substring, "")
        return string.strip()

    substrings = ['studenckie koło naukowe technologów chemicznych', 'koło naukowe projektantów chemicznych ',
                  'stowarzyszenie naukowe studentów ',
                  'studenckie koło naukowe ', 'koło naukowe studentów ', 'knpc ', 'skntch ', 'koło naukowe ', 'skn ',
                  'sns ',
                  'kn ', "\""]

    n1 = remove_substrings(name_source1.lower())
    n2 = remove_substrings(name_source2.lower())

    return n1 == n2 or SCI_CLUBS_NAMES_ALIASES.get(name_source1.strip(), None) == name_source2


SCI_CLUBS_NAMES_ALIASES = {
    "Biomedical AI": "BioMedical Al",
    "Projekt Scorpio": "Koło Naukowe Pojazdów Niekonwencjonalnych OFF-ROAD",
    "PMG (Project Management Group)": "Project Management Group - PMGroup",
    "ASE PWr": "Akademickie Stowarzyszenie E-sportowe",
    "GDSC Google Developer Student Club": "Google Developers Student Club",
    "KN Kredek": "Kredek - Creation and Development Group",
    "Akademicki Chór Politechniki Wrocławskiej (AChPWr)": "Akademicki Chór Politechniki Wrocławskiej",
    "IAESTE Politechnika Wrocławska": "Komitet Lokalny IAESTE przy Politechnice Wrocławskiej",
    'Aquae Ductus': 'Koło Naukowe AQUE DUCTUS',
    'PrzeWrotka': 'Klub Kajakowy przeWrotka',
    'Rekiny Jakości': 'Studenckie Koło Naukowe Zarządzania Jakością REKINY JAKOŚCI',
    'ALLIN': 'Koło Naukowe Studentów Chemii „Allin”',
    'Telewizja Studencka Styk': 'Telewizja Studencka Politechniki Wrocławskiej STYK',
    'M3': 'Koło Naukowe Mikroinżynierii, Mikroelektroniki i Mikrosystemów "M3"',
    'KoNaR': 'Koło Naukowe Robotyków KoNaR',
    'Habitat NOW Studenckie Koło Naukowe': 'Koło Naukowe Habitat NOW!',
    'KS Giuoco Piano': 'Koło Szachowe Giuoco Piano',
    'Koło Naukowe NewWay': 'Koło Naukowe Inżynierii Materiałów i Procesów Budowlanych "NEWWAY"',
    'ThermoRES': 'Studenckie Kolo Naukowe ThermoRES',
    'SKNU CARDO': 'Studenckie Koło Naukowe Urbanistyki CARDO',
    'DebateLab': 'Koło Naukowe Debate Lab',
    'ESN Politechnika Wrocławska (ESN PWr)': 'ESN Politechnika Wrocławska',
    'Koło Naukowe Mechatroniki i Robotyki "Synergia"': 'Koło Naukowe Mechatroniki i Robotyki „Synergia”',
    "Photonics and Bionanotechnology Association 'PhoBiA'": "Międzywydziałowe Koło Naukowe Photonics and Bionanotechnology Association PhoBiA",
    'SpAF': 'Stowarzyszenie para Artystycznej Fotografii SpAF',
    "Humanizacja Środowiska Miejskiego (HŚM)": "Koło Naukowe Humanizacja Środowiska Miejskiego",
    "LEM Wrocław Motorsport": "Koło Naukowe Pojazdów i Robotów Mobilnych",
    'SKTT Iskra PWr': "Studencki Klub Tańca Towarzyskiego ISKRA",
    'Akademickie Stowarzyszenie Informatyczne - ASI': "Akademickie Stowarzyszenie Informatyczne (ASI)",
    'SKT': "Studencki Klub Turystyczny",
    'Audio Engineering Society Wrocław Student Section': "Studenckie Koło Naukowe Polskiej Sekcji Audio Engineering Society",
    'Koło Naukowe Obrabiarek Sterowanych Numerycznie': "Koło Naukowe Obrabiarek Sterowanych Numerycznie (OSN)",
    'Koło Naukowo-Badawcze GIS im. dr Józefa Woźniaka': "Koło Naukowo-Badawcze GIS",
    'SNS Automatyk PWr': "Stowarzyszenie Naukowe Studentów AUTOMATYK",
}
