# cobot_integration.py
"""
Script for integrating collaborative robotics (Cobots).
"""

class Cobot:
    def __init__(self, id, model, capabilities):
        self.id = id
        self.model = model
        self.capabilities = capabilities

    def perform_task(self, task):
        if task in self.capabilities:
            print(f'Cobot {self.id} performing task: {task}')
        else:
            print(f'Task {task} not supported by Cobot {self.id}')

class CobotIntegration:
    def __init__(self):
        self.cobots = []

    def add_cobot(self, cobot):
        self.cobots.append(cobot)

    def assign_task(self, cobot_id, task):
        for cobot in self.cobots:
            if cobot.id == cobot_id:
                cobot.perform_task(task)
                return
        print(f'Cobot {cobot_id} not found')

# Example usage
if __name__ == "__main__":
    # Create some cobots
    cobot1 = Cobot(id='cobot_001', model='UR5', capabilities=['welding', 'assembly'])
    cobot2 = Cobot(id='cobot_002', model='Baxter', capabilities=['packing', 'inspection'])

    # Integrate cobots
    integration = CobotIntegration()
    integration.add_cobot(cobot1)
    integration.add_cobot(cobot2)

    # Assign tasks to cobots
    integration.assign_task('cobot_001', 'welding')
    integration.assign_task('cobot_002', 'inspection')
    integration.assign_task('cobot_001', 'painting')  # Task not supported
