# AI Chatbot Collection 🤖

A collection of interactive AI chatbot applications built with Google's Gemini API and Streamlit. This project includes multiple chatbot implementations with different features and interfaces.

## 🚀 Features

- **Multiple Chatbot Interfaces**: Different implementations with varying UI/UX approaches
- **Google Gemini AI Integration**: Powered by Google's advanced AI model
- **Streamlit Web Interface**: Modern, responsive web applications
- **Chat History**: Persistent conversation memory
- **Interactive Elements**: Pills, buttons, and chat inputs for enhanced user experience

## 📁 Project Structure

```
chatttttt bot intern/
├── eee.py          # Basic Q&A chatbot with chat history
├── hellow.py       # Number guessing game
├── hihi.py         # Advanced chat interface with role management
└── teco.py         # Interactive chatbot with pills selection
```

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hira299/ai-chatbot-collection.git
   cd ai-chatbot-collection
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit
google-generativeai
python-dotenv
streamlit-pills
```

## 🎮 Usage

### Running the Chatbots

1. **Basic Q&A Chatbot (eee.py)**
   ```bash
   streamlit run "chatttttt bot intern/eee.py"
   ```

2. **Number Guessing Game (hellow.py)**
   ```bash
   python "chatttttt bot intern/hellow.py"
   ```

3. **Advanced Chat Interface (hihi.py)**
   ```bash
   streamlit run "chatttttt bot intern/hihi.py"
   ```

4. **Interactive Chatbot with Pills (teco.py)**
   ```bash
   streamlit run "chatttttt bot intern/teco.py"
   ```

## 🔧 Configuration

### API Key Setup

1. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Replace the API keys in the respective files or use environment variables
3. For security, it's recommended to use environment variables instead of hardcoding API keys

### Environment Variables

Create a `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
```

## 🎯 Features by File

### eee.py
- Basic Q&A interface
- Chat history persistence
- Simple text input and response display

### hellow.py
- Number guessing game (1-100)
- 3 attempts limit
- Console-based interface

### hihi.py
- Advanced chat interface
- Role-based message display
- Persistent chat history
- Modern Streamlit chat UI

### teco.py
- Interactive pills selection
- Pre-defined conversation starters
- Enhanced user experience with icons
- Chat history management

## 🚨 Security Notes

⚠️ **Important**: The current implementation has API keys hardcoded in the files. For production use:

1. Use environment variables
2. Never commit API keys to version control
3. Add `.env` to your `.gitignore` file

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hiro47** - [GitHub Profile](https://github.com/hira299)

## 🙏 Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Streamlit for the web framework
- The open-source community for various libraries and tools

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the author.

---

**Note**: This project is for educational and demonstration purposes. Make sure to comply with Google's API usage terms and conditions. 