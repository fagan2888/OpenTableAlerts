# OpenTableAlerts
A basic Python script for landing hard to get reservations

## Setup

1. Download the latest [zipped release](https://github.com/kleprevost/OpenTableAlerts/releases)
2. Author a new Lambda function "from scratch"
3. Create a new custom role when promopted, copy and paste the contents of lambda_opentable_policy.json into the policy editor
4. Upload zipped release and add environment variables (see below)
5. Create your CloudWatch Alarm (named "OpenTableAlerts") and set it to trigger every few minutes
6. ???
7. Profit!