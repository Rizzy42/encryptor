FROM alpine:latest as builder
ENV PATH "$PATH:/home/root/.local/bin"
WORKDIR /src
COPY . ./
RUN apk update && \
		apk add py3-pip binutils && \
			pip install pipenv && \	
				pipenv install --system && \		
					pipenv run docker-build

FROM alpine:latest as runtime
COPY --from=builder /src/dist/encryptor ./
ENTRYPOINT [ "./encryptor" ]