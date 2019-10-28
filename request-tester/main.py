import requests
# desk_light_on, desk_light_off, bedside_light_on, bedside_light_off

while True:
    x = input("Maker event:")
    paranum = int(input("Number of parameters:"))
    params = ["none", "none", "none"]
    if paranum > 0:
        for i in range(paranum):
            params[i] = input("Parameter - " + str(i + 1) + ":")
    if input("Run (Y/N):").lower() == "y":
        r = requests.post('https://maker.ifttt.com/trigger/' + x + '/with/key/fQc9wPk6IwnJm0zSwpwYxo5MXreMprz8NfcmXIjwPWR', params= {"value1":params[0], "value2":params[1], "value3":params[2]})
    print("\n \n")