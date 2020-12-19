# Futoi Auth Portal

Contains the CDK infrastructure & lambda python package for using the [Futoi Authentication Service](https://github.com/RyanSharp/FutoiAuth) as an auth provider.

## Deployment

1. Retrieve an application_id, secret, and owner_id from the authentication service.  These three values will be used to facilitate the authentication flow for your application.
2. In the `configs` directory, create a directory (if one does not already exist) for your app (ex. `sans`)
3. Under the directory in step 2, create a file for the stage (ex. `beta`)
4. In the file, create 4 lines with the following format:
    ```
    applicationId={application_id}
    secret={secret}
    ownerId={owner_id}
    profileId={aws_profile}
    ```
5. Then run the following comment
    ```
    # creates a local copy of the python application and creates a zip archive
    package_local
    # Synthesizes the cloudformation stack and deploys the app
    ./bin/deploy.sh -a sans -s beta
    ```
