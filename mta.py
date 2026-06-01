# imports
import requests

# info
# https://subwayinfo.nyc/docs#overview

def unfurl_json(json, type_desc, limit=0):
    if type_desc == 'arrivals':
        # print(len(json['arrivals']))

        for i in range(len(json['arrivals'])):
            train_info = json['arrivals'][i]
            train_string = f'A {'South' if train_info['direction'] == "S" else 'North'} bound {train_info['line']} train {train_info['directionLabel']} is {train_info['minutesAway']} minutes away'
            print(train_string)

    if type_desc == 'alerts':
        # print(json)
        for i in range(len(json)):
            alert_info = json[i]
            alert_string = f'Alert: {alert_info['headerText']}.\nInfo: {alert_info['descriptionText']}'
            print(alert_string)

def get_info(u, type_desc, limit=0):
    # print(u)
    url = u
    response = requests.get(url)

    if response.status_code == 200:
        # print(response.json())
        unfurl_json(response.json(), type_desc, limit)

    return    

def main():
    # print('hello world')
    arrivals_limit=5
    direction="S" #this should be user input
    arrivals = f'https://subwayinfo.nyc/api/arrivals?station_id=116&direction={direction}&limit={arrivals_limit}'
    alerts = "https://subwayinfo.nyc/api/alerts?line=1"

    get_info(arrivals, 'arrivals', 5)
    print('\n')
    get_info(alerts, "alerts")

if __name__ == "__main__": 
    main()    