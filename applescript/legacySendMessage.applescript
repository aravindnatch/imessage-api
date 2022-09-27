on run {targetBuddyPhone, serviceType, targetMessage}
	tell application "Messages"

		if serviceType is "iMessage" then
			set targetService to 1st service whose service type = iMessage
		else
			set targetService to 1st service whose service type = SMS
		end if

		set targetBuddy to buddy targetBuddyPhone of targetService
		send targetMessage to targetBuddy

	end tell
end run