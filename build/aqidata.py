# -*- coding: utf-8 -*-
"""Indian city AQI snapshot.

SOURCE   : aqi.in live city tables (US AQI), captured 12 November 2026
SCALE    : US AQI, stored exactly as the source publishes it. The index formally
           tops out at 500 but aqi.in extrapolates past that in severe episodes
           (Barnala 892 on 12 Nov). We keep their number so the figure matches
           the source we cite and link. Do not mix CPCB
           band labels into this data -- the two scales break at different numbers.
THRESHOLD: AQI_THRESHOLD below is the line between "an air purifier is worth it"
           and "probably not". 100 matches the top of the US "Moderate" band.

TO UPDATE: replace the numbers in CITIES and change CAPTURED. Nothing else needs
touching -- the site re-reads the max, re-sorts, and rebuilds the search index.
Run `python3 build/build.py` afterwards.

A number here is a one-morning reading, not a forecast. Indian AQI swings hard
by season: the same city can read 90 in July and 400 in November. The site says
so next to the figure, and that wording should stay.
"""

CAPTURED = "12 November 2026"
SOURCE_NAME = "aqi.in"
SOURCE_URL = "https://www.aqi.in/in/dashboard/india"
AQI_THRESHOLD = 100

# (city, state, aqi)
CITIES = [
 # --- Uttar Pradesh ---
  ("Agra","Uttar Pradesh",279), ("Aligarh","Uttar Pradesh",821),
  ("Allahabad","Uttar Pradesh",269), ("Amethi","Uttar Pradesh",287),
  ("Azamgarh","Uttar Pradesh",267), ("Baghpat","Uttar Pradesh",658),
  ("Bahraich","Uttar Pradesh",275), ("Banda","Uttar Pradesh",193),
  ("Bareilly","Uttar Pradesh",250), ("Bijnor","Uttar Pradesh",169),
  ("Budaun","Uttar Pradesh",478), ("Bulandshahr","Uttar Pradesh",707),
  ("Etawah","Uttar Pradesh",326), ("Faizabad","Uttar Pradesh",370),
  ("Fatehpur","Uttar Pradesh",192), ("Fatehpur Sikri","Uttar Pradesh",273),
  ("Firozabad","Uttar Pradesh",272), ("Gautam Buddha Nagar","Uttar Pradesh",638),
  ("Ghaziabad","Uttar Pradesh",699), ("Ghazipur","Uttar Pradesh",487),
  ("Gorakhpur","Uttar Pradesh",466), ("Greater Noida","Uttar Pradesh",669),
  ("Hapur","Uttar Pradesh",475), ("Hathras","Uttar Pradesh",636),
  ("Jaunpur","Uttar Pradesh",374), ("Jhansi","Uttar Pradesh",249),
  ("Kairana","Uttar Pradesh",360), ("Kanpur","Uttar Pradesh",354),
  ("Khurja","Uttar Pradesh",658), ("Lucknow","Uttar Pradesh",295),
  ("Mathura","Uttar Pradesh",383), ("Meerut","Uttar Pradesh",372),
  ("Mirzapur","Uttar Pradesh",312), ("Modinagar","Uttar Pradesh",551),
  ("Moradabad","Uttar Pradesh",184), ("Muzaffarnagar","Uttar Pradesh",288),
  ("Noida","Uttar Pradesh",626), ("Pilibhit","Uttar Pradesh",180),
  ("Prayagraj","Uttar Pradesh",272), ("Rampur","Uttar Pradesh",181),
  ("Saharanpur","Uttar Pradesh",270), ("Sambhal","Uttar Pradesh",492),
  ("Shahjahanpur","Uttar Pradesh",327), ("Shamli","Uttar Pradesh",280),
  ("Sitapur","Uttar Pradesh",348), ("Sonbhadra","Uttar Pradesh",266),
  ("Varanasi","Uttar Pradesh",288), ("Vrindavan","Uttar Pradesh",498),
 # --- Maharashtra ---
  ("Ahilyanagar","Maharashtra",176), ("Akola","Maharashtra",202),
  ("Ambernath","Maharashtra",210), ("Amravati","Maharashtra",174),
  ("Aurangabad","Maharashtra",174), ("Badlapur","Maharashtra",174),
  ("Bhiwandi","Maharashtra",158), ("Bhusawal","Maharashtra",283),
  ("Chandrapur","Maharashtra",170), ("Dhule","Maharashtra",208), ("Dombivli","Maharashtra",171),
  ("Ichalkaranji","Maharashtra",184), ("Jalgaon","Maharashtra",251),
  ("Kalyan","Maharashtra",174), ("Kharghar","Maharashtra",163), ("Kolhapur","Maharashtra",200),
  ("Latur","Maharashtra",174), ("Malegaon","Maharashtra",174),
  ("Mira Bhayandar","Maharashtra",165), ("Mumbai","Maharashtra",148),
  ("Nagpur","Maharashtra",205), ("Nala Sopara","Maharashtra",153), ("Nanded","Maharashtra",169),
  ("Nashik","Maharashtra",169), ("Navi Mumbai","Maharashtra",161),
  ("Osmanabad","Maharashtra",168), ("Palghar","Maharashtra",144),
  ("Panchgani","Maharashtra",184), ("Panvel","Maharashtra",162), ("Parbhani","Maharashtra",171),
  ("Pimpri Chinchwad","Maharashtra",181), ("Pune","Maharashtra",181),
  ("Raigad","Maharashtra",168), ("Sangli","Maharashtra",158), ("Solapur","Maharashtra",167),
  ("Thane","Maharashtra",141), ("Ulhasnagar","Maharashtra",164),
  ("Vasai Virar","Maharashtra",152), ("Yavatmal","Maharashtra",178),
 # --- West Bengal ---
  ("Asansol","West Bengal",245), ("Baharampur","West Bengal",192),
  ("Balurghat","West Bengal",179), ("Bangaon","West Bengal",181), ("Bankura","West Bengal",205),
  ("Barasat","West Bengal",165), ("Barddhaman","West Bengal",186),
  ("Barrackpore","West Bengal",169), ("Basirhat","West Bengal",166),
  ("Berhampore","West Bengal",191), ("Bhatpara","West Bengal",177),
  ("Chandannagar","West Bengal",168), ("Chinsurah","West Bengal",189),
  ("Darjeeling","West Bengal",139), ("Dum Dum","West Bengal",167),
  ("Durgapur","West Bengal",194), ("English Bazar","West Bengal",194),
  ("Haldia","West Bengal",162), ("Hooghly","West Bengal",176), ("Howrah","West Bengal",167),
  ("Jalpaiguri","West Bengal",143), ("Jhargram","West Bengal",239),
  ("Kalyani","West Bengal",182), ("Kharagpur","West Bengal",200), ("Kolkata","West Bengal",164),
  ("Krishnanagar","West Bengal",182), ("Medinipur","West Bengal",181),
  ("Nabadwip","West Bengal",182), ("Naihati","West Bengal",178), ("Panihati","West Bengal",181),
  ("Raiganj","West Bengal",194), ("Raniganj","West Bengal",266),
  ("Serampore","West Bengal",166), ("Shantipur","West Bengal",189),
  ("Siliguri","West Bengal",140), ("Uluberiya","West Bengal",161),
 # --- Andhra Pradesh ---
  ("Adoni","Andhra Pradesh",151), ("Amaravati","Andhra Pradesh",168),
  ("Anakapalle","Andhra Pradesh",152), ("Anantapur","Andhra Pradesh",142),
  ("Bhimavaram","Andhra Pradesh",109), ("Chirala","Andhra Pradesh",156),
  ("Chittoor","Andhra Pradesh",151), ("Cuddapah","Andhra Pradesh",167),
  ("Dharmavaram","Andhra Pradesh",117), ("Eluru","Andhra Pradesh",158),
  ("Guntur","Andhra Pradesh",169), ("Hindupur","Andhra Pradesh",113),
  ("Kakinada","Andhra Pradesh",118), ("Kurnool","Andhra Pradesh",127),
  ("Machilipatnam","Andhra Pradesh",102), ("Madanapalle","Andhra Pradesh",124),
  ("Nandyal","Andhra Pradesh",157), ("Narasaraopet","Andhra Pradesh",158),
  ("Nellore","Andhra Pradesh",167), ("Ongole","Andhra Pradesh",167),
  ("Proddatur","Andhra Pradesh",158), ("Rajamahendravaram","Andhra Pradesh",152),
  ("Srikakulam","Andhra Pradesh",153), ("Tenali","Andhra Pradesh",178),
  ("Tirupati","Andhra Pradesh",148), ("Vijayawada","Andhra Pradesh",160),
  ("Visakhapatnam","Andhra Pradesh",150), ("Vizianagaram","Andhra Pradesh",149),
 # --- Karnataka ---
  ("Bagalkote","Karnataka",125), ("Ballari","Karnataka",142), ("Belagavi","Karnataka",153),
  ("Bengaluru","Karnataka",106), ("Bidar","Karnataka",167), ("Chikkaballapur","Karnataka",104),
  ("Chikkamagaluru","Karnataka",159), ("Davangere","Karnataka",150),
  ("Gulbarga","Karnataka",169), ("Hassan","Karnataka",128), ("Haveri","Karnataka",136),
  ("Hospet","Karnataka",142), ("Hubballi","Karnataka",136), ("Kalaburagi","Karnataka",169),
  ("Kolar","Karnataka",114), ("Koppal","Karnataka",119), ("Madikeri","Karnataka",179),
  ("Mandya","Karnataka",112), ("Mangaluru","Karnataka",185), ("Mysuru","Karnataka",110),
  ("Raichur","Karnataka",141), ("Ramanagara","Karnataka",113), ("Shivamogga","Karnataka",158),
  ("Tumakuru","Karnataka",125), ("Udupi","Karnataka",172), ("Vijayapura","Karnataka",181),
  ("Yadgiri","Karnataka",158),
 # --- Tamil Nadu ---
  ("Avadi","Tamil Nadu",161), ("Chengalpattu","Tamil Nadu",168), ("Chennai","Tamil Nadu",164),
  ("Coimbatore","Tamil Nadu",181), ("Cuddalore","Tamil Nadu",160),
  ("Dindigul","Tamil Nadu",171), ("Erode","Tamil Nadu",197), ("Hosur","Tamil Nadu",120),
  ("Kancheepuram","Tamil Nadu",166), ("Karur","Tamil Nadu",182),
  ("Kodaikanal","Tamil Nadu",177), ("Madurai","Tamil Nadu",171), ("Nagercoil","Tamil Nadu",128),
  ("Ooty","Tamil Nadu",168), ("Rajapalaiyam","Tamil Nadu",177),
  ("Ramanathapuram","Tamil Nadu",175), ("Rameswaram","Tamil Nadu",159),
  ("Salem","Tamil Nadu",166), ("Thanjavur","Tamil Nadu",164), ("Thoothukudi","Tamil Nadu",134),
  ("Tiruchirappalli","Tamil Nadu",177), ("Tiruppur","Tamil Nadu",177),
  ("Tiruvallur","Tamil Nadu",134), ("Tiruvannamalai","Tamil Nadu",158),
  ("Tuticorin","Tamil Nadu",125), ("Valparai","Tamil Nadu",181), ("Vellore","Tamil Nadu",154),
 # --- Haryana ---
  ("Ambala","Haryana",210), ("Bahadurgarh","Haryana",523), ("Bhiwani","Haryana",537),
  ("Charkhi Dadri","Haryana",548), ("Dharuhera","Haryana",359), ("Faridabad","Haryana",692),
  ("Fatehabad","Haryana",444), ("Gurgaon","Haryana",539), ("Hisar","Haryana",322),
  ("Jagadhri","Haryana",199), ("Jhajjar","Haryana",670), ("Jind","Haryana",615),
  ("Kaithal","Haryana",234), ("Karnal","Haryana",233), ("Kurukshetra","Haryana",209),
  ("Manesar","Haryana",342), ("Mewat","Haryana",225), ("Narnaul","Haryana",352),
  ("Palwal","Haryana",705), ("Panchkula","Haryana",172), ("Panipat","Haryana",389),
  ("Rewari","Haryana",381), ("Rohtak","Haryana",632), ("Sirsa","Haryana",434),
  ("Sonipat","Haryana",678), ("Yamuna Nagar","Haryana",195),
 # --- Bihar ---
  ("Araria","Bihar",223), ("Arrah","Bihar",210), ("Aurangabad","Bihar",206),
  ("Begusarai","Bihar",321), ("Bettiah","Bihar",334), ("Bhagalpur","Bihar",258),
  ("Bihar Sharif","Bihar",212), ("Buxar","Bihar",410), ("Chapra","Bihar",212),
  ("Danapur","Bihar",212), ("Darbhanga","Bihar",272), ("Gaya","Bihar",210),
  ("Hajipur","Bihar",211), ("Katihar","Bihar",215), ("Kishanganj","Bihar",196),
  ("Motihari","Bihar",358), ("Munger","Bihar",316), ("Muzaffarpur","Bihar",344),
  ("Patna","Bihar",212), ("Purnea","Bihar",207), ("Rajgir","Bihar",234),
  ("Saharsa","Bihar",291), ("Samastipur","Bihar",265), ("Sasaram","Bihar",287),
  ("Siwan","Bihar",305),
 # --- Madhya Pradesh ---
  ("Bhopal","Madhya Pradesh",199), ("Burhanpur","Madhya Pradesh",208),
  ("Chhatarpur","Madhya Pradesh",238), ("Chhindwara","Madhya Pradesh",167),
  ("Damoh","Madhya Pradesh",190), ("Dewas","Madhya Pradesh",177), ("Dhar","Madhya Pradesh",189),
  ("Gwalior","Madhya Pradesh",292), ("Indore","Madhya Pradesh",182),
  ("Jabalpur","Madhya Pradesh",173), ("Katni","Madhya Pradesh",189),
  ("Khajuraho","Madhya Pradesh",195), ("Khargone","Madhya Pradesh",175),
  ("Maihar","Madhya Pradesh",231), ("Mandsaur","Madhya Pradesh",187),
  ("Morena","Madhya Pradesh",206), ("Pithampur","Madhya Pradesh",191),
  ("Ratlam","Madhya Pradesh",172), ("Rewa","Madhya Pradesh",270),
  ("Sagar","Madhya Pradesh",213), ("Satna","Madhya Pradesh",250),
  ("Singrauli","Madhya Pradesh",338), ("Ujjain","Madhya Pradesh",168),
  ("Vidisha","Madhya Pradesh",228),
 # --- Gujarat ---
  ("Ahmedabad","Gujarat",162), ("Anand","Gujarat",197), ("Ankleshwar","Gujarat",156),
  ("Bharuch","Gujarat",154), ("Bhavnagar","Gujarat",155), ("Bhuj","Gujarat",134),
  ("Daman","Gujarat",162), ("Dwarka","Gujarat",118), ("Gandhinagar","Gujarat",162),
  ("Godhra","Gujarat",167), ("Himatnagar","Gujarat",203), ("Jamnagar","Gujarat",157),
  ("Khambhat","Gujarat",189), ("Mehsana","Gujarat",155), ("Mundra","Gujarat",117),
  ("Navsari","Gujarat",156), ("Porbandar","Gujarat",148), ("Rajkot","Gujarat",144),
  ("Surat","Gujarat",155), ("Vadodara","Gujarat",172), ("Valsad","Gujarat",164),
  ("Vapi","Gujarat",168),
 # --- Rajasthan ---
  ("Ajmer","Rajasthan",144), ("Alwar","Rajasthan",300), ("Bharatpur","Rajasthan",242),
  ("Bhilwara","Rajasthan",188), ("Bhiwadi","Rajasthan",303), ("Bikaner","Rajasthan",165),
  ("Chittaurgarh","Rajasthan",186), ("Churu","Rajasthan",265), ("Jaipur","Rajasthan",182),
  ("Jaisalmer","Rajasthan",165), ("Jodhpur","Rajasthan",167), ("Kota","Rajasthan",212),
  ("Mount Abu","Rajasthan",167), ("Pali","Rajasthan",167), ("Pushkar","Rajasthan",148),
  ("Sikar","Rajasthan",176), ("Sri Ganganagar","Rajasthan",214), ("Tonk","Rajasthan",178),
  ("Udaipur","Rajasthan",170),
 # --- Punjab ---
  ("Abohar","Punjab",220), ("Amritsar","Punjab",287), ("Barnala","Punjab",892),
  ("Bathinda","Punjab",593), ("Faridkot","Punjab",771), ("Fatehgarh Sahib","Punjab",238),
  ("Gurdaspur","Punjab",252), ("Hoshiarpur","Punjab",249), ("Jalandhar","Punjab",243),
  ("Kharar","Punjab",208), ("Ludhiana","Punjab",379), ("Malaut","Punjab",558),
  ("Mohali","Punjab",192), ("Pathankot","Punjab",200), ("Patiala","Punjab",450),
  ("Rupnagar","Punjab",232), ("Zirakpur","Punjab",175),
 # --- Telangana ---
  ("Adilabad","Telangana",171), ("Hanamkonda","Telangana",160), ("Hyderabad","Telangana",171),
  ("Jagtial","Telangana",175), ("Kamareddy","Telangana",175), ("Karimnagar","Telangana",178),
  ("Khammam","Telangana",165), ("Mahbubnagar","Telangana",182), ("Nalgonda","Telangana",171),
  ("Nizamabad","Telangana",192), ("Sangareddy","Telangana",170),
  ("Secunderabad","Telangana",166), ("Suryapet","Telangana",165), ("Vikarabad","Telangana",169),
  ("Warangal","Telangana",160),
 # --- Delhi ---
  ("New Delhi","Delhi",674),
]

BY_NAME = {c.lower(): (c, s, a) for c, s, a in CITIES}
WORST = max(CITIES, key=lambda r: r[2])
