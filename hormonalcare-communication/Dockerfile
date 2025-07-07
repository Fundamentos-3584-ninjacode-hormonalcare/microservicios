FROM openjdk:21-slim
COPY "./target/hormonalcare-microservice-communication-0.0.1-SNAPSHOT.jar" "hormonalcare-microservice-communication.jar"
EXPOSE 8084
ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=docker", "hormonalcare-microservice-communication.jar"]
