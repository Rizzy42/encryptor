FROM alpine:latest as builder
ENV PATH "$PATH:/home/root/.local/bin"
WORKDIR /src
COPY . ./
RUN apk update && \
		apk add py3-pip binutils && \
			pip install pipenv && \	
				pipenv install --system && \		
					pyinstaller --onefile main.py

FROM alpine:latest as runtime
COPY --from=builder /src/dist/main ./
ENTRYPOINT [ "./main" ]