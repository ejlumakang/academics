import time

class QueueApp:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task, priority):
        self.task_queue.append((priority, task))
        print(f"Task added: {task} (Priority: {priority})")
        time.sleep(1)
        self.task_queue.sort(reverse=True)
        return self.task_queue

    def process_task(self):
        if self.task_queue:
            priority, current_task = self.task_queue.pop(0)
            print(f"\nProcessing task: {current_task}")
            time.sleep(1)

    def dequeue(self):
        if self.task_queue:
            dequeued_task = self.task_queue.pop(0)
            priority, task = dequeued_task
            print(f"Tasks Completed: {dequeued_task})")
            time.sleep(1)
            return dequeued_task

    def remaining_task(self):
        if self.task_queue:
            print("\nRemaining Tasks:")
            for priority, task in self.task_queue:
                print(f"{task} (Priority: {priority})")
                time.sleep(1)

scheduler = QueueApp()

scheduler.add_task("Fixing my bed", priority=5)
scheduler.add_task("Cleaning my room", priority=1)
scheduler.add_task("Washing dishes", priority=3)

scheduler.process_task()
scheduler.remaining_task()

scheduler.process_task()
scheduler.remaining_task()

scheduler.process_task()
scheduler.remaining_task()