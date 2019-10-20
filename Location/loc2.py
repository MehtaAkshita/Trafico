import requests
def display_ip():
    """  Function To Print GeoIP Latitude & Longitude """
    my_ip='14.139.243.170'
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})
    my_ip1='157.47.178.92'
    geo_request1 = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip1 + '.json')
    geo_data1 = geo_request1.json()
    print({'latitude': geo_data1['latitude'], 'longitude': geo_data1['longitude']})
    

if __name__ == '__main__':
    display_ip()
