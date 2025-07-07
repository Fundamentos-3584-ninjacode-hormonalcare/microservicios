FROM openjdk:21-slim
COPY "./target/hormonalcare-microservice-medicalRecord-0.0.1-SNAPSHOT.jar" "hormonalcare-microservice-medicalRecord.jar"
EXPOSE 8082
ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=docker", "hormonalcare-microservice-medicalRecord.jar"]
