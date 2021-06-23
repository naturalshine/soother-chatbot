from adapt.engine import IntentDeterminationEngine
import cherrypy 

# Create adapt engine
def create_engine(engineEntities):
	"""
	Returns an Adapt engine.
	"""
	engine = IntentDeterminationEngine()

	# Register entities on engine
	if engineEntities["entities"]:
		cherrypy.log("ENTITIES")
		for entity, keywords in engineEntities["entities"].items():
			for keyword in keywords:
				engine.register_entity(keyword, entity)

	if engineEntities["single_regex_entities"]:
		cherrypy.log("SINGLE REG ENT")
		for entity in engineEntities["single_regex_entities"]:
			engine.register_regex_entity(entity)

	# Register intents on engine
	if engineEntities["skill_intents"]:
		cherrypy.log("INTENTS")
		for intent in engineEntities["skill_intents"]:
			engine.register_intent_parser(intent)

	return engine

