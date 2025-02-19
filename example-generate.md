
From the [Ollama GitHub](https://github.com/ollama/ollama?tab=readme-ov-file#rest-api) docs.

## Generate a response

This uses the `/api/generate` endpoint; as opposed to, the `api/chat` endpoint.


This is the equivalent `Httpie` command to the `curl` example given by the docs.
```
$ http :11434/api/generate model="llama3.2" prompt="What is love?"
```

From the docs:
```
$ curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "prompt": "What is love?"}'

{"model":"llama3.2","created_at":"2024-10-28T10:44:14.568202Z","response":"What","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.581214Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.594769Z","response":" profound","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.608238Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.619051Z","response":" complex","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.629672Z","response":" question","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.644613Z","response":"!","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.656053Z","response":" Love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.667412Z","response":" is","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.678937Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.690889Z","response":" multif","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.701721Z","response":"ac","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.712288Z","response":"eted","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.724403Z","response":" concept","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.736103Z","response":" that","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.748337Z","response":" has","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.760816Z","response":" been","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.772266Z","response":" debated","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.785092Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.798342Z","response":" explored","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.811847Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.823736Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.835219Z","response":" experienced","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.84765Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.859677Z","response":" humans","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.872367Z","response":" for","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.88391Z","response":" centuries","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.897072Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.910098Z","response":" While","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.923033Z","response":" it","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.934485Z","response":" can","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.945961Z","response":" be","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.957569Z","response":" subjective","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.970559Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.981991Z","response":" vary","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:14.993966Z","response":" from","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.006914Z","response":" person","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.020439Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.033595Z","response":" person","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.047117Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.06063Z","response":" here","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.073955Z","response":"'s","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.087266Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.100453Z","response":" comprehensive","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.113673Z","response":" attempt","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.127495Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.141114Z","response":" define","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.154815Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.168389Z","response":":\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.181736Z","response":"Love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.195616Z","response":" is","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.209113Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.221629Z","response":" strong","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.233595Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.246777Z","response":" positive","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.26051Z","response":" emotion","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.272958Z","response":" characterized","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.285019Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.297948Z","response":" feelings","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.311403Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.324922Z","response":" affection","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.337217Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.349739Z","response":" attachment","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.36351Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.377622Z","response":" care","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.39237Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.407586Z","response":" compassion","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.423004Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.438147Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.452173Z","response":" deep","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.467078Z","response":" emotional","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.483072Z","response":" connection","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.498703Z","response":" with","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.5151Z","response":" another","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.532458Z","response":" person","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.548908Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.566575Z","response":" place","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.584865Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.603366Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.623408Z","response":" thing","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.64524Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.668767Z","response":" It","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.687428Z","response":" encompasses","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.704099Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.718557Z","response":" range","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.732244Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.744046Z","response":" emotions","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.755027Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.765645Z","response":" including","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.775172Z","response":" happiness","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.784807Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.794687Z","response":" content","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.803997Z","response":"ment","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.814089Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.82392Z","response":" warmth","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.833561Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.84334Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.853498Z","response":" tend","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.863573Z","response":"erness","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.873378Z","response":".\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.883478Z","response":"There","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.89376Z","response":" are","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.903303Z","response":" many","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.913407Z","response":" forms","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.923486Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.932978Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.942963Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.95287Z","response":" including","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.96276Z","response":":\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.972581Z","response":"1","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.982774Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:15.992923Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.002742Z","response":"Rom","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.012876Z","response":"antic","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.023051Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.032641Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.042816Z","response":" intense","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.052982Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.062519Z","response":" passionate","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.072541Z","response":" attraction","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.082688Z","response":" between","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.092777Z","response":" two","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.102663Z","response":" people","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.112828Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.122985Z","response":" often","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.132621Z","response":" accompanied","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.142768Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.1529Z","response":" feelings","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.162327Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.172057Z","response":" desire","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.182205Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.191722Z","response":" intimacy","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.20178Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.211839Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.221712Z","response":" commitment","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.231665Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.241979Z","response":"2","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.252013Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.261808Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.27203Z","response":"F","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.282365Z","response":"amil","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.291898Z","response":"ial","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.302092Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.312251Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.322057Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.332253Z","response":" bond","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.342528Z","response":" between","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.35253Z","response":" family","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.362497Z","response":" members","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.372656Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.382829Z","response":" such","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.392532Z","response":" as","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.40277Z","response":" parents","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.41293Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.422456Z","response":" children","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.432573Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.442857Z","response":" siblings","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.452309Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.462592Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.472774Z","response":" extended","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.482585Z","response":" family","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.49267Z","response":" relationships","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.502842Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.513018Z","response":"3","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.523077Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.533529Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.54383Z","response":"Pl","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.554028Z","response":"at","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.563885Z","response":"onic","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.573669Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.58368Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.593921Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.603869Z","response":" deep","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.613857Z","response":" friendship","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.624096Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.634365Z","response":" affection","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.644145Z","response":"ate","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.654499Z","response":" relationship","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.664713Z","response":" between","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.674571Z","response":" friends","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.684816Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.695189Z","response":" often","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.704689Z","response":" characterized","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.714902Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.725143Z","response":" mutual","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.735043Z","response":" support","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.745268Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.754928Z","response":" trust","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.765219Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.774802Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.784827Z","response":" shared","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.79501Z","response":" interests","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.804608Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.814879Z","response":"4","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.824555Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.834335Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.844331Z","response":"Self","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.854561Z","response":"-lo","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.864289Z","response":"ve","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.874647Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.885039Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.894922Z","response":" positive","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.904767Z","response":" self","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.914925Z","response":"-image","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.92491Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.934828Z","response":" self","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.945256Z","response":"-","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.955493Z","response":"accept","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.965115Z","response":"ance","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.975182Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.98539Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:16.995136Z","response":" self","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.005401Z","response":"-care","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.015944Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.025759Z","response":" which","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.035866Z","response":" involves","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.046157Z","response":" apprec","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.056122Z","response":"iating","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.066152Z","response":" one","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.076273Z","response":"'s","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.086444Z","response":" own","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.096032Z","response":" worth","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.10632Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.116705Z","response":" values","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.126286Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.136472Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.146728Z","response":" unique","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.156972Z","response":" qualities","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.167139Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.17675Z","response":"5","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.187093Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.197468Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.207133Z","response":"Un","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.217489Z","response":"conditional","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.227473Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.237406Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.247687Z","response":" an","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.258086Z","response":" unw","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.267786Z","response":"av","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.278095Z","response":"ering","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.288443Z","response":" acceptance","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.298017Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.308323Z","response":" devotion","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.31835Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.327993Z","response":" someone","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.337813Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.348077Z","response":" something","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.358116Z","response":" without","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.367929Z","response":" expectations","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.378204Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.388392Z","response":" conditions","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.398274Z","response":".\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.408499Z","response":"Love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.418936Z","response":" can","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.428647Z","response":" also","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.438966Z","response":" be","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.449248Z","response":" experienced","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.458854Z","response":" in","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.469306Z","response":" various","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.479594Z","response":" contexts","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.489537Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.500298Z","response":" such","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.51069Z","response":" as","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.521021Z","response":":\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.531378Z","response":"1","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.54131Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.551741Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.561753Z","response":"Int","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.571881Z","response":"im","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.582116Z","response":"acy","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.592532Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.602308Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.612518Z","response":" deep","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.622835Z","response":" emotional","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.632651Z","response":" connection","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.642967Z","response":" with","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.653406Z","response":" another","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.663352Z","response":" person","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.673243Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.68364Z","response":" often","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.693634Z","response":" characterized","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.703889Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.71428Z","response":" vulnerability","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.72448Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.734453Z","response":" trust","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.744711Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.755008Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.764869Z","response":" clos","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.775282Z","response":"eness","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.78574Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.79564Z","response":"2","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.806069Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.816547Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.826322Z","response":"Com","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.836455Z","response":"pass","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.846795Z","response":"ion","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.856676Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.866954Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.877472Z","response":" desire","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.887671Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.897733Z","response":" alleviate","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.907537Z","response":" suffering","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.917958Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.928343Z","response":" care","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.938307Z","response":" for","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.948743Z","response":" others","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.9592Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.969351Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.979625Z","response":" promote","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:17.990015Z","response":" well","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.000351Z","response":"-being","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.010511Z","response":".\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.020818Z","response":"3","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.030873Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.040744Z","response":" **","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.051162Z","response":"Attachment","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.061338Z","response":"**:","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.071256Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.081765Z","response":" strong","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.092171Z","response":" bond","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.102103Z","response":" between","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.112588Z","response":" two","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.123053Z","response":" people","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.132794Z","response":" or","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.143263Z","response":" entities","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.153655Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.163398Z","response":" often","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.173373Z","response":" accompanied","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.183887Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.19384Z","response":" feelings","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.204415Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.214871Z","response":" security","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.22495Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.235389Z","response":" comfort","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.245839Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.256057Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.265948Z","response":" loyalty","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.276405Z","response":".\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.286801Z","response":"Ultimately","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.296779Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.307268Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.317852Z","response":" is","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.327704Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.338164Z","response":" complex","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.348597Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.358439Z","response":" dynamic","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.368965Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.379471Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.389196Z","response":" multif","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.399784Z","response":"ac","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.410382Z","response":"eted","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.420871Z","response":" emotion","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.431231Z","response":" that","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.441129Z","response":" can","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.451726Z","response":" be","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.462169Z","response":" both","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.472107Z","response":" exhilar","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.482656Z","response":"ating","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.493257Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.503231Z","response":" challenging","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.51371Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.524308Z","response":" While","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.534164Z","response":" it","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.544707Z","response":"'s","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.555326Z","response":" impossible","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.565415Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.576152Z","response":" fully","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.58682Z","response":" capture","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.59681Z","response":" its","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.607399Z","response":" essence","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.618064Z","response":" in","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.628101Z","response":" words","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.638649Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.649252Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.6595Z","response":" has","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.669599Z","response":" been","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.679831Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.690277Z","response":" universal","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.70055Z","response":" human","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.711061Z","response":" experience","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.721423Z","response":" throughout","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.731685Z","response":" history","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.741803Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.752332Z","response":" transc","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.762824Z","response":"ending","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.77277Z","response":" cultures","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.783269Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.793853Z","response":" languages","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.804186Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.814772Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.824973Z","response":" societies","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.83496Z","response":".\n\n","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.845217Z","response":"What","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.85589Z","response":" do","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.866383Z","response":" you","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.876908Z","response":" believe","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.887543Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.897872Z","response":" is","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.907982Z","response":"?","done":false}
{"model":"llama3.2","created_at":"2024-10-28T10:44:18.91862Z","response":"","done":true,"done_reason":"stop","context":[128006,9125,128007,271,38766,1303,33025,2696,25,6790,220,2366,18,271,128009,128006,882,128007,271,3923,374,3021,30,128009,128006,78191,128007,271,3923,264,28254,323,6485,3488,0,10919,374,264,62387,582,25489,7434,430,706,1027,59674,11,36131,11,323,10534,555,12966,369,24552,13,6104,433,649,387,44122,323,13592,505,1732,311,1732,11,1618,596,264,16195,4879,311,7124,3021,1473,29351,374,264,3831,11,6928,20356,32971,555,16024,315,37805,11,20581,11,2512,11,30481,11,323,5655,14604,3717,449,2500,1732,11,2035,11,477,3245,13,1102,71010,264,2134,315,21958,11,2737,23871,11,2262,479,11,41463,11,323,8541,29668,382,3947,527,1690,7739,315,3021,11,2737,1473,16,13,3146,45459,8322,3021,96618,19428,11,25429,33464,1990,1403,1274,11,3629,24895,555,16024,315,12876,11,66264,11,323,15507,627,17,13,3146,37,21606,532,3021,96618,279,11049,1990,3070,3697,11,1778,439,6699,323,2911,11,37783,11,477,11838,3070,12135,627,18,13,3146,2169,266,14338,3021,96618,264,5655,27607,477,37805,349,5133,1990,4885,11,3629,32971,555,27848,1862,11,7095,11,323,6222,12034,627,19,13,3146,12363,27578,588,96618,264,6928,659,14064,11,659,12,10543,685,11,323,659,41206,11,902,18065,9989,23747,832,596,1866,5922,11,2819,11,323,5016,29600,627,20,13,3146,1844,46468,3021,96618,459,15375,402,4776,26586,323,56357,311,4423,477,2555,2085,17078,477,4787,382,29351,649,1101,387,10534,304,5370,38697,11,1778,439,1473,16,13,3146,1090,318,2826,96618,264,5655,14604,3717,449,2500,1732,11,3629,32971,555,34104,11,7095,11,323,4597,24639,627,17,13,3146,1110,6519,290,96618,279,12876,311,61705,16066,11,2512,369,3885,11,323,12192,1664,33851,627,18,13,3146,34669,96618,264,3831,11049,1990,1403,1274,477,15086,11,3629,24895,555,16024,315,4868,11,6981,11,323,32883,382,67343,11,3021,374,264,6485,11,8915,11,323,62387,582,25489,20356,430,649,387,2225,91826,1113,323,17436,13,6104,433,596,12266,311,7373,12602,1202,28591,304,4339,11,3021,706,1027,264,20789,3823,3217,6957,3925,11,42590,2518,27833,11,15823,11,323,34775,382,3923,656,499,4510,3021,374,30],"total_duration":5737591958,"load_duration":1325900875,"prompt_eval_count":29,"prompt_eval_duration":58396000,"eval_count":400,"eval_duration":4350626000}
```
