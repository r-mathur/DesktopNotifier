from pynotifier import Notification


def notification_popup(main_title,quote):

	Notification(
	title=main_title,
	description=quote,
	icon_path=None, # On Windows .ico is required, on Linux - .png
	duration=10,                              # Duration in seconds
	urgency=Notification.URGENCY_CRITICAL
	).send()