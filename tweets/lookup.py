AGENCY_ACRONYMS = {
  # geographic
  'New York Police Department':'NYPD',
  'Los Angeles Police Department': 'LAPD',
  # turn into nouns
  "Sheriff's Department":'Sheriffs',
  'Sheriff Office':'Sheriffs',
  "Sheriff's Office":'Sheriffs',
  "Sherrif's Department": 'Sheriffs',
  "police officers": "officers",
  # department specific
  'Police Department':'PD',
  'Police Deptartment': 'PD', #typo
  'State Police': 'SP',
  "Drug Enforcement Administration": 'DEA Agents',
  "Special Response Team": 'SWAT', #effectively equivalent
  "uniformed Secret Service": "Secret Service", #too long, shorten
  " and ": '&', #ampersands are cool
  }

# gross hack
# but we need some way to link the sequential images with fatal encounters
# and the designer is unable to change the output filename format
IMAGE_ID_LOOKUP = {
  "Raymond Herisse":1,
  "Stanley LaVon Gibson":2,
  "Dason Peters":3,
  "Dylan Samuel-Peters":4,
  "Rosette Samuel":5,
  "Jeremy Powell":6,
  "Kermith Sonnier Jr.":7,
  "Aaron Hunter":8,
  "Ahmede Jabbar Bradley":9,
  "Amos G. Smith":10,
  "Andrena Kitt":11,
  "Anthony Rawls":12,
  "Bobby Moore III":13,
  "Brandon Jones":14,
  "Cameron Massey":15,
  "Carleton J. Wallace":16,
  "Carlos Williams":17,
  "Carulus Hines":18,
  "Cheryl Blount-Burton":19,
  "Dakota Bright":20,
  "David Lee Turner":21,
  "David O. Okot":22,
  "Dawntree Ta'Shawn Williams":23,
  "DeJuan Colbert":24,
  "Demarcus Derell Celestine":25,
  "Deonte Traylor":26,
  "DeOntrel Davis":27,
  "Georgy Louisgene":28,
  "Herman Pickens":29,
  "Ishmael Muhammad":30,
  "Jack Lamar Robertson":31,
  "Jacqueline Culp":32,
  "Jalen Ricks":33,
  "James Brissette":34,
  "James Brown":35,
  "Joetavius Stafford":36,
  "Jonathan A. Ferrell":37,
  "Kedrian Edwards":38,
  "Kendall Walker":39,
  "Kenneth Chamberlain Sr.":40,
  "Kenneth Dewayne Cooper":41,
  "Kenneth Harding":42,
  "Kenneth King":43,
  "Kenneth Suggs":44,
  "Kenneth Walker":45,
  "Kevin Bolden":46,
  "Kevin M. Bailey":47,
  "Kevin Willingham":48,
  "Kimani Gray":49,
  "Korey Marcel Germaine":50,
  "Latricka Sloan":51,
  "Louis DecQuir":52,
  "Mister Bobby Lowe":53,
  "Monroe Isadore":54,
  "Montellis Clark":55,
  "Ray Charles Hayes":56,
  "Raymond A. Smith":57,
  "Ron Pettaway":58,
  "Ronald Madison":59,
  'Sammie "Junebug" Davis Jr.':60,
  "Samuel Thomas Cunningham III":61,
  "Shawn J. Maxwell":62,
  "Shelley Amos":63,
  "Stacy Rondell Bostic":64,
  "Stephen Seignious":65,
  "Taft Sellers":66,
  "Tendai Nhekairo":67,
  "Terrance Lamar Abrams":68,
  "Terry Laffitte":69,
  "Timothy Stansbury Jr.":70,
  "Tony Louis Francis":71,
  "Trevion Davis":72,
  "Waseem Jung":73,
  "Willie Davis Jr.":74,
  "Tyler Damon Woods":75,
  "Aaron Jones":76,
  "Aaron Marcell Campbell":77,
  "Alan Blueford":78,
  "Amir Rashid Crump":79,
  "Angel Jesus Hinojoza":80,
  "Anita Gay":81,
  "Anthony Antwan Davis":82,
  "Anthony Minner":83,
  "Barrington Hall":84,
  "Bernard Pate":85,
  "Billy Ray Finks":86,
  "Booker Carloss II":87,
  "Byron Hammick":88,
  "Casper Banjo":89,
  "Charles M. Rorie III":90,
  "Charles Whaley":91,
  "Christopher Hawkins":92,
  "Damien W. Morton":93,
  "Damon Edward Beal":94,
  "Daniel Taiwan Hathorne":95,
  "Darris Eugene Johnson":96,
  "Davon Jackson":97,
  "Denise Nicole Glasco":98,
  "Deon Johnson":99,
  "Derrick Jones":100,
  "Ernest Williams Jr.":101,
  "Frakelin Marice Hardy":102,
  "Gary King Jr.":103,
  "Glen Willis":104,
  "Glennel Givens Jr.":105,
  "Hezekiah Lewis":106,
  "James Jahar Perez":107,
  "Jamil Wheatfall":108,
  "Jeffrey Williams":109,
  "John Sloan":110,
  "Johnnie Weatherspoon":111,
  "Johnny Lee Wicks":112,
  "Justin Brimmer":113,
  "Keaton Dupree Otis":114,
  "Keith Maurice Williams":115,
  "Kendra James":116,
  "Kyone Johnson":117,
  "Lovelle Mixon":118,
  "Orlando Barlow":119,
  "Raheim Brown":120,
  "Richard Bernard Nolton":121,
  "Ronald Brazier":122,
  "Ronald Neal Joseph Jr.":123,
  "Roshawn Hill":124,
  "Sammie Lee Clay":125,
  "Sharmel Edwards":126,
  "Swauve Devon Lopez":127,
  "Tarance Deshon Hall":128,
  "Terrance Mearis":129,
  "Tommy Lee Gest":130,
  "Trevon Cole":131,
  "Tyrise M. Bell":132,
  "Vernon Allen":133,
  "Willie Thomas Grigsby":134,
  "Willie Wilkens":135,
  "Oscar Grant III":136,
  "Kenneth Jewell Stafford":137,
  "Rodney L. Wright":138,
  "D'Andre Berghardt Jr.":139,
  "Bernard Lofton":140,
  "Shawn Dean":141,
  "Daryl Hicks":142,
  "Alfred Redwine":143,
  "Vincent Wood":144,
  "James Lewis":145,
  "William Billy Lomax":146,
  "Thomas G. Manuel III":147,
  "Alexander Wilson":148,
  "Dennis Clark III":149,
  "Archie Lee Chambers Jr.":150,
  "Larry Hooker":151,
  "Amjustine Hunter":152,
  "Kenzell Hobbs":153,
  "Cary Ball":154,
  "James Coleman":155,
  "Cody Point":156,
  "Byron Carter Jr.":157,
  "Tavontae Jamar Haney":158,
  "Ryan Koontz":159,
  "Kenneth Knight":160,
  "Stephen O'Neal Wattley II":161,
  "Malik Williams":162,
  "John Adams":163,
  "Gabriel Winzer":164,
  "Thomas Dewitt Johnson":165,
  "Eddie Callaway":166,
  "Demetrius Bennett":167,
  "Carnell Moore":168,
  "Jordan West-Morson":169,
  "Marquis James Spencer":170,
  "Tywon Jones":171,
  "Emmanuel Gatewood":172,
  "Kourtney Hahn":173,
  "Kendra Diggs":174,
  "Shaaliver Douse":175,
  "Maurice Leroy Cox":176,
  "Lawrence Smith":177,
  "Mohamed Bah":178,
  "Darrien Hunt":179,
  "Jared Brown-Garnham":180,
  "Alonzo Ashley":181,
  "DeAunta Terrell Farrow":182,
  "Jeremey Lake":183,
  "Edward Ned Jr.":184,
  "Malissa Williams":185,
  "Timothy Russell":186,
  "Kendrick Brown":187,
  "Ricky Junior Toney":188,
  "William Jackson":189,
  "Anthony Dwain Lee":190,
  "Tyrone F. Thomas":191,
  "Peter Jourdan":192,
  "Tysheen Bourne":193,
  "Andre Fields":194,
  "Annette Green":195,
  "Ronald Beasley":196,
  "Earl Murray":197,
  "Dainell Simmons":198,
  "Charles A. Baker Jr.":199,
  "Orlando Santos":200,
  "Kenneth R. Herring":201,
  "Cimarron Lamar Lamb":202,
  "Jacqueline Reynolds":203,
  "Marlon Brown":204,
  "Cameron Tillman":205,
  "Keith T. Shumway":206,
  "Blondel Lassegue":207,
  "Paul Johnson":208,
  "Patricia Thompson":209,
  "Ernest Prather":210,
  "Darryl Bain":211,
  "Tamon Robinson":212,
  "Christian Eaddy":213,
  "Jermaine Darden":214,
  "Hayden Blackman":215,
  "Robert Desir":216,
  "Jose Quinonez":217,
  "Don White":218,
  "Abdul Kamal":219,
  "Shawn M. Rieves":220,
  "Willie James Williams":221,
  "Jason D. White":222,
  "Jonathan Wilcher":223,
  "Sharon Rebecca McDowell":224,
  "James Torres":225,
  "Somourian Jamal Wingo":226,
  "Kendall Alexander":227,
  "Julias Michael Reese":228,
  "Christopher Ridley":229,
  "Jeffrey Ragland":230,
  "Jelani Manigault":231,
  "Jerome Alford":232,
  "Terrence Thomas":233,
  "Timur Person":234,
  "Walter Washington":235,
  "Zikarious Flint":236,
  "Dashawn Vasconcellos":237,
  "Paul Smith":238,
  "Gregory Vaughn Hill Jr":239,
  "Henry Jackson":240,
  "Dominique Smith":241,
  "Ramesh Dwayne Sweeney":242,
  "Vernard Davis":243,
  "Lawrence Rogers":244,
  "Eldrin Smart":245,
  "Pierree Davis":246,
  "Charles Hull":247,
  "Christopher Stirkens":248,
  "Rafael Briscoe":249,
  "Jamil Moore":250,
  "Christopher Brown":251,
  "Anesson Joseph":252,
  "James L. Norris":253,
  "Shantel Davis":254,
  "Reno Sayles":255,
  "Anton Barrett":256,
  "Marshall Tobin":257,
  "Mario Romero":258,
  "Kendrec McDade":259,
  "Terrance Terrell Franklin":260,
  'Gerald "Skip" Tyrone Murphy':261,
  "Louis M. Squires":262,
  "Frankie Pitt":263,
  "Ramarley Graham":264,
  "Lejoy Grissom":265,
  "Terrence Dawson":266,
  "Henry Glover":267,
  'Joshua "Omar" Johnson':268,
  "Anthony Michael Bland":269,
  'Belton "Amir" Lomax':270,
  "Clinton Roebexar Allen":271,
  "Julian Dawkins":272,
  "Thomas Bean":273,
  "Charles Curl":274,
  "Leonard Thomas":275,
  "Ajani Mitchell":276,
  "William Dupree":277,
  "Jaleel Jackson":278,
  "Nathaniel McRae":279,
  "Gary Hatcher":280,
  "Aiyana Mo'Nay Stanley Jones":281,
  "Jermie McCraven":282,
  "Christian Freeman":283,
  "Hernandez Dowdy":284,
  "Lorenzo Davis":285,
  "Delois Epps":286,
  "Makayla Ross":287,
  "Justin Thompson":288,
  "Charles Livingston III":289,
  "Steven Askew":290,
  "Horace Whiting":291,
  "John Walker":292,
  "Marvin Amerson":293,
  "Aaron Dumas":294,
  "Dwight Moorer Jr.":295,
  "Keoshia L. Hill":296,
  "Bill Jackson":297,
  "Edward Mwaura":298,
  "Sherlon Smikle":299,
  "Lana Morris":300,
  "Rustin Wilkerson":301,
  "Virgil Millon":302,
  "Dontae Daveon Lewis Hayes":303,
  "Lee Deante Brown":304,
  'Terry "Big Champ" Rabb':305,
  "Summer Marie Lane":306,
  "Volne Lamont Stokes":307,
  "Joseph Paige":308,
  "Darrius J. Lowery-Baptiste":309,
  "Wayne Arnold Jones":310,
  "Joe White III":311,
  "Antwon Johnson":312,
  "Recardio Shormon Clark":313,
  "Sammie Lamont Wallace":314,
  "Michael Westly":315,
  "Cedric Howard":316,
  "Eliakim Shabazz":317,
  "Jaquaz Walker":318,
  "Lawrence Allen":319,
  "Adolphus Pinkney":320,
  "Darrell Banks":321,
  "Donnell Carter":322,
  "Jourdan Akili Wagner":323,
  "Cacedrick White":324,
  "Elip Cheatham":325,
  "Michael Lembhard":326,
  "Terry Davis":327,
  "Marvin E. Parker":328,
  "Deangelo Lopez":329,
  "James Eric Griffin":330,
  "Willie Sudduth":331,
  "Kenneth Smith":332,
  "Aron Jones":333,
  "Leon James":334,
  "Angelo Ferguson":335,
  "David Crenshaw":336,
  "Laray Renshaw":337,
  "Brandon McCloud":338,
  "Eren Beyah":339,
  "Ricardo Mason":340,
  "Jeffrey Hopkins":341,
  "Stephon Keith Moore":342,
  "Craig Bickerstaff":343,
  "Jermaine Sanders":344,
  "Daniel Harris":345,
  "Icarus Randolph":346,
  "Eric Garner":347,
  "Miriam Iris Carey":348,
  "Larry Eugene Jackson Jr.":349,
  "Michael Brown":350,
  "Dontre Hamilton":351,
  "Bryan Stukes":352,
  "Steven Tyrone Mallory":353,
  "Ezell Ford":354,
  "Micah Anthony Key":355,
  "Seneca Darden":356,
  "David Latham":357,
  "Levester Carter Jr.":358,
  "Tevin Robinson":359,
  "Ronald Roland":360,
  "Darius Colegarrit":361,
  "Michael Myers":362,
  "Warren Robinson":363,
  "Rekia Boyd":364,
  "Flint Farmer":365,
  "Burrell Ramsey-White":366,
  "Travis Floyd":367,
  "Dartanya Bentley, Jr.":368,
  "Timothy Thomas":369,
  "Remis M. Andrews":370,
  "John H. Crawford III":371,
  "Derek Deandre Walker":372,
  "Hydra Lacy Jr.":373,
  "Michelle Cusseaux":374,
  "Milton Hall":375,
  "Stephon Watts":376,
  "Davon Mullins":377,
  "Danroy Henry Jr.":378,
  "Greg Thompson Jr.":379,
  "Idriss Shelley":380,
  "Howard Tucker":381,
  "Nahcream Moore":382,
  "Jerry Brown":383,
  "Londrell E. Johnson":384,
  "Timothy Wall":385,
  "David Ellis":386,
  "Jason Harrison":387,
  "Brian Simms Jr.":388,
  "Quentin Eric Hicks":389,
  "Yvette Smith":390,
  "Kayla Moore":391,
  "Oliver 'Big 'O'' Lefiti":392,
  "Kathryn Johnston":393,
  "Gregory Hooper":394,
  "Antonio Latuanee Pryce":395,
  "Marquez Eugene Smart":396,
  "Albert Duane Denton":397,
  "Victor White III":398,
  "Lajuanzo Brooks":399,
  "Donte Lamonte Jordan":400,
  "Darius Jamal Murphy":401,
  "Michael Anglin Jr.":402,
  "Jose Valerio":403,
  "Rexford Dasrath":404,
  "Mark Anthony Barmore":405,
  "Michael Moore":406,
  "Ismael Sadiq":407,
  "Eurie Stamps":408,
  "Eddie Davis":409,
  "Kajieme Powell":410,
  "Shawn Greenwood":411,
  "Mark Salazar":412,
  "Alfred Sanders":413,
  'Clifton "Pete" Lee Jr.':414,
  "Jacorey Calhoun":415,
  "Nathaniel McRae":416,
  "Maurice Clemmons":417,
  "John Frank Brown":418,
  "Bert W. Bowen":419,
  "Justin Sipp":420,
  "Hailu Brook":421,
  "Wendell Allen":422,
  "Michael McCullen":423,
  "Tarika Wilson":424,
  "Clifford Paul Maxwell":425,
  "John Bior Deng":426,
  "Reginald Bernard Smith":427,
  "Omar Abrego":428,
  "Tommy Yancy":429,
  "La-Reko Williams":430,
  "Roshad McIntosh":431,
  "Desean Pittman":432,
  "Rondre Hornbeak":433,
  "Dante Parker":434,
  "Jacorey Calhoun":435,
  "Steven Lashone Douglas":436,
  "Marcella Byrd":437,
  "Sean Bell":438,
  "Chavis Carter":439,
  "Victor Demarius Steen":440,
  "Lawrence H. Faine":441,
  "Manuel Loggins Jr.":442,
  "Melvin Lawhorn":443,
  "Jordan Baker":444,
  "Timothy Russell":445,
  "Steve Eugene Washington":446,
  "Ousmane Zongo":447,
  "Shurron Grant":448,
  "Gregory Lewis":449,
  "Michael Sanders":450,
  "James Edward Taylor":451,
  "Rodney Abernathy":452,
  "Albert Rucker":453,
  "Robert Ventry":454,
  "Cortez Washington":455,
  "Montez Dewayne Hambric":456,
  "Pierre M. Jackson":457,
  "Tyrone Brown":458,
  "James Rivera":459,
  'Deandre "Trey" Brunston':460,
  "Antoinette Griffin":461,
  "Erica Stevenson":462,
  "Dominique Hurtt":463,
  "Antonio Miller":464,
  "Quentin Maurice Reed":465,
  "David Wayne Summers":466,
  "John Lindsey Myers":467,
  "Julian Alexander":468,
  "Woodrow Player III":469,
  "Alberta Spruill":470,
  "Ernest Vassell":471,
  "Kiwane Carrington":472,
  "Marquise Jones":473,
  "Michael Blair":474,
  "Justin Fields":475,
  "Larry Jerome Jenkins":476,
  "Eugene N. Turner III":477,
  "Mark Fernandes McMullen":478,
  "Maliki Yawmi-Deen Raymond":479,
  "Guy Jermone Jarreau Jr.":480,
  "Russell Lydell Smith":481,
  "James Lamont":482,
  "Desjon Jamal Edwards":483,
  "Donovan Tyrone Graham":484,
  "Frederick Devon McAllister":485,
  'Gary "Chris" Tyson':486,
  "Jamar Marrow":487,
  "Jashon Bryant":488,
  "Jonathan Mosely":489,
  "Mack N. Lucky":490,
  "Marcus G. Brown":491,
  "Raylyn George":492,
  "Robert Davis":493,
  "Tyshan Napoleon":494,
  "Othniel Askew":495,
  "Eric Stuart Allen Jones":496,
  "Allen Newsome":497,
  "Lavon King":498,
  "Aaron Harrison":499,
  "Ryan L. Stokes":500,
  "Gregory Lewis Towns Jr":501,
  "Malcolm Ferguson":502,
  "Marlon Horton":503,
  "Corey Ward":504,
  "Glen Boldware":505,
  "Ronald Boone":506,
  "Manuel DaVeiga":507,
  "Tahiem Goffe":508,
  "Joseph Ramos":509,
  "Kerby Revelus":510,
  "Denis Reynoso":511,
  "Stanley Seney":512,
  "Clyde D. Ratcliff":513,
  "Brandon Payne":514,
  "Delano M. Walker":515,
  "Douglas Cooper":516,
  "Cornel Young Jr.":517,
  "Howard Wallace Bowe Jr.":518,
  "Shem Walker":519,
  "Errol Shaw Sr.":520,
  "James C. Tomlin":521,
  "Clifton Armstrong":522,
  "Antonio Bryant":523,
  "Lennard Whittle":524,
  "Herve Gilles":525,
  "Lonnie Taylor":526,
  "George Harvey":527,
  "Jonathan D. Rogers":528,
  "Shereese Francis":529,
  "Perlie Golden":530,
  "Nathaniel Cobbs":531,
  "Darin John Richardson":532,
  "Khazyier Pugh":533,
  "Duane Brown":534,
  #batch 2
  "Jack Sun Keewatinawin":1,
  "Andy Lopez":2,
  "Adolfo Vargas Tovar":3,
  "Angel Miguel Lopez":4,
  'Bernie Cervantes "Chino" Villegas':5,
  "Carlos Carrillo":6,
  "Christopher Jonathan Gonzales":7,
  "David Miguel Ventura":8,
  "Denis John Chabot":9,
  "Denny Gonzales":10,
  "Eliseo Mercado":11,
  "Eric Marquez":12,
  "Esau Marin":13,
  "Husien Shehada":14,
  "Joel Acevedo":15,
}