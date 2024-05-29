from plyer import notification
# from PIL import Image
# Function to display notification
import time
# filename = 'camera.jpg'
# img = Image.open(filename,'r')
import psutil
def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery is None:
        return 0
    else:
        return battery.percent


def laptop_notification(title, message):
    notification.notify(
        title=title,
        message=message,
    #    app_name = 'Name',
        #app_icon=img,  # If you have an icon, specify the path here
        timeout=10  # How long the notification should stay on the screen (in seconds)
    )

# Example usage
# title = "Notification Title"
# message = "This is the notification message."
# laptop_notification(title, message)

while(True):
    if get_battery_percentage() < 40:
        laptop_notification("Plug charger", "Battery is less than 40%")
        time.sleep(60)
    elif get_battery_percentage() > 60:
        laptop_notification("Remove Charger", "Battery is greater than 60%")
        time.sleep(60)

