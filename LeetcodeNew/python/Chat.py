'''
Scope / Clarifications:

Registration with Parent & Child
Add / Remove Parent / Child account within family
Login & Logout
Cross Country & Cross States
Unlimited history viewing but scroll up and lazy load the old messages
Unread messages
Push notification when new messages arrived
Support sending multi-media including images, video and sound clip
Assumptions:

Average length of text message is 100 characters, i.e. 1.6 KB if using UTF-16
Since sending raw images consume too much bandwidth, the mobile app will resize the images to < 2000 px in any dimension
Average size of images after resize is 200 KB
Average size of video is 3 MB
Average size of sound clip is 1 MB
Ratio of text : images : sound : video is 10 : 3 : 3 : 1
Components:

Authentication API, for login, logout & registration
Account Management API, for add / remove accounts from family
Message Exchange for real time messaging of all online devices
Storage for multi-media contents
Storage for message histories
Storage for unread messages
Design:

Multiple Authentication Servers per Country / State, load balancers are in front of each Country / State Authentication Server
When First Time Login / Register, the mobile app will contact the default Authentication Server. No matter Login / Register success or not, the response will contain the correct Authentication Server's URL for the device next Login / Register, based on geolocation of the devices' IP address.
There is a mapping table inside each Authentication Server to map IP range to corresponding location's Authentication Server. The mapping table will be updated periodically.
The device will remember the Authentication Server URL, so that it will contact to the nearest Authentication Server directly on next login.
After login success with Authentication Server, a token generated by shared secret key will be generated and the device will use this key in all the following API call / data retrieval.
Separate servers used for Account Management, Message Exchange, multi-media storage, message histories storage and unread message storage
Same token is used for calling all of the above servers. The verification is simple and scalable, since they use shared secret key, signature based authentication.
There are multiple servers for Account Management, Message Exchange, multi-media storage, message histories storage and unread message storage, the corresponding server URL are assigned to a device once login. The assignment is based on consistent hash.
The message exchange servers will state connected with online device through HTTP connection. In order to push message to the devices in real time.
For the message exchange servers, there is an internal gateway within the same region in order to interchange the messages to devices belongs to different exchange servers.
And there is an external gateway per region for cross region messages interchange. So that all the exchange server in the world don't need to interconnected with each others.
The unread message storage servers are using in-memory cache, since unread message are suppose to be retrieve frequently and should be faster, compare with that of reading message histories.
Suppose every multi-media resources will have an GUID and an server ID, when device connected storage server cannot find the corresponding resources, the storage server will pull the resource from the correct server, and then serve the content to the client device, so that when the family member within the same region try to access the same content, it will be faster.
'''