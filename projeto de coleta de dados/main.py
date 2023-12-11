import sqlite3

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('fortnite_data.db')
cursor = conn.cursor()

# Criar uma tabela para armazenar os dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        vitorias INTEGER,
        kills INTEGER,
        partidas INTEGER
    )
''')

# Dados a serem inseridos no banco de dados

#Name , Vitorias , kills , partidas
dados_jogadores = [
    ("ZERO BUILD GOAT", 1859, 25362, 1780),
    ("Byskix is Back亗", 1636, 24856, 1938),
    ("KingTrio-Beninho", 1565, 23460, 1730),
    ("KICK BBSHOTZ", 1522, 23639, 1602),
    ("Nytrixz", 1457, 23337, 1408),
    ("ᴷᶦᶜᵏBBSHOTZ", 1420, 20090, 1609),
    ("TikTok Beliize", 1383, 19174, 1904),
    ("YOUTUBE VELENTY", 1313, 19572, 1679),
    ("ᵀⁱᵏᵀᵒᵏPrxsumoシ", 1299, 17188, 1552),
    ("Ship", 1295, 16573, 1626),
    ("PRADAGˢᵗʳᵉᵃᵉᵐˢ", 1273, 16829, 1637),
    ("Sinvicted.exe", 1252, 15798, 1525),
    ("MaxSineFN", 1198, 18238, 1526),
    ("Unseen ag0ny", 1190, 17702, 1415),
    ("NykZBᵀᵀⱽ", 1188, 23323, 1488),
    ("Tangkaap.exe", 1143, 12744, 1701),
    ("Nizma ᵗᵗᵛ", 1138, 12923, 1861),
    ("ₑᵥₑᵣʸₒₙₑ ᴰᵢₑₛ", 1120, 13909, 1882),
    ("Mangeur.depoulet", 1108, 12008, 1931),
    ("TTV Dr C Funk", 1103, 12364, 1923),
    ("MiSsKoNeJu", 1094, 12100, 1253),
    ("VIL Andreas", 1090, 12133, 1131),
    ("Twitch Rapper", 1060, 13400, 1162),
    ("Twitch-637Nickel", 1039, 13925, 1281),
    ("Twitch x9mg", 1036, 12502, 1496),
    ("TikTok ChrisZB", 1021, 10655, 1593),
    ("YT_ImmortalKxlla", 1009, 12975, 1538),
    ("GL Nizh", 999, 12182, 1544),
    ("KyronFN", 992, 12452, 1442),
    ("TWITCH.GRYPHONRB", 980, 12289, 1196),
    ("TIKTOK zbjayden", 978, 11380, 1378),
    ("Twitch Tezzio ネ", 968, 11265, 1131),
    ("stepbrodevonᵗᵗᵛ", 958, 10430, 1165),
    ("citsatnaF", 957, 13431, 1207),
    ("TikTok ibnanh", 953, 13656, 1258),
    ("AceOnCombatPro", 948, 13826, 1119),
    ("Tiktok Jzvlw", 946, 13323, 1335),
    ("TikTok_ImKyZeNN", 941, 22640, 1460),
    ("no brain jus aim", 941, 11630, 1244),
    ("iitsWadeᵗᵗᵛ", 936, 13923, 1136),
    ("ッーＤａｒｋｅｙｅｓ", 931, 13923, 1269),
    ("SimplyDari ᵀⱽ", 929, 13932, 1176),
    ("LegendZBᵀᵀⱽ", 909, 11805, 1414),
    ("ㅜƦǚɱρ", 908, 11319, 1379),
    ("Shaylz", 905, 12293, 1495),
    ("TikTok-KingRyzen", 902, 14965, 1307),
    ("Rexter-Kick", 895, 13630, 1354),
    ("Op fQxll", 888, 11170, 1316),
    ("PEMUDA TERSESAT.", 882, 13839, 1448),
    ("PENNY", 874, 12423, 1447),
    ("Marty", 872, 11758, 1395),
    ("7sw", 857, 11319, 1482),
    ("TTV_VwVendetta", 840, 12374, 1462),
    ("UpperHamster9244", 834, 12831, 1384),
    ("JakeOn90ping", 829, 12831, 1303),
    ("TZD Marci", 821, 12831, 1194),
    ("Magicasoso", 816, 12931, 1256),
    ("zb kaelen", 809, 12832, 1220),
    ("ꜰʀᴇᴇ xᴘ", 802, 12014, 1500),
    ("OwnedByAndý", 781, 11019, 1322),
    ("SAWーMatraˢᵉˡᵃᵗᵃᶯ", 770, 12923, 1169),
    ("ichinohane", 769, 12931, 1258),
    ("DiabeteSaurusZB", 768, 12841, 1296),
    ("Artkamron.IG", 764, 10699, 1451),
    ("DokK3abiXII", 763, 12922, 1258),
    ("TIKTOK ALONE BOY", 760, 12554, 1328),
    ("Ʋƞknown", 760, 12381, 1308),
    ("ItsAbixo Fan", 758, 12941, 1268),
    ("Scottish Swziry", 755, 13161, 1404),
    ("Dark-azak", 751, 12324, 1199),
    ("Whoa そ", 747, 12321, 1136),
    ("MF YUNGEN", 746, 12489, 1318),
    ("KAllDayEveryday", 745, 12231, 1145),
    ("EzClipZ-TTV", 744, 22335, 1494),
    ("we smokin ivan", 742, 12185, 1123),
    ("Bahgy", 737, 12123, 1267),
    ("NowWeGameTV", 734, 14496, 1194),
    ("小钰一拳锤哭好几个1", 733, 14231, 1371),
    ("Milea.exe", 731, 11899, 1429),
    ("Zero3ffortᵀᵀⱽ", 731, 14231, 1211),
    ("GLObal36", 729, 15312, 1481),
    ("Moody177", 728, 12903, 1288),
    ("GWAPO-_-8", 726, 11231, 1258),
    ("Nауr", 718, 15453, 1333),
    ("SorryımSleepy", 715, 12374, 1399),
    ("player21312", 711, 12293, 1254),
    ("TBSxBlackStar", 708, 13761, 1286),
    ("Oхin", 704, 11400, 1185),
    ("Twitch xxSHIFTx", 703, 11232, 1267),
    ("ToxicPunk_", 702, 11232, 1132),
    ("ᵀⁱᵏᵀᵒᵏBassie", 701, 11900, 1230),
    ("Dom-staa", 699, 11327, 1284),
    ("ᵗⁱᵏᵗᵒᵏ Favelado", 697, 11793, 1210),
    ("EVO KillingSpree", 696, 11800, 1301),
    ("Chizzy2K", 695, 11758, 1440),
    ("amber ͅ", 689, 11500, 1380),
    ("darleeean", 689, 10100, 1218),
    ("Peеk", 688, 10600, 1432),
    ("YouTube Vybess-", 686, 10608, 1290),
    ("VeYz-luNaTicS", 685, 10860, 1426)
]
   
# Inserir os dados na tabela
for jogador in dados_jogadores:
    cursor.execute('''
        INSERT INTO jogadores (nome, vitorias, kills, partidas)
        VALUES (?, ?, ?, ?)
    ''', jogador)

# Confirmar as alterações no banco de dados e fechar a conexão
conn.commit()
conn.close()
