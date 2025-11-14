"""Constants for Syncleo Kettle integration."""
DOMAIN = "syncleo_kettle"
MANUFACTURER = "Polaris IQ Home"

POLARIS_DEVICE = {
    0:   {"model": "Unknown", "class": "all"},
    37:  {"model": "PWK-7111CGLD-WIFI-(old)", "class": "kettle"},
    245: {"model": "PWK-0105", "class": "kettle"},
    205: {"model": "PWK-1538CC", "class": "kettle"},
    271: {"model": "PWK-1701CGLD", "class": "kettle"},
    36:  {"model": "PWK-17107CGLD-WIFI-(old)", "class": "kettle"},
    29:  {"model": "PWK-1712CGLD", "class": "kettle"},
    38:  {"model": "PWK-1712CGLD", "class": "kettle"},
    54:  {"model": "PWK-1712CGLD", "class": "kettle"},
    59:  {"model": "PWK-1712CGLD", "class": "kettle"},
    63:  {"model": "PWK-1712CGLD", "class": "kettle"},
    97:  {"model": "PWK-1712CGLD", "class": "kettle"},
    117: {"model": "PWK-1712CGLD", "class": "kettle"},
    208: {"model": "PWK-1712CGLD", "class": "kettle"},
    83:  {"model": "PWK-1712CGLD-RGB", "class": "kettle"},
    253: {"model": "PWK-1715", "class": "kettle"},
    244: {"model": "PWK-1716CGLD", "class": "kettle"},
    67:  {"model": "PWK-1720CGLD", "class": "kettle"},
    84:  {"model": "PWK-1720CGLD-RGB", "class": "kettle"},
    6:   {"model": "PWK-1725CGLD", "class": "kettle"},
    52:  {"model": "PWK-1725CGLD", "class": "kettle"},
    57:  {"model": "PWK-1725CGLD", "class": "kettle"},
    61:  {"model": "PWK-1725CGLD", "class": "kettle"},
    82:  {"model": "PWK-1725CGLD", "class": "kettle"},
    86:  {"model": "PWK-1725CGLD", "class": "kettle"},
    105: {"model": "PWK-1725CGLD", "class": "kettle"},
    106: {"model": "PWK-1725CGLD", "class": "kettle"},
    177: {"model": "PWK-1725CGLD", "class": "kettle"},
    194: {"model": "PWK-1725CGLD", "class": "kettle"},
    196: {"model": "PWK-1725CGLD", "class": "kettle"},
    164: {"model": "PWK-1728CGLDA", "class": "kettle"},
    209: {"model": "PWK-1729CAD", "class": "kettle"},
    189: {"model": "PWK-1746CA", "class": "kettle"},
    260: {"model": "PWK-1746CA", "class": "kettle"},
    308: {"model": "PWK-1746CA", "class": "kettle"},
    8:   {"model": "PWK-1755CAD", "class": "kettle"},
    53:  {"model": "PWK-1755CAD", "class": "kettle"},
    58:  {"model": "PWK-1755CAD", "class": "kettle"},
    62:  {"model": "PWK-1755CAD", "class": "kettle"},
    185: {"model": "PWK-1755CAD", "class": "kettle"},
    165: {"model": "PWK-1755CAD-VOICE", "class": "kettle"},
    121: {"model": "PWK-1774CAD", "class": "kettle"},
    2:   {"model": "PWK-1775CGLD", "class": "kettle"},
    51:  {"model": "PWK-1775CGLD", "class": "kettle"},
    56:  {"model": "PWK-1775CGLD", "class": "kettle"},
    60:  {"model": "PWK-1775CGLD", "class": "kettle"},
    98:  {"model": "PWK-1775CGLD", "class": "kettle"},
    188: {"model": "PWK-1775CGLD", "class": "kettle"},
    223: {"model": "PWK-1775CGLD", "class": "kettle"},
    262: {"model": "PWK-1775CGLD", "class": "kettle"},
    263: {"model": "PWK-1775CGLD", "class": "kettle"},
    275: {"model": "PWK-1775CGLD", "class": "kettle"},
    294: {"model": "PWK-1775CGLD", "class": "kettle"},
    85:  {"model": "PWK-1775CGLD-SMART", "class": "kettle"},
    139: {"model": "PWK-1775CGLD-VOICE", "class": "kettle"},
    175: {"model": "PWK-1823CGLD", "class": "kettle"},
    254: {"model": "PWK-1823CGLD", "class": "kettle"},
    176: {"model": "PWK-1841CGLD", "class": "kettle"},
    255: {"model": "PWK-1841CGLD", "class": "kettle"},
    147: {"model": "PUH-0205", "class": "humidifier"},
    71:  {"model": "PUH-1010", "class": "humidifier"},
    72:  {"model": "PUH-2300", "class": "humidifier"},
    73:  {"model": "PUH-3030", "class": "humidifier"},
    75:  {"model": "PUH-4040", "class": "humidifier"},
    99:  {"model": "PUH-4040", "class": "humidifier"},
    153: {"model": "PUH-4055", "class": "humidifier"},
    137: {"model": "PUH-4066", "class": "humidifier"},
    157: {"model": "PUH-4550", "class": "humidifier"},
    158: {"model": "PUH-6060", "class": "humidifier"},
    25:  {"model": "PUH-6090", "class": "humidifier"},
    15:  {"model": "PUH-7406", "class": "humidifier"},
    87:  {"model": "PUH-8080/PUH-4606", "class": "humidifier"},
    155: {"model": "PUH-8802", "class": "humidifier"},
    74:  {"model": "PUH-9009", "class": "humidifier"},
    4:   {"model": "PUH-9105/PUH-2709", "class": "humidifier"},
    17:  {"model": "PUH-9105/PUH-2709", "class": "humidifier"},
    18:  {"model": "PUH-9105/PUH-2709", "class": "humidifier"},
    44:  {"model": "PUH-9105/PUH-2709", "class": "humidifier"},
    70:  {"model": "PUH-9105/PUH-2709", "class": "humidifier"},
    1:   {"model": "EVO-0225", "class": "cooker"},
    95:  {"model": "PMC-00000", "class": "cooker"},
    303: {"model": "PMC-0510", "class": "cooker"},
    301: {"model": "PMC-0515", "class": "cooker"},
    10:  {"model": "PMC-0521WIFI", "class": "cooker"},
    41:  {"model": "PMC-0521WIFI", "class": "cooker"},
    267: {"model": "PMC-0521WIFI", "class": "cooker"},
    55:  {"model": "PMC-0524WIFI", "class": "cooker"},
    206: {"model": "PMC-0524WIFI", "class": "cooker"},
    9:   {"model": "PMC-0526WIFI", "class": "cooker"},
    40:  {"model": "PMC-0526WIFI", "class": "cooker"},
    138: {"model": "PMC-0526WIFI", "class": "cooker"},
    39:  {"model": "PMC-0528WIFI", "class": "cooker"},
    48:  {"model": "PMC-0528WIFI", "class": "cooker"},
    268: {"model": "PMC-0528WIFI", "class": "cooker"},
    47:  {"model": "PMC-0530WIFI", "class": "cooker"},
    270: {"model": "PMC-0530WIFI", "class": "cooker"},
    210: {"model": "PMC-0590AD", "class": "cooker"},
    302: {"model": "PMC-0597", "class": "cooker"},
    215: {"model": "PMC-5001WIFI", "class": "cooker"},
    79:  {"model": "PMC-5017WIFI", "class": "cooker"},
    192: {"model": "PMC-5017WIFI", "class": "cooker"},
    80:  {"model": "PMC-5020WIFI", "class": "cooker"},
    266: {"model": "PMC-5020WIFI", "class": "cooker"},
    77:  {"model": "PMC-5040WIFI", "class": "cooker"},
    78:  {"model": "PMC-5050WIFI", "class": "cooker"},
    89:  {"model": "PMC-5055WIFI", "class": "cooker"},
    114: {"model": "PMC-5060-Smart-Motion", "class": "cooker"},
    240: {"model": "PMC-5060-Smart-Motion", "class": "cooker"},
    162: {"model": "PMC-5063WIFI", "class": "cooker"},
    169: {"model": "PPC-1505-WiFI", "class": "cooker"},
    183: {"model": "PPC-1505-WiFI", "class": "cooker"},
    235: {"model": "AM7310-(test)", "class": "coffeemaker"},
    305: {"model": "PACM-2072", "class": "coffeemaker"},
    103: {"model": "PACM-2080AC", "class": "coffeemaker"},
    261: {"model": "PACM-2080AC", "class": "coffeemaker"},
    276: {"model": "PACM-2080AC", "class": "coffeemaker"},
    277: {"model": "PACM-2080AC", "class": "coffeemaker"},
    200: {"model": "PACM-2081AC", "class": "coffeemaker"},
    265: {"model": "PACM-2081AC", "class": "coffeemaker"},
    280: {"model": "PACM-2081AC", "class": "coffeemaker"},
    166: {"model": "PACM-2085GC", "class": "coffeemaker"},
    278: {"model": "PACM-2085GC", "class": "coffeemaker"},
    247: {"model": "PCM-1255", "class": "coffeemaker"},
    45:  {"model": "PCM-1540WIFI", "class": "coffeemaker"},
    222: {"model": "PCM-1540WIFI", "class": "coffeemaker"},
    274: {"model": "PCM-1540WIFI", "class": "coffeemaker"},
    279: {"model": "PCM-1540WIFI", "class": "coffeemaker"},
    190: {"model": "PCM-1560", "class": "coffeemaker"},
    207: {"model": "PCM-2070CG", "class": "coffeemaker"},
    172: {"model": "PAW-0804", "class": "air-cleaner"},
    140: {"model": "PAW-0804(c3-test)", "class": "air-cleaner"},
    151: {"model": "PPA-2025", "class": "air-cleaner"},
    203: {"model": "PPA-2025", "class": "air-cleaner"},
    250: {"model": "PPA-2025", "class": "air-cleaner"},
    152: {"model": "PPA-4050", "class": "air-cleaner"},
    204: {"model": "PPA-4050", "class": "air-cleaner"},
    251: {"model": "PPA-4050", "class": "air-cleaner"},
    236: {"model": "PPAT-02A", "class": "air-cleaner"},
    238: {"model": "PPAT-80P", "class": "air-cleaner"},
    239: {"model": "PPAT-90GDi", "class": "air-cleaner"},
    132: {"model": "PWF-2005", "class": "irrigator"},
    252: {"model": "PWF-2005", "class": "irrigator"},
    273: {"model": "PAF-4001WIFI", "class": "air_fryer"},
    290: {"model": "PAF-6003WIFI", "class": "air_fryer"},
    291: {"model": "PAF-8003WIFI", "class": "air_fryer"},
    292: {"model": "PAF-8005WIFI", "class": "air_fryer"},
    31:  {"model": "ENIGMA-WI-FI", "class": "boiler"},
    11:  {"model": "PWH-IDF06", "class": "boiler"},
    30:  {"model": "SIGMA-WIFI", "class": "boiler"},
    249: {"model": "VEKTOR-WIFI", "class": "boiler"},
    46:  {"model": "PCH-0320WIFI", "class": "heater"},
    65:  {"model": "PCH-0320WIFI", "class": "heater"},
    16:  {"model": "PHV-1401", "class": "heater"},
    49:  {"model": "PMH-21XX", "class": "heater"},
    64:  {"model": "PMH-21XX", "class": "heater"},
    246: {"model": "PRWC-3001", "class": "cleaner"},
    101: {"model": "PVCR-0726-Aqua", "class": "cleaner"},
    108: {"model": "PVCR-0726-GYRO", "class": "cleaner"},
    21:  {"model": "PVCR-0735", "class": "cleaner"},
    163: {"model": "PVCR-0735", "class": "cleaner"},
    19:  {"model": "PVCR-0833", "class": "cleaner"},
    43:  {"model": "PVCR-0833", "class": "cleaner"},
    104: {"model": "PVCR-0905", "class": "cleaner"},
    156: {"model": "PVCR-0905", "class": "cleaner"},
    107: {"model": "PVCR-0926", "class": "cleaner"},
    23:  {"model": "PVCR-1028", "class": "cleaner"},
    22:  {"model": "PVCR-1050", "class": "cleaner"},
    102: {"model": "PVCR-1226-Aqua", "class": "cleaner"},
    109: {"model": "PVCR-1226-GYRO", "class": "cleaner"},
    24:  {"model": "PVCR-1229", "class": "cleaner"},
    68:  {"model": "PVCR-3100", "class": "cleaner"},
    7:   {"model": "PVCR-3200", "class": "cleaner"},
    76:  {"model": "PVCR-3200", "class": "cleaner"},
    115: {"model": "PVCR-3200", "class": "cleaner"},
    12:  {"model": "PVCR-3300", "class": "cleaner"},
    81:  {"model": "PVCR-3400", "class": "cleaner"},
    130: {"model": "PVCR-3600", "class": "cleaner"},
    112: {"model": "PVCR-3700", "class": "cleaner"},
    88:  {"model": "PVCR-3800", "class": "cleaner"},
    66:  {"model": "PVCR-3900", "class": "cleaner"},
    131: {"model": "PVCR-3900", "class": "cleaner"},
    113: {"model": "PVCR-4000", "class": "cleaner"},
    197: {"model": "PVCR-4000", "class": "cleaner"},
    110: {"model": "PVCR-4105", "class": "cleaner"},
    127: {"model": "PVCR-4105", "class": "cleaner"},
    199: {"model": "PVCR-4250", "class": "cleaner"},
    241: {"model": "PVCR-4250", "class": "cleaner"},
    211: {"model": "PVCR-4260", "class": "cleaner"},
    269: {"model": "PVCR-4260", "class": "cleaner"},
    142: {"model": "PVCR-4500", "class": "cleaner"},
    195: {"model": "PVCR-4500", "class": "cleaner"},
    307: {"model": "PVCR-4750", "class": "cleaner"},
    119: {"model": "PVCR-5001", "class": "cleaner"},
    146: {"model": "PVCR-5001", "class": "cleaner"},
    154: {"model": "PVCR-5001", "class": "cleaner"},
    201: {"model": "PVCR-5003", "class": "cleaner"},
    242: {"model": "PVCR-5005", "class": "cleaner"},
    123: {"model": "PVCR-6001", "class": "cleaner"},
    148: {"model": "PVCR-6001", "class": "cleaner"},
    221: {"model": "PVCR-6001", "class": "cleaner"},
    187: {"model": "PVCR-6003", "class": "cleaner"},
    256: {"model": "PVCR-7026", "class": "cleaner"},
    128: {"model": "PVCRAC-7050", "class": "cleaner"},
    212: {"model": "PVCRAC-7290", "class": "cleaner"},
    178: {"model": "PVCRAC-7750", "class": "cleaner"},
    198: {"model": "PVCRAC-7790", "class": "cleaner"},
    264: {"model": "PVCRAC-7790", "class": "cleaner"},
    126: {"model": "PVCRDC-0101", "class": "cleaner"},
    160: {"model": "PVCRDC-0101", "class": "cleaner"},
    124: {"model": "PVCRDC-5002", "class": "cleaner"},
    149: {"model": "PVCRDC-5002", "class": "cleaner"},
    213: {"model": "PVCRDC-5002", "class": "cleaner"},
    202: {"model": "PVCRDC-5004", "class": "cleaner"},
    181: {"model": "PVCRDC-5006", "class": "cleaner"},
    125: {"model": "PVCRDC-6002", "class": "cleaner"},
    150: {"model": "PVCRDC-6002", "class": "cleaner"},
    186: {"model": "PVCRDC-6004", "class": "cleaner"},
    257: {"model": "PVCRDC-7028", "class": "cleaner"},
    217: {"model": "PVCRDC-G2-5002", "class": "cleaner"},
    218: {"model": "PVCRDC-G2-6002", "class": "cleaner"},
    133: {"model": "PVCR-G2-0726W", "class": "cleaner"},
    193: {"model": "PVCR-G2-0826", "class": "cleaner"},
    134: {"model": "PVCR-G2-0926W", "class": "cleaner"},
    135: {"model": "PVCR-G2-1226", "class": "cleaner"},
    129: {"model": "PVCR-G2-3200", "class": "cleaner"},
    122: {"model": "PVCR-G2-3600", "class": "cleaner"},
    219: {"model": "PVCR-G2-5001", "class": "cleaner"},
    220: {"model": "PVCR-G2-6001", "class": "cleaner"},
    100: {"model": "PVCR-Wave-15", "class": "cleaner"},
    93:  {"model": "PHB-1350-WIFI", "class": "blender"},
    35:  {"model": "PHB-1503-WIFI-(old)", "class": "blender"},
    34:  {"model": "PHB-1551-WIFI", "class": "blender"},
    282: {"model": "induction-hob", "class": "cooktop"},
    286: {"model": "XFC302I-B3SF", "class": "cooktop"},
    288: {"model": "XFC302T-B1D", "class": "cooktop"},
    285: {"model": "XFC604I", "class": "cooktop"},
    304: {"model": "XFC604I-(test)", "class": "cooktop"},
    284: {"model": "XFC604I-B8F", "class": "cooktop"},
    287: {"model": "XFC604T-B7D", "class": "cooktop"},
    289: {"model": "XFG640F-B3P", "class": "cooktop"},
    111: {"model": "PVCS-1150", "class": "cordless_cleaner"},
    90:  {"model": "PVCS-2090", "class": "cordless_cleaner"},
    136: {"model": "PVCS-4070", "class": "cordless_cleaner"},
    229: {"model": "PVCS-4070", "class": "cordless_cleaner"},
    232: {"model": "PVCS-6020", "class": "cordless_cleaner"},
    281: {"model": "PVCS-6020", "class": "cordless_cleaner"},
    230: {"model": "PVCS-8200", "class": "cordless_cleaner"},
    234: {"model": "PVCSDC-3000", "class": "cordless_cleaner"},
    233: {"model": "PVCSDC-3005", "class": "cordless_cleaner"},
    306: {"model": "PVCSDC-3005", "class": "cordless_cleaner"},
    180: {"model": "PSF-3315", "class": "fan"},
    248: {"model": "PSF-4025", "class": "fan"},
    179: {"model": "PGP-3010-SMOKELESS", "class": "grill"},
    96:  {"model": "PGP-4001", "class": "grill"},
    120: {"model": "PHD-4000", "class": "hair_care"},
    184: {"model": "PHS-1300", "class": "hair_care"},
    171: {"model": "PHSB-5000DF", "class": "hair_care"},
    145: {"model": "PHSC-1234", "class": "hair_care"},
    297: {"model": "8006", "class": "hood"},
    296: {"model": "8029", "class": "hood"},
    295: {"model": "6065A-600", "class": "hood"},
    283: {"model": "PGS-2250VA", "class": "iron"},
    91:  {"model": "PIR-2624AK-3m", "class": "iron"},
    161: {"model": "PIR-3074SG", "class": "iron"},
    173: {"model": "PIR-3210AK-3m", "class": "iron"},
    174: {"model": "PIR-3225AK-3m", "class": "iron"},
    191: {"model": "PSS-2002K", "class": "iron"},
    259: {"model": "PSS-8010K", "class": "iron"},
    159: {"model": "PSS-9090K", "class": "iron"},
    237: {"model": "SM-8095", "class": "kitchen_machine"},
    272: {"model": "SM-8095", "class": "kitchen_machine"},
    32:  {"model": "PMG-2580", "class": "meat_grinder"},
    216: {"model": "PMG-3060", "class": "meat_grinder"},
    116: {"model": "Smart-Lid", "class": "other"},
    299: {"model": "xbcook55", "class": "oven"},
    300: {"model": "xbcook56", "class": "oven"},
    298: {"model": "xbcook62", "class": "oven"},
    92:  {"model": "PGS-1450CWIFI", "class": "steamer"},
    94:  {"model": "PSS-7070KWIFI", "class": "steamer"},
    50:  {"model": "PETB-0202TC", "class": "toothbrush"},
    ### Мой водогрей, надо будет выпилить
    33:  {"model": "Electrolux Centurio IQ 3.0", "class": "boiler"},

}

POLARIS_KETTLE_TYPE = ["2","6","8","29","36","37","38","51","52","53","54","56","57","58","59","60","61","62","63","67","82","83","84","85","86","97","105","106","117","121","139","165","175","176","177","189","194","196","205","209","253","254","255","260","271","308"]
POLARIS_KETTLE_WITH_WEIGHT_TYPE = ["98","164","185","188","208","223","244","245","262","263","275","294"]
POLARIS_KETTLE_WITH_NIGHT_TYPE = ["36","37","86","97","106","117","164","175","176","177","189","194","196","205","208","209","244","253","254","255","260","271","308"]
POLARIS_KETTLE_WITH_BACKLIGHT_TYPE = ["36","37","51","52","53","54","60","61","62","63","67","82","83","84","85","86","97","98","105","106","117","139","164","175","176","177","188","189","194","196","208","209","223","244","245","253","254","255","260","262","263","271","275","294","308"]
POLARIS_KETTLE_WITH_TEA_TIME_MODE_TYPE = ["2","8","51","53","56","58","60","62","85","98","139","165","185","188","205","223","262","263","275","294"]
POLARIS_KETTLE_WITH_KEEP_WITH_WARM_MODE_TYPE = ["205","262","294"]
POLARIS_HUMIDDIFIER_TYPE = ["4","15","17","18","25","44","70","71","72","73","74","75","87","99","137","147","153","155","157","158"]
POLARIS_HUMIDDIFIER_WITH_IONISER_TYPE = ["4","15","17","18","44","70","72","73","74","137","147","153","155","157","158"]
POLARIS_HUMIDDIFIER_WITH_WARM_STREAM_TYPE = ["4","15","17","18","44","70","72","74","147","157","158"]
POLARIS_HUMIDDIFIER_LOW_FAN_TYPE = ["25","71","72","73","74","75","87","99","137","153","155","157","158"]
POLARIS_HUMIDDIFIER_7_MODE_TYPE = ["17","18","44","70"]
POLARIS_HUMIDDIFIER_5A_MODE_TYPE = ["4"]
POLARIS_HUMIDDIFIER_5B_MODE_TYPE = ["72","74","87","147","155"]
POLARIS_HUMIDDIFIER_4_MODE_TYPE = ["15","71","73","75","99"]
POLARIS_HUMIDDIFIER_3A_MODE_TYPE = ["25"]
POLARIS_HUMIDDIFIER_3B_MODE_TYPE = ["153","157","158"]

####
HOMMYN_BOILER_TYPE = ["33"]
HOMMYN_BOILER_WITH_IONISER_TYPE = ["33"]


PRESET_700W = "700W"
PRESET_1400W = "1400W"
PRESET_2000W = "2000W"

POWER_PRESETS = [PRESET_700W, PRESET_1400W, PRESET_2000W]
####



#Список всех девайсов РусКлимата из приложения Hommyn 

RUSCLIMATE_DEVICE = {
    1: {"model": "Electrolux EAP-1040D/1055D", "class": "air-cleaner"},
    2: {"model": "SmartInverter", "class": "boiler"},
    3: {"model": "Ballu ONEAIR ASP-200", "class": "ventilation"},
    4: {"model": "Electrolux EHU-3910D/EHU-3915D", "class": "humidifier"},
    5: {"model": "WFN-02", "class": "other"},
    6: {"model": "Transformer DI 3.0", "class": "heater"},
    7: {"model": "Zanussi Artendo WiFi/ Azurro PRO WiFi", "class": "boiler"},
    8: {"model": "Electrolux Atrium DC / Zanussi Siena DC / Ballu Lagoon", "class": "air-conditioner"},
    9: {"model": "Transformer DI 3.0 S", "class": "heater"},
    10: {"model": "Zanussi Massimo Solar", "class": "air-conditioner"},
    11: {"model": "Ballu Rapid", "class": "heater"},
    12: {"model": "Electrolux Centurio IQ 2.0/ Maximus WiFi", "class": "boiler"},
    13: {"model": "Electrolux Smartline/ Ballu Eco Smart/ Ice Peak", "class": "air-conditioner"},
    14: {"model": "Transformer DI", "class": "heater"},
    15: {"model": "Electrolux Viking DC / Zanussi Perfecto DC / Ballu Greenland DC", "class": "air-conditioner"},
    16: {"model": "Ballu Smart WiFi", "class": "boiler"},
    17: {"model": "Wi-Fi Convection Heater", "class": "heater"},
    18: {"model": "Electrolux Maximus/ Megapolis WiFi/ Zanussi Splendore XP 2.0/ Artendo PRO-C WiFi", "class": "boiler"},
    19: {"model": "Electrolux Regency", "class": "boiler"},
    20: {"model": "Ballu Platinum Evol. DC/Olympio Legend", "class": "air-conditioner"},
    21: {"model": "Zanussi Moderno DC/Electrolux Loft DC", "class": "air-conditioner"},
    22: {"model": "Hommyn Hub HH-01", "class": "other"},
    23: {"model": "TZE200", "class": "thermostatic-radiator"},
    24: {"model": "Royal Thermo Smart Heat", "class": "thermostatic-radiator"},
    25: {"model": "WFN-02 D4", "class": "other"},
    26: {"model": "Electrolux EAP-2050D/2075D", "class": "air-cleaner"},
    27: {"model": "Ballu RDU ANTICOVIDgenerator WiFi", "class": "recirculator"},
    28: {"model": "Transformer DI 4.0", "class": "heater"},
    29: {"model": "Electrolux/Royal Thermo", "class": "thermostat"},
    30: {"model": "Ballu ONEAIR ASP-200S", "class": "ventilation"},
    31: {"model": "Transformer 4.0", "class": "heater"},
    32: {"model": "Ballu ASP-100 / Electrolux EASP-100", "class": "ventilation"},
    33: {"model": "Electrolux Centurio IQ 3.0", "class": "boiler"},
    34: {"model": "Electrolux EPVS / ERVX inv", "class": "ventilation"},
    35: {"model": "Electrolux YOGAhealthline 2.0.", "class": "humidifier"},
    36: {"model": "Electrolux EPVS / ERVX inv", "class": "ventilation"},
    37: {"model": "Water leak sensor WS-20-Z", "class": "sensor"},
    38: {"model": "Toshiba Shorai EE", "class": "air-conditioner"},
    39: {"model": "Temperature sensor TS-20-Z", "class": "sensor"},
    40: {"model": "Motion and Light sensor MS-21-Z", "class": "sensor"},
    41: {"model": "Electrolux Monaco DC", "class": "air-conditioner"},
    42: {"model": "Transformer DI 3.0 XS", "class": "heater"},
    43: {"model": "WFN-02-01/02", "class": "other"},
    44: {"model": "Royal Thermo Aqua Inverter/ Royal Thermo Aqua Inox Inverter", "class": "boiler"},
    46: {"model": "Transformer DI 4.0", "class": "heater"},
    47: {"model": "Wi-Fi Convection Heater", "class": "heater"},
    49: {"model": "Transformer 4.0", "class": "heater"},
    50: {"model": "Electrolux 3D Fireplace", "class": "fireplace"},
    51: {"model": "Zanussi Massimo Solar 2023", "class": "air-conditioner"},
    52: {"model": "Water leak sensor WS-30-Z", "class": "sensor"},
    53: {"model": "Temperature sensor HTSZ-01", "class": "sensor"},
    54: {"model": "Opening sensor DS-20-Z", "class": "sensor"},
    55: {"model": "Zanussi Barocco DC/ Royal Thermo Barocco DC", "class": "air-conditioner"},
    56: {"model": "Toshiba", "class": "air-conditioner"},
    57: {"model": "Shuft Berg/ MBO M-1", "class": "air-conditioner"},
    58: {"model": "Smart socket RKNZ01", "class": "socket"},
    59: {"model": "Ballu ONEAIR ASP-200S", "class": "ventilation"},
    60: {"model": "Ballu Discovery DC", "class": "air-conditioner"},
    61: {"model": "One-channel relay", "class": "socket"},
    62: {"model": "Two-channel relay", "class": "socket"},
    63: {"model": "One-key switch SWZBNN01W", "class": "socket"},
    64: {"model": "Two-key switch SWZBNN02W", "class": "socket"},
    65: {"model": "SmartControl", "class": "thermostat"},
    66: {"model": "Smart valve manipulator WZB400W", "class": "other"},
    67: {"model": "Electrolux/Royal Thermo", "class": "thermostat"},
    68: {"model": "Electrolux Loft DC/Ballu Platinum Black DC", "class": "air-conditioner"},
    69: {"model": "Ballu ASP-100 / Electrolux EASP-100 with music", "class": "ventilation"},
    70: {"model": "Ballu Universal 3, DC, Free Match", "class": "air-conditioner"},
    71: {"model": "Transformer DI 4.0", "class": "heater"},
    72: {"model": "Zanussi Barocco/ Royal Thermo Barocco", "class": "air-conditioner"},
    73: {"model": "SmartControl Pro", "class": "thermostat"},
    74: {"model": "Aurus S", "class": "boiler"},
    75: {"model": "Aurus Infrared", "class": "ir-heater"},
    76: {"model": "Electrolux Royal Flash/ Centurio IQ Inverter", "class": "boiler"},
    77: {"model": "Royal Thermo Major Inverter/ Smalto Inverter", "class": "boiler"},
    78: {"model": "Electrolux/Royal Thermo", "class": "thermostat"},
    79: {"model": "Opening sensor OS30ZB", "class": "sensor"},
    80: {"model": "Aurus F", "class": "boiler"},
    81: {"model": "UHB-960 ET", "class": "humidifier"},
    82: {"model": "Goldstar GSAC/GSACI", "class": "air-conditioner"},
    83: {"model": "Ballu Aura", "class": "air-conditioner"},
    84: {"model": "Ballu Aura", "class": "air-conditioner"},
    85: {"model": "Aurus D", "class": "air-conditioner"},
    86: {"model": "Motion and Light sensor MBS30ZB", "class": "sensor"},
    87: {"model": "Water leak sensor WLS30ZB", "class": "sensor"},
    88: {"model": "1-channel AC/DC relay DCRLZBN01", "class": "socket"},
    89: {"model": "Aurus", "class": "heater"},
    90: {"model": "Ballu Cetrion Inverter/ Ballu Cetrion Inox Inverter", "class": "boiler"},
    91: {"model": "Royal Thermo Regency", "class": "boiler"},
    92: {"model": "Temperature and Humidity sensor THS30ZB", "class": "sensor"},
    93: {"model": "Smart valve manipulator WZB400W", "class": "other"},
    94: {"model": "Smart socket RKNZ02", "class": "socket"},
    95: {"model": "Climer Dresden", "class": "air-conditioner"},
    97: {"model": "Hommyn Hub HH-01*", "class": "other"},
    98: {"model": "Shuft Allston-VH/ERV Комплектный пульт", "class": "ventilation"},
    99: {"model": "AURUS A", "class": "air-conditioner"},
    100: {"model": "Shuft Allston-VH/ERV Пульт AirPad 7", "class": "ventilation"},
    101: {"model": "Royal Thermo Smart Heat schedule modes", "class": "thermostatic-radiator"},
    102: {"model": "Ballu ONEAIR ASP-90", "class": "ventilation"},
    103: {"model": "Inwall outlet RKNWOZ01W", "class": "socket"},
    104: {"model": "Dimmer switch rotary DSWZBN01W", "class": "socket"},
    105: {"model": "Ballu ONEAIR ASP-90", "class": "ventilation"},
    106: {"model": "Ballu ONEAIR ASP-90", "class": "ventilation"},
    107: {"model": "Ballu ONEAIR ASP-90", "class": "ventilation"},
    108: {"model": "Royal Thermo Diamond DC", "class": "air-conditioner"},
}

# Группировка девайсов по типу
RUSCLIMATE_AIR_CLEANER_TYPE = ["1","26"]
RUSCLIMATE_AIR_CONDITIONER_TYPE = ["8","10","13","15","20","21","38","41","51","55","56","57","60","68","70","72","82","83","84","85","95","99","108"]
RUSCLIMATE_BOILER_TYPE = ["2","7","12","16","18","19","33","44","74","76","77","80","90","91"]
RUSCLIMATE_FIREPLACE_TYPE = ["50"]
RUSCLIMATE_HEATER_TYPE = ["6","9","11","14","17","28","31","42","46","47","49","71","89"]
RUSCLIMATE_HUMIDIFIER_TYPE = ["4","35","81"]
RUSCLIMATE_IR_HEATER_TYPE = ["75"]
RUSCLIMATE_OTHER_TYPE = ["5","22","25","43","66","93","97"]
RUSCLIMATE_RECIRCULATOR_TYPE = ["27"]
RUSCLIMATE_SENSOR_TYPE = ["37","39","40","52","53","54","79","86","87","92"]
RUSCLIMATE_SOCKET_TYPE = ["58","61","62","63","64","88","94","103","104"]
RUSCLIMATE_THERMOSTAT_TYPE = ["29","65","67","73","78"]
RUSCLIMATE_THERMOSTATIC_RADIATOR_TYPE = ["23","24","101"]
RUSCLIMATE_VENTILATION_TYPE = ["3","30","32","34","36","59","69","98","100","102","105","106","107"]

# Девайсы по наличию функций
RUSCLIMATE_FEATURE_AMOUNT_TYPE = ["40","59","69","75","86","104"]
RUSCLIMATE_FEATURE_BACKLIGHT_TYPE = ["1","4","6","9","11","14","15","17","20","21","26","28","29","30","31","32","35","41","42","46","47","49","50","55","57","58","59","60","65","67","68","69","70","71","72","73","75","78","81","82","84","85","89","94","95","99","102","103","105","106","107","108"]
RUSCLIMATE_FEATURE_BATTERY_TYPE = ["37","39","40","52","53","54","79","86","87","92"]
RUSCLIMATE_FEATURE_BSS_TYPE = ["2","7","12","18","19","24","33","44","55","72","74","76","77","80","90","91","101"]
RUSCLIMATE_FEATURE_CHILD_LOCK_TYPE = ["1","4","6","9","11","14","17","23","26","27","28","29","31","35","42","46","47","49","65","67","71","73","78","81","89","94","98","100","103"]
RUSCLIMATE_FEATURE_CURRENT_AMPERAGE_TYPE = ["58","94","103"]
RUSCLIMATE_FEATURE_CURRENT_CO2_TYPE = ["1","3","26","27","30","32","34","36","59","69","98","100","102","105","106","107"]
RUSCLIMATE_FEATURE_CURRENT_HUMIDITY_TYPE = ["4","29","34","35","36","39","53","65","67","73","78","81","92","98","100"]
RUSCLIMATE_FEATURE_CURRENT_PM2_TYPE = ["1","3","26","27","30","34","36","59","98","100"]
RUSCLIMATE_FEATURE_CURRENT_POWER_TYPE = ["58","73","94","103"]
RUSCLIMATE_FEATURE_CURRENT_TEMPERATURE_TYPE = ["2","3","4","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","23","24","28","29","30","31","32","33","34","35","36","38","39","41","42","44","46","47","49","51","53","55","56","57","59","60","65","67","68","69","70","71","72","73","74","76","77","78","80","81","82","83","84","85","89","90","91","92","95","98","99","100","101","102","104","105","106","107","108"]
RUSCLIMATE_FEATURE_CURRENT_VOLTAGE_TYPE = ["58","94","103"]
RUSCLIMATE_FEATURE_DAMPER_TYPE = ["3","6","9","11","14","17","24","28","29","30","31","42","46","47","49","59","65","66","67","71","78","89","93","101"]
RUSCLIMATE_FEATURE_DEMO_TYPE = ["1","2","3","6","7","8","9","11","12","13","14","15","16","17","18","19","20","21","24","26","27","28","29","30","31","33","34","35","37","38","39","40","41","42","47","50","51","52","53","54","55","56","57","59","60","61","62","63","64","65","66","67","68","70","72","73","74","75","76","78","79","82","84","85","86","87","88","91","92","93","95","98","99","100","101","104","108"]
RUSCLIMATE_FEATURE_EXPENDABLES_TYPE = ["1","3","26","27","30","32","34","35","36","44","59","69","76","77","80","90","98","100","102","105","106","107"]
RUSCLIMATE_FEATURE_HUMIDITY_TYPE = ["4","34","35","36","50","81"]
RUSCLIMATE_FEATURE_IONISER_TYPE = ["1","3","4","15","20","26","27","30","35","41","56","59","70","85","98"]
RUSCLIMATE_FEATURE_KEEP_WARM_TYPE = ["2","44","74","77","80","90"]
RUSCLIMATE_FEATURE_NIGHT_TYPE = ["8","10","13","15","20","21","41","51","55","57","60","68","70","72","81","82","83","84","85","95","99","108"]
RUSCLIMATE_FEATURE_POWER_CONSUME_TYPE = ["2","7","12","16","18","19","29","33","44","58","65","67","74","76","77","78","80","90","91","94","103"]
RUSCLIMATE_FEATURE_PROGRAM_TYPE = ["1","2","3","4","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","23","24","26","27","28","29","30","31","32","33","34","35","36","38","41","42","44","46","47","49","50","51","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","88","89","90","91","93","94","95","98","99","100","101","102","103","104","105","106","107","108"]
RUSCLIMATE_FEATURE_SCHEDULE_TYPE = ["1","2","3","4","6","7","8","9","10","11","12","13","14","15","17","18","19","20","21","23","24","26","27","28","29","30","31","32","33","34","35","36","38","41","42","44","46","47","49","50","51","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","88","89","90","91","93","94","95","98","99","100","101","102","103","104","105","106","107","108"]
RUSCLIMATE_FEATURE_SMART_MODE_TYPE = ["2","44","60","68","74","76","77","80","82","90","99","108"]
RUSCLIMATE_FEATURE_SPEED_TYPE = ["1","3","4","6","8","9","10","11","13","14","15","17","20","21","26","28","30","31","32","34","35","36","38","41","42","46","47","49","50","51","55","56","57","59","60","68","69","70","71","72","73","81","82","83","84","85","89","95","98","99","100","102","105","106","107","108"]
RUSCLIMATE_FEATURE_STREAM_WARM_TYPE = ["4","35","81"]
RUSCLIMATE_FEATURE_TEMPERATURE_TYPE = ["2","3","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","23","24","28","29","30","31","32","33","34","36","38","41","42","44","46","47","49","51","55","56","57","59","60","65","67","68","69","70","71","72","73","74","75","76","77","78","80","82","83","84","85","89","90","91","95","99","101","102","104","105","106","107","108"]
RUSCLIMATE_FEATURE_TIMER_TYPE = ["4","6","9","11","14","17","23","27","28","30","31","32","34","35","36","42","46","47","49","59","69","71","81","89","102","104","105","106","107"]
RUSCLIMATE_FEATURE_TURBO_TYPE = ["8","13","15","20","21","30","32","38","41","55","56","57","59","60","69","70","72","75","82","84","85","95","99","108"]
RUSCLIMATE_FEATURE_ULTRAVIOLET_TYPE = ["1","3","4","26","30","35","55","59","72","98","99"]
RUSCLIMATE_FEATURE_UUID_TYPE = ["5","25","43"]
RUSCLIMATE_FEATURE_VOLUME_TYPE = ["3","4","6","9","11","14","17","28","30","31","32","35","42","46","47","49","50","55","59","60","69","71","72","85","89","102","105","106","107","108"]
RUSCLIMATE_FEATURE_WATER_TANK_TYPE = ["2","7","12","16","18","19","33","44","50","74","76","77","80","90","91"]

# Список девайсов, принимающих только булевое значение
RUSCLIMATE_BOOLEAN_FEATURES = ["backlight","bss","child_lock","damper","ioniser","keep_warm","night","smart_mode","stream_warm","turbo","ultraviolet","volume"]

# Список девайсов, принимающих значения в промежутке от и до
RUSCLIMATE_RANGE_FEATURES = ["amount","humidity","night","speed","temperature","timer","volume","water_tank"]

# Лимиты. Пусть пока будет
RUSCLIMATE_BOOL_LIMITS = {
    1: ["backlight","child_lock","ioniser","ultraviolet"],
    2: ["bss","keep_warm","smart_mode"],
    3: ["damper","ioniser","ultraviolet","volume"],
    4: ["child_lock","ioniser","stream_warm","ultraviolet","volume"],
    6: ["child_lock","damper","volume"],
    7: ["bss","keep_warm"],
    8: ["ioniser","night","turbo"],
    9: ["child_lock","damper","volume"],
    10: ["ioniser","night"],
    11: ["child_lock","damper","volume"],
    12: ["bss","keep_warm"],
    13: ["ioniser","night","turbo"],
    14: ["child_lock","damper","volume"],
    15: ["backlight","ioniser","night","turbo"],
    16: ["bss","keep_warm"],
    17: ["child_lock","damper","volume"],
    18: ["bss","keep_warm"],
    19: ["bss","keep_warm"],
    20: ["backlight","ioniser","night","turbo"],
    21: ["backlight","night","turbo"],
    23: ["child_lock"],
    24: ["bss","damper"],
    26: ["backlight","child_lock","ioniser","ultraviolet"],
    27: ["child_lock","ioniser"],
    28: ["child_lock","damper","volume"],
    29: ["backlight","child_lock","damper"],
    30: ["damper","ioniser","turbo","ultraviolet","volume"],
    31: ["child_lock","damper","volume"],
    32: ["turbo","volume"],
    33: ["bss","keep_warm"],
    35: ["child_lock","ioniser","stream_warm","ultraviolet","volume"],
    38: ["ioniser","turbo"],
    41: ["backlight","ioniser","night","turbo"],
    42: ["child_lock","damper","volume"],
    44: ["bss","keep_warm","smart_mode"],
    46: ["child_lock","damper","volume"],
    47: ["child_lock","damper","volume"],
    49: ["child_lock","damper","volume"],
    50: ["backlight"],
    51: ["ioniser","night"],
    55: ["backlight","ioniser","turbo","volume"],
    56: ["ioniser","turbo"],
    57: ["backlight","ioniser","night","turbo"],
    58: ["backlight"],
    59: ["damper","ioniser","turbo","ultraviolet","volume"],
    60: ["backlight","ioniser","night","smart_mode","turbo","volume"],
    65: ["backlight","child_lock","damper"],
    66: ["damper"],
    67: ["backlight","child_lock","damper"],
    68: ["backlight","smart_mode"],
    69: ["turbo","volume"],
    70: ["backlight","ioniser","night","turbo"],
    71: ["child_lock","damper","volume"],
    72: ["backlight","ioniser","turbo","volume"],
    73: ["backlight","child_lock"],
    74: ["bss","keep_warm","smart_mode"],
    75: ["backlight","turbo"],
    76: ["bss","keep_warm","smart_mode"],
    77: ["bss","keep_warm","smart_mode"],
    78: ["backlight","child_lock","damper"],
    80: ["bss","keep_warm","smart_mode"],
    81: ["backlight","child_lock","night","stream_warm"],
    82: ["backlight","night","smart_mode","turbo"],
    83: ["ioniser","night"],
    84: ["backlight","ioniser","night","turbo"],
    85: ["backlight","ioniser","night","turbo","volume"],
    89: ["child_lock","damper","volume"],
    90: ["bss","keep_warm","smart_mode"],
    91: ["bss","keep_warm"],
    93: ["damper"],
    94: ["backlight","child_lock"],
    95: ["backlight","ioniser","night","turbo"],
    99: ["backlight","ioniser","smart_mode","turbo"],
    101: ["bss","damper"],
    102: ["backlight","volume"],
    103: ["backlight","child_lock"],
    105: ["backlight","volume"],
    106: ["backlight","volume"],
    107: ["backlight","volume"],
    108: ["backlight","ioniser","night","smart_mode","turbo","volume"],
}

# Лимиты значений от и до
RUSCLIMATE_RANGE_LIMITS = {
    1: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
    },
    2: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    3: {
        "speed": {"min": 0, "max": 8, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
    },
    4: {
        "humidity": {"min": 1, "max": 99, "step": 1, "default": 50},
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
    },
    6: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    7: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    8: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 17, "max": 30, "step": 1, "default": 22},
    },
    9: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    10: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 18, "max": 32, "step": 1, "default": 22},
    },
    11: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86400, "step": 60, "default": 0},
    },
    12: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    13: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 30, "step": 1, "default": 22},
    },
    14: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    15: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 30, "step": 1, "default": 22},
    },
    16: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    17: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    18: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    19: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    20: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    21: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 18, "max": 32, "step": 1, "default": 22},
    },
    23: {
        "temperature": {"min": 5, "max": 30, "step": 0.5, "default": 25},
        "timer": {"min": 0, "max": 300, "step": 1, "default": 0},
    },
    24: {
        "temperature": {"min": 5, "max": 30, "step": 1, "default": 25},
    },
    26: {
        "speed": {"min": 0, "max": 4, "step": 1, "default": 0},
    },
    27: {
        "timer": {"min": 1800, "max": 86400, "step": 1800, "default": 1800},
    },
    28: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    29: {
        "temperature": {"min": 5, "max": 45, "step": 0.1, "default": 25},
    },
    30: {
        "speed": {"min": 0, "max": 8, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    31: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    32: {
        "speed": {"min": 0, "max": 8, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    33: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    34: {
        "humidity": {"min": 0, "max": 10, "step": 1, "default": 1},
        "speed": {"min": 0, "max": 10, "step": 1, "default": 1},
        "temperature": {"min": 10, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    35: {
        "humidity": {"min": 30, "max": 85, "step": 5, "default": 50},
        "speed": {"min": 1, "max": 3, "step": 1, "default": 1},
        "timer": {"min": 300, "max": 1800, "step": 300, "default": 300},
    },
    36: {
        "humidity": {"min": 0, "max": 10, "step": 1, "default": 1},
        "speed": {"min": 0, "max": 10, "step": 1, "default": 1},
        "temperature": {"min": 10, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    38: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 17, "max": 30, "step": 1, "default": 22},
    },
    40: {
        "amount": {"min": 0, "max": 500, "step": 1, "default": 0},
    },
    41: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 30, "step": 1, "default": 22},
    },
    42: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    44: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    46: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    47: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    49: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    50: {
        "humidity": {"min": 0, "max": 3, "step": 1, "default": 1},
        "speed": {"min": 0, "max": 2, "step": 1, "default": 0},
        "volume": {"min": 0, "max": 2, "step": 1, "default": 0},
        "water_tank": {"min": 0, "max": 5, "step": 1, "default": 0},
    },
    51: {
        "speed": {"min": 0, "max": 2, "step": 1, "default": 0},
        "temperature": {"min": 18, "max": 32, "step": 1, "default": 22},
    },
    55: {
        "night": {"min": 0, "max": 3, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 31, "step": 1, "default": 22},
    },
    56: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 17, "max": 30, "step": 1, "default": 22},
    },
    57: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    59: {
        "amount": {"min": 0, "max": 5, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 8, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    60: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 31, "step": 1, "default": 22},
    },
    65: {
        "temperature": {"min": 5, "max": 45, "step": 0.1, "default": 25},
    },
    67: {
        "temperature": {"min": 5, "max": 45, "step": 0.1, "default": 25},
    },
    68: {
        "night": {"min": 0, "max": 4, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 30, "step": 1, "default": 22},
    },
    69: {
        "amount": {"min": 0, "max": 5, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 8, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    70: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    71: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 0},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    72: {
        "night": {"min": 0, "max": 3, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 31, "step": 1, "default": 22},
    },
    73: {
        "speed": {"min": 20, "max": 100, "step": 1, "default": 20},
        "temperature": {"min": 5, "max": 30, "step": 0.5, "default": 25},
    },
    74: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    75: {
        "amount": {"min": 0, "max": 100, "step": 2, "default": 0},
        "temperature": {"min": 0, "max": 100, "step": 2, "default": 22},
    },
    76: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    77: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    78: {
        "temperature": {"min": 5, "max": 45, "step": 0.1, "default": 25},
    },
    80: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    81: {
        "humidity": {"min": 1, "max": 99, "step": 1, "default": 50},
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "timer": {"min": 0, "max": 43200, "step": 3600, "default": 0},
    },
    82: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    83: {
        "speed": {"min": 1, "max": 2, "step": 1, "default": 1},
        "temperature": {"min": 18, "max": 32, "step": 1, "default": 22},
    },
    84: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    85: {
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 30, "step": 1, "default": 22},
    },
    86: {
        "amount": {"min": 0, "max": 500, "step": 1, "default": 0},
    },
    89: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 1},
        "temperature": {"min": 10, "max": 35, "step": 1, "default": 10},
        "timer": {"min": 0, "max": 86340, "step": 60, "default": 0},
    },
    90: {
        "temperature": {"min": 30, "max": 75, "step": 1, "default": 55},
    },
    91: {
        "temperature": {"min": 35, "max": 75, "step": 1, "default": 55},
    },
    95: {
        "speed": {"min": 0, "max": 3, "step": 1, "default": 0},
        "temperature": {"min": 17, "max": 30, "step": 1, "default": 22},
    },
    98: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 1},
    },
    99: {
        "night": {"min": 0, "max": 4, "step": 1, "default": 0},
        "speed": {"min": 0, "max": 5, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 32, "step": 1, "default": 22},
    },
    100: {
        "speed": {"min": 0, "max": 10, "step": 1, "default": 1},
    },
    101: {
        "temperature": {"min": 5, "max": 30, "step": 1, "default": 25},
    },
    102: {
        "speed": {"min": 0, "max": 6, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    104: {
        "amount": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 0, "max": 100, "step": 1, "default": 0},
        "timer": {"min": 0, "max": 7200, "step": 300, "default": 0},
    },
    105: {
        "speed": {"min": 0, "max": 6, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    106: {
        "speed": {"min": 0, "max": 6, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    107: {
        "speed": {"min": 0, "max": 6, "step": 1, "default": 0},
        "temperature": {"min": 5, "max": 25, "step": 1, "default": 18},
        "timer": {"min": 0, "max": 900, "step": 1, "default": 0},
    },
    108: {
        "speed": {"min": 0, "max": 100, "step": 1, "default": 0},
        "temperature": {"min": 16, "max": 31, "step": 1, "default": 22},
    },
}

# Возможные функции
RUSCLIMATE_ENUM_INSTANCES = ["fan_speed","heat","motion","open","program","swing","thermostat","water_leak","work_speed"]

# Глобальные варианты параметров функций
RUSCLIMATE_ENUM_INSTANCE_VALUES = {
    "fan_speed": ["auto","fast","high","low","max","medium","min","normal","quiet","slow","turbo"],
    "heat": ["auto","eco","fan_only","high","low","medium","min","normal","turbo"],
    "motion": ["detected","not_detected"],
    "open": ["closed","opened"],
    "program": ["auto","eco","quiet","turbo"],
    "swing": ["auto","horizontal","stationary","vertical"],
    "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet","turbo"],
    "water_leak": ["dry","leak"],
    "work_speed": ["auto","fast","high","low","max","medium","min","normal","quiet","slow","turbo"],
}

# Варианты значений которые девайс умеет принимать
RUSCLIMATE_ENUMS_BY_DEVTYPE = {
    1: {
        "work_speed": ["auto","high","low","medium","quiet"],
    },
    2: {
        "heat": ["low","normal","turbo"],
    },
    3: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
        "work_speed": ["auto","quiet","turbo"],
    },
    4: {
        "program": ["auto","quiet"],
        "work_speed": ["high","low","medium"],
    },
    6: {
        "heat": ["auto","eco","min"],
    },
    7: {
        "heat": ["low","normal","turbo"],
    },
    8: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    9: {
        "heat": ["auto","eco","min"],
    },
    10: {
        "thermostat": ["cool","dry","fan_only","heat"],
    },
    12: {
        "heat": ["low","normal","turbo"],
    },
    13: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    14: {
        "heat": ["auto","eco","min"],
    },
    15: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    16: {
        "heat": ["medium","turbo"],
    },
    17: {
        "heat": ["auto","eco"],
    },
    18: {
        "heat": ["low","normal","turbo"],
    },
    19: {
        "heat": ["low","normal","turbo"],
    },
    20: {
        "fan_speed": ["auto","high","low","medium"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    21: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet","turbo"],
        "work_speed": ["auto","high","low","medium"],
    },
    26: {
        "work_speed": ["auto","high","low","medium","quiet","turbo"],
    },
    28: {
        "heat": ["auto","eco"],
    },
    30: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
        "work_speed": ["auto","quiet","turbo"],
    },
    31: {
        "heat": ["auto","eco"],
    },
    32: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
        "work_speed": ["auto","quiet","turbo"],
    },
    33: {
        "heat": ["low","normal","turbo"],
    },
    34: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
    },
    35: {
        "program": ["auto","quiet"],
        "work_speed": ["high","low","medium"],
    },
    36: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
    },
    37: {
        "water_leak": ["dry","leak"],
    },
    38: {
        "fan_speed": ["auto","high","low","max","medium","min","quiet"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","turbo"],
    },
    40: {
        "motion": ["detected","not_detected"],
    },
    41: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    42: {
        "heat": ["auto","eco","min"],
    },
    44: {
        "heat": ["low","normal","turbo"],
    },
    46: {
        "heat": ["auto","eco","min"],
        "work_speed": ["max","min","normal"],
    },
    47: {
        "heat": ["auto","eco","min"],
    },
    49: {
        "heat": ["auto","eco","min"],
        "work_speed": ["max","min"],
    },
    50: {
        "heat": ["high","low","medium"],
        "work_speed": ["high","low","medium"],
    },
    51: {
        "thermostat": ["cool","dry","fan_only","heat","quiet"],
        "work_speed": ["high","low"],
    },
    52: {
        "water_leak": ["dry","leak"],
    },
    54: {
        "open": ["closed","opened"],
    },
    55: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet"],
        "work_speed": ["auto","fast","low","max","medium","min","slow","turbo"],
    },
    56: {
        "fan_speed": ["auto","high","low","max","medium","min","quiet"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","turbo"],
    },
    57: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet"],
        "work_speed": ["auto","high","low","medium","turbo"],
    },
    59: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
        "work_speed": ["auto","quiet","turbo"],
    },
    60: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet","turbo"],
        "work_speed": ["auto","high","low","medium","quiet","turbo"],
    },
    67: {
        "heat": ["normal","turbo"],
    },
    68: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet"],
        "work_speed": ["auto","high","low","medium","quiet"],
    },
    69: {
        "fan_speed": ["auto","high","low","medium","quiet","turbo"],
        "work_speed": ["auto","quiet","turbo"],
    },
    70: {
        "fan_speed": ["auto","high","low","medium"],
        "swing": ["horizontal","stationary"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat"],
    },
    71: {
        "heat": ["auto","eco","min"],
    },
    72: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet"],
        "work_speed": ["auto","fast","low","max","medium","min","slow","turbo"],
    },
    73: {
        "fan_speed": ["fast","high","low","max","medium","min","normal","slow","turbo"],
        "heat": ["fan_only","normal"],
    },
    74: {
        "heat": ["min","normal","turbo"],
    },
    76: {
        "heat": ["low","normal","turbo"],
    },
    77: {
        "heat": ["low","normal","turbo"],
    },
    78: {
        "heat": ["normal","turbo"],
    },
    80: {
        "heat": ["low","normal","turbo"],
    },
    81: {
        "fan_speed": ["auto","high","low","medium"],
    },
    82: {
        "fan_speed": ["auto","high","medium","min"],
        "program": ["eco","turbo"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    83: {
        "fan_speed": ["high","low"],
        "thermostat": ["cool","dry","fan_only"],
    },
    84: {
        "fan_speed": ["high","low","medium"],
        "thermostat": ["cool","dry","fan_only"],
    },
    85: {
        "fan_speed": ["auto","high","low","medium","min","quiet"],
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","fan_only","heat"],
    },
    86: {
        "motion": ["detected","not_detected"],
    },
    90: {
        "heat": ["low","normal","turbo"],
    },
    91: {
        "heat": ["low","normal","turbo"],
    },
    95: {
        "thermostat": ["auto","cool","dry","fan_only","heat","quiet","turbo"],
        "work_speed": ["auto","high","low","medium"],
    },
    98: {
        "fan_speed": ["auto","high","low","max","medium","min","quiet"],
    },
    99: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet","turbo"],
        "work_speed": ["auto","high","low","max","medium","quiet"],
    },
    100: {
        "fan_speed": ["auto","high","low","max","medium","min","quiet"],
    },
    102: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "program": ["quiet","turbo"],
    },
    105: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "program": ["auto","quiet","turbo"],
    },
    106: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "program": ["quiet","turbo"],
    },
    107: {
        "fan_speed": ["auto","high","low","max","medium","min"],
        "program": ["auto","quiet","turbo"],
    },
    108: {
        "swing": ["auto","horizontal","stationary","vertical"],
        "thermostat": ["auto","cool","dry","eco","fan_only","heat","quiet","turbo"],
        "work_speed": ["auto","high","low","medium","quiet","turbo"],
    },
}