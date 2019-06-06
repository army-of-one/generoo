FROM java:8

ADD example-api/target/{{artifact_id}}-api*.jar /tmp/{{artifact_id}}-api.jar

ENV ENV=local

ENTRYPOINT /usr/bin/java -jar -Dspring.profiles.active=$ENV /tmp/{{artifact_id}}-api.jar