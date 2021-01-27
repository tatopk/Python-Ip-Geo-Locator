from tkinter import *
import pygeoip
import webbrowser

gip = pygeoip.GeoIP("GeoLiteCity.dat")

root = Tk()
root.geometry("500x600")
root.title("Ip Locatior")


def onClick():

    res = gip.record_by_addr(ip_address_e.get())

    dma_code_e.delete(0, "end")
    area_code_e.delete(0, "end")
    metro_code_e.delete(0, "end")
    postal_code_e.delete(0, "end")
    country_code_e.delete(0, "end")
    country_e.delete(0, "end")
    continent_e.delete(0, "end")
    region_code_e.delete(0, "end")
    city_e.delete(0, "end")
    latitude_e.delete(0, "end")
    longitude_e.delete(0, "end")
    time_zone_e.delete(0, "end")

    if res["dma_code"] == 0:
        dma_code_e.insert(0, "None")
    else:
        dma_code_e.insert(0, res["dma_code"])
    if res["area_code"] == 0:
        area_code_e.insert(0, "None")
    else:
        area_code_e.insert(0, res["area_code"])
    if res["metro_code"] is None:
        metro_code_e.insert(0, "None")
    else:
        metro_code_e.insert(0, res["metro_code"])

    if res["metro_code"] is None:
        postal_code_e.insert(0, "None")
    else:
        postal_code_e.insert(0, res["postal_code"])
    country_code_e.insert(0, res["country_code"])
    country_e.insert(0, res["country_name"])
    continent_e.insert(0, res["continent"])
    region_code_e.insert(0, res["region_code"])
    city_e.insert(0, res["city"])
    latitude_e.insert(0, res["latitude"])
    longitude_e.insert(0, res["longitude"])
    time_zone_e.insert(0, res["time_zone"])


def openmaps():

    res = gip.record_by_addr(ip_address_e.get())

    webbrowser.open('https://www.google.com/maps/?q=' + str(res["latitude"]) + "," + str(res["longitude"]))

#Buttons

bt = Button(root, text="Locate", height="1", width="10", command=onClick)
bt.place(relx=0.525, rely=0.17)

btgoogle = Button(root, text="Google Maps", height="1", width="15", command=openmaps)
btgoogle.place(relx=0.485, rely=0.9)

#Labels

ip_address = Label(root, text="Enter ip Address", width="20", height="5", font=("Calibri", 13))

dma_code = Label(root, text="Dma Code: ", width="20", height="1", font=("Calibri", 13))
area_code = Label(root, text="Area Code: ", width="20", height="1", font=("Calibri", 13))
metro_code = Label(root, text="Metro Code: ", width="20", height="1", font=("Calibri", 13))
postal_code = Label(root, text="Postal Code: ", width="20", height="1", font=("Calibri", 13))
country_code = Label(root, text="Country Code: ", width="20", height="1", font=("Calibri", 13))
country = Label(root, text="Country: ", width="20", height="1", font=("Calibri", 13))
continent = Label(root, text="Continent: ", width="20", height="1", font=("Calibri", 13))
region_code = Label(root, text="Region Code: ", width="20", height="1", font=("Calibri", 13))
city = Label(root, text="City: ", width="20", height="1", font=("Calibri", 13))
latitude = Label(root, text="Latitude: ", width="20", height="1", font=("Calibri", 13))
longitude = Label(root, text="Longitude: ", width="20", height="1", font=("Calibri", 13))
time_zone = Label(root, text="Time Zone: ", width="20", height="1", font=("Calibri", 13))

#Entries

ip_address_e = Entry(root)

dma_code_e = Entry(root)
area_code_e = Entry(root)
metro_code_e = Entry(root)
postal_code_e = Entry(root)
country_code_e = Entry(root)
country_e = Entry(root)
continent_e = Entry(root)
region_code_e = Entry(root)
city_e = Entry(root)
latitude_e = Entry(root)
longitude_e = Entry(root)
time_zone_e = Entry(root)

#Griding Labels

ip_address.grid(row=0)

dma_code.grid(row=2, sticky=E)
area_code.grid(row=3, sticky=E)
metro_code.grid(row=4, sticky=E)
postal_code.grid(row=5, sticky=E)
country_code.grid(row=6, sticky=E)
country.grid(row=7, sticky=E)
continent.grid(row=8, sticky=E)
region_code.grid(row=9, sticky=E)
city.grid(row=10, sticky=E)
latitude.grid(row=11, sticky=E)
longitude.grid(row=12, sticky=E)
time_zone.grid(row=13, sticky=E)

#Griding Entries

ip_address_e.grid(row=0, column=1)

dma_code_e.grid(row=2, column=1)
area_code_e.grid(row=3, column=1)
metro_code_e.grid(row=4, column=1)
postal_code_e.grid(row=5, column=1)
country_code_e.grid(row=6, column=1)
country_e.grid(row=7, column=1)
continent_e.grid(row=8, column=1)
region_code_e.grid(row=9, column=1)
city_e.grid(row=10, column=1)
latitude_e.grid(row=11, column=1)
longitude_e.grid(row=12, column=1)
time_zone_e.grid(row=13, column=1)


root.mainloop()
