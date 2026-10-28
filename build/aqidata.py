# -*- coding: utf-8 -*-
"""Indian city AQI snapshot.

SOURCE   : aqi.in live city tables (US AQI), captured 28 October 2026, ~05:12 IST
SCALE    : US AQI, because that is what the source publishes. Do not mix CPCB
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

CAPTURED = "28 October 2026"
SOURCE_NAME = "aqi.in"
SOURCE_URL = "https://www.aqi.in/in/dashboard/india"
AQI_THRESHOLD = 100

# (city, state, aqi)
CITIES = [
 # --- Delhi NCR -----------------------------------------------------------
 ("New Delhi","Delhi",154),("Noida","Uttar Pradesh",161),
 ("Greater Noida","Uttar Pradesh",152),("Ghaziabad","Uttar Pradesh",142),
 ("Gurgaon","Haryana",157),("Faridabad","Haryana",157),
 ("Bahadurgarh","Haryana",154),("Sonipat","Haryana",147),
 ("Gautam Buddha Nagar","Uttar Pradesh",152),
 # --- Uttar Pradesh -------------------------------------------------------
 ("Agra","Uttar Pradesh",158),("Aligarh","Uttar Pradesh",153),
 ("Prayagraj","Uttar Pradesh",185),("Allahabad","Uttar Pradesh",168),
 ("Amethi","Uttar Pradesh",154),("Amroha","Uttar Pradesh",121),
 ("Ayodhya","Uttar Pradesh",137),("Azamgarh","Uttar Pradesh",174),
 ("Baghpat","Uttar Pradesh",129),("Bahraich","Uttar Pradesh",131),
 ("Banda","Uttar Pradesh",141),("Bareilly","Uttar Pradesh",154),
 ("Bijnor","Uttar Pradesh",86),("Budaun","Uttar Pradesh",156),
 ("Bulandshahr","Uttar Pradesh",152),("Etawah","Uttar Pradesh",158),
 ("Faizabad","Uttar Pradesh",132),("Fatehpur","Uttar Pradesh",138),
 ("Fatehpur Sikri","Uttar Pradesh",156),("Firozabad","Uttar Pradesh",155),
 ("Ghazipur","Uttar Pradesh",159),("Gorakhpur","Uttar Pradesh",110),
 ("Hapur","Uttar Pradesh",129),("Hathras","Uttar Pradesh",157),
 ("Jaunpur","Uttar Pradesh",167),("Jhansi","Uttar Pradesh",158),
 ("Kairana","Uttar Pradesh",125),("Kanpur","Uttar Pradesh",126),
 ("Khurja","Uttar Pradesh",150),("Lucknow","Uttar Pradesh",132),
 ("Mathura","Uttar Pradesh",154),("Meerut","Uttar Pradesh",121),
 ("Mirzapur","Uttar Pradesh",170),("Modinagar","Uttar Pradesh",151),
 ("Moradabad","Uttar Pradesh",143),("Muzaffarnagar","Uttar Pradesh",124),
 ("Pilibhit","Uttar Pradesh",92),("Rampur","Uttar Pradesh",150),
 ("Saharanpur","Uttar Pradesh",117),("Sambhal","Uttar Pradesh",130),
 ("Shahjahanpur","Uttar Pradesh",128),("Shamli","Uttar Pradesh",99),
 ("Sitapur","Uttar Pradesh",121),("Sonbhadra","Uttar Pradesh",114),
 ("Varanasi","Uttar Pradesh",166),("Vrindavan","Uttar Pradesh",158),
 # --- Haryana -------------------------------------------------------------
 ("Ambala","Haryana",134),("Bhiwani","Haryana",136),
 ("Charkhi Dadri","Haryana",133),("Dharuhera","Haryana",153),
 ("Fatehabad","Haryana",114),("Hisar","Haryana",128),
 ("Jhajjar","Haryana",140),("Jind","Haryana",128),("Kaithal","Haryana",124),
 ("Karnal","Haryana",118),("Kurukshetra","Haryana",126),
 ("Manesar","Haryana",137),("Mewat","Haryana",151),("Narnaul","Haryana",152),
 ("Palwal","Haryana",152),("Panchkula","Haryana",139),("Panipat","Haryana",150),
 ("Rewari","Haryana",150),("Rohtak","Haryana",145),("Sirsa","Haryana",125),
 ("Yamuna Nagar","Haryana",109),("Jagadhri","Haryana",98),
 # --- Punjab --------------------------------------------------------------
 ("Amritsar","Punjab",123),("Abohar","Punjab",175),("Barnala","Punjab",119),
 ("Bathinda","Punjab",145),("Faridkot","Punjab",153),
 ("Fatehgarh Sahib","Punjab",111),("Gurdaspur","Punjab",118),
 ("Hoshiarpur","Punjab",103),("Jalandhar","Punjab",126),("Kharar","Punjab",132),
 ("Ludhiana","Punjab",124),("Malaut","Punjab",146),("Mohali","Punjab",104),
 ("Pathankot","Punjab",85),("Patiala","Punjab",119),("Rupnagar","Punjab",112),
 ("Zirakpur","Punjab",137),
 # --- Bihar ---------------------------------------------------------------
 ("Patna","Bihar",156),("Araria","Bihar",115),("Arrah","Bihar",155),
 ("Aurangabad","Bihar",142),("Begusarai","Bihar",190),("Bettiah","Bihar",158),
 ("Bhagalpur","Bihar",165),("Bhojpur","Bihar",195),("Bihar Sharif","Bihar",160),
 ("Buxar","Bihar",159),("Chapra","Bihar",140),("Danapur","Bihar",132),
 ("Darbhanga","Bihar",145),("Gaya","Bihar",160),("Hajipur","Bihar",158),
 ("Katihar","Bihar",158),("Kishanganj","Bihar",102),("Motihari","Bihar",150),
 ("Munger","Bihar",177),("Muzaffarpur","Bihar",134),("Purnea","Bihar",121),
 ("Rajgir","Bihar",168),("Saharsa","Bihar",155),("Samastipur","Bihar",161),
 ("Sasaram","Bihar",174),("Siwan","Bihar",154),
 # --- Rajasthan -----------------------------------------------------------
 ("Jaipur","Rajasthan",111),("Ajmer","Rajasthan",111),("Alwar","Rajasthan",152),
 ("Baran","Rajasthan",151),("Bharatpur","Rajasthan",144),
 ("Bhilwara","Rajasthan",109),("Bhiwadi","Rajasthan",147),
 ("Bikaner","Rajasthan",100),("Chittaurgarh","Rajasthan",112),
 ("Churu","Rajasthan",133),("Dausa","Rajasthan",105),
 ("Sri Ganganagar","Rajasthan",182),("Jaisalmer","Rajasthan",101),
 ("Jodhpur","Rajasthan",100),("Kota","Rajasthan",144),("Pali","Rajasthan",98),
 ("Pushkar","Rajasthan",104),("Sikar","Rajasthan",114),("Tonk","Rajasthan",106),
 ("Udaipur","Rajasthan",117),("Mount Abu","Rajasthan",119),
 # --- Madhya Pradesh ------------------------------------------------------
 ("Bhopal","Madhya Pradesh",144),("Indore","Madhya Pradesh",138),
 ("Gwalior","Madhya Pradesh",161),("Jabalpur","Madhya Pradesh",115),
 ("Ujjain","Madhya Pradesh",142),("Burhanpur","Madhya Pradesh",162),
 ("Chhatarpur","Madhya Pradesh",152),("Chhindwara","Madhya Pradesh",187),
 ("Damoh","Madhya Pradesh",139),("Dewas","Madhya Pradesh",144),
 ("Dhar","Madhya Pradesh",137),("Guna","Madhya Pradesh",159),
 ("Katni","Madhya Pradesh",132),("Khajuraho","Madhya Pradesh",152),
 ("Khargone","Madhya Pradesh",147),("Maihar","Madhya Pradesh",152),
 ("Mandsaur","Madhya Pradesh",117),("Morena","Madhya Pradesh",163),
 ("Neemuch","Madhya Pradesh",121),("Pithampur","Madhya Pradesh",151),
 ("Ratlam","Madhya Pradesh",116),("Rewa","Madhya Pradesh",150),
 ("Sagar","Madhya Pradesh",140),("Satna","Madhya Pradesh",152),
 ("Singrauli","Madhya Pradesh",153),("Vidisha","Madhya Pradesh",147),
 # --- Maharashtra ---------------------------------------------------------
 ("Mumbai","Maharashtra",139),("Pune","Maharashtra",87),
 ("Nagpur","Maharashtra",110),("Nashik","Maharashtra",125),
 ("Thane","Maharashtra",142),("Navi Mumbai","Maharashtra",131),
 ("Akola","Maharashtra",136),("Ambernath","Maharashtra",137),
 ("Amravati","Maharashtra",79),("Aurangabad","Maharashtra",150),
 ("Badlapur","Maharashtra",132),("Bhiwandi","Maharashtra",144),
 ("Bhusawal","Maharashtra",141),("Chandrapur","Maharashtra",88),
 ("Dhule","Maharashtra",138),("Dombivli","Maharashtra",144),
 ("Ichalkaranji","Maharashtra",104),("Jalgaon","Maharashtra",154),
 ("Kalyan","Maharashtra",147),("Kharghar","Maharashtra",129),
 ("Kolhapur","Maharashtra",100),("Latur","Maharashtra",111),
 ("Malegaon","Maharashtra",128),("Mira Bhayandar","Maharashtra",132),
 ("Nala Sopara","Maharashtra",132),("Nanded","Maharashtra",113),
 ("Osmanabad","Maharashtra",95),("Palghar","Maharashtra",128),
 ("Panvel","Maharashtra",124),("Parbhani","Maharashtra",109),
 ("Pimpri Chinchwad","Maharashtra",97),("Raigad","Maharashtra",146),
 ("Sangli","Maharashtra",84),("Satara","Maharashtra",85),
 ("Solapur","Maharashtra",89),("Ulhasnagar","Maharashtra",142),
 ("Vasai Virar","Maharashtra",130),("Yavatmal","Maharashtra",98),
 ("Ahilyanagar","Maharashtra",77),("Panchgani","Maharashtra",90),
 # --- West Bengal ---------------------------------------------------------
 ("Kolkata","West Bengal",115),("Howrah","West Bengal",123),
 ("Asansol","West Bengal",129),("Durgapur","West Bengal",133),
 ("Siliguri","West Bengal",71),("Darjeeling","West Bengal",70),
 ("Baharampur","West Bengal",139),("Balurghat","West Bengal",118),
 ("Bangaon","West Bengal",141),("Bankura","West Bengal",131),
 ("Barasat","West Bengal",108),("Barddhaman","West Bengal",136),
 ("Barrackpore","West Bengal",126),("Basirhat","West Bengal",106),
 ("Berhampore","West Bengal",143),("Bhatpara","West Bengal",133),
 ("Chandannagar","West Bengal",128),("Chinsurah","West Bengal",145),
 ("Dum Dum","West Bengal",108),("English Bazar","West Bengal",125),
 ("Haldia","West Bengal",94),("Hooghly","West Bengal",134),
 ("Jalpaiguri","West Bengal",71),("Jhargram","West Bengal",181),
 ("Kalyani","West Bengal",134),("Kharagpur","West Bengal",148),
 ("Krishnanagar","West Bengal",128),("Medinipur","West Bengal",106),
 ("Nabadwip","West Bengal",133),("Naihati","West Bengal",135),
 ("Panihati","West Bengal",122),("Raiganj","West Bengal",114),
 ("Raniganj","West Bengal",135),("Serampore","West Bengal",112),
 ("Shantipur","West Bengal",133),("Uluberiya","West Bengal",104),
 # --- Gujarat -------------------------------------------------------------
 ("Ahmedabad","Gujarat",114),("Surat","Gujarat",89),("Vadodara","Gujarat",94),
 ("Rajkot","Gujarat",114),("Gandhinagar","Gujarat",110),("Anand","Gujarat",121),
 ("Ankleshwar","Gujarat",92),("Bharuch","Gujarat",96),
 ("Bhavnagar","Gujarat",85),("Bhuj","Gujarat",117),("Dahod","Gujarat",88),
 ("Dwarka","Gujarat",115),("Gandhidham","Gujarat",124),("Godhra","Gujarat",93),
 ("Himatnagar","Gujarat",122),("Jamnagar","Gujarat",122),
 ("Khambhat","Gujarat",112),("Mehsana","Gujarat",121),("Mundra","Gujarat",116),
 ("Navsari","Gujarat",99),("Porbandar","Gujarat",111),("Valsad","Gujarat",117),
 ("Vapi","Gujarat",103),("Daman","Gujarat",103),
 # --- Karnataka -----------------------------------------------------------
 ("Bengaluru","Karnataka",138),("Mysuru","Karnataka",89),
 ("Mangaluru","Karnataka",140),("Hubballi","Karnataka",84),
 ("Belagavi","Karnataka",88),("Ballari","Karnataka",98),
 ("Bidar","Karnataka",103),("Davangere","Karnataka",97),
 ("Gulbarga","Karnataka",96),("Hassan","Karnataka",100),
 ("Haveri","Karnataka",93),("Hospet","Karnataka",97),
 ("Kalaburagi","Karnataka",96),("Kolar","Karnataka",96),
 ("Koppal","Karnataka",90),("Madikeri","Karnataka",122),
 ("Mandya","Karnataka",95),("Manipal","Karnataka",142),
 ("Raichur","Karnataka",100),("Ramanagara","Karnataka",97),
 ("Shivamogga","Karnataka",103),("Tumakuru","Karnataka",96),
 ("Udupi","Karnataka",145),("Vijayapura","Karnataka",90),
 ("Yadgiri","Karnataka",100),("Chikkamagaluru","Karnataka",99),
 ("Chikkaballapur","Karnataka",93),("Bagalkote","Karnataka",83),
 # --- Tamil Nadu ----------------------------------------------------------
 ("Chennai","Tamil Nadu",110),("Coimbatore","Tamil Nadu",137),
 ("Madurai","Tamil Nadu",129),("Tiruchirappalli","Tamil Nadu",123),
 ("Salem","Tamil Nadu",119),("Tiruppur","Tamil Nadu",128),
 ("Erode","Tamil Nadu",129),("Vellore","Tamil Nadu",85),
 ("Thoothukudi","Tamil Nadu",144),("Thanjavur","Tamil Nadu",111),
 ("Dindigul","Tamil Nadu",122),("Cuddalore","Tamil Nadu",125),
 ("Karur","Tamil Nadu",126),("Hosur","Tamil Nadu",116),
 ("Kancheepuram","Tamil Nadu",102),("Chengalpattu","Tamil Nadu",103),
 ("Avadi","Tamil Nadu",112),("Nagercoil","Tamil Nadu",142),
 ("Rajapalaiyam","Tamil Nadu",140),("Ramanathapuram","Tamil Nadu",134),
 ("Rameswaram","Tamil Nadu",118),("Ooty","Tamil Nadu",124),
 ("Kodaikanal","Tamil Nadu",139),("Valparai","Tamil Nadu",134),
 ("Tiruvallur","Tamil Nadu",83),("Tiruvannamalai","Tamil Nadu",109),
 ("Tuticorin","Tamil Nadu",139),
 # --- Telangana -----------------------------------------------------------
 ("Hyderabad","Telangana",111),("Secunderabad","Telangana",117),
 ("Warangal","Telangana",105),("Nizamabad","Telangana",112),
 ("Karimnagar","Telangana",109),("Khammam","Telangana",106),
 ("Ramagundam","Telangana",95),("Mahbubnagar","Telangana",114),
 ("Nalgonda","Telangana",124),("Adilabad","Telangana",99),
 ("Suryapet","Telangana",114),("Sangareddy","Telangana",109),
 ("Jagtial","Telangana",107),("Kamareddy","Telangana",107),
 ("Vikarabad","Telangana",101),("Hanamkonda","Telangana",105),
 # --- Andhra Pradesh ------------------------------------------------------
 ("Visakhapatnam","Andhra Pradesh",53),("Vijayawada","Andhra Pradesh",98),
 ("Guntur","Andhra Pradesh",91),("Nellore","Andhra Pradesh",110),
 ("Kurnool","Andhra Pradesh",102),("Tirupati","Andhra Pradesh",86),
 ("Rajamahendravaram","Andhra Pradesh",88),("Kakinada","Andhra Pradesh",45),
 ("Anantapur","Andhra Pradesh",101),("Eluru","Andhra Pradesh",98),
 ("Ongole","Andhra Pradesh",111),("Chittoor","Andhra Pradesh",88),
 ("Cuddapah","Andhra Pradesh",111),("Machilipatnam","Andhra Pradesh",99),
 ("Bhimavaram","Andhra Pradesh",92),("Srikakulam","Andhra Pradesh",57),
 ("Vizianagaram","Andhra Pradesh",54),("Amaravati","Andhra Pradesh",104),
 ("Adoni","Andhra Pradesh",94),("Hindupur","Andhra Pradesh",95),
 ("Madanapalle","Andhra Pradesh",92),("Proddatur","Andhra Pradesh",106),
 ("Nandyal","Andhra Pradesh",100),("Dharmavaram","Andhra Pradesh",102),
 ("Tenali","Andhra Pradesh",104),("Chirala","Andhra Pradesh",100),
 ("Anakapalle","Andhra Pradesh",48),("Narasaraopet","Andhra Pradesh",104),
 # --- other ---------------------------------------------------------------
 ("Srinagar","Jammu and Kashmir",154),("Rudrapur","Uttarakhand",159),
 ("Chandigarh","Chandigarh",121),
]

BY_NAME = {c.lower(): (c, s, a) for c, s, a in CITIES}
WORST = max(CITIES, key=lambda r: r[2])
