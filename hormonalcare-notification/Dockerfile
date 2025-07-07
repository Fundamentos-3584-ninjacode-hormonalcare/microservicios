FROM openjdk:21-slim
COPY "./target/hormonalcare-microservice-notification-0.0.1-SNAPSHOT.jar" "hormonalcare-microservice-notification.jar"
EXPOSE 8083
ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=docker", "hormonalcare-microservice-notification.jar"]
