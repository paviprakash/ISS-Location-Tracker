
import json
import urllib.request
import turtle
import time


class ClassA():

    def run(self,t):
        try:
            if str(t) == "":
                t = "Space Center, Houston"
            
            screenISS = turtle.Screen()
            screenISS.setup(720, 360)
            screenISS.setworldcoordinates(-180, -90, 180, 90)
            
            screenISS.register_shape('images/iss.gif')

            
            screenISS.bgpic('images/map.gif')
            iss = turtle.Turtle()
            iss.shape('images/iss.gif')
            iss.setheading(90)
            iss.penup()

            lat = 88
            lon = -100

            locationTurtle = turtle.Turtle()
            locationTurtle.penup()
            locationTurtle.color('yellow')
            locationTurtle.goto(lon, lat)
            locationTurtle.dot(10)
            locationTurtle.hideturtle()
            tracking = 'International Space Center is been Tracked from: ' + str(t)
            locationTurtle.write(tracking)


            while True:
                
                url = 'http://api.open-notify.org/astros.json'
                responseAPI = urllib.request.urlopen(url)
                
                resultAPI = json.loads(responseAPI.read())

                lat =  15
                lon = -175

                location = turtle.Turtle()
                location.penup()
                location.color('yellow')
                location.goto(lon,lat)
                location.dot(10)
                location.hideturtle()
                
                print('People in Space: ', resultAPI['number'])
                noOfPeople = 'People in Space: ' + str(resultAPI['number'])
                location.write(noOfPeople)

                namesCraft = ""
                people = resultAPI['people']
                for p in people:
                  name = str(p['name'])
                  craft = str(p['craft'])
                  namesCraft +='\n' + name + ' in ' + craft
                  print(p['name'], ' in ', p['craft'])

                lat = -35
                lon = -175
               
                location = turtle.Turtle()
                location.penup()
                location.color('red')
                location.goto(lon, lat)
                location.dot(10)
                location.hideturtle()
                location.write(namesCraft)

                
                url = 'http://api.open-notify.org/iss-now.json'
                response = urllib.request.urlopen(url)
                
                resultAPI = json.loads(response.read())

                location = resultAPI['iss_position']
                lat = location['latitude']
                lon = location['longitude']
                print('Latitude: ', lat)
                print('Longitude: ', lon)

                iss.goto(float(lon), float(lat))
                
                if str(t) == "Space Center, Houston":
                    
                    lat = 29.5502
                    lon = -95.097
                elif str(t) == "london":
                    
                    lat = 51.5072
                    lon = 0.1275
                elif str(t) == "Tokyo":
                    
                    lat = 35.689487
                    lon = 139.691706
                elif str(t) == "India":
                    
                    lat = 20.5937
                    lon = 78.9629
                elif str(t) == "Russia":
                    
                    lat = 61.5240
                    lon = 105.3188
                elif str(t) == "England":
                   
                    lat = 52.3555
                    lon = 1.1743
                elif str(t) == "Germany":
                    
                    lat = 51.1657
                    lon = 10.4515
                elif str(t) == "China":
                    
                    lat = 39.9042
                    lon = 116.4074

                
                location = turtle.Turtle()
                location.penup()
                location.color('white')
                location.goto(lon,lat)
                location.dot(10)
                location.hideturtle()

                url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
                response = urllib.request.urlopen(url)
                resultAPI = json.loads(response.read())
                print("###############33",resultAPI)
                
                over = resultAPI['response'][1]['risetime']
                location.write(time.ctime(over))
        except Exception as e:
            print("Program Exited")
            exit(1)

