

while getopts a:s: flag
do
    case "${flag}" in
        a) app=${OPTARG};;
        s) stage=${OPTARG};;
    esac
done

if [ -z ${app+x} ]; then 
    echo "-a (app) argument is required"; 
    exit 9999
else 
    echo "Application set to $app"; 
fi

if [ -z ${stage+x} ]; then 
    echo "-s (stage) argument is required"; 
    exit 9999
else 
    export APP_STAGE=$stage
    echo "Stage set to $stage"; 
fi

CONFIG_FILE="./configs/$app/$stage"

if [ ! -f $CONFIG_FILE ]; then
    echo "No configuration file found for app ($app) stage ($stage)"
    exit 9999
fi

IFS='='
while read -r key value
do
    if [ "$key" == "applicationId" ]; then
        export APP_ID=$value
    elif [ "$key" == "secret" ]; then
        export APP_SECRET=$value
    elif [ "$key" == "ownerId" ]; then
        export OWNER_ID=$value
    elif [ "$key" == "profileId" ]; then
        export PROFILE_ID=$value
    fi
done <$CONFIG_FILE

if [ -z ${PROFILE_ID+x} ]; then 
    echo "profileId must be set in the configuration file"; 
    exit 9999
else 
    echo "ProfileId set to $PROFILE_ID"; 
fi

cd infrastructure/authApp

cdk synth
cdk bootstrap --profile $PROFILE_ID
cdk deploy --profile $PROFILE_ID
