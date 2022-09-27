on run(addressList, serviceType, message, isFile)
	tell application "Messages"
		set fileCheck to (isFile as boolean)

		if fileCheck then
			set message to (message as POSIX file) 
		end if
		
		if serviceType is "iMessage" then
			set targetService to 1st service whose service type = iMessage
		else
			set targetService to service serviceType
		end if

  		set AppleScript's text item delimiters to ","
   		set theList to every text item of addressList
    		set AppleScript's text item delimiters to ""
		
		set participantList to {}
		repeat with address in theList
			set end of participantList to a reference to buddy address of targetService
		end repeat
		
		set createdChat to make new text chat with properties {participants: participantList}
		
		send message to createdChat
	end tell
end run