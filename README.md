# Gas Canister Notification

An application that notify on the owner to some residence over the level of your gas canister.  

To avoid that the app have an error because several residences notify at once i added a message brocker 
and for notify on real time, socketIO, this is a test for try real time notify and queue, because we will
install in many houses the system. So we are monitoring several houses at once.

For the backend i used python that is a script language, i thought to use mysql but in the moment i don't know.
For messaging i used Kafka and socketIO for real time interactions per events.

## Getting Started

Run the docker script, install python env and install the packages on env of python. After etc.


# Technology Stack

This project was build using [Python v3]() and uses the following techologies:

- [Flask]() - For make the apis.
- [Pytest]() - For unit testing.
- [Pylint]() - For validate the convention.
- [Kafka]() - For messaging.
- [SocketIO]() - For real time interactions.
- [Pre-commit]() - For identifying simple issues before submission to code review.

Other techs:
- [Docker]() - For containerization.


# Feactures

- [ ] Make that the house publishe on queue the state of gas canister and notify per phone number to owner of the residence.
The first notification is only to owner of residence by message and the last send to owner and agence of gas.

- [ ] After the owner can get the new gas canister clicking on the button  'Request new gas canister' in app.tada Contributing

# License

Released in 2022. This project is under the [MIT license](LICENSE)

Made by [António Gabriel](https://github.com/Antonio-Gabriel)