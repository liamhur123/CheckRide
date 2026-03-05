import check_ride as cr
from appJar import gui
app = gui("Check Ride")
app.setSticky("news")


def press(button):
    if button == "Shortfield take off distance":
        app.setBg("Grey")
        removeall()
        ct = app.integerBox("current temperature","Enter current temperature")
        pa = app.integerBox("pressure altitude","Enter pressure altitude")
        ground_data,obs_data,ground_header,obs_header = cr.shortfield_takeoff_dist(ct,pa)
        app.addLabel("ground title", "Ground", 0, 0,3)
        headers(ground_header,obs_header)
        app.addHorizontalSeparator(2, 0, 7, colour="white")
        app.addLabel("l1", ground_data[0][0], 7, 0)
        app.addLabel("l2", ground_data[0][1], 7, 1)
        app.addLabel("l3", ground_data[0][2], 7, 2)
        app.addLabel("l4", ground_data[1][0], 9, 0)
        app.addFlashLabel("l5", ground_data[1][1], 9, 1)
        app.addLabel("l6", ground_data[1][2], 9, 2)
        app.addLabel("l7", ground_data[2][0], 11, 0)
        app.addLabel("l8", ground_data[2][1], 11, 1)
        app.addLabel("l9", ground_data[2][2], 11, 2)
        app.addVerticalSeparator(0, 3, 0,12, colour="white")
        app.addLabel("obs title", "OBS", 0, 4,3,)

        app.addLabel("t1", obs_data[0][0],  7, 4)
        app.addLabel("t2", obs_data[0][1],  7, 5)
        app.addLabel("t3", obs_data[0][2],  7, 6)
        app.addLabel("t4", obs_data[1][0],  9, 4)
        app.addFlashLabel("t5", obs_data[1][1],  9, 5)
        app.addLabel("t6", obs_data[1][2],  9, 6)
        app.addLabel("t7", obs_data[2][0], 11, 4)
        app.addLabel("t9", obs_data[2][2], 11, 5)
        app.addLabel("t8", obs_data[2][1], 11, 6)
        app.setLabelBg("l5", "red")
        app.setLabelBg("t5", "red")
        app.addButton("Main Menu", press)
    elif button == "Pressure Altitude":
        app.setBg("Grey")
        removeall()
        cp = app.floatBox("current pressure altitude","Enter current pressure altitude")
        el = app.floatBox("pressure altitude","Enter pressure altitude")
        pressure_diff, pressure_solve = cr.pressure_alt(cp,el)
        app.addLabel("diff_clac", "29.92 - " + str(cp), 0, 0)
        app.addLabel("difference", pressure_diff, 1, 0)
        app.addLabel("multi", str(pressure_diff) + " x 1000", 2)
        app.addLabel("something", pressure_diff * 1000,3  )
        app.addLabel("add alt and press", str(pressure_diff * 1000) +" + "+ str(el), 4)
        app.addFlashLabel("final", pressure_solve, 5)
        app.setLabelBg("final", "green")
        app.addButton("Main Menu",press)
    elif button == "Main Menu":
        start()



def headers(ground_header,obs_header):
    app.addLabel("gh1", ground_header[0], 1, 0)
    app.addLabel("gh2", ground_header[1], 1, 1)
    app.addLabel("gh3", ground_header[2], 1, 2)
    app.addLabel("oh1", obs_header[0], 1, 4)
    app.addLabel("oh2", obs_header[1], 1, 5)
    app.addLabel("oh3", obs_header[2], 1, 6)



def removeall():
    app.removeAllWidgets()



app.setBg("maroon")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
def start():
    app.removeAllWidgets()
    app.setBg("maroon")
    app.setFont(18)
    app.addLabel("title", "Check Ride Calculator")
    app.setLabelBg("title", "maroon")
    app.setLabelFg("title", "white")

    app.addButton("Pressure Altitude",press)
    app.addButton("Shortfield take off distance",press)

start()
app.go()