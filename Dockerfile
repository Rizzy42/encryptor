FROM alpine:latest as builder
ENV PATH "$PATH:/home/root/.local/bin"
WORKDIR /src
COPY . ./
# I'm building using the docker-build in my Pipfile as the normal build task fails in this container (very cryptic error)
# We lose obfuscation here though :(
RUN apk update && \
		apk add py3-pip binutils && \
			pip install pipenv && \	
				pipenv install --system && \		
					pipenv run docker-build

FROM alpine:latest as runtime
COPY --from=builder /src/dist/encryptor ./
ENTRYPOINT [ "./encryptor" ]