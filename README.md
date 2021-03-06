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

To kill session variables (and context):
`http://localhost:5456/assistant/expire_sessions/`

To query chatbot: 
`http://localhost:5456/assistant/perform_skill?text=hello+soother`

Access also at:
`https://api.urn.systems/assistant/`

n.b. Session variables expire every hour. If you're having problems with the front-end app, you might want to: `https://api.urn.systems/assistant/expire_sessions`


### PROVENANCE AND ARCHITECTURE
- I have hacked the [Macsen chatbot API](https://github.com/techiaith/macsen-sgwrsfot) to serve my purposes here, without completing all sensible refactoring. This means that the intent-parsing workflow is ineffficient.
- The macsen chatbot API is a simple question and answer chatbot. It uses `Brain.py` to branch out to different skills, which are assigned their intents and keywords in `$skillDir/intents`.
- My hack is to add conversationl context, which I've done by customising the skill class (in `Skill.py`) and adding `SootherContext.py`, which draws on MycroftAI's [`adapt`](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/adapt) intent parser. Adapt enables the persistance of conversationl context between requests to the server. (A simple demo of Adapt's conversational context is found in the "tea" skill at `skills/tea/tea.py`.)

The current intent-parsing workflow is as follows: 
- `Brain.py` checks to see if `activeSkill` is set in the cherrypy session variables
- If not, `Brain.py` evaluates the incoming request using the first-level intent-parsing architecture (borrowed from the Macsen chatbot and thus routed through each skill's `$skillDir/intents` directory). 
- This process results in a selected skill, which is set as `activeSkill` in the cherrypy session variables
- The request is then routed to the second-level intent-parsing architecture, defined in `$skillDir/intents.py` and implemented as dialogue in `$skillDir/$skillName.py`
- Soother's dialogue is returned
- `activeSkill` is now assigned to a specific skill in the cherrpy session variables. The next user request is thus automatically routed to this skill. This enables the persistance of a skill until the end of a sub-conversation. 
- Within a skill, context is implemented within the skill via the `SootherContext` class and the Adapt intent parser (as mentioned above). 
- When a user returns to the menu or otherwise exits the skill, the `activeSkill` session variable is reset, enabling the selection of a different skill.
- The "host" personality is currently set also via a cherrypy session variable, `RolePlayContext`.

This two-tiered intent parsing architecture probably doesn't make sense, and the hacked macsen first-level intent-parsing architecture should be eliminated in favor a purely Adapt-based architecture that carries the `activeSkill` paradigm only through the use of Adapt's "context" capabilities. In my opinion, this would be the next logical step in architectural refinement. 


### CURRENT SKILLS

Skills implemented in the alpha are as follows: 
- Personality: This is the first skill that the user encounters upon saying "hello". It sets the "host" of the SOOTHER session and can be reset if the user says "change personality" while in the "menu" skill 
- Menu: This is the skill that tells the user what SOOTHER is capable of. It uses the "persona" set in the `Personality` skill
- ASMR: This skill tells the user about ASMR
- Soother: This skill tells hte user about Soother
- Youtube: This skill recommends content from Youtube
- Friend: This is the "role play" that corresponds to the "friend" host persona. It should only be accessible when the "friend" is set as the SOOTHER host, but currently it is always accessible. 
- Dog: This is the "role play" that corresponds to the "dog therapist" host persona. It's also always availble, though its availability should be limited to sessions where the therapist is the host persona.
- Alien: This is the "role play" that corresponds to the "alien" host persona. It's also always availble, though its availability should be limited to sessions where the alien is the host persona.

- Tea: This skill is not currently active, but is included as a simple and easy-to-understand demo of the adapt intent parser's conversational context capability. 
- Spotify: This skill is not currently active. It was included in the Macsen chatbot and I didn't delete it as I was thinking about also implementing a Spotify ASMR recommendation system. 


### PERSONALITIES

The SOOTHER personalities were hastily written and should be further refined. At the moment, they're extreme caricatures of ASMR role-play personality tropes and should be "toned down" in my opinion, or just given more consideration. They could all be enhanced with e.g. sound effects, etc. 

Some existing issues with personalities: 
- The "therapist" persona often malfunctions when accessed via the app (but not via the chatbot web interface) for reasons I have not determined!
- The "therapist" persona also does not give accurate conversational feedback to the user. This persona is based upon ELIZA (the first therapy chatbot developed at MIT) and should follow ELIZA's rules for understanding conversational context in a more sophisticated way. My implementation is a hasty first pass at imbuing my therapist persona with some of ELIZA's dialogue. This could easily be expanded and refined with a bit more attention. 
- The "friend" and "alien" personas have dialogue that is entirely too long for the synthesized whisper to support (and to display on the current chatbot interface). Either the dialogue needs to be split on the sentence at the chatbot server, or in the app before the text is sent to the TTS API for synthesis. 
- The user is not currently able to switch persona from within each persona's sub-conversation. The user must return to the menu and, from there, say "switch personality". Personas should be able to be switched on demand from anywhere in the app. 


### SYNTHESIS VS PRE-RECORDED VOICE

Because my sythesized whisper is quite rough around the edges (and because of the cost of GPU servers), I have recorded all of SOOTHER's current dialogue as audio files that are simply included with the app. The chatbot API, as you can see, returns a file name that corresponds to the correct file in the app along with the text of the dialogue. 

Because in this version, I am relying on the pre-recoreded audio files, I do not take full advantage of the possiblity of generating dialogue on the fly. I believe that this could be a very valuable feature of SOOTHER in the future and give the personalities more life. 

The current architecture of including audio files in the app works fine for an alpha release but in the future any audio files should be streamed from the internet and/or temporarily downloaded and then deleted. 


### EXISTING ISSUES: 
- Code is untested, and I'm sure there are bugs -- this is a very alpha version of the chatbot!
- Code also definitely needs to be refactored and is in many ways inefficient -- all to say -- this is a rough version ;) 