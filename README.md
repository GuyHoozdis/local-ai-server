# Running Ollama and OpenWebUI

See the [OpenWebUI docs](https://docs.openwebui.com/) and [Ollama docs](https://github.com/ollama/ollama?tab=readme-ov-file#ollama).

Running Ollama in a container on a Mac with Apple Silicon doesn't work.  Well, it can't leverage the 
integrated GPU in the M1, M2, M3, ... chips because the pass through vitalization logic doesn't exist
or doesn't work or can't work yet for some reason.

If you watch the docker logs as the container boots you will find a message in there that mentions
something to the effect of "No GPUs detected."  Running the Ollama server directly on the host gets 
around this issue.

>[!NOTE]
> M-Series OSX platforms should run Ollama natively and OpenWebUI in a container.  See the [section
> below](#running-openwebui-with-ollama-running-on-the-host) for more details.

See other work / experiments I was doing in `~/Development/sandbox/ollama`.


## Running Ollama Alone

Ollama will give you a REPL style prompt if you want to interact with a model.  The `ollama run <model>` 
command does this.  To get a ChatGPT style UI, you need to use something like OpenWebUI.

On its own, Ollama still offers a port over which it can communicate using OpenAI API protocol.  It is
a REST API with endpoints `/api/generate` and `/api/chat`.  Responses are tokens.  The server will respond
with an HTTP code `101 Switching Protocols` before responding with the stream of tokens.  The response body
of for the response that contains each token also has a `done` attribute.  It will be `false` until the 
final token is being transmitted.  When `done` is `true` that response body will also contain metrics about
the interaction.

???: I am using `llama3.2` while doing this.  Is it the same for other models?


### Generate a Response

```
$ http :11434/api/generate model="llama3.2" prompt="What is love?"
```


### Chat with a Model

```
$ http :11434/api/chat model="llama3.2" prompt="What is love?"
```


## Running OpenWebUI with Ollama Running on the Host

This is the scenario for Apple Silicon.  To run the OpenWebUI server in a container and have it be able to 
interact with the Ollama server running on the host you need to use the `--add-host` parameter or, in 
[docker compose](https://github.com/compose-spec/compose-spec/blob/main/spec.md#extra_hosts), use the `extra_hosts`
directive.

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

If Ollama is already running and using its default port, that is all that is needed.  Open a browser and
navigate to [http://localhost:3000](http://localhost:3000).
