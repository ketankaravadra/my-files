#Test: driver added after all the info & settings is deleted.
# Menu -> Tasks -> Master Data -> Driver options -> Select '+' -> type Fname and Lname -> save


#object definations(store in separate object_names.py):
menuButton = { "name": "menuButton", "id": 51001, "type": "QMLMenuButton", "visible": 1}
tasks = { "name": "tasks", "id": 51011, "text":"Tasks", "type": "icon", "visible": 1}
master_Data = { "name": "masterData", "id": 51012, "text":"Master Data", "type": "text", "visible": 1}
driverSeatIcon = { "name": "driverSeatIcon", "id": 51013, "type": "icon", "visible": 1}
plusIcon = { "name": "plusIcon", "id": 51014, "type": "icon", "visible": 1}
firstNameInputField = { "name": "firstNameInputField", "id": 51003, "type": "inputField", "visible": 1}
lastNameInputField = { "name": "lastNameInputField", "id": 51002, "type": "inputField", "visible": 1}
saveIcon = { "name": "saveIcon", "id": 51015, "type": "icon", "visible": 1}





def add_verify_driver(driverFirstName, driverLastName):
    # add driver 
    clickButton(waitForObject(menuButton)) #click menu button to open menu
    clickButton(waitForObject(tasks)) # click Tasks tab
    clickButton(waitForObject(master_Data)) # click Master Data sub-tab
    clickButton(waitForObject(driverSeatIcon)) # click Driver Seat Icon
    clickButton(waitForObject(plusIcon)) # click + icon to add new driver
    type(waitForObject(firstNameInputField), driverFirstName) # enter first name in resp field
    type(waitForObject(lastNameInputField), driverLastName) # enter last name in resp field
    clickButton(waitForObject(saveIcon)) # click save icon

    # verify added driver
    # condition: driver page is loaded once we enter driver details & click save icon.
    waitForObject(driverSeatIcon, 30)


    #examples where real name can be considered instead of symbolic name.
    test.compare(waitForObject({ "name": "fNameElement", "id": 52001, "text":driverFirstName, "row":0, "column":0, "type": "text", "visible": 1}, 30).text, driverFirstName)
    test.compare(waitForObject({ "name": "lNameElement", "id": 52002, "text":driverLastName, "row":0, "column":1, "type": "text", "visible": 1}, 30).text, driverLastName)



def main():
    startApplication("LaunchCEMIS")
    add_verify_driver("Ketan","Karavadra")

    