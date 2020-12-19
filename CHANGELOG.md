# Record of updates

## 2020.12.18
* Created handlers:
  * handler.redirect_to_auth_service - navigates user to auth page which correct app & owner ID's
  * handler.handle_code_exchange - Exchanges provided for an authentication token
* CDK application - `infrastructure/authApp`
  * Spins up CDK infrastructure for setting up an authentication redirect API for a service authenticating with futoi auth service.
* Added configuration for sans beta stage
* Created `bin/deploy.sh` script, which simplifies deploying the cdk application