import csv
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
chatbot = ChatBot('SlayTheSpireBot')

# Create a trainer for the chatbot
trainer = ListTrainer(chatbot)

# Function to load training data from a CSV file
def load_training_data_from_csv(file_path):
    training_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Ensure there are two columns
                training_data.append(row[0])  # User input
                training_data.append(row[1])  # Bot response
    return training_data

# Load training data from CSV
csv_file_path = 'training_data.csv'  # Specify your CSV file path here
training_data = load_training_data_from_csv(csv_file_path)

# Train the chatbot with the training data
trainer.train(training_data)

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Hello! I'm SlayTheSpireBot. Ask me anything about Slay the Spire!")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            response = get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
