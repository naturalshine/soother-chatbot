"""An intent parsing service using the Adapt parser."""
from threading import Lock
import time

from adapt.context import ContextManagerFrame


def _strip_result(context_features):
    """Keep only the latest instance of each keyword.
    Arguments
        context_features (iterable): context features to check.
    """
    stripped = []
    processed = []
    for feature in context_features:
        keyword = feature['data'][0][1]
        if keyword not in processed:
            stripped.append(feature)
            processed.append(keyword)
    return stripped

class SootherContextManager:
    """Adapt Context Manager
    Use to track context throughout the course of a conversational session.
    How to manage a session's lifecycle is not captured here.
    """
    def __init__(self):
        self.frame_stack = []
        self.timeout = 1 * 60  # minutes to seconds

    def clear_context(self):
        """Remove all contexts."""
        self.frame_stack = []

    def handle_add_context(self, context):
        """Add context
        Args:
            message: data contains the 'context' item to add
                     optionally can include 'word' to be injected as
                     an alias for the context item.
        """
        entity = {'confidence': 1.0}

        entity['data'] = [('', context)]
        entity['match'] = ''
        entity['key'] = ''
        entity['origin'] = ''
        self.inject_context(entity)

    def remove_context(self, context_id):
        """
        Remove a specific context entry.
        Args:
            context_id (str): context entry to remove
        """
        self.frame_stack = [(f, t) for (f, t) in self.frame_stack
                            if context_id in f.entities[0].get('data', [])]

    def inject_context(self, entity, metadata=None):
        """
        Args:
            entity(object): Format example...
                               {'data': 'Entity tag as <str>',
                                'key': 'entity proper name as <str>',
                                'confidence': <float>'
                               }
            metadata(object): dict, arbitrary metadata about entity injected
        """
        metadata = metadata or {}
        try:
            if self.frame_stack:
                top_frame = self.frame_stack[0]
            else:
                top_frame = None
            if top_frame and top_frame[0].metadata_matches(metadata):
                top_frame[0].merge_context(entity, metadata)
            else:
                frame = ContextManagerFrame(entities=[entity],
                                            metadata=metadata.copy())
                self.frame_stack.insert(0, (frame, time.time()))
        except (IndexError, KeyError):
            pass

    def get_context(self, max_frames=None, missing_entities=None):
        """ Constructs a list of entities from the context.
        Args:
            max_frames(int): maximum number of frames to look back
            missing_entities(list of str): a list or set of tag names,
            as strings
        Returns:
            list: a list of entities
        """
        missing_entities = missing_entities or []

        relevant_frames = [frame[0] for frame in self.frame_stack if
                           time.time() - frame[1] < self.timeout]
        if not max_frames or max_frames > len(relevant_frames):
            max_frames = len(relevant_frames)

        missing_entities = list(missing_entities)
        context = []
        last = ''
        depth = 0
        entity = {}
        for i in range(max_frames):
            frame_entities = [entity.copy() for entity in
                              relevant_frames[i].entities]
            for entity in frame_entities:
                entity['confidence'] = entity.get('confidence', 1.0) \
                                       / (2.0 + depth)
            context += frame_entities

            # Update depth
            if entity['origin'] != last or entity['origin'] == '':
                depth += 1
            last = entity['origin']

        result = []
        if missing_entities:
            for entity in context:
                if entity.get('data') in missing_entities:
                    result.append(entity)
                    # NOTE: this implies that we will only ever get one
                    # of an entity kind from context, unless specified
                    # multiple times in missing_entities. Cannot get
                    # an arbitrary number of an entity kind.
                    missing_entities.remove(entity.get('data'))
        else:
            result = context

        # Only use the latest  keyword
        return _strip_result(result)

