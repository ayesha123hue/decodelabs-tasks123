# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Industrial Training Kit

# Step 1: Knowledge base (Dictionary) - yahan apne sawal-jawab dalo
responses = {
    "hello": "Hi there! Kaise ho aap?",
    "hi": "Hello! Main aapki kya madad kar sakta hoon?",
    "how are you": "Main theek hoon, shukriya! Aap kaise hain?",
    "what is your name": "Mera naam DecodeBot hai.",
    "help": "Aap mujhse 'hello', 'how are you', 'what is your name' jaise sawal pooch sakte hain.",
}

exit_commands = ["bye", "exit", "quit"]

def get_response(user_input):
    # Agar dictionary mein match mil gaya to wo jawab do,
    # warna default fallback jawab do
    return responses.get(user_input, "Mujhe samajh nahi aaya, dobara try karein.")

def run_chatbot():
    print("Chatbot start ho gaya! Baat karne ke liye kuch likhein (band karne ke liye 'bye' likhein)")

    while True:  # Step 2: Continuous loop
        raw_input_text = input("You: ")

        # Step 3: Sanitization - lowercase + extra spaces hatana
        clean_input = raw_input_text.lower().strip()

        # Step 4: Exit condition
        if clean_input in exit_commands:
            print("Bot: Allah Hafiz! Phir milte hain.")
            break

        # Step 5: Response dena
        reply = get_response(clean_input)
        print("Bot:", reply)

if __name__ == "__main__":
    run_chatbot()
