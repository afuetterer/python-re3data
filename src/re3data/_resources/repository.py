# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""API resources for the /repository{repository_id} endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlPeriod

from re3data._resources.mixins import IdMixin

__NAMESPACE__ = "http://www.re3data.org/schema/2-2"


class AccessRestrictions(Enum):
    FEE_REQUIRED = "feeRequired"
    REGISTRATION = "registration"
    OTHER = "other"


class AccessTypes(Enum):
    OPEN = "open"
    RESTRICTED = "restricted"
    CLOSED = "closed"


class AidSystems(Enum):
    AUTHOR_CLAIM = "AuthorClaim"
    ISNI = "ISNI"
    ORCID = "ORCID"
    RESEARCHER_ID = "ResearcherID"
    OTHER = "other"
    NONE = "none"


class ApiTypes(Enum):
    FTP = "FTP"
    NET_CDF = "NetCDF"
    OAI_PMH = "OAI-PMH"
    OPEN_DAP = "OpenDAP"
    REST = "REST"
    SOAP = "SOAP"
    SPARQL = "SPARQL"
    SWORD = "SWORD"
    OTHER = "other"


class Certificates(Enum):
    CLARIN_CERTIFICATE_B = "CLARIN certificate B"
    DIN_31644 = "DIN 31644"
    DINI_CERTIFICATE = "DINI Certificate"
    DRAMBORA = "DRAMBORA"
    DSA = "DSA"
    ISO_16363 = "ISO 16363"
    ISO_16919 = "ISO 16919"
    RAT_SWD = "RatSWD"
    TRAC = "TRAC"
    TRUSTED_DIGITAL_REPOSITORY = "Trusted Digital Repository"
    WDS = "WDS"
    OTHER = "other"


class ContentTypeText(Enum):
    STANDARD_OFFICE_DOCUMENTS = "Standard office documents"
    NETWORKBASED_DATA = "Networkbased data"
    DATABASES = "Databases"
    IMAGES = "Images"
    STRUCTURED_GRAPHICS = "Structured graphics"
    AUDIOVISUAL_DATA = "Audiovisual data"
    SCIENTIFIC_AND_STATISTICAL_DATA_FORMATS = "Scientific and statistical data formats"
    RAW_DATA = "Raw data"
    PLAIN_TEXT = "Plain text"
    STRUCTURED_TEXT = "Structured text"
    ARCHIVED_DATA = "Archived data"
    SOFTWARE_APPLICATIONS = "Software applications"
    SOURCE_CODE = "Source code"
    CONFIGURATION_DATA = "Configuration data"
    OTHER = "other"


class Countries(Enum):
    """Attributes:
    ABW: Aruba
    AFG: Afghanistan
    AGO: Angola
    AIA: Anguilla
    ALA: Aland Islands
    ALB: Albania
    AND: Andorra
    ARE: United Arab Emirates
    ARG: Argentina
    ARM: Armenia
    ASM: American Samoa
    ATA: Antarctica
    ATF: French Southern Territories
    ATG: Antigua and Barbuda
    AUS: Australia
    AUT: Austria
    AZE: Azerbaijan
    BDI: Burundi
    BEL: Belgium
    BEN: Benin
    BES: Bonaire, Sint Eustatius and Saba
    BFA: Burkina Faso
    BGD: Bangladesh
    BGR: Bulgaria
    BHR: Bahrain
    BHS: Bahamas
    BIH: Bosnia and Herzegovina
    BLM: Saint Barthelemy
    BLR: Belarus
    BLZ: Belize
    BMU: Bermuda
    BOL: Bolivia, Plurinational State of
    BRA: Brazil
    BRB: Barbados
    BRN: Brunei Darussalam
    BTN: Bhutan
    BVT: Bouvet Island
    BWA: Botswana
    CAF: Central African Republic
    CAN: Canada
    CCK: Cocos (Keeling) Islands
    CHE: Switzerland
    CHL: Chile
    CHN: China
    CIV: Cote d'Ivoire
    CMR: Cameroon
    COD: Congo, the Democratic Republic of the
    COG: Congo
    COK: Cook Islands
    COL: Colombia
    COM: Comoros
    CPV: Cape Verde
    CRI: Costa Rica
    CUB: Cuba
    CUW: Curacao
    CXR: Christmas Island
    CYM: Cayman Islands
    CYP: Cyprus
    CZE: Czech Republic
    DEU: Germany
    DJI: Djibouti
    DMA: Dominica
    DNK: Denmark
    DOM: Dominican Republic
    DZA: Algeria
    ECU: Ecuador
    EGY: Egypt
    ERI: Eritrea
    ESH: Western Sahara
    ESP: Spain
    EST: Estonia
    ETH: Ethiopia
    FIN: Finland
    FJI: Fiji
    FLK: Falkland Islands (Malvinas)
    FRA: France
    FRO: Faroe Islands
    FSM: Micronesia, Federated States of
    GAB: Gabon
    GBR: United Kingdom
    GEO: Georgia
    GGY: Guernsey
    GHA: Ghana
    GIB: Gibraltar
    GIN: Guinea
    GLP: Guadeloupe
    GMB: Gambia
    GNB: Guinea-Bissau
    GNQ: Equatorial Guinea
    GRC: Greece
    GRD: Grenada
    GRL: Greenland
    GTM: Guatemala
    GUF: French Guiana
    GUM: Guam
    GUY: Guyana
    HKG: Hong Kong
    HMD: Heard Island and McDonald Islands
    HND: Honduras
    HRV: Croatia
    HTI: Haiti
    HUN: Hungary
    IDN: Indonesia
    IMN: Isle of Man
    IND: India
    IOT: British Indian Ocean Territory
    IRL: Ireland
    IRN: Iran, Islamic Republic of
    IRQ: Iraq
    ISL: Iceland
    ISR: Israel
    ITA: Italy
    JAM: Jamaica
    JEY: Jersey
    JOR: Jordan
    JPN: Japan
    KAZ: Kazakhstan
    KEN: Kenya
    KGZ: Kyrgyzstan
    KHM: Cambodia
    KIR: Kiribati
    KNA: Saint Kitts and Nevis
    KOR: Korea, Republic of
    KWT: Kuwait
    LAO: Lao People's Democratic Republic
    LBN: Lebanon
    LBR: Liberia
    LBY: Libya
    LCA: Saint Lucia
    LIE: Liechtenstein
    LKA: Sri Lanka
    LSO: Lesotho
    LTU: Lithuania
    LUX: Luxembourg
    LVA: Latvia
    MAC: Macao
    MAF: Saint Martin (French part)
    MAR: Morocco
    MCO: Monaco
    MDA: Moldova, Republic of
    MDG: Madagascar
    MDV: Maldives
    MEX: Mexico
    MHL: Marshall Islands
    MKD: Macedonia, the former Yugoslav Republic of
    MLI: Mali
    MLT: Malta
    MMR: Myanmar
    MNE: Montenegro
    MNG: Mongolia
    MNP: Northern Mariana Islands
    MOZ: Mozambique
    MRT: Mauritania
    MSR: Montserrat
    MTQ: Martinique
    MUS: Mauritius
    MWI: Malawi
    MYS: Malaysia
    MYT: Mayotte
    NAM: Namibia
    NCL: New Caledonia
    NER: Niger
    NFK: Norfolk Island
    NGA: Nigeria
    NIC: Nicaragua
    NIU: Niue
    NLD: Netherlands
    NOR: Norway
    NPL: Nepal
    NRU: Nauru
    NZL: New Zealand
    OMN: Oman
    PAK: Pakistan
    PAN: Panama
    PCN: Pitcairn
    PER: Peru
    PHL: Philippines
    PLW: Palau
    PNG: Papua New Guinea
    POL: Poland
    PRI: Puerto Rico
    PRK: Korea, Democratic People's Republic of
    PRT: Portugal
    PRY: Paraguay
    PSE: Palestinian Territory, Occupied
    PYF: French Polynesia
    QAT: Qatar
    REU: Reunion
    ROU: Romania
    RUS: Russian Federation
    RWA: Rwanda
    SAU: Saudi Arabia
    SDN: Sudan
    SEN: Senegal
    SGP: Singapore
    SGS: South Georgia and the South Sandwich Islands
    SHN: Saint Helena, Ascension and Tristan da Cunha
    SJM: Svalbard and Jan Mayen
    SLB: Solomon Islands
    SLE: Sierra Leone
    SLV: El Salvador
    SMR: San Marino
    SOM: Somalia
    SPM: Saint Pierre and Miquelon
    SRB: Serbia
    SSD: South Sudan
    STP: Sao Tome and Principe
    SUR: Suriname
    SVK: Slovakia
    SVN: Slovenia
    SWE: Sweden
    SWZ: Swaziland
    SXM: Sint Maarten (Dutch part)
    SYC: Seychelles
    SYR: Syrian Arab Republic
    TCA: Turks and Caicos Islands
    TCD: Chad
    TGO: Togo
    THA: Thailand
    TJK: Tajikistan
    TKL: Tokelau
    TKM: Turkmenistan
    TLS: Timor-Leste
    TON: Tonga
    TTO: Trinidad and Tobago
    TUN: Tunisia
    TUR: Turkey
    TUV: Tuvalu
    TWN: Taiwan, Province of China
    TZA: Tanzania, United Republic of
    UGA: Uganda
    UKR: Ukraine
    UMI: United States Minor Outlying Islands
    URY: Uruguay
    USA: United States
    UZB: Uzbekistan
    VAT: Holy See (Vatican City State)
    VCT: Saint Vincent and the Grenadines
    VEN: Venezuela, Bolivarian Republic of
    VGB: Virgin Islands, British
    VIR: Virgin Islands, U.S.
    VNM: Viet Nam
    VUT: Vanuatu
    WLF: Wallis and Futuna
    WSM: Samoa
    YEM: Yemen
    ZAF: South Africa
    ZMB: Zambia
    ZWE: Zimbabwe
    EEC: European Union
    AAA: International
    """

    ABW = "ABW"
    AFG = "AFG"
    AGO = "AGO"
    AIA = "AIA"
    ALA = "ALA"
    ALB = "ALB"
    AND = "AND"
    ARE = "ARE"
    ARG = "ARG"
    ARM = "ARM"
    ASM = "ASM"
    ATA = "ATA"
    ATF = "ATF"
    ATG = "ATG"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BDI = "BDI"
    BEL = "BEL"
    BEN = "BEN"
    BES = "BES"
    BFA = "BFA"
    BGD = "BGD"
    BGR = "BGR"
    BHR = "BHR"
    BHS = "BHS"
    BIH = "BIH"
    BLM = "BLM"
    BLR = "BLR"
    BLZ = "BLZ"
    BMU = "BMU"
    BOL = "BOL"
    BRA = "BRA"
    BRB = "BRB"
    BRN = "BRN"
    BTN = "BTN"
    BVT = "BVT"
    BWA = "BWA"
    CAF = "CAF"
    CAN = "CAN"
    CCK = "CCK"
    CHE = "CHE"
    CHL = "CHL"
    CHN = "CHN"
    CIV = "CIV"
    CMR = "CMR"
    COD = "COD"
    COG = "COG"
    COK = "COK"
    COL = "COL"
    COM = "COM"
    CPV = "CPV"
    CRI = "CRI"
    CUB = "CUB"
    CUW = "CUW"
    CXR = "CXR"
    CYM = "CYM"
    CYP = "CYP"
    CZE = "CZE"
    DEU = "DEU"
    DJI = "DJI"
    DMA = "DMA"
    DNK = "DNK"
    DOM = "DOM"
    DZA = "DZA"
    ECU = "ECU"
    EGY = "EGY"
    ERI = "ERI"
    ESH = "ESH"
    ESP = "ESP"
    EST = "EST"
    ETH = "ETH"
    FIN = "FIN"
    FJI = "FJI"
    FLK = "FLK"
    FRA = "FRA"
    FRO = "FRO"
    FSM = "FSM"
    GAB = "GAB"
    GBR = "GBR"
    GEO = "GEO"
    GGY = "GGY"
    GHA = "GHA"
    GIB = "GIB"
    GIN = "GIN"
    GLP = "GLP"
    GMB = "GMB"
    GNB = "GNB"
    GNQ = "GNQ"
    GRC = "GRC"
    GRD = "GRD"
    GRL = "GRL"
    GTM = "GTM"
    GUF = "GUF"
    GUM = "GUM"
    GUY = "GUY"
    HKG = "HKG"
    HMD = "HMD"
    HND = "HND"
    HRV = "HRV"
    HTI = "HTI"
    HUN = "HUN"
    IDN = "IDN"
    IMN = "IMN"
    IND = "IND"
    IOT = "IOT"
    IRL = "IRL"
    IRN = "IRN"
    IRQ = "IRQ"
    ISL = "ISL"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JEY = "JEY"
    JOR = "JOR"
    JPN = "JPN"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KHM = "KHM"
    KIR = "KIR"
    KNA = "KNA"
    KOR = "KOR"
    KWT = "KWT"
    LAO = "LAO"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LCA = "LCA"
    LIE = "LIE"
    LKA = "LKA"
    LSO = "LSO"
    LTU = "LTU"
    LUX = "LUX"
    LVA = "LVA"
    MAC = "MAC"
    MAF = "MAF"
    MAR = "MAR"
    MCO = "MCO"
    MDA = "MDA"
    MDG = "MDG"
    MDV = "MDV"
    MEX = "MEX"
    MHL = "MHL"
    MKD = "MKD"
    MLI = "MLI"
    MLT = "MLT"
    MMR = "MMR"
    MNE = "MNE"
    MNG = "MNG"
    MNP = "MNP"
    MOZ = "MOZ"
    MRT = "MRT"
    MSR = "MSR"
    MTQ = "MTQ"
    MUS = "MUS"
    MWI = "MWI"
    MYS = "MYS"
    MYT = "MYT"
    NAM = "NAM"
    NCL = "NCL"
    NER = "NER"
    NFK = "NFK"
    NGA = "NGA"
    NIC = "NIC"
    NIU = "NIU"
    NLD = "NLD"
    NOR = "NOR"
    NPL = "NPL"
    NRU = "NRU"
    NZL = "NZL"
    OMN = "OMN"
    PAK = "PAK"
    PAN = "PAN"
    PCN = "PCN"
    PER = "PER"
    PHL = "PHL"
    PLW = "PLW"
    PNG = "PNG"
    POL = "POL"
    PRI = "PRI"
    PRK = "PRK"
    PRT = "PRT"
    PRY = "PRY"
    PSE = "PSE"
    PYF = "PYF"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SAU = "SAU"
    SDN = "SDN"
    SEN = "SEN"
    SGP = "SGP"
    SGS = "SGS"
    SHN = "SHN"
    SJM = "SJM"
    SLB = "SLB"
    SLE = "SLE"
    SLV = "SLV"
    SMR = "SMR"
    SOM = "SOM"
    SPM = "SPM"
    SRB = "SRB"
    SSD = "SSD"
    STP = "STP"
    SUR = "SUR"
    SVK = "SVK"
    SVN = "SVN"
    SWE = "SWE"
    SWZ = "SWZ"
    SXM = "SXM"
    SYC = "SYC"
    SYR = "SYR"
    TCA = "TCA"
    TCD = "TCD"
    TGO = "TGO"
    THA = "THA"
    TJK = "TJK"
    TKL = "TKL"
    TKM = "TKM"
    TLS = "TLS"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TUV = "TUV"
    TWN = "TWN"
    TZA = "TZA"
    UGA = "UGA"
    UKR = "UKR"
    UMI = "UMI"
    URY = "URY"
    USA = "USA"
    UZB = "UZB"
    VAT = "VAT"
    VCT = "VCT"
    VEN = "VEN"
    VGB = "VGB"
    VIR = "VIR"
    VNM = "VNM"
    VUT = "VUT"
    WLF = "WLF"
    WSM = "WSM"
    YEM = "YEM"
    ZAF = "ZAF"
    ZMB = "ZMB"
    ZWE = "ZWE"
    EEC = "EEC"
    AAA = "AAA"


class DataAccessRestrictions(Enum):
    FEE_REQUIRED = "feeRequired"
    INSTITUTIONAL_MEMBERSHIP = "institutional membership"
    REGISTRATION = "registration"
    OTHER = "other"


class DataAccessTypes(Enum):
    OPEN = "open"
    EMBARGOED = "embargoed"
    RESTRICTED = "restricted"
    CLOSED = "closed"


class DataLicenseNames(Enum):
    APACHE_LICENSE_2_0 = "Apache License 2.0"
    BSD = "BSD"
    CC = "CC"
    CC0 = "CC0"
    COPYRIGHTS = "Copyrights"
    ODC = "ODC"
    OGL = "OGL"
    OGLC = "OGLC"
    PUBLIC_DOMAIN = "Public Domain"
    RL = "RL"
    OTHER = "other"
    NONE = "none"


class DataUploadRestrictions(Enum):
    FEE_REQUIRED = "feeRequired"
    INSTITUTIONAL_MEMBERSHIP = "institutional membership"
    REGISTRATION = "registration"
    OTHER = "other"


class DatabaseLicenseNames(Enum):
    APACHE_LICENSE_2_0 = "Apache License 2.0"
    BSD = "BSD"
    CC = "CC"
    CC0 = "CC0"
    COPYRIGHTS = "Copyrights"
    ODC = "ODC"
    PUBLIC_DOMAIN = "Public Domain"
    OTHER = "other"


class InstitutionTypes(Enum):
    COMMERCIAL = "commercial"
    NON_PROFIT = "non-profit"


class Languages(Enum):
    """Attributes:
    DEU: German
    ENG: English
    FRA: French
    AAR: Afar
    ABK: Abkhaz
    AFR: Afrikaans
    AKA: Akan
    AMH: Amharic
    ARA: Arabic
    ARG: Aragonese
    ASM: Assamese
    AVA: Avaric
    AVE: Avestan
    AYM: Aymara
    AZE: Azerbaijani
    BAK: Bashkir
    BAM: Bambara
    BEL: Belarusian
    BEN: Bengali
    BIS: Bislama
    BOD: Tibetan Standard, Tibetan, Central
    BOS: Bosnian
    BRE: Breton
    BUL: Bulgarian
    CAT: Catalan; Valencian
    CES: Czech
    CHA: Chamorro
    CHE: Chechen
    CHU: Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic
    CHV: Chuvash
    COR: Cornish
    COS: Corsican
    CRE: Cree
    CYM: Welsh
    DAN: Danish
    DIV: Divehi; Dhivehi; Maldivian;
    DZO: Dzongkha
    ELL: Greek, Modern
    EPO: Esperanto
    EST: Estonian
    EUS: Basque
    EWE: Ewe
    FAO: Faroese
    FAS: Persian
    FIJ: Fijian
    FIN: Finnish
    FRY: Western Frisian
    FUL: Fula; Fulah; Pulaar; Pular
    GLA: Scottish Gaelic; Gaelic
    GLE: Irish
    GLG: Galician
    GLV: Manx
    GRN: Guarani
    GUJ: Gujarati
    HAT: Haitian; Haitian Creole
    HAU: Hausa
    HEB: Hebrew (modern)
    HER: Herero
    HIN: Hindi
    HMO: Hiri Motu
    HRV: Croatian
    HUN: Hungarian
    HYE: Armenian
    IBO: Igbo
    IDO: Ido
    III: Nuosu
    IKU: Inuktitut
    ILE: Interlingue
    INA: Interlingua
    IND: Indonesian
    IPK: Inupiaq
    ISL: Icelandic
    ITA: Italian
    JAV: Javanese
    JPN: Japanese
    KAL: Kalaallisut, Greenlandic
    KAN: Kannada
    KAS: Kashmiri
    KAT: Georgian
    KAU: Kanuri
    KAZ: Kazakh
    KHM: Khmer
    KIK: Kikuyu, Gikuyu
    KIN: Kinyarwanda
    KIR: Kyrgyz
    KOM: Komi
    KON: Kongo
    KOR: Korean
    KUA: Kwanyama, Kuanyama
    KUR: Kurdish
    LAO: Lao
    LAT: Latin
    LAV: Latvian
    LIM: Limburgish, Limburgan, Limburger
    LIN: Lingala
    LIT: Lithuanian
    LTZ: Luxembourgish, Letzeburgesch
    LUB: Luba-Katanga
    LUG: Ganda
    MAH: Marshallese
    MAL: Malayalam
    MAR: Marathi
    MKD: Macedonian
    MLG: Malagasy
    MLT: Maltese
    MON: Mongolian
    MRI: Maori
    MSA: Malay
    MYA: Burmese
    NAU: Nauru
    NAV: Navajo, Navaho
    NBL: South Ndebele
    NDE: North Ndebele
    NDO: Ndonga
    NEP: Nepali
    NLD: Dutch
    NNO: Norwegian Nynorsk
    NOB: Norwegian Bokmal
    NOR: Norwegian
    NYA: Chichewa; Chewa; Nyanja
    OCI: Occitan
    OJI: Ojibwe, Ojibwa
    ORI: Oriya
    ORM: Oromo
    OSS: Ossetian, Ossetic
    PAN: Panjabi, Punjabi
    PLI: Pali
    POL: Polish
    POR: Portuguese
    PUS: Pashto, Pushto
    QUE: Quechua
    ROH: Romansh
    RON: Romanian, Moldavian(Romanian from Republic of Moldova)
    RUN: Kirundi
    RUS: Russian
    SAG: Sango
    SAN: Sanskrit (Samskrta)
    SIN: Sinhala, Sinhalese
    SLK: Slovak
    SLV: Slovene
    SME: Northern Sami
    SMO: Samoan
    SNA: Shona
    SND: Sindhi
    SOM: Somali
    SOT: Southern Sotho
    SPA: Spanish; Castilian
    SQI: Albanian
    SRD: Sardinian
    SRP: Serbian
    SSW: Swati
    SUN: Sundanese
    SWA: Swahili
    SWE: Swedish
    TAH: Tahitian
    TAM: Tamil
    TAT: Tatar
    TEL: Telugu
    TGK: Tajik
    TGL: Tagalog
    THA: Thai
    TIR: Tigrinya
    TON: Tonga (Tonga Islands)
    TSN: Tswana
    TSO: Tsonga
    TUK: Turkmen
    TUR: Turkish
    TWI: Twi
    UIG: Uighur, Uyghur
    UKR: Ukrainian
    URD: Urdu
    UZB: Uzbek
    VEN: Venda
    VIE: Vietnamese
    VOL: Volapuk
    WLN: Walloon
    WOL: Wolof
    XHO: Xhosa
    YID: Yiddish
    YOR: Yoruba
    ZHA: Zhuang, Chuang
    ZHO: Chinese
    ZUL: Zulu
    """

    DEU = "deu"
    ENG = "eng"
    FRA = "fra"
    AAR = "aar"
    ABK = "abk"
    AFR = "afr"
    AKA = "aka"
    AMH = "amh"
    ARA = "ara"
    ARG = "arg"
    ASM = "asm"
    AVA = "ava"
    AVE = "ave"
    AYM = "aym"
    AZE = "aze"
    BAK = "bak"
    BAM = "bam"
    BEL = "bel"
    BEN = "ben"
    BIS = "bis"
    BOD = "bod"
    BOS = "bos"
    BRE = "bre"
    BUL = "bul"
    CAT = "cat"
    CES = "ces"
    CHA = "cha"
    CHE = "che"
    CHU = "chu"
    CHV = "chv"
    COR = "cor"
    COS = "cos"
    CRE = "cre"
    CYM = "cym"
    DAN = "dan"
    DIV = "div"
    DZO = "dzo"
    ELL = "ell"
    EPO = "epo"
    EST = "est"
    EUS = "eus"
    EWE = "ewe"
    FAO = "fao"
    FAS = "fas"
    FIJ = "fij"
    FIN = "fin"
    FRY = "fry"
    FUL = "ful"
    GLA = "gla"
    GLE = "gle"
    GLG = "glg"
    GLV = "glv"
    GRN = "grn"
    GUJ = "guj"
    HAT = "hat"
    HAU = "hau"
    HEB = "heb"
    HER = "her"
    HIN = "hin"
    HMO = "hmo"
    HRV = "hrv"
    HUN = "hun"
    HYE = "hye"
    IBO = "ibo"
    IDO = "ido"
    III = "iii"
    IKU = "iku"
    ILE = "ile"
    INA = "ina"
    IND = "ind"
    IPK = "ipk"
    ISL = "isl"
    ITA = "ita"
    JAV = "jav"
    JPN = "jpn"
    KAL = "kal"
    KAN = "kan"
    KAS = "kas"
    KAT = "kat"
    KAU = "kau"
    KAZ = "kaz"
    KHM = "khm"
    KIK = "kik"
    KIN = "kin"
    KIR = "kir"
    KOM = "kom"
    KON = "kon"
    KOR = "kor"
    KUA = "kua"
    KUR = "kur"
    LAO = "lao"
    LAT = "lat"
    LAV = "lav"
    LIM = "lim"
    LIN = "lin"
    LIT = "lit"
    LTZ = "ltz"
    LUB = "lub"
    LUG = "lug"
    MAH = "mah"
    MAL = "mal"
    MAR = "mar"
    MKD = "mkd"
    MLG = "mlg"
    MLT = "mlt"
    MON = "mon"
    MRI = "mri"
    MSA = "msa"
    MYA = "mya"
    NAU = "nau"
    NAV = "nav"
    NBL = "nbl"
    NDE = "nde"
    NDO = "ndo"
    NEP = "nep"
    NLD = "nld"
    NNO = "nno"
    NOB = "nob"
    NOR = "nor"
    NYA = "nya"
    OCI = "oci"
    OJI = "oji"
    ORI = "ori"
    ORM = "orm"
    OSS = "oss"
    PAN = "pan"
    PLI = "pli"
    POL = "pol"
    POR = "por"
    PUS = "pus"
    QUE = "que"
    ROH = "roh"
    RON = "ron"
    RUN = "run"
    RUS = "rus"
    SAG = "sag"
    SAN = "san"
    SIN = "sin"
    SLK = "slk"
    SLV = "slv"
    SME = "sme"
    SMO = "smo"
    SNA = "sna"
    SND = "snd"
    SOM = "som"
    SOT = "sot"
    SPA = "spa"
    SQI = "sqi"
    SRD = "srd"
    SRP = "srp"
    SSW = "ssw"
    SUN = "sun"
    SWA = "swa"
    SWE = "swe"
    TAH = "tah"
    TAM = "tam"
    TAT = "tat"
    TEL = "tel"
    TGK = "tgk"
    TGL = "tgl"
    THA = "tha"
    TIR = "tir"
    TON = "ton"
    TSN = "tsn"
    TSO = "tso"
    TUK = "tuk"
    TUR = "tur"
    TWI = "twi"
    UIG = "uig"
    UKR = "ukr"
    URD = "urd"
    UZB = "uzb"
    VEN = "ven"
    VIE = "vie"
    VOL = "vol"
    WLN = "wln"
    WOL = "wol"
    XHO = "xho"
    YID = "yid"
    YOR = "yor"
    ZHA = "zha"
    ZHO = "zho"
    ZUL = "zul"


class MetadataStandardDccnames(Enum):
    """Attributes:
    ABCD_ACCESS_TO_BIOLOGICAL_COLLECTION_DATA: http://www.dcc.ac.uk/resources/metadata-standards/abcd-access-
        biological-collection-data
    AG_MES_AGRICULTURAL_METADATA_ELEMENT_SET: http://www.dcc.ac.uk/resources/metadata-standards/agmes-
        agricultural-metadata-element-set
    AVM_ASTRONOMY_VISUALIZATION_METADATA: http://www.dcc.ac.uk/resources/metadata-standards/avm-astronomy-
        visualization-metadata
    CF_CLIMATE_AND_FORECAST_METADATA_CONVENTIONS: http://www.dcc.ac.uk/resources/metadata-standards/cf-
        climate-and-forecast-metadata-conventions
    CIF_CRYSTALLOGRAPHIC_INFORMATION_FRAMEWORK: http://www.dcc.ac.uk/resources/metadata-standards/cif-
        crystallographic-information-framework
    CIM_COMMON_INFORMATION_MODEL: http://www.dcc.ac.uk/resources/metadata-standards/cim-common-information-
        model
    CSMD_CCLRC_CORE_SCIENTIFIC_METADATA_MODEL: http://www.dcc.ac.uk/resources/metadata-standards/csmd-cclrc-
        core-scientific-metadata-model
    DARWIN_CORE: http://www.dcc.ac.uk/resources/metadata-standards/darwin-core
    DATA_CITE_METADATA_SCHEMA: http://www.dcc.ac.uk/resources/metadata-standards/datacite-metadata-schema
    DCAT_DATA_CATALOG_VOCABULARY: http://www.dcc.ac.uk/resources/metadata-standards/dcat-data-catalog-
        vocabulary
    DDI_DATA_DOCUMENTATION_INITIATIVE: http://www.dcc.ac.uk/resources/metadata-standards/ddi-data-
        documentation-initiative
    DIF_DIRECTORY_INTERCHANGE_FORMAT: http://www.dcc.ac.uk/resources/metadata-standards/dif-directory-
        interchange-format
    DUBLIN_CORE: http://www.dcc.ac.uk/resources/metadata-standards/dublin-core
    EML_ECOLOGICAL_METADATA_LANGUAGE: http://www.dcc.ac.uk/resources/metadata-standards/eml-ecological-
        metadata-language
    FGDC_CSDGM_FEDERAL_GEOGRAPHIC_DATA_COMMITTEE_CONTENT_STANDARD_FOR_DIGITAL_GEOSPATIAL_METADATA:
        http://www.dcc.ac.uk/resources/metadata-standards/fgdccsdgm-federal-geographic-data-committee-
        content-standard-digital-ge
    FITS_FLEXIBLE_IMAGE_TRANSPORT_SYSTEM: http://www.dcc.ac.uk/resources/metadata-standards/fits-flexible-
        image-transport-system
    GENOME_METADATA: http://www.dcc.ac.uk/resources/metadata-standards/genome-metadata
    INTERNATIONAL_VIRTUAL_OBSERVATORY_ALLIANCE_TECHNICAL_SPECIFICATIONS:
        http://www.dcc.ac.uk/resources/metadata-standards/international-virtual-observatory-alliance-
        technical-specifications
    ISA_TAB: http://www.dcc.ac.uk/resources/metadata-standards/isa-tab
    ISO_19115: http://www.dcc.ac.uk/resources/metadata-standards/iso-19115
    MIBBI_MINIMUM_INFORMATION_FOR_BIOLOGICAL_AND_BIOMEDICAL_INVESTIGATIONS:
        http://www.dcc.ac.uk/resources/metadata-standards/mibbi-minimum-information-biological-and-
        biomedical-investigations
    MIDAS_HERITAGE: http://www.dcc.ac.uk/resources/metadata-standards/midas-heritage
    OAI_ORE_OPEN_ARCHIVES_INITIATIVE_OBJECT_REUSE_AND_EXCHANGE: http://www.dcc.ac.uk/resources/metadata-
        standards/oai-ore-open-archives-initiative-object-reuse-and-exchange
    OBSERV_OM: http://www.dcc.ac.uk/resources/metadata-standards/observ-om
    OBSERVATIONS_AND_MEASUREMENTS: http://www.dcc.ac.uk/resources/metadata-standards/observations-and-
        measurements
    OME_XML_OPEN_MICROSCOPY_ENVIRONMENT_XML: http://www.dcc.ac.uk/resources/metadata-standards/ome-xml-open-
        microscopy-environment-xml
    PROTOCOL_DATA_ELEMENT_DEFINITIONS: http://www.dcc.ac.uk/resources/metadata-standards/protocol-data-
        element-definitions
    PROV: http://www.dcc.ac.uk/resources/metadata-standards/prov
    QU_DEX_QUALITATIVE_DATA_EXCHANGE_FORMAT: http://www.dcc.ac.uk/resources/metadata-standards/qudex-
        qualitative-data-exchange-format
    RDF_DATA_CUBE_VOCABULARY: http://www.dcc.ac.uk/resources/metadata-standards/rdf-data-cube-vocabulary
    REPOSITORY_DEVELOPED_METADATA_SCHEMAS: http://www.dcc.ac.uk/resources/metadata-standards/repository-
        developed-metadata-schemas
    SDMX_STATISTICAL_DATA_AND_METADATA_EXCHANGE: http://www.dcc.ac.uk/resources/metadata-standards/sdmx-
        statistical-data-and-metadata-exchange
    SPASE_DATA_MODEL: http://www.dcc.ac.uk/resources/metadata-standards/spase-data-model
    OTHER: other
    """

    ABCD_ACCESS_TO_BIOLOGICAL_COLLECTION_DATA = "ABCD - Access to Biological Collection Data"
    AG_MES_AGRICULTURAL_METADATA_ELEMENT_SET = "AgMES - Agricultural Metadata Element Set"
    AVM_ASTRONOMY_VISUALIZATION_METADATA = "AVM - Astronomy Visualization Metadata"
    CF_CLIMATE_AND_FORECAST_METADATA_CONVENTIONS = "CF (Climate and Forecast) Metadata Conventions"
    CIF_CRYSTALLOGRAPHIC_INFORMATION_FRAMEWORK = "CIF - Crystallographic Information Framework"
    CIM_COMMON_INFORMATION_MODEL = "CIM - Common Information Model"
    CSMD_CCLRC_CORE_SCIENTIFIC_METADATA_MODEL = "CSMD-CCLRC Core Scientific Metadata Model"
    DARWIN_CORE = "Darwin Core"
    DATA_CITE_METADATA_SCHEMA = "DataCite Metadata Schema"
    DCAT_DATA_CATALOG_VOCABULARY = "DCAT - Data Catalog Vocabulary"
    DDI_DATA_DOCUMENTATION_INITIATIVE = "DDI - Data Documentation Initiative"
    DIF_DIRECTORY_INTERCHANGE_FORMAT = "DIF - Directory Interchange Format"
    DUBLIN_CORE = "Dublin Core"
    EML_ECOLOGICAL_METADATA_LANGUAGE = "EML - Ecological Metadata Language"
    FGDC_CSDGM_FEDERAL_GEOGRAPHIC_DATA_COMMITTEE_CONTENT_STANDARD_FOR_DIGITAL_GEOSPATIAL_METADATA = (
        "FGDC/CSDGM - Federal Geographic Data Committee Content Standard for Digital Geospatial Metadata"
    )
    FITS_FLEXIBLE_IMAGE_TRANSPORT_SYSTEM = "FITS - Flexible Image Transport System"
    GENOME_METADATA = "Genome Metadata"
    INTERNATIONAL_VIRTUAL_OBSERVATORY_ALLIANCE_TECHNICAL_SPECIFICATIONS = (
        "International Virtual Observatory Alliance Technical Specifications"
    )
    ISA_TAB = "ISA-Tab"
    ISO_19115 = "ISO 19115"
    MIBBI_MINIMUM_INFORMATION_FOR_BIOLOGICAL_AND_BIOMEDICAL_INVESTIGATIONS = (
        "MIBBI - Minimum Information for Biological and Biomedical Investigations"
    )
    MIDAS_HERITAGE = "MIDAS-Heritage"
    OAI_ORE_OPEN_ARCHIVES_INITIATIVE_OBJECT_REUSE_AND_EXCHANGE = (
        "OAI-ORE - Open Archives Initiative Object Reuse and Exchange"
    )
    OBSERV_OM = "Observ-OM"
    OBSERVATIONS_AND_MEASUREMENTS = "Observations and Measurements"
    OME_XML_OPEN_MICROSCOPY_ENVIRONMENT_XML = "OME-XML - Open Microscopy Environment XML"
    PROTOCOL_DATA_ELEMENT_DEFINITIONS = "Protocol Data Element Definitions"
    PROV = "PROV"
    QU_DEX_QUALITATIVE_DATA_EXCHANGE_FORMAT = "QuDEx - Qualitative Data Exchange Format"
    RDF_DATA_CUBE_VOCABULARY = "RDF Data Cube Vocabulary"
    REPOSITORY_DEVELOPED_METADATA_SCHEMAS = "Repository-Developed Metadata Schemas"
    SDMX_STATISTICAL_DATA_AND_METADATA_EXCHANGE = "SDMX - Statistical Data and Metadata Exchange"
    SPASE_DATA_MODEL = "SPASE Data Model"
    OTHER = "other"


class MetadataStandardDccurls(Enum):
    """Attributes:
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ABCD_ACCESS_BIOLOGICAL_COLLECTION_DATA: ABCD - Access to
        Biological Collection Data
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_AGMES_AGRICULTURAL_METADATA_ELEMENT_SET: AgMES -
        Agricultural Metadata Element Set
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_AVM_ASTRONOMY_VISUALIZATION_METADATA: AVM - Astronomy
        Visualization Metadata
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CF_CLIMATE_AND_FORECAST_METADATA_CONVENTIONS: CF (Climate
        and Forecast) Metadata Conventions
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CIF_CRYSTALLOGRAPHIC_INFORMATION_FRAMEWORK: CIF -
        Crystallographic Information Framework
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CIM_COMMON_INFORMATION_MODEL: CIM - Common Information
        Model
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CSMD_CCLRC_CORE_SCIENTIFIC_METADATA_MODEL: CSMD-CCLRC
        Core Scientific Metadata Model
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DARWIN_CORE: Darwin Core
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DATACITE_METADATA_SCHEMA: DataCite Metadata Schema
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DCAT_DATA_CATALOG_VOCABULARY: DCAT - Data Catalog
        Vocabulary
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DDI_DATA_DOCUMENTATION_INITIATIVE: DDI - Data
        Documentation Initiative
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DIF_DIRECTORY_INTERCHANGE_FORMAT: DIF - Directory
        Interchange Format
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DUBLIN_CORE: Dublin Core
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_EML_ECOLOGICAL_METADATA_LANGUAGE: EML - Ecological
        Metadata Language
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_FGDCCSDGM_FEDERAL_GEOGRAPHIC_DATA_COMMITTEE_CONTENT_STANDARD_DIGITAL_GE:
        FGDC/CSDGM - Federal Geographic Data Committee Content Standard for Digital Geospatial Metadata
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_FITS_FLEXIBLE_IMAGE_TRANSPORT_SYSTEM: FITS - Flexible
        Image Transport System
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_GENOME_METADATA: Genome Metadata
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_INTERNATIONAL_VIRTUAL_OBSERVATORY_ALLIANCE_TECHNICAL_SPECIFICATIONS:
        International Virtual Observatory Alliance Technical Specifications
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ISA_TAB: ISA-Tab
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ISO_19115: ISO 19115
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_MIBBI_MINIMUM_INFORMATION_BIOLOGICAL_AND_BIOMEDICAL_INVESTIGATIONS:
        MIBBI - Minimum Information for Biological and Biomedical Investigations
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_MIDAS_HERITAGE: MIDAS-Heritage
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OAI_ORE_OPEN_ARCHIVES_INITIATIVE_OBJECT_REUSE_AND_EXCHANGE:
        OAI-ORE - Open Archives Initiative Object Reuse and Exchange
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OBSERV_OM: Observ-OM
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OBSERVATIONS_AND_MEASUREMENTS: Observations and
        Measurements
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OME_XML_OPEN_MICROSCOPY_ENVIRONMENT_XML: OME-XML - Open
        Microscopy Environment XML
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_PROTOCOL_DATA_ELEMENT_DEFINITIONS: Protocol Data Element
        Definitions
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_PROV: PROV
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_QUDEX_QUALITATIVE_DATA_EXCHANGE_FORMAT: QuDEx -
        Qualitative Data Exchange Format
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_RDF_DATA_CUBE_VOCABULARY: RDF Data Cube Vocabulary
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_REPOSITORY_DEVELOPED_METADATA_SCHEMAS: Repository-
        Developed Metadata Schemas
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_SDMX_STATISTICAL_DATA_AND_METADATA_EXCHANGE: SDMX -
        Statistical Data and Metadata Exchange
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_SPASE_DATA_MODEL: SPASE Data Model
    OTHER: other
    """

    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ABCD_ACCESS_BIOLOGICAL_COLLECTION_DATA = (
        "http://www.dcc.ac.uk/resources/metadata-standards/abcd-access-biological-collection-data"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_AGMES_AGRICULTURAL_METADATA_ELEMENT_SET = (
        "http://www.dcc.ac.uk/resources/metadata-standards/agmes-agricultural-metadata-element-set"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_AVM_ASTRONOMY_VISUALIZATION_METADATA = (
        "http://www.dcc.ac.uk/resources/metadata-standards/avm-astronomy-visualization-metadata"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CF_CLIMATE_AND_FORECAST_METADATA_CONVENTIONS = (
        "http://www.dcc.ac.uk/resources/metadata-standards/cf-climate-and-forecast-metadata-conventions"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CIF_CRYSTALLOGRAPHIC_INFORMATION_FRAMEWORK = (
        "http://www.dcc.ac.uk/resources/metadata-standards/cif-crystallographic-information-framework"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CIM_COMMON_INFORMATION_MODEL = (
        "http://www.dcc.ac.uk/resources/metadata-standards/cim-common-information-model"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_CSMD_CCLRC_CORE_SCIENTIFIC_METADATA_MODEL = (
        "http://www.dcc.ac.uk/resources/metadata-standards/csmd-cclrc-core-scientific-metadata-model"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DARWIN_CORE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/darwin-core"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DATACITE_METADATA_SCHEMA = (
        "http://www.dcc.ac.uk/resources/metadata-standards/datacite-metadata-schema"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DCAT_DATA_CATALOG_VOCABULARY = (
        "http://www.dcc.ac.uk/resources/metadata-standards/dcat-data-catalog-vocabulary"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DDI_DATA_DOCUMENTATION_INITIATIVE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/ddi-data-documentation-initiative"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DIF_DIRECTORY_INTERCHANGE_FORMAT = (
        "http://www.dcc.ac.uk/resources/metadata-standards/dif-directory-interchange-format"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_DUBLIN_CORE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/dublin-core"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_EML_ECOLOGICAL_METADATA_LANGUAGE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/eml-ecological-metadata-language"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_FGDCCSDGM_FEDERAL_GEOGRAPHIC_DATA_COMMITTEE_CONTENT_STANDARD_DIGITAL_GE = "http://www.dcc.ac.uk/resources/metadata-standards/fgdccsdgm-federal-geographic-data-committee-content-standard-digital-ge"
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_FITS_FLEXIBLE_IMAGE_TRANSPORT_SYSTEM = (
        "http://www.dcc.ac.uk/resources/metadata-standards/fits-flexible-image-transport-system"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_GENOME_METADATA = (
        "http://www.dcc.ac.uk/resources/metadata-standards/genome-metadata"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_INTERNATIONAL_VIRTUAL_OBSERVATORY_ALLIANCE_TECHNICAL_SPECIFICATIONS = "http://www.dcc.ac.uk/resources/metadata-standards/international-virtual-observatory-alliance-technical-specifications"
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ISA_TAB = (
        "http://www.dcc.ac.uk/resources/metadata-standards/isa-tab"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_ISO_19115 = (
        "http://www.dcc.ac.uk/resources/metadata-standards/iso-19115"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_MIBBI_MINIMUM_INFORMATION_BIOLOGICAL_AND_BIOMEDICAL_INVESTIGATIONS = "http://www.dcc.ac.uk/resources/metadata-standards/mibbi-minimum-information-biological-and-biomedical-investigations"
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_MIDAS_HERITAGE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/midas-heritage"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OAI_ORE_OPEN_ARCHIVES_INITIATIVE_OBJECT_REUSE_AND_EXCHANGE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/oai-ore-open-archives-initiative-object-reuse-and-exchange"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OBSERV_OM = (
        "http://www.dcc.ac.uk/resources/metadata-standards/observ-om"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OBSERVATIONS_AND_MEASUREMENTS = (
        "http://www.dcc.ac.uk/resources/metadata-standards/observations-and-measurements"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_OME_XML_OPEN_MICROSCOPY_ENVIRONMENT_XML = (
        "http://www.dcc.ac.uk/resources/metadata-standards/ome-xml-open-microscopy-environment-xml"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_PROTOCOL_DATA_ELEMENT_DEFINITIONS = (
        "http://www.dcc.ac.uk/resources/metadata-standards/protocol-data-element-definitions"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_PROV = "http://www.dcc.ac.uk/resources/metadata-standards/prov"
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_QUDEX_QUALITATIVE_DATA_EXCHANGE_FORMAT = (
        "http://www.dcc.ac.uk/resources/metadata-standards/qudex-qualitative-data-exchange-format"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_RDF_DATA_CUBE_VOCABULARY = (
        "http://www.dcc.ac.uk/resources/metadata-standards/rdf-data-cube-vocabulary"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_REPOSITORY_DEVELOPED_METADATA_SCHEMAS = (
        "http://www.dcc.ac.uk/resources/metadata-standards/repository-developed-metadata-schemas"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_SDMX_STATISTICAL_DATA_AND_METADATA_EXCHANGE = (
        "http://www.dcc.ac.uk/resources/metadata-standards/sdmx-statistical-data-and-metadata-exchange"
    )
    HTTP_WWW_DCC_AC_UK_RESOURCES_METADATA_STANDARDS_SPASE_DATA_MODEL = (
        "http://www.dcc.ac.uk/resources/metadata-standards/spase-data-model"
    )
    OTHER = "other"


class PidSystems(Enum):
    ARK = "ARK"
    DOI = "DOI"
    HDL = "hdl"
    PURL = "PURL"
    URN = "URN"
    OTHER = "other"
    NONE = "none"


class ProviderTypes(Enum):
    DATA_PROVIDER = "dataProvider"
    SERVICE_PROVIDER = "serviceProvider"


class ContentTypeScheme(Enum):
    PARSE = "parse"


@dataclass(slots=True)
class DataUploadLicense:
    """Attributes:
    data_upload_license_name: Name of the license for data upload.
    data_upload_license_url: Data upload license URL.
    """

    class Meta:
        global_type = False

    data_upload_license_name: None | str = field(
        default=None,
        metadata={
            "name": "dataUploadLicenseName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    data_upload_license_url: None | str = field(
        default=None,
        metadata={
            "name": "dataUploadLicenseURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


class MetadataStandardScheme(Enum):
    DCC = "DCC"


@dataclass(slots=True)
class Policy:
    """Attributes:
    policy_name: Name of the policy.
    policy_url: URL of the policy.
    """

    class Meta:
        global_type = False

    policy_name: None | str = field(
        default=None,
        metadata={
            "name": "policyName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    policy_url: None | str = field(
        default=None,
        metadata={
            "name": "policyURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


@dataclass(slots=True)
class Size:
    """Attributes:
    value:
    updated: The date of the last update of the research data repository size.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    # Note: Unfortunately, we had to add `str` type manually due to inconsistencies between the API data and
    # the XSD schema. This led to numerous `ConverterWarnings`. Ideally, the data would conform to the schema,
    # but until then, this workaround helps maintain compatibility.
    updated: None | XmlPeriod | XmlDate | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )


class SubjectScheme(Enum):
    DFG = "DFG"


class RepositoryTypes(Enum):
    DISCIPLINARY = "disciplinary"
    INSTITUTIONAL = "institutional"
    OTHER = "other"


class ResponsibilityTypes(Enum):
    FUNDING = "funding"
    GENERAL = "general"
    SPONSORING = "sponsoring"
    TECHNICAL = "technical"


# Note: Unfortunately, we had to change `DataVerse` to `Dataverse` manually due to inconsistencies between the API data
# and the XSD schema. This led to numerous `ConverterWarnings`. Ideally, the data would conform to the schema,
# but until then, this workaround helps maintain compatibility.
class SoftwareNames(Enum):
    CKAN = "CKAN"
    DATA_VERSE = "Dataverse"
    DIGITAL_COMMONS = "DigitalCommons"
    D_LIBRA = "dLibra"
    DSPACE = "DSpace"
    EPRINTS = "EPrints"
    E_SCI_DOC = "eSciDoc"
    FEDORA = "Fedora"
    MY_SQL = "MySQL"
    NESSTAR = "Nesstar"
    OPUS = "Opus"
    OTHER = "other"
    UNKNOWN = "unknown"


class SubjectText(Enum):
    VALUE_1_HUMANITIES_AND_SOCIAL_SCIENCES = "1 Humanities and Social Sciences"
    VALUE_11_HUMANITIES = "11 Humanities"
    VALUE_101_ANCIENT_CULTURES = "101 Ancient Cultures"
    VALUE_10101_PREHISTORY = "10101 Prehistory"
    VALUE_10102_CLASSICAL_PHILOLOGY = "10102 Classical Philology"
    VALUE_10103_ANCIENT_HISTORY = "10103 Ancient History"
    VALUE_10104_CLASSICAL_ARCHAEOLOGY = "10104 Classical Archaeology"
    VALUE_10105_EGYPTOLOGY_AND_ANCIENT_NEAR_EASTERN_STUDIES = "10105 Egyptology and Ancient Near Eastern Studies"
    VALUE_102_HISTORY = "102 History"
    VALUE_10201_MEDIEVAL_HISTORY = "10201 Medieval History"
    VALUE_10202_EARLY_MODERN_HISTORY = "10202 Early Modern History"
    VALUE_10203_MODERN_AND_CURRENT_HISTORY = "10203 Modern and Current History"
    VALUE_10204_HISTORY_OF_SCIENCE = "10204 History of Science"
    VALUE_103_FINE_ARTS_MUSIC_THEATRE_AND_MEDIA_STUDIES = "103 Fine Arts, Music, Theatre and Media Studies"
    VALUE_10301_ART_HISTORY = "10301 Art History"
    VALUE_10302_MUSICOLOGY = "10302 Musicology"
    VALUE_10303_THEATRE_AND_MEDIA_STUDIES = "10303 Theatre and Media Studies"
    VALUE_104_LINGUISTICS = "104 Linguistics"
    VALUE_10401_GENERAL_AND_APPLIED_LINGUISTICS = "10401 General and Applied Linguistics"
    VALUE_10402_INDIVIDUAL_LINGUISTICS = "10402 Individual Linguistics"
    VALUE_10403_TYPOLOGY_NON_EUROPEAN_LANGUAGES_HISTORICAL_LINGUISTICS = (
        "10403 Typology, Non-European Languages, Historical Linguistics"
    )
    VALUE_105_LITERARY_STUDIES = "105 Literary Studies"
    VALUE_10501_MEDIEVAL_GERMAN_LITERATURE = "10501 Medieval German Literature"
    VALUE_10502_MODERN_GERMAN_LITERATURE = "10502 Modern German Literature"
    VALUE_10503_EUROPEAN_AND_AMERICAN_LITERATURE = "10503 European and American Literature"
    VALUE_10504_GENERAL_AND_COMPARATIVE_LITERATURE_AND_CULTURAL_STUDIES = (
        "10504 General and Comparative Literature and Cultural Studies"
    )
    VALUE_106_NON_EUROPEAN_LANGUAGES_AND_CULTURES_SOCIAL_AND_CULTURAL_ANTHROPOLOGY_JEWISH_STUDIES_AND_RELIGIOUS_STUDIES = "106 Non-European Languages and Cultures, Social and Cultural Anthropology, Jewish Studies and Religious Studies"
    VALUE_10601_SOCIAL_AND_CULTURAL_ANTHROPOLOGY_AND_ETHNOLOGY_FOLKLORE = (
        "10601 Social and Cultural Anthropology and Ethnology/Folklore"
    )
    VALUE_10602_ASIAN_STUDIES = "10602 Asian Studies"
    VALUE_10603_AFRICAN_AMERICAN_AND_OCEANIA_STUDIES = "10603 African, American and Oceania Studies"
    VALUE_10604_ISLAMIC_STUDIES_ARABIAN_STUDIES_SEMITIC_STUDIES = (
        "10604 Islamic Studies, Arabian Studies, Semitic Studies"
    )
    VALUE_10605_RELIGIOUS_STUDIES_AND_JEWISH_STUDIES = "10605 Religious Studies and Jewish Studies"
    VALUE_107_THEOLOGY = "107 Theology"
    VALUE_10701_PROTESTANT_THEOLOGY = "10701 Protestant Theology"
    VALUE_10702_ROMAN_CATHOLIC_THEOLOGY = "10702 Roman Catholic Theology"
    VALUE_108_PHILOSOPHY = "108 Philosophy"
    VALUE_10801_HISTORY_OF_PHILOSOPHY = "10801 History of Philosophy"
    VALUE_10802_THEORETICAL_PHILOSOPHY = "10802 Theoretical Philosophy"
    VALUE_10803_PRACTICAL_PHILOSOPHY = "10803 Practical Philosophy"
    VALUE_12_SOCIAL_AND_BEHAVIOURAL_SCIENCES = "12 Social and Behavioural Sciences"
    VALUE_109_EDUCATION_SCIENCES = "109 Education Sciences"
    VALUE_10901_GENERAL_EDUCATION_AND_HISTORY_OF_EDUCATION = "10901 General Education and History of Education"
    VALUE_10902_RESEARCH_ON_TEACHING_LEARNING_AND_TRAINING = "10902 Research on Teaching, Learning and Training"
    VALUE_10903_RESEARCH_ON_SOCIALIZATION_AND_EDUCATIONAL_INSTITUTIONS_AND_PROFESSIONS = (
        "10903 Research on Socialization and Educational Institutions and Professions"
    )
    VALUE_110_PSYCHOLOGY = "110 Psychology"
    VALUE_11001_GENERAL_BIOLOGICAL_AND_MATHEMATICAL_PSYCHOLOGY = "11001 General, Biological and Mathematical Psychology"
    VALUE_11002_DEVELOPMENTAL_AND_EDUCATIONAL_PSYCHOLOGY = "11002 Developmental and Educational Psychology"
    VALUE_11003_SOCIAL_PSYCHOLOGY_INDUSTRIAL_AND_ORGANISATIONAL_PSYCHOLOGY = (
        "11003 Social Psychology, Industrial and Organisational Psychology"
    )
    VALUE_11004_DIFFERENTIAL_PSYCHOLOGY_CLINICAL_PSYCHOLOGY_MEDICAL_PSYCHOLOGY_METHODOLOGY = (
        "11004 Differential Psychology, Clinical Psychology, Medical Psychology, Methodology"
    )
    VALUE_111_SOCIAL_SCIENCES = "111 Social Sciences"
    VALUE_11101_SOCIOLOGICAL_THEORY = "11101 Sociological Theory"
    VALUE_11102_EMPIRICAL_SOCIAL_RESEARCH = "11102 Empirical Social Research"
    VALUE_11103_COMMUNICATION_SCIENCE = "11103 Communication Science"
    VALUE_11104_POLITICAL_SCIENCE = "11104 Political Science"
    VALUE_112_ECONOMICS = "112 Economics"
    VALUE_11201_ECONOMIC_THEORY = "11201 Economic Theory"
    VALUE_11202_ECONOMIC_AND_SOCIAL_POLICY = "11202 Economic and Social Policy"
    VALUE_11203_PUBLIC_FINANCE = "11203 Public Finance"
    VALUE_11204_BUSINESS_ADMINISTRATION = "11204 Business Administration"
    VALUE_11205_STATISTICS_AND_ECONOMETRICS = "11205 Statistics and Econometrics"
    VALUE_11206_ECONOMIC_AND_SOCIAL_HISTORY = "11206 Economic and Social History"
    VALUE_113_JURISPRUDENCE = "113 Jurisprudence"
    VALUE_11301_LEGAL_AND_POLITICAL_PHILOSOPHY_LEGAL_HISTORY_LEGAL_THEORY = (
        "11301 Legal and Political Philosophy, Legal History, Legal Theory"
    )
    VALUE_11302_PRIVATE_LAW = "11302 Private Law"
    VALUE_11303_PUBLIC_LAW = "11303 Public Law"
    VALUE_11304_CRIMINAL_LAW_AND_LAW_OF_CRIMINAL_PROCEDURE = "11304 Criminal Law and Law of Criminal Procedure"
    VALUE_11305_CRIMINOLOGY = "11305 Criminology"
    VALUE_2_LIFE_SCIENCES = "2 Life Sciences"
    VALUE_21_BIOLOGY = "21 Biology"
    VALUE_201_BASIC_BIOLOGICAL_AND_MEDICAL_RESEARCH = "201 Basic Biological and Medical Research"
    VALUE_20101_BIOCHEMISTRY = "20101 Biochemistry"
    VALUE_20102_BIOPHYSICS = "20102 Biophysics"
    VALUE_20103_CELL_BIOLOGY = "20103 Cell Biology"
    VALUE_20104_STRUCTURAL_BIOLOGY = "20104 Structural Biology"
    VALUE_20105_GENERAL_GENETICS = "20105 General Genetics"
    VALUE_20106_DEVELOPMENTAL_BIOLOGY = "20106 Developmental Biology"
    VALUE_20107_BIOINFORMATICS_AND_THEORETICAL_BIOLOGY = "20107 Bioinformatics and Theoretical Biology"
    VALUE_20108_ANATOMY = "20108 Anatomy"
    VALUE_202_PLANT_SCIENCES = "202 Plant Sciences"
    VALUE_20201_PLANT_SYSTEMATICS_AND_EVOLUTION = "20201 Plant Systematics and Evolution"
    VALUE_20202_PLANT_ECOLOGY_AND_ECOSYSTEM_ANALYSIS = "20202 Plant Ecology and Ecosystem Analysis"
    VALUE_20203_INTER_ORGANISMIC_INTERACTIONS_OF_PLANTS = "20203 Inter-organismic Interactions of Plants"
    VALUE_20204_PLANT_PHYSIOLOGY = "20204 Plant Physiology"
    VALUE_20205_PLANT_BIOCHEMISTRY_AND_BIOPHYSICS = "20205 Plant Biochemistry and Biophysics"
    VALUE_20206_PLANT_CELL_AND_DEVELOPMENTAL_BIOLOGY = "20206 Plant Cell and Developmental Biology"
    VALUE_20207_PLANT_GENETICS = "20207 Plant Genetics"
    VALUE_203_ZOOLOGY = "203 Zoology"
    VALUE_20301_SYSTEMATICS_AND_MORPHOLOGY = "20301 Systematics and Morphology"
    VALUE_20302_EVOLUTION_ANTHROPOLOGY = "20302 Evolution, Anthropology"
    VALUE_20303_ANIMAL_ECOLOGY_BIODIVERSITY_AND_ECOSYSTEM_RESEARCH = (
        "20303 Animal Ecology, Biodiversity and Ecosystem Research"
    )
    VALUE_20304_SENSORY_AND_BEHAVIOURAL_BIOLOGY = "20304 Sensory and Behavioural Biology"
    VALUE_20305_BIOCHEMISTRY_AND_ANIMAL_PHYSIOLOGY = "20305 Biochemistry and Animal Physiology"
    VALUE_20306_ANIMAL_GENETICS_CELL_AND_DEVELOPMENTAL_BIOLOGY = "20306 Animal Genetics, Cell and Developmental Biology"
    VALUE_22_MEDICINE = "22 Medicine"
    VALUE_204_MICROBIOLOGY_VIROLOGY_AND_IMMUNOLOGY = "204 Microbiology, Virology and Immunology"
    VALUE_20401_METABOLISM_BIOCHEMISTRY_AND_GENETICS_OF_MICROORGANISMS = (
        "20401 Metabolism, Biochemistry and Genetics of Microorganisms"
    )
    VALUE_20402_MICROBIAL_ECOLOGY_AND_APPLIED_MICROBIOLOGY = "20402 Microbial Ecology and Applied Microbiology"
    VALUE_20403_MEDICAL_MICROBIOLOGY_MOLECULAR_INFECTION_BIOLOGY = (
        "20403 Medical Microbiology, Molecular Infection Biology"
    )
    VALUE_20404_VIROLOGY = "20404 Virology"
    VALUE_20405_IMMUNOLOGY = "20405 Immunology"
    VALUE_205_MEDICINE = "205 Medicine"
    VALUE_20501_EPIDEMIOLOGY_MEDICAL_BIOMETRY_MEDICAL_INFORMATICS = (
        "20501 Epidemiology, Medical Biometry, Medical Informatics"
    )
    VALUE_20502_PUBLIC_HEALTH_HEALTH_SERVICES_RESEARCH_SOCIAL_MEDICINE = (
        "20502 Public Health, Health Services Research, Social Medicine"
    )
    VALUE_20503_HUMAN_GENETICS = "20503 Human Genetics"
    VALUE_20504_PHYSIOLOGY = "20504 Physiology"
    VALUE_20505_NUTRITIONAL_SCIENCES = "20505 Nutritional Sciences"
    VALUE_20506_PATHOLOGY_AND_FORENSIC_MEDICINE = "20506 Pathology and Forensic Medicine"
    VALUE_20507_CLINICAL_CHEMISTRY_AND_PATHOBIOCHEMISTRY = "20507 Clinical Chemistry and Pathobiochemistry"
    VALUE_20508_PHARMACY = "20508 Pharmacy"
    VALUE_20509_PHARMACOLOGY = "20509 Pharmacology"
    VALUE_20510_TOXICOLOGY_AND_OCCUPATIONAL_MEDICINE = "20510 Toxicology and Occupational Medicine"
    VALUE_20511_ANAESTHESIOLOGY = "20511 Anaesthesiology"
    VALUE_20512_CARDIOLOGY_ANGIOLOGY = "20512 Cardiology, Angiology"
    VALUE_20513_PNEUMOLOGY_CLINICAL_INFECTIOLOGY_INTENSIVE_CARE_MEDICINE = (
        "20513 Pneumology, Clinical Infectiology Intensive Care Medicine"
    )
    VALUE_20514_HEMATOLOGY_ONCOLOGY_TRANSFUSION_MEDICINE = "20514 Hematology, Oncology, Transfusion Medicine"
    VALUE_20515_GASTROENTEROLOGY_METABOLISM = "20515 Gastroenterology, Metabolism"
    VALUE_20516_NEPHROLOGY = "20516 Nephrology"
    VALUE_20517_ENDOCRINOLOGY_DIABETOLOGY = "20517 Endocrinology, Diabetology"
    VALUE_20518_RHEUMATOLOGY_CLINICAL_IMMUNOLOGY_ALLERGOLOGY = "20518 Rheumatology, Clinical Immunology, Allergology"
    VALUE_20519_DERMATOLOGY = "20519 Dermatology"
    VALUE_20520_PEDIATRIC_AND_ADOLESCENT_MEDICINE = "20520 Pediatric and Adolescent Medicine"
    VALUE_20521_GYNAECOLOGY_AND_OBSTETRICS = "20521 Gynaecology and Obstetrics"
    VALUE_20522_REPRODUCTIVE_MEDICINE_BIOLOGY = "20522 Reproductive Medicine/Biology"
    VALUE_20523_UROLOGY = "20523 Urology"
    VALUE_20524_GERONTOLOGY_AND_GERIATRIC_MEDICINE = "20524 Gerontology and Geriatric Medicine"
    VALUE_20525_VASCULAR_AND_VISCERAL_SURGERY = "20525 Vascular and Visceral Surgery"
    VALUE_20526_CARDIOTHORACIC_SURGERY = "20526 Cardiothoracic Surgery"
    VALUE_20527_TRAUMATOLOGY_AND_ORTHOPAEDICS = "20527 Traumatology and Orthopaedics"
    VALUE_20528_DENTISTRY_ORAL_SURGERY = "20528 Dentistry, Oral Surgery"
    VALUE_20529_OTOLARYNGOLOGY = "20529 Otolaryngology"
    VALUE_20530_RADIOLOGY_AND_NUCLEAR_MEDICINE = "20530 Radiology and Nuclear Medicine"
    VALUE_20531_RADIATION_ONCOLOGY_AND_RADIOBIOLOGY = "20531 Radiation Oncology and Radiobiology"
    VALUE_20532_BIOMEDICAL_TECHNOLOGY_AND_MEDICAL_PHYSICS = "20532 Biomedical Technology and Medical Physics"
    VALUE_206_NEUROSCIENCES = "206 Neurosciences"
    VALUE_20601_MOLECULAR_NEUROSCIENCE_AND_NEUROGENETICS = "20601 Molecular Neuroscience and Neurogenetics"
    VALUE_20602_CELLULAR_NEUROSCIENCE = "20602 Cellular Neuroscience"
    VALUE_20603_DEVELOPMENTAL_NEUROBIOLOGY = "20603 Developmental Neurobiology"
    VALUE_20604_SYSTEMIC_NEUROSCIENCE_COMPUTATIONAL_NEUROSCIENCE_BEHAVIOUR = (
        "20604 Systemic Neuroscience, Computational Neuroscience, Behaviour"
    )
    VALUE_20605_COMPARATIVE_NEUROBIOLOGY = "20605 Comparative Neurobiology"
    VALUE_20606_COGNITIVE_NEUROSCIENCE_AND_NEUROIMAGING = "20606 Cognitive Neuroscience and Neuroimaging"
    VALUE_20607_MOLECULAR_NEUROLOGY = "20607 Molecular Neurology"
    VALUE_20608_CLINICAL_NEUROSCIENCES_I_NEUROLOGY_NEUROSURGERY = (
        "20608 Clinical Neurosciences I - Neurology, Neurosurgery"
    )
    VALUE_20609_BIOLOGICAL_PSYCHIATRY = "20609 Biological Psychiatry"
    VALUE_20610_CLINICAL_NEUROSCIENCES_II_PSYCHIATRY_PSYCHOTHERAPY_PSYCHOSOMATIC_MEDICINE = (
        "20610 Clinical Neurosciences II - Psychiatry, Psychotherapy, Psychosomatic Medicine"
    )
    VALUE_20611_CLINICAL_NEUROSCIENCES_III_OPHTHALMOLOGY = "20611 Clinical Neurosciences III - Ophthalmology"
    VALUE_23_AGRICULTURE_FORESTRY_HORTICULTURE_AND_VETERINARY_MEDICINE = (
        "23 Agriculture, Forestry, Horticulture and Veterinary Medicine"
    )
    VALUE_207_AGRICULTURE_FORESTRY_HORTICULTURE_AND_VETERINARY_MEDICINE = (
        "207 Agriculture, Forestry, Horticulture and Veterinary Medicine"
    )
    VALUE_20701_SOIL_SCIENCES = "20701 Soil Sciences"
    VALUE_20702_PLANT_CULTIVATION = "20702 Plant Cultivation"
    VALUE_20703_PLANT_NUTRITION = "20703 Plant Nutrition"
    VALUE_20704_ECOLOGY_OF_AGRICULTURAL_LANDSCAPES = "20704 Ecology of Agricultural Landscapes"
    VALUE_20705_PLANT_BREEDING = "20705 Plant Breeding"
    VALUE_20706_PHYTOMEDICINE = "20706 Phytomedicine"
    VALUE_20707_AGRICULTURAL_AND_FOOD_PROCESS_ENGINEERING = "20707 Agricultural and Food Process Engineering"
    VALUE_20708_AGRICULTURAL_ECONOMICS_AND_SOCIOLOGY = "20708 Agricultural Economics and Sociology"
    VALUE_20709_INVENTORY_CONTROL_AND_USE_OF_FOREST_RESOURCES = "20709 Inventory Control and Use of Forest Resources"
    VALUE_20710_BASIC_FOREST_RESEARCH = "20710 Basic Forest Research"
    VALUE_20711_ANIMAL_HUSBANDRY_BREEDING_AND_HYGIENE = "20711 Animal Husbandry, Breeding and Hygiene"
    VALUE_20712_ANIMAL_NUTRITION_AND_NUTRITION_PHYSIOLOGY = "20712 Animal Nutrition and Nutrition Physiology"
    VALUE_20713_BASIC_VETERINARY_MEDICAL_SCIENCE = "20713 Basic Veterinary Medical Science"
    VALUE_20714_BASIC_RESEARCH_ON_PATHOGENESIS_DIAGNOSTICS_AND_THERAPY_AND_CLINICAL_VETERINARY_MEDICINE = (
        "20714 Basic Research on Pathogenesis, Diagnostics and Therapy and Clinical Veterinary Medicine"
    )
    VALUE_3_NATURAL_SCIENCES = "3 Natural Sciences"
    VALUE_31_CHEMISTRY = "31 Chemistry"
    VALUE_301_MOLECULAR_CHEMISTRY = "301 Molecular Chemistry"
    VALUE_30101_INORGANIC_MOLECULAR_CHEMISTRY = "30101 Inorganic Molecular Chemistry"
    VALUE_30102_ORGANIC_MOLECULAR_CHEMISTRY = "30102 Organic Molecular Chemistry"
    VALUE_302_CHEMICAL_SOLID_STATE_AND_SURFACE_RESEARCH = "302 Chemical Solid State and Surface Research"
    VALUE_30201_SOLID_STATE_AND_SURFACE_CHEMISTRY_MATERIAL_SYNTHESIS = (
        "30201 Solid State and Surface Chemistry, Material Synthesis"
    )
    VALUE_30202_PHYSICAL_CHEMISTRY_OF_SOLIDS_AND_SURFACES_MATERIAL_CHARACTERISATION = (
        "30202 Physical Chemistry of Solids and Surfaces, Material Characterisation"
    )
    VALUE_30203_THEORY_AND_MODELLING = "30203 Theory and Modelling"
    VALUE_303_PHYSICAL_AND_THEORETICAL_CHEMISTRY = "303 Physical and Theoretical Chemistry"
    VALUE_30301_PHYSICAL_CHEMISTRY_OF_MOLECULES_INTERFACES_AND_LIQUIDS_SPECTROSCOPY_KINETICS = (
        "30301 Physical Chemistry of Molecules, Interfaces and Liquids - Spectroscopy, Kinetics"
    )
    VALUE_30302_GENERAL_THEORETICAL_CHEMISTRY = "30302 General Theoretical Chemistry"
    VALUE_304_ANALYTICAL_CHEMISTRY_METHOD_DEVELOPMENT_CHEMISTRY = (
        "304 Analytical Chemistry, Method Development (Chemistry)"
    )
    VALUE_30401_ANALYTICAL_CHEMISTRY_METHOD_DEVELOPMENT_CHEMISTRY = (
        "30401 Analytical Chemistry, Method Development (Chemistry)"
    )
    VALUE_305_BIOLOGICAL_CHEMISTRY_AND_FOOD_CHEMISTRY = "305 Biological Chemistry and Food Chemistry"
    VALUE_30501_BIOLOGICAL_AND_BIOMIMETIC_CHEMISTRY = "30501 Biological and Biomimetic Chemistry"
    VALUE_30502_FOOD_CHEMISTRY = "30502 Food Chemistry"
    VALUE_306_POLYMER_RESEARCH = "306 Polymer Research"
    VALUE_30601_PREPARATORY_AND_PHYSICAL_CHEMISTRY_OF_POLYMERS = "30601 Preparatory and Physical Chemistry of Polymers"
    VALUE_30602_EXPERIMENTAL_AND_THEORETICAL_PHYSICS_OF_POLYMERS = (
        "30602 Experimental and Theoretical Physics of Polymers"
    )
    VALUE_30603_POLYMER_MATERIALS = "30603 Polymer Materials"
    VALUE_32_PHYSICS = "32 Physics"
    VALUE_307_CONDENSED_MATTER_PHYSICS = "307 Condensed Matter Physics"
    VALUE_30701_EXPERIMENTAL_CONDENSED_MATTER_PHYSICS = "30701 Experimental Condensed Matter Physics"
    VALUE_30702_THEORETICAL_CONDENSED_MATTER_PHYSICS = "30702 Theoretical Condensed Matter Physics"
    VALUE_308_OPTICS_QUANTUM_OPTICS_AND_PHYSICS_OF_ATOMS_MOLECULES_AND_PLASMAS = (
        "308 Optics, Quantum Optics and Physics of Atoms, Molecules and Plasmas"
    )
    VALUE_30801_OPTICS_QUANTUM_OPTICS_ATOMS_MOLECULES_PLASMAS = (
        "30801 Optics, Quantum Optics, Atoms, Molecules, Plasmas"
    )
    VALUE_309_PARTICLES_NUCLEI_AND_FIELDS = "309 Particles, Nuclei and Fields"
    VALUE_30901_PARTICLES_NUCLEI_AND_FIELDS = "30901 Particles, Nuclei and Fields"
    VALUE_310_STATISTICAL_PHYSICS_SOFT_MATTER_BIOLOGICAL_PHYSICS_NONLINEAR_DYNAMICS = (
        "310 Statistical Physics, Soft Matter, Biological Physics, Nonlinear Dynamics"
    )
    VALUE_31001_STATISTICAL_PHYSICS_SOFT_MATTER_BIOLOGICAL_PHYSICS_NONLINEAR_DYNAMICS = (
        "31001 Statistical Physics, Soft Matter, Biological Physics, Nonlinear Dynamics"
    )
    VALUE_311_ASTROPHYSICS_AND_ASTRONOMY = "311 Astrophysics and Astronomy"
    VALUE_31101_ASTROPHYSICS_AND_ASTRONOMY = "31101 Astrophysics and Astronomy"
    VALUE_33_MATHEMATICS = "33 Mathematics"
    VALUE_312_MATHEMATICS = "312 Mathematics"
    VALUE_31201_MATHEMATICS = "31201 Mathematics"
    VALUE_34_GEOSCIENCES_INCLUDING_GEOGRAPHY = "34 Geosciences (including Geography)"
    VALUE_313_ATMOSPHERIC_SCIENCE_AND_OCEANOGRAPHY = "313 Atmospheric Science and Oceanography"
    VALUE_31301_ATMOSPHERIC_SCIENCE = "31301 Atmospheric Science"
    VALUE_31302_OCEANOGRAPHY = "31302 Oceanography"
    VALUE_314_GEOLOGY_AND_PALAEONTOLOGY = "314 Geology and Palaeontology"
    VALUE_31401_GEOLOGY_AND_PALAEONTOLOGY = "31401 Geology and Palaeontology"
    VALUE_315_GEOPHYSICS_AND_GEODESY = "315 Geophysics and Geodesy"
    VALUE_31501_GEOPHYSICS = "31501 Geophysics"
    VALUE_31502_GEODESY_PHOTOGRAMMETRY_REMOTE_SENSING_GEOINFORMATICS_CARTOGAPHY = (
        "31502 Geodesy, Photogrammetry, Remote Sensing, Geoinformatics, Cartogaphy"
    )
    VALUE_316_GEOCHEMISTRY_MINERALOGY_AND_CRYSTALLOGRAPHY = "316 Geochemistry, Mineralogy and Crystallography"
    VALUE_31601_GEOCHEMISTRY_MINERALOGY_AND_CRYSTALLOGRAPHY = "31601 Geochemistry, Mineralogy and Crystallography"
    VALUE_317_GEOGRAPHY = "317 Geography"
    VALUE_31701_PHYSICAL_GEOGRAPHY = "31701 Physical Geography"
    VALUE_31702_HUMAN_GEOGRAPHY = "31702 Human Geography"
    VALUE_318_WATER_RESEARCH = "318 Water Research"
    VALUE_31801_HYDROGEOLOGY_HYDROLOGY_LIMNOLOGY_URBAN_WATER_MANAGEMENT_WATER_CHEMISTRY_INTEGRATED_WATER_RESOURCES_MANAGEMENT = "31801 Hydrogeology, Hydrology, Limnology, Urban Water Management, Water Chemistry, Integrated Water Resources Management"
    VALUE_4_ENGINEERING_SCIENCES = "4 Engineering Sciences"
    VALUE_41_MECHANICAL_AND_INDUSTRIAL_ENGINEERING = "41 Mechanical and industrial Engineering"
    VALUE_401_PRODUCTION_TECHNOLOGY = "401 Production Technology"
    VALUE_40101_METAL_CUTTING_MANUFACTURING_ENGINEERING = "40101 Metal-Cutting Manufacturing Engineering"
    VALUE_40102_PRIMARY_SHAPING_AND_RESHAPING_TECHNOLOGY = "40102 Primary Shaping and Reshaping Technology"
    VALUE_40103_MICRO_PRECISION_MOUNTING_JOINING_SEPARATION_TECHNOLOGY = (
        "40103 Micro-, Precision, Mounting, Joining, Separation Technology"
    )
    VALUE_40104_PLASTICS_ENGINEERING = "40104 Plastics Engineering"
    VALUE_40105_PRODUCTION_AUTOMATION_FACTORY_OPERATION_OPERATIONS_MANANGEMENT = (
        "40105 Production Automation, Factory Operation, Operations Manangement"
    )
    VALUE_402_MECHANICS_AND_CONSTRUCTIVE_MECHANICAL_ENGINEERING = (
        "402 Mechanics and Constructive Mechanical Engineering"
    )
    VALUE_40201_CONSTRUCTION_MACHINE_ELEMENTS = "40201 Construction, Machine Elements"
    VALUE_40202_MECHANICS = "40202 Mechanics"
    VALUE_40203_LIGHTWEIGHT_CONSTRUCTION_TEXTILE_TECHNOLOGY = "40203 Lightweight Construction, Textile Technology"
    VALUE_40204_ACOUSTICS = "40204 Acoustics"
    VALUE_42_THERMAL_ENGINEERING_PROCESS_ENGINEERING = "42 Thermal Engineering/Process Engineering"
    VALUE_403_PROCESS_ENGINEERING_TECHNICAL_CHEMISTRY = "403 Process Engineering, Technical Chemistry"
    VALUE_40301_CHEMICAL_AND_THERMAL_PROCESS_ENGINEERING = "40301 Chemical and Thermal Process Engineering"
    VALUE_40302_TECHNICAL_CHEMISTRY = "40302 Technical Chemistry"
    VALUE_40303_MECHANICAL_PROCESS_ENGINEERING = "40303 Mechanical Process Engineering"
    VALUE_40304_BIOLOGICAL_PROCESS_ENGINEERING = "40304 Biological Process Engineering"
    VALUE_404_HEAT_ENERGY_TECHNOLOGY_THERMAL_MACHINES_FLUID_MECHANICS = (
        "404 Heat Energy Technology, Thermal Machines, Fluid Mechanics"
    )
    VALUE_40401_ENERGY_PROCESS_ENGINEERING = "40401 Energy Process Engineering"
    VALUE_40402_TECHNICAL_THERMODYNAMICS = "40402 Technical Thermodynamics"
    VALUE_40403_FLUID_MECHANICS = "40403 Fluid Mechanics"
    VALUE_40404_HYDRAULIC_AND_TURBO_ENGINES_AND_PISTON_ENGINES = "40404 Hydraulic and Turbo Engines and Piston Engines"
    VALUE_43_MATERIALS_SCIENCE_AND_ENGINEERING = "43 Materials Science and Engineering"
    VALUE_405_MATERIALS_ENGINEERING = "405 Materials Engineering"
    VALUE_40501_METALLURGICAL_AND_THERMAL_PROCESSES_THERMOMECHANICAL_TREATMENT_OF_MATERIALS = (
        "40501 Metallurgical and Thermal Processes, Thermomechanical Treatment of Materials"
    )
    VALUE_40502_SINTERED_METALLIC_AND_CERAMIC_MATERIALS = "40502 Sintered Metallic and Ceramic Materials"
    VALUE_40503_COMPOSITE_MATERIALS = "40503 Composite Materials"
    VALUE_40504_MECHANICAL_BEHAVIOUR_OF_CONSTRUCTION_MATERIALS = "40504 Mechanical Behaviour of Construction Materials"
    VALUE_40505_COATING_AND_SURFACE_TECHNOLOGY = "40505 Coating and Surface Technology"
    VALUE_406_MATERIALS_SCIENCE = "406 Materials Science"
    VALUE_40601_THERMODYNAMICS_AND_KINETICS_OF_MATERIALS = "40601 Thermodynamics and Kinetics of Materials"
    VALUE_40602_SYNTHESIS_AND_PROPERTIES_OF_FUNCTIONAL_MATERIALS = (
        "40602 Synthesis and Properties of Functional Materials"
    )
    VALUE_40603_MICROSTRUCTURAL_MECHANICAL_PROPERTIES_OF_MATERIALS = (
        "40603 Microstructural Mechanical Properties of Materials"
    )
    VALUE_40604_STRUCTURING_AND_FUNCTIONALISATION = "40604 Structuring and Functionalisation"
    VALUE_40605_BIOMATERIALS = "40605 Biomaterials"
    VALUE_44_COMPUTER_SCIENCE_ELECTRICAL_AND_SYSTEM_ENGINEERING = (
        "44 Computer Science, Electrical and System Engineering"
    )
    VALUE_407_SYSTEMS_ENGINEERING = "407 Systems Engineering"
    VALUE_40701_AUTOMATION_CONTROL_SYSTEMS_ROBOTICS_MECHATRONICS = (
        "40701 Automation, Control Systems, Robotics, Mechatronics"
    )
    VALUE_40702_MEASUREMENT_SYSTEMS = "40702 Measurement Systems"
    VALUE_40703_MICROSYSTEMS = "40703 Microsystems"
    VALUE_40704_TRAFFIC_AND_TRANSPORT_SYSTEMS_LOGISTICS = "40704 Traffic and Transport Systems, Logistics"
    VALUE_40705_HUMAN_FACTORS_ERGONOMICS_HUMAN_MACHINE_SYSTEMS = (
        "40705 Human Factors, Ergonomics, Human-Machine Systems"
    )
    VALUE_408_ELECTRICAL_ENGINEERING = "408 Electrical Engineering"
    VALUE_40801_ELECTRONIC_SEMICONDUCTORS_COMPONENTS_CIRCUITS_SYSTEMS = (
        "40801 Electronic Semiconductors, Components, Circuits, Systems"
    )
    VALUE_40802_COMMUNICATION_HIGH_FREQUENCY_AND_NETWORK_TECHNOLOGY_THEORETICAL_ELECTRICAL_ENGINEERING = (
        "40802 Communication, High-Frequency and Network Technology, Theoretical Electrical Engineering"
    )
    VALUE_40803_ELECTRICAL_ENERGY_GENERATION_DISTRIBUTION_APPLICATION = (
        "40803 Electrical Energy Generation, Distribution, Application"
    )
    VALUE_409_COMPUTER_SCIENCE = "409 Computer Science"
    VALUE_40901_THEORETICAL_COMPUTER_SCIENCE = "40901 Theoretical Computer Science"
    VALUE_40902_SOFTWARE_TECHNOLOGY = "40902 Software Technology"
    VALUE_40903_OPERATING_COMMUNICATION_AND_INFORMATION_SYSTEMS = (
        "40903 Operating, Communication and Information Systems"
    )
    VALUE_40904_ARTIFICIAL_INTELLIGENCE_IMAGE_AND_LANGUAGE_PROCESSING = (
        "40904 Artificial Intelligence, Image and Language Processing"
    )
    VALUE_40905_COMPUTER_ARCHITECTURE_AND_EMBEDDED_SYSTEMS = "40905 Computer Architecture and Embedded Systems"
    VALUE_45_CONSTRUCTION_ENGINEERING_AND_ARCHITECTURE = "45 Construction Engineering and Architecture"
    VALUE_410_CONSTRUCTION_ENGINEERING_AND_ARCHITECTURE = "410 Construction Engineering and Architecture"
    VALUE_41001_ARCHITECTURE_BUILDING_AND_CONSTRUCTION_HISTORY_SUSTAINABLE_BUILDING_TECHNOLOGY_BUILDING_DESIGN = (
        "41001 Architecture, Building and Construction History, Sustainable Building Technology, Building Design"
    )
    VALUE_41002_URBANISM_SPATIAL_PLANNING_TRANSPORTATION_AND_INFRASTRUCTURE_PLANNING_LANDSCAPE_PLANNING = (
        "41002 Urbanism, Spatial Planning, Transportation and Infrastructure Planning, Landscape Planning"
    )
    VALUE_41003_CONSTRUCTION_MATERIAL_SCIENCES_CHEMISTRY_BUILDING_PHYSICS = (
        "41003 Construction Material Sciences, Chemistry, Building Physics"
    )
    VALUE_41004_STRUCTURAL_ENGINEERING_BUILDING_INFORMATICS_CONSTRUCTION_OPERATION = (
        "41004 Structural Engineering, Building Informatics, Construction Operation"
    )
    VALUE_41005_APPLIED_MECHANICS_STATICS_AND_DYNAMICS = "41005 Applied Mechanics, Statics and Dynamics"
    VALUE_41006_GEOTECHNICS_HYDRAULIC_ENGINEERING = "41006 Geotechnics, Hydraulic Engineering"


class SyndicationTypes(Enum):
    ATOM = "ATOM"
    RSS = "RSS"
    OTHER = "other"


class Yesno(Enum):
    YES = "yes"
    NO = "no"


class Yesnoun(Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class AdditionalName:
    """Attributes:
    value:
    language: Language of the research data repository additional name.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: None | Languages = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Api:
    """Attributes:
    value:
    api_type: Type of API.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    api_type: None | ApiTypes = field(
        default=None,
        metadata={
            "name": "apiType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class ContentType:
    """Attributes:
    value:
    content_type_scheme: The name and/or URL of the subject scheme or classification code (e.g.parse).
    """

    class Meta:
        global_type = False

    value: None | ContentTypeText = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    content_type_scheme: None | ContentTypeScheme = field(
        default=None,
        metadata={
            "name": "contentTypeScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class DataAccess:
    """Attributes:
    data_access_type: Type of access to data.
    data_access_restriction: All existing access restrictions to the research data. (Required if restricted
        is chosen).
    """

    class Meta:
        global_type = False

    data_access_type: None | DataAccessTypes = field(
        default=None,
        metadata={
            "name": "dataAccessType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    data_access_restriction: list[DataAccessRestrictions] = field(
        default_factory=list,
        metadata={
            "name": "dataAccessRestriction",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )


@dataclass(slots=True)
class DataLicense:
    """Attributes:
    data_license_name: Name of the data license.
    data_license_url: Data license URL.
    """

    class Meta:
        global_type = False

    data_license_name: None | DataLicenseNames = field(
        default=None,
        metadata={
            "name": "dataLicenseName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    data_license_url: None | str = field(
        default=None,
        metadata={
            "name": "dataLicenseURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


@dataclass(slots=True)
class DataUpload:
    """Attributes:
    data_upload_type: Type of data upload.
    data_upload_restriction: All existing restrictions to the data upload. (Required if restricted is
        chosen).
    """

    class Meta:
        global_type = False

    data_upload_type: None | AccessTypes = field(
        default=None,
        metadata={
            "name": "dataUploadType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    data_upload_restriction: list[DataUploadRestrictions] = field(
        default_factory=list,
        metadata={
            "name": "dataUploadRestriction",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )


@dataclass(slots=True)
class DatabaseAccess:
    """Attributes:
    database_access_type: Type of access to the research data repository.
    database_access_restriction: All existing access restrictions to the research data repository. (Required
        if restricted is chosen).
    """

    class Meta:
        global_type = False

    database_access_type: None | AccessTypes = field(
        default=None,
        metadata={
            "name": "databaseAccessType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    database_access_restriction: list[AccessRestrictions] = field(
        default_factory=list,
        metadata={
            "name": "databaseAccessRestriction",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )


@dataclass(slots=True)
class DatabaseLicense:
    """Attributes:
    database_license_name: Name of database license.
    database_license_url: Database license URL.
    """

    class Meta:
        global_type = False

    database_license_name: None | DatabaseLicenseNames = field(
        default=None,
        metadata={
            "name": "databaseLicenseName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    database_license_url: None | str = field(
        default=None,
        metadata={
            "name": "databaseLicenseURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


@dataclass(slots=True)
class Description:
    """Attributes:
    value:
    language: Language of the research data repository description.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1000,
        },
    )
    language: None | Languages = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class InstitutionAdditionalName:
    """Attributes:
    value:
    language: Language of the institution additional name.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: None | Languages = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class InstitutionName:
    """Attributes:
    value:
    language: Language of the institution name.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: None | Languages = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class MetadataStandardName:
    """Attributes:
    value:
    metadata_standard_scheme: The scheme of the metadata standards.
    """

    class Meta:
        global_type = False

    value: None | MetadataStandardDccnames = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    metadata_standard_scheme: None | MetadataStandardScheme = field(
        default=None,
        metadata={
            "name": "metadataStandardScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class RepositoryName:
    """Attributes:
    value:
    language: Language of the research data repository name.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: None | Languages = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Software:
    """Attributes:
    software_name: Name of the research data repository software.
    """

    class Meta:
        global_type = False

    software_name: None | SoftwareNames = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


@dataclass(slots=True)
class Subject:
    """Attributes:
    value:
    subject_scheme: The subject scheme according to which the subject (see ID 13 subject) of the research
        data repository described.
    """

    class Meta:
        global_type = False

    value: None | SubjectText = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    subject_scheme: None | SubjectScheme = field(
        default=None,
        metadata={
            "name": "subjectScheme",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Syndication:
    """Attributes:
    value:
    syndication_type: Type of alerting service.
    """

    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    syndication_type: None | SyndicationTypes = field(
        default=None,
        metadata={
            "name": "syndicationType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Institution:
    """Attributes:
    institution_name: Name of the responsible institution.
    institution_additional_name: The alternative name or acronym for the responsible institution.
    institution_country: Location of the responsible institution.
    responsibility_type: Type of responsibility for each responsible institution.
    institution_type: Type of responsible institution.
    institution_url: URL of the responsible institution.
    institution_identifier: A globally unique identifier that refers to the institution (e.g. ISNI, VIAF,
        GND).
    responsibility_start_date: Start date of period of responsibility.
    responsibility_end_date: End date of period of responsibility.
    institution_contact: Email address of the contact or an URL of an online contact form of the institution.
    """

    class Meta:
        global_type = False

    institution_name: None | InstitutionName = field(
        default=None,
        metadata={
            "name": "institutionName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    institution_additional_name: list[InstitutionAdditionalName] = field(
        default_factory=list,
        metadata={
            "name": "institutionAdditionalName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    institution_country: None | Countries = field(
        default=None,
        metadata={
            "name": "institutionCountry",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    responsibility_type: list[ResponsibilityTypes] = field(
        default_factory=list,
        metadata={
            "name": "responsibilityType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    institution_type: None | InstitutionTypes = field(
        default=None,
        metadata={
            "name": "institutionType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    institution_url: None | str = field(
        default=None,
        metadata={
            "name": "institutionURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    institution_identifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "institutionIdentifier",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    # Note: Unfortunately, we had to add `str` type manually.
    responsibility_start_date: None | XmlPeriod | XmlDate | str = field(
        default=None,
        metadata={
            "name": "responsibilityStartDate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )
    # Note: Unfortunately, we had to add `str` type manually.
    responsibility_end_date: None | XmlPeriod | XmlDate | str = field(
        default=None,
        metadata={
            "name": "responsibilityEndDate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )
    institution_contact: list[str] = field(
        default_factory=list,
        metadata={
            "name": "institutionContact",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )


@dataclass(slots=True)
class MetadataStandard:
    """Attributes:
    metadata_standard_name: Metadata standards the research data repository complies with.
    metadata_standard_url: The URL of the metadata standard.
    """

    class Meta:
        global_type = False

    metadata_standard_name: None | MetadataStandardName = field(
        default=None,
        metadata={
            "name": "metadataStandardName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    metadata_standard_url: None | MetadataStandardDccurls = field(
        default=None,
        metadata={
            "name": "metadataStandardURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )


@dataclass(slots=True)
class Repository(IdMixin):
    """Attributes:
    re3data_org_identifier: A globally unique and persistent identifier that refers to the research data
        repository entry in re3data.dorg. The ID is assigned by re3data.org.
    repository_name: The full name of the research data repository.
    additional_name: The alternative name or acronym for the research data repository.
    repository_url: The URL, which gives reference to the research data repository.
    repository_identifier: A globally unique identifier (identifier in form of a link) that refers to the
        research data repository (e.g. DOI, URN, VIAF, GND).
    description: A textual description containing additional information about the data repository (primary
        language is English).
    repository_contact: Email address of the contact or an URL of an online contact form of the repository.
    type_value: The type of the research data repository.
    size: The number of items contained in the research data repository.
    start_date: Releasing date of the research data repository.
    end_date: Date when the research data repository went offline or stopped ingesting new research data
        (still making the research data available).
    repository_language: The user interface language of the research data repository.
    subject: The subject(s) of the research data repository.
    mission_statement_url: The URL of a mission statement describing the designated community of the research
        data repository.
    content_type: All types of resources available in the research data repository.
    provider_type: The type of provider.
    keyword: English keyword(s) describing the subject focus of the research data repository.
    institution: All institutions being responsible for funding, creating and/or running the research data
        repository (wrapper element).
    policy: Any kind of policy (e.g. data policy, etc.) provided by the research data repository to clarify
        legal aspects (wrapper element).
    database_access: (wrapper element)
    database_license: Database license of the research data repository (wrapper element).
    data_access: (wrapper element)
    data_license: License of the data, existing in the research data repository. (wrapper element)
    data_upload: (wrapper element)
    data_upload_license: The license for data upload (wrapper element).
    software: The software that is used to run the research data repository (wrapper element).
    versioning: The research data repository supports versioning of research data.
    api: API URL.
    pid_system: The persistent identifier system that is used by the research data repository.
    citation_guideline_url: The URL of the research data repository providing information on how to cite its
        research data. The DataCite citation format is recommended (http://www.datacite.org/whycitedata).
    aid_system: The author identifier system that is used by the research data repository.
    enhanced_publication: The research data repository offers the interlinking between publications and data.
    quality_management: Any form of quality management concerning the data or metadata of the research data
        repository.
    certificate: The certificate, seal or standard the research data repository complies with.
    metadata_standard: (wrapper element)
    syndication: URL of the alerting service(s) provided by the research data repository.
    remarks: Additional remarks that are visible to all users.
    entry_date: The date the research data repository was indexed in re3data.org.
    last_update: The date the metadata of the research data repository was updated.
    """

    class Meta:
        global_type = False

    re3data_org_identifier: None | str = field(
        default=None,
        metadata={
            "name": "re3data.orgIdentifier",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    repository_name: None | RepositoryName = field(
        default=None,
        metadata={
            "name": "repositoryName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    additional_name: list[AdditionalName] = field(
        default_factory=list,
        metadata={
            "name": "additionalName",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    repository_url: None | str = field(
        default=None,
        metadata={
            "name": "repositoryURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    repository_identifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "repositoryIdentifier",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    repository_contact: list[str] = field(
        default_factory=list,
        metadata={
            "name": "repositoryContact",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    type_value: list[RepositoryTypes] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    size: None | Size = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    # Note: Unfortunately, we had to add `str` type manually.
    start_date: None | XmlPeriod | XmlDate | str = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )
    # Note: Unfortunately, we had to add `str` type manually.
    end_date: None | XmlPeriod | XmlDate | str = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )
    repository_language: list[Languages] = field(
        default_factory=list,
        metadata={
            "name": "repositoryLanguage",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    subject: list[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    mission_statement_url: None | str = field(
        default=None,
        metadata={
            "name": "missionStatementURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    content_type: list[ContentType] = field(
        default_factory=list,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    provider_type: list[ProviderTypes] = field(
        default_factory=list,
        metadata={
            "name": "providerType",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    keyword: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    policy: list[Policy] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    database_access: None | DatabaseAccess = field(
        default=None,
        metadata={
            "name": "databaseAccess",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
        },
    )
    database_license: list[DatabaseLicense] = field(
        default_factory=list,
        metadata={
            "name": "databaseLicense",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    data_access: list[DataAccess] = field(
        default_factory=list,
        metadata={
            "name": "dataAccess",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    data_license: list[DataLicense] = field(
        default_factory=list,
        metadata={
            "name": "dataLicense",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    data_upload: list[DataUpload] = field(
        default_factory=list,
        metadata={
            "name": "dataUpload",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    data_upload_license: list[DataUploadLicense] = field(
        default_factory=list,
        metadata={
            "name": "dataUploadLicense",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    software: list[Software] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    versioning: None | Yesno = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    api: list[Api] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    pid_system: list[PidSystems] = field(
        default_factory=list,
        metadata={
            "name": "pidSystem",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "min_occurs": 1,
        },
    )
    citation_guideline_url: None | str = field(
        default=None,
        metadata={
            "name": "citationGuidelineURL",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    aid_system: list[AidSystems] = field(
        default_factory=list,
        metadata={
            "name": "aidSystem",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    enhanced_publication: None | Yesnoun = field(
        default=None,
        metadata={
            "name": "enhancedPublication",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    quality_management: None | Yesnoun = field(
        default=None,
        metadata={
            "name": "qualityManagement",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    certificate: list[Certificates] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    metadata_standard: list[MetadataStandard] = field(
        default_factory=list,
        metadata={
            "name": "metadataStandard",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    syndication: list[Syndication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    remarks: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
        },
    )
    entry_date: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "name": "entryDate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )
    last_update: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Element",
            "namespace": "http://www.re3data.org/schema/2-2",
            "required": True,
            "min_inclusive": XmlDate(1000, 1, 1),
            "max_inclusive": XmlDate(2999, 12, 31),
        },
    )


@dataclass(slots=True)
class Re3Data:
    class Meta:
        name = "re3data"
        namespace = "http://www.re3data.org/schema/2-2"

    repository: list[Repository] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
