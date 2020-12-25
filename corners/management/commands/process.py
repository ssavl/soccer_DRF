from django.core.management.base import BaseCommand, CommandError
from corners.models import Country, League, Team, StatsCorner
import json
import requests

API_KEY = '&APIkey=f664ebf8b8068a555caade215a5493834309a319d85d9b22036609461e64edf4'
BASE_URL = ('https://apiv2.apifootball.com/?action=get_countries' + API_KEY)

###############################################################################################
BASE_COUNTRY = {'Africa': '162', 'Albania': '1', 'Algeria': '2', 'Andorra': '3', 'Angola': '4', 'Argentina': '5',
                'Armenia': '6', 'Asia': '163', 'Australia': '7', 'Australia & Oceania': '164', 'Austria': '8',
                'Azerbaijan': '9', 'Bahrain': '10', 'Bangladesh': '11', 'Belarus': '12', 'Belgium': '13', 'Benin': '14',
                'Bermuda': '15', 'Bolivia': '16', 'Bosnia and Herzegovina': '17', 'Botswana': '18', 'Brazil': '19',
                'Bulgaria': '20', 'Burkina Faso': '21', 'Burundi': '22', 'Cambodia': '23', 'Cameroon': '24',
                'Canada': '25', 'Cape Verde': '26', 'Chile': '27', 'China': '28', 'Colombia': '29', 'Costa Rica': '30',
                'Croatia': '31', 'Cyprus': '32', 'Czech Republic': '33', 'Denmark': '34', 'Djibouti': '35',
                'Dominican Republic': '36', 'DR Congo': '37', 'Ecuador': '38', 'Egypt': '39', 'El Salvador': '40',
                'England': '41', 'Estonia': '42', 'Ethiopia': '43', 'Europe': '165', 'Faroe Islands': '44',
                'Finland': '45', 'France': '46', 'FYR of Macedonia': '47', 'Gabon': '48', 'Gambia': '49',
                'Georgia': '50', 'Germany': '51', 'Ghana': '52', 'Gibraltar': '53', 'Greece': '54', 'Guatemala': '55',
                'Guinea': '56', 'Haiti': '57', 'Honduras': '58', 'Hong Kong': '59', 'Hungary': '60', 'Iceland': '61',
                'India': '62', 'Indonesia': '63', 'Iran': '64', 'Iraq': '65', 'Ireland': '66', 'Israel': '67',
                'Italy': '68', 'Ivory Coast': '69', 'Jamaica': '70', 'Japan': '71', 'Jordan': '72', 'Kazakhstan': '73',
                'Kenya': '74', 'Kosovo': '75', 'Kuwait': '76', 'Kyrgyzstan': '77', 'Latvia': '78', 'Lebanon': '79',
                'Lesotho': '80', 'Liberia': '81', 'Libya': '82', 'Liechtenstein': '83', 'Lithuania': '84',
                'Luxembourg': '85', 'Malawi': '86', 'Malaysia': '87', 'Maldives': '88', 'Mali': '89', 'Malta': '90',
                'Mauritania': '91', 'Mauritius': '92', 'Mexico': '93', 'Moldova': '94', 'Montenegro': '95',
                'Morocco': '96', 'Mozambique': '97', 'Myanmar': '98', 'Namibia': '99', 'Netherlands': '100',
                'New Zealand': '101', 'Nicaragua': '102', 'Niger': '103', 'Nigeria': '104',
                'North & Central America': '166', 'Northern Ireland': '105', 'Norway': '106', 'Oman': '107',
                'Pakistan': '108', 'Palestine': '109', 'Panama': '110', 'Paraguay': '111', 'Peru': '112',
                'Philippines': '113', 'Poland': '114', 'Portugal': '115', 'Qatar': '116',
                'Republic of the Congo': '117', 'Réunion': '118', 'Romania': '119', 'Russia': '120', 'Rwanda': '121',
                'San Marino': '122', 'Saudi Arabia': '123', 'Scotland': '124', 'Senegal': '125', 'Serbia': '126',
                'Seychelles': '127', 'Sierra Leone': '128', 'Singapore': '129', 'Slovakia': '130', 'Slovenia': '131',
                'Somalia': '132', 'South Africa': '133', 'South America': '167', 'South Korea': '134', 'Spain': '135',
                'Sri Lanka': '136', 'Sudan': '137', 'Swaziland': '138', 'Sweden': '139', 'Switzerland': '140',
                'Syria': '141', 'Tajikistan': '142', 'Tanzania': '143', 'Thailand': '144', 'Togo': '145',
                'Trinidad and Tobago': '146', 'Tunisia': '147', 'Turkey': '148', 'Turkmenistan': '149', 'Uganda': '150',
                'Ukraine': '151', 'United Arab Emirates': '152', 'Uruguay': '153', 'USA': '154', 'Uzbekistan': '155',
                'Venezuela': '156', 'Vietnam': '157', 'Wales': '158', 'World': '168', 'Yemen': '159', 'Zambia': '160',
                'Zimbabwe': '161'}
BASE_LEAGUE = {'Africa Cup of Nations': '559', 'Albanian Cup': '2', 'Algeria Cup': '5', 'Andorra Cup': '8',
               'Girabola': '10', 'Copa Argentina': '17', 'Armenian Cup': '21', 'A-League': '23',
               'OFC Champions League': '580', '2. Liga': '34', 'Azerbaijan Cup': '42', 'Bahrain Cup': '45',
               'Premier League': '522', 'Belarusian Cup': '49', '1st National Women': '9658', 'Ligue 1': '433',
               'Division Profesional': '62', 'Bosnia and Herzegovina Cup': '66', 'Brasileiro U20': '8669',
               'B PFG East': '80', 'Primus League': '86', 'C-League': '87', 'Elite One': '88',
               'Canadian Premier League': '9885', 'Campeonato Nacional': '92', 'Chilean Cup': '95', 'FA Cup': '316',
               'Copa Colombia': '105', 'Copa Costa Rica': '108', '1. HNL': '110', '2. Division B1': '116',
               '1. Liga': '9673', '1st Division': '131', 'Division 1': '556', 'LDF': '141', 'Copa Ecuador': '10010',
               'Egypt Cup': '145', 'Primera Division': '147', 'Championship': '149', 'Esiliiga': '159',
               'Antalya Cup': '8802', 'Faroe Islands Cup': '164', 'Kakkonen East': '8680', 'Coupe de France': '184',
               'Championnat D1': '190', 'GFA League': '191', 'Erovnuli Liga': '192', '2. Bundesliga': '196',
               'Gibraltar Cup': '207', 'Football League': '210', 'Liga Nacional': '222', 'Championnat National': '507',
               'Hungarian Cup': '229', 'Division 2': '234', 'Calcutta Premier Division A': '242',
               'Championship Cup': '9669', 'Super League': '557', 'Leumit League': '258', 'Coppa Italia': '8726',
               'Emperors Cup': '277', 'Jordan Cup': '282', 'First Division': '10038', 'Kosovar Cup': '291',
               'Emir Cup': '294', 'Premier Liga': '296', 'LFA First Division': '303', 'Liechtenstein Cup': '305',
               'A Lyga': '306', 'Luxembourg Cup': '311', 'Dhivehi Premier League': '317', 'Premiere Division': '319',
               'Mauritian League': '326', 'Ascenso MX': '328', 'Divizia Nationala': '331', 'Druga Liga': '335',
               'Botola 2': '338', 'Mocambola': '340', 'National League': '341', 'MTC Premiership': '342',
               'Derde Divisie': '346', 'Football Championship': '350', 'Liga Primera': '351', 'Aiteo Cup': '9912',
               'Campeones Cup': '9952', 'Charity Shield': '358', 'Division 2 - Group 1': '361',
               'Professional League': '369', 'West Bank League': '373', 'LPF': '374', 'Copa Paraguay': '10046',
               'Copa Bicentenario': '9917', 'Copa Paulino Alcantara': '10047', 'Central Youth League': '390',
               'Campeonato de Portugal': '393', 'Crown Prince Cup': '9683', 'Regionale 1': '399', 'Cupa Ligii': '405',
               'FNL': '408', 'National Football league': '417', 'Campionato Sammarinese': '418', 'Challenge Cup': '432',
               'Prva Liga': '435', 'First Division League': '437', 'League Cup': '441', '2. liga': '444',
               '1. SZNL Women': '10052', 'Nation Link Telecom Championship': '457', 'GladAfrica Championship': '459',
               'Copa América': '607', 'K League 1': '463', 'Copa de la Reina Women': '8764', 'Champions League': '478',
               'Allsvenskan': '481', '1.Liga Classic Group 1': '494', 'Vysshaya Liga': '502', 'Ligi Kuu Bara': '503',
               'Champions Cup': '506', 'Pro League': '508', 'Ligue 2': '9931', '1. Lig': '512', 'Yokary Liga': '521',
               'Druha Liga': '525', 'Arabian Gulf Cup': '530', 'Liguilla': '535', 'Atlanta MLS Challenge': '541',
               'Super Cup': '9943', 'Copa Hesperia': '549', 'V.League 1': '550', 'Cymru Alliance': '553',
               'Algarve Cup Women': '8864', 'Premier Soccer League': '558'}
BASE_TEAM = {'Tunisia': 8227, 'Laci': '3', 'Saoura': '37', 'UE Santa Coloma': '101', 'Primeiro de Agosto': '114',
             'Estudiantes L.P.': '204', 'Gandzasar': '697', 'Central Coast Mariners': '705', 'Auckland City': '5174',
             'Wacker Innsbruck': '934', 'Neftci Baku': '1012', 'Al Riffa': '1024', 'Vipers': '1', 'Brest': '1055',
             'Femina Woluwe W': '12552', 'Niary Tally': '6663', 'Blooming': '1442', 'FK Sarajevo': '1454',
             'Corinthians U20 (Bra)': '9077', 'Bujumbura C.': '1731', 'Electricite Du Cambodge': '1733',
             'Colombe Lobo': '1745', 'Edmonton': '1767', 'Mindelense': '1826', 'Antofagasta': '1836', 'Kedah': '4776',
             'Cortulua': '1937', 'Istra 1961': '2048', 'Grobina': '4535', 'F. Amager': '2345',
             'Atletico Pantoja': '2412', 'Delfin': '2467', 'Wadi Degla': '2565', 'Santa Tecla': '2599',
             'Swansea': '2618', 'Parnu JK Vaprus': '2833', 'HB Torshavn': '2930', 'Lille': '3022',
             'CF Mounana (Gab)': '8280', 'Brikama U.': '3177', 'Dinamo Batumi': '3190', 'Stuttgart': '3221',
             'Lions Gibraltar': '3413', 'Trikala FC': '3444', 'CD Honduras': '3623', 'AS Togo-Port': '7565',
             'Puskas Academy': '3643', 'IR Reykjavik': '3839', 'Mohun Bagan': '3902', 'Kabwe': '8190',
             'Beitar Tel Aviv': '4120', 'Torino': '4170', 'FC Tokyo': '4363', 'Al Ahli': '4438', 'FK Akzhayik': '4456',
             'KF Feronikeli': '4489', 'Al Qadisiya': '4506', 'Alay Osh': '4521', 'LPRC Oiler': '4606',
             'Eschen C': '4645', 'Suduva': '4574', 'Benfica': '4695', 'Maziya': '4820', 'Black Stars': '4825',
             'Grande Riviere': '4883', 'Celaya': '4911', 'Milsami': '4937', 'Decic': '4973', 'Kawkab Marrakech': '5006',
             'Ferroviario Beira': '5035', 'Zwekapin United': '5050', 'Tura Magic': '5063', 'Lienden': '5117',
             'Waitakere United': '5173', 'Managua FC': '5177', 'Gombe': '5201', 'Club America': '4904', 'Floro': '5443',
             'Fanja SC': '5670', 'Ahli Al-Khalil': '5714', 'Miguelito': '5726', 'Sp. Luqueno': '5738',
             'Comerciantes Unidos': '5810', 'Gornik Z. U18': '12604', 'U. Madeira': '6127', 'Al-Duhail': '6262',
             'Trois Bassins': '6289', 'SKA Khabarovsk': '6417', 'AS Kigali': '6533', 'Domagnano': '6549',
             'Solihull': '2719', 'Borac': '6677', 'Lightstars': '6714', 'Podbrezova': '6745',
             'O. Ljubljana W (Slo)': '11841', 'Banaadir': '6951', 'Ajax Cape Town': '6965', 'Brazil': '8300',
             'Jeonbuk': '7004', 'Betis W': '9379', 'UP Country Lions': '7220', 'AIK': '7262',
             'La Chaux-De-Fonds': '7414', 'Istiqlol Dushanbe': '7520', 'Tanzania Prisons': '7528',
             'Chiangrai Utd': '7557', 'Central FC': '7580', 'CO Medenine': '7590', 'Bursaspor': '7607',
             'Altyn Asyr': '7741', 'Veres Rivne': '7770', 'Al Ain': '7831', 'Ho Chi Minh': '8075', 'Prestatyn': '8094',
             'Germany W': '9841', 'CAPS Utd': '8209'}


###############################################################################################
# teams = {}

class Command(BaseCommand):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def handle (self, *args, **options):
        for name_country, number_country in BASE_COUNTRY.items():
            country = Country.objects.create(name=name_country,number=number_country)
            base_leagues = ('https://apiv2.apifootball.com/?action=get_leagues&country_id=' + number_country + API_KEY)
            url = requests.get(base_leagues).text
            data = json.loads(url)
            for items in data:

                name_league = items['league_name']
                league_id = items['league_id']
                leagues = League.objects.create(name=name_league,number=league_id,key=country)

                BASE_TEAM = ('https://apiv2.apifootball.com/?action=get_teams&league_id=' + league_id + API_KEY)
                url = requests.get(BASE_TEAM).text
                data = json.loads(url)
                try:
                    for items in data:
                        name_team = items['team_name']
                        team_id = items['team_key']
                        Team.objects.create(name=name_team, number=team_id, key=leagues)
                except:pass


#
# from django.core.management import BaseCommand
#
# from processing.models import Country, Team, Player
# import requests
# import json
#
# WEB_ADDRESS = 'https://apiv2.apifootball.com/?action=get_teams&league_id=164&APIkey=3bf98daddb6610ed6e6d88d195637e6b70345db8697e3d33f20a817390e41051'
#
# COUNTRY_MAPPING = {
#     'Forel Islands': 'https://apiv2.apifootball.com/?action=get_teams&league_id=164&APIkey=3bf98daddb6610ed6e6d88d195637e6b70345db8697e3d33f20a817390e41051',
#     'Bahrain': 'https://apiv2.apifootball.com/?action=get_teams&league_id=44&APIkey=3bf98daddb6610ed6e6d88d195637e6b70345db8697e3d33f20a817390e41051',
#
# }
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **kwargs):
#         for country_name, country_web_address in COUNTRY_MAPPING.items():
#             country = Country.objects.create(name=country_name)
#             response = requests.get(country_web_address)
#             data = json.loads(response.text)  # '{"a": 2}' -> {'a': 2}
#             for team in data:
#                 name = team['team_name']
#                 created_team = Team.objects.create(
#                     title=name,
#                     country=country,
#                 )
#                 players = team['players']
#                 for player in players:
#                     name = player['player_name']
#                     age = player['player_age']
#                     if age == '?':
#                         age = 0
#                     avg_yellow = player['player_yellow_cards']
#                     surname = ''
#                     Player.objects.create(
#                         name=name,
#                         age=age,
#                         average_yellow_cards_count=avg_yellow,
#                         surname=surname,
#                         team=created_team,
#                     )
