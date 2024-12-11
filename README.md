
[![License][license-shield]](LICENSE)
![Project Maintenance][maintenance-shield]

# Instagram followers counter Integration for Home Assistant
This integration adds a sensor that retrieves the number of Instagram followers for a specified user.

## 🛠️ Installation

1.Add this repository to your HACS with the following button:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=xamrex&repository=Hacs_Insta_follower&category=integration)

2.Install this integration with the follwing button:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=insta_follower)

3.Enter Instagram Account name and Token and press Submit.
![Configuration](https://raw.githubusercontent.com/xamrex/Hacs_Insta_follower/main/image/pic1.png)

## ❓How to get token
1. To get token you need to create an account on  https://rapidapi.com/,
2. Search for instagram scraper api https://rapidapi.com/social-api1-instagram/api/instagram-scraper-api2 and press Subscribe for Basic
![Instagram API](https://raw.githubusercontent.com/xamrex/Hacs_Insta_follower/main/image/api1.png)
3. **Token** is your **x-rapidapi-key** 
![Token](https://raw.githubusercontent.com/xamrex/Hacs_Insta_follower/main/image/api2.png)

## 🤷‍♂️ How it works?
1. Every 6 hours there is an API call to get instagram followers counter.
2. There is a **500** API Calls limit per month

## 🎯 Results
![Result](https://raw.githubusercontent.com/xamrex/Hacs_Insta_follower/main/image/result.png)


[integration_blueprint]: https://github.com/ludeeus/integration_blueprint
[license-shield]: https://img.shields.io/github/license/ludeeus/integration_blueprint.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-xamrex-blue.svg?style=for-the-badge


## 🤝 Contributing

You can contribute by creating a PR, but also by testing:

- Provide general feedback or report issues.

## 🛟 Need help?

If you have a feature request or encounter a problem, feel free to open an issue! Have a general question, need help setting up then go to the discussions.
