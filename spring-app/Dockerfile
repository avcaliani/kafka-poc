FROM openjdk:11

ENV GRADLE_HOME="/opt/gradle"
ENV GRADLE_VERSION="6.8.3"
ENV PATH="${GRADLE_HOME}/bin:${PATH}"

WORKDIR /opt

ADD "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" .
RUN unzip -q gradle*.zip && rm -f gradle*.zip && mv gradle* gradle

WORKDIR /app
ADD . .
RUN gradle build

CMD java -jar /app/build/libs/*.jar
