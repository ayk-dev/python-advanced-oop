from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: list = []  # list of Category objects
        self.topics: list = []  # list of topic objects
        self.documents: list = []
        self.category_ids = {}
        self.topic_ids = {}
        self.document_ids = {}

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
            self.category_ids[category.id] = category

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
            self.topic_ids[topic.id] = topic

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
            self.document_ids[document.id] = document

    def edit_category(self, category_id: int, new_name:str):
        category = self.category_ids.get(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.topic_ids.get(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.document_ids.get(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.category_ids.get(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.topic_ids.get(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.document_ids.get(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.document_ids.get(document_id)
        return document

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])


