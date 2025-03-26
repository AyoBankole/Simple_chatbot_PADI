PADI Simple Chatbot

PADI Simple Chatbot is a conversational AI chatbot built using GPT-2 and Streamlit. It allows users to interact with a pre-trained language model and receive responses in a conversational format.

🚀 Features

Interactive chatbot powered by GPT-2

Supports conversation history tracking

Uses Streamlit for a lightweight web interface

Implements top-k and top-p sampling for better response generation

Handles padding and indexing errors gracefully

📌 Prerequisites

Ensure you have the following installed on your system:

Python 3.7 or later

pip package manager

🔧 Installation

Clone the repository:

git clone https://github.com/your-username/PADI-Simple-Chatbot.git
cd PADI-Simple-Chatbot

Create a virtual environment (optional but recommended):

python -m venv chatbot_env
source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

🚀 Running the Chatbot

Start the chatbot by running the Streamlit app:

streamlit run app_interface.py

This will launch the chatbot in your default web browser.

🛠 Troubleshooting

1. IndexError: index out of range in self

✅ Solution: This error typically occurs when the chatbot's response token indices exceed the context length. Ensure the latest version of the code includes safe indexing and padding handling.

2. ImportError: No module named 'transformers'

✅ Solution: Install the missing package using:

pip install transformers

3. Streamlit is not recognized as a command

✅ Solution: Ensure the virtual environment is activated before running streamlit run app_interface.py.

🏗️ Project Structure

PADI-Simple-Chatbot/
│── app_interface.py         # Main chatbot script
│── requirements.txt         # List of dependencies
│── README.md                # Documentation
└── chatbot_env/             # Virtual environment (optional)

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch: git checkout -b feature-branch-name

Commit your changes: git commit -m 'Add new feature'

Push to the branch: git push origin feature-branch-name

Submit a pull request.

📧 Contact

For questions or support, reach out via email at ogunsanya.a.akanbi@gmail.com.
