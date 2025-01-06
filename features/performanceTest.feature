Feature: Performance Testing for API

  Scenario Outline: Load testing the client registration API
    Given the '/client_registeration' is running
    When I send <user_count> registration requests with a spawn rate of <spawn_rate> over <duration>

  Examples:
    | user_count | spawn_rate | duration |
    |10          |1           |1m        |
#    | 200        | 20         | 30m      |  /client_login        |