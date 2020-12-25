import json
import requests
API_KEY = '&APIkey=f664ebf8b8068a555caade215a5493834309a319d85d9b22036609461e64edf4'

BASE_COUNTRY = {'Africa': '162', 'Albania': '1', 'Algeria': '2', 'Andorra': '3', 'Angola': '4', 'Argentina': '5', 'Armenia': '6', 'Asia': '163', 'Australia': '7', 'Australia & Oceania': '164', 'Austria': '8', 'Azerbaijan': '9', 'Bahrain': '10', 'Bangladesh': '11', 'Belarus': '12', 'Belgium': '13', 'Benin': '14', 'Bermuda': '15', 'Bolivia': '16', 'Bosnia and Herzegovina': '17', 'Botswana': '18', 'Brazil': '19', 'Bulgaria': '20', 'Burkina Faso': '21', 'Burundi': '22', 'Cambodia': '23', 'Cameroon': '24', 'Canada': '25', 'Cape Verde': '26', 'Chile': '27', 'China': '28', 'Colombia': '29', 'Costa Rica': '30', 'Croatia': '31', 'Cyprus': '32', 'Czech Republic': '33', 'Denmark': '34', 'Djibouti': '35', 'Dominican Republic': '36', 'DR Congo': '37', 'Ecuador': '38', 'Egypt': '39', 'El Salvador': '40', 'England': '41', 'Estonia': '42', 'Ethiopia': '43', 'Europe': '165', 'Faroe Islands': '44', 'Finland': '45', 'France': '46', 'FYR of Macedonia': '47', 'Gabon': '48', 'Gambia': '49', 'Georgia': '50', 'Germany': '51', 'Ghana': '52', 'Gibraltar': '53', 'Greece': '54', 'Guatemala': '55', 'Guinea': '56', 'Haiti': '57', 'Honduras': '58', 'Hong Kong': '59', 'Hungary': '60', 'Iceland': '61', 'India': '62', 'Indonesia': '63', 'Iran': '64', 'Iraq': '65', 'Ireland': '66', 'Israel': '67', 'Italy': '68', 'Ivory Coast': '69', 'Jamaica': '70', 'Japan': '71', 'Jordan': '72', 'Kazakhstan': '73', 'Kenya': '74', 'Kosovo': '75', 'Kuwait': '76', 'Kyrgyzstan': '77', 'Latvia': '78', 'Lebanon': '79', 'Lesotho': '80', 'Liberia': '81', 'Libya': '82', 'Liechtenstein': '83', 'Lithuania': '84', 'Luxembourg': '85', 'Malawi': '86', 'Malaysia': '87', 'Maldives': '88', 'Mali': '89', 'Malta': '90', 'Mauritania': '91', 'Mauritius': '92', 'Mexico': '93', 'Moldova': '94', 'Montenegro': '95', 'Morocco': '96', 'Mozambique': '97', 'Myanmar': '98', 'Namibia': '99', 'Netherlands': '100', 'New Zealand': '101', 'Nicaragua': '102', 'Niger': '103', 'Nigeria': '104', 'North & Central America': '166', 'Northern Ireland': '105', 'Norway': '106', 'Oman': '107', 'Pakistan': '108', 'Palestine': '109', 'Panama': '110', 'Paraguay': '111', 'Peru': '112', 'Philippines': '113', 'Poland': '114', 'Portugal': '115', 'Qatar': '116', 'Republic of the Congo': '117', 'Réunion': '118', 'Romania': '119', 'Russia': '120', 'Rwanda': '121', 'San Marino': '122', 'Saudi Arabia': '123', 'Scotland': '124', 'Senegal': '125', 'Serbia': '126', 'Seychelles': '127', 'Sierra Leone': '128', 'Singapore': '129', 'Slovakia': '130', 'Slovenia': '131', 'Somalia': '132', 'South Africa': '133', 'South America': '167', 'South Korea': '134', 'Spain': '135', 'Sri Lanka': '136', 'Sudan': '137', 'Swaziland': '138', 'Sweden': '139', 'Switzerland': '140', 'Syria': '141', 'Tajikistan': '142', 'Tanzania': '143', 'Thailand': '144', 'Togo': '145', 'Trinidad and Tobago': '146', 'Tunisia': '147', 'Turkey': '148', 'Turkmenistan': '149', 'Uganda': '150', 'Ukraine': '151', 'United Arab Emirates': '152', 'Uruguay': '153', 'USA': '154', 'Uzbekistan': '155', 'Venezuela': '156', 'Vietnam': '157', 'Wales': '158', 'World': '168', 'Yemen': '159', 'Zambia': '160', 'Zimbabwe': '161'}

# def handler():
#     for i,z in BASE_COUNTRY.items():
#     # country = Country.objects.create(name=i)
#         BASE_LEAGUE = ('https://apiv2.apifootball.com/?action=get_leagues&country_id=' + z + API_KEY)
#         url = requests.get(BASE_LEAGUE).text
#         data = json.loads(url)
#         for items in data:
#             country_name = items['country_name']
#             # number = items[0]['country_id']
#             # name_league = items[0]['league_name']
#             # league_id = items[0]['league_id']
#             print(f"Имя странны: {country_name}")
#
#
# handler()

BASE_TEAM = ('https://apiv2.apifootball.com/?action=get_teams&league_id=' + '2' + API_KEY)
url = requests.get(BASE_TEAM).text
data = json.loads(url)

for items in data:
    name_team = items['team_name']
    team_id = items['team_key']
    print(name_team, team_id)

