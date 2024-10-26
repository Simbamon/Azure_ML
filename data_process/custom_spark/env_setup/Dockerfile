FROM openjdk:11 AS build-stage

FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
COPY --from=build-stage /opt/java/openjdk /opt/java/openjdk

ENV JAVA_HOME=/opt/java/openjdk
ENV PATH="$JAVA_HOME/bin:$PATH"

COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt