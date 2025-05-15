FROM openjdk:21-slim
COPY "./target/Remodify-microservice-iam-0.0.1-SNAPSHOT.jar" "remodify-microservice-iam.jar"
EXPOSE 8082
ENTRYPOINT ["java", "-jar", "remodify-microservice-iam.jar"]
