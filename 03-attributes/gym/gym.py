from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: Customer = []
        self.trainers: Trainer = []
        self.equipment: Equipment = []
        self.plans: ExercisePlan = []
        self.subscriptions: Subscription = []
        self.subscription_ids = {}
        self.customer_ids = {}
        self.trainer_ids = {}
        self.plans_ids = {}
        self.equipment_ids = {}

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_ids[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            self.trainer_ids[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            self.equipment_ids[equipment.id] = equipment

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
            self.plans_ids[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            self.subscription_ids[subscription.id] = subscription

    def subscription_info(self, subscription_id: int):
        subscription = self.subscription_ids.get(subscription_id)
        customer = self.customer_ids.get(subscription.customer_id)
        trainer = self.trainer_ids.get(subscription.trainer_id)
        plan = self.plans_ids.get(subscription.exercise_id)
        equipment = self.equipment_ids.get(plan.equipment_id)
        return '\n'.join([subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(), plan.__repr__()])


