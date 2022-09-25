# Gas Canister Notification

An application that notifies the homeowner about the level of their gas canister.

As a way to prevent the app from dying due to the large data responses that the server tells the owner about the level of their gas canister, I added message queue (Kafka) and socket for real-time interactions.

The idea is that the project works in several residences at once, and Helps the owner of the same to have the best control of the condition of the gas cylinder

## Getting Started

For run, first open your bash and execute this command:

```bash
docker-compose up --build
```
the command runs the zookeeper and kafka. After start:

```bash
python3 sms_server.py
python3 main.py
```

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

- [x] Make that the house publishe on queue the state of gas canister and notify per phone number to owner of the residence.
The first notification is only to owner of residence by message and the last send to owner and agence of gas.

- [ ] After the owner can get the new gas canister clicking on the button  'Request new gas canister' in app.tada Contributing

# License

Released in 2022. This project is under the [MIT license](LICENSE)

Made by [António Gabriel](https://github.com/Antonio-Gabriel)