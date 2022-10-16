# Driving dataset pre-processing:
For the purpose of building driver behaviour identification models considering the uniqueness of the driver's behavior, we aimed to use driving datasets that mainly rely on capturing car sensor's data through time.
The two open source datasets, HCIlab and security dataset, needs to be pre-processed as we presented in hcilab.py and security.py files.
The data processing includes normalization, sliding windows, noise filtering, and features selection.
## HCIlab dataset overview: 
    - Data collected of 10 drivers (7 men, 3 women).  
    - The route was about 23 km.
    - The trip period is about 30 minutes.
    - The data contains information about GPS, brightness, acceleration, physiological data.
    - The trip route contains fivedifferent road types: 30 km/h zone, 50 km/h zone, highway, freeway, and tunnel.
    
## Security dataset overview:
    - The driving data records of 10 different drivers on the same paths.
    - Every driver has 4 trips on 3 different roads, city way, motorway and parking lot. 
    - The data is a collection of 51 features extracted with a frequency of 1Hz. 
    - All drivers have driven the same recent model of KIA Motors Corporation in South Korea for data collection. 
    - The total length of trips on the 4 paths is 23Km.

