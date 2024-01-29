from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer) if customer not in self.customers else None

    def add_trainer(self, trainer: Trainer):
        self.trainers.append(trainer) if trainer not in self.trainers else None

    def add_equipment(self, equipment: Equipment):
        self.equipment.append(equipment) if equipment not in self.equipment else None

    def add_plan(self, plan: ExercisePlan):
        self.plans.append(plan) if plan not in self.plans else None

    def add_subscription(self, subscription: Subscription):
        self.subscriptions.append(subscription) if subscription not in self.subscriptions else None

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        exercise_plan = [e for e in self.plans if e.trainer_id == trainer.id][0]
        equipment_id = exercise_plan.equipment_id
        equipment = [eq for eq in self.equipment if eq.id == equipment_id][0]
        info = [subscription.__repr__(), customer.__repr__(), trainer.__repr__(),
                equipment.__repr__(), exercise_plan.__repr__()]

        return '\n'.join(info)
