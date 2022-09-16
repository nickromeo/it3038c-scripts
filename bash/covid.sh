DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
DEATH=$( echo $DATA | jq '.[0].death')
NEG=$( echo $DATA | jq '.[0].negative')
CURRENT=$(echo $DATA | jq '.[0].hospitalizedCurrently')


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEG negative cases, $CURRENT currently hospitalized, and $DEATH deaths"
