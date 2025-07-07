FROM openjdk:21-slim
COPY "./target/hormonalcare-microservice-iam-0.0.1-SNAPSHOT.jar" "hormonalcare-microservice-iam.jar"
EXPOSE 8081
ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=docker", "hormonalcare-microservice-iam.jar"]
