# SOOTHER CHATBOT
## v.1.0.0

### INSTALLATION:
 
```
$ git clone https://github.com/naturalshine/soother-chatbot.git
$ cd soother-chatbot
$ make build
$ make run
```

### USAGE

To kill session (context):
`http://localhost:5456/assistant/expire_sessions/`

To query chatbot: 
`http://localhost:5456/assistant/perform_skill?text=hello+soother`

See also:
`https://api.urn.systems/assistant/`


### PROVENANCE AND ARCHITECTURE
- I have hacked the [Macsen chatbot API](https://github.com/techiaith/macsen-sgwrsfot) to serve my purposes here, without completing all sensible refactoring. This means that the system of intent parsing doesn't totally make sense. 
- The macsen chatbot API is a simple question and answer chatbot. It uses `Brain.py` to branch out to different skills, which are assigned their intents/keywords in the `intents` directory in each skill's directory. 
- My hack is to add conversationl context, which I've done by customising the skill class (in Skill.py) and adding `SootherContext.py`, which draws on MycroftAI's [`adapt`](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/adapt) intent parser. Adapt allows for the persistance of context between requests to the server. 

The current intent parsing workflow is as follows: 
- `Brain.py` checks to see if `activeSkill` is set in the session variables
- if not, `Brain.py` evaluates the incoming request using the first-level intent parsing architecture (borrowed from the Macsen chatbot and determined via each skill's `intents` directory)
- The selected skill is set as `activeSkill` in the session variables
- The request is then routed to the second-level intent-parsing mechanism, defined in `$skillDir/intents.py` and selected in `$skillDir/$skillName.py`
- Soother's dialogue is returned
- When the next request comes in, `activeSkill` is already set in the session variables
- Thus, the request is routed automatically to the `activeSkill` directory, enabling the persistance of a skill until the end of a sub-conversation. Context is applied within the skill via the `SootherContext` class and adapt intent parser as mentioned above. 
- When a user returns to the menu or otherwise exits the skill, the `activeSkill` session variable is reset, enabling the selection of a different skill.

This two-tiered intent parsing architecture probably doesn't make sense, and the hacked macsen first-level intent-parsing architecture should be eliminated in favor a purely Adapt-based architecture that carries the `activeSkill` paradigm purely through the use of Adapt's "context" capabilities. In my opinion, this would be the next logical step in architectural refinement. 

### EXISTING ISSUES: 
- Code is untested, and I'm sure there are bugs -- this is a very alpha version of the chatbot!
- Code also definitely needs to be refactored and is in many ways inefficient -- all to say -- this is a rough version ;) 