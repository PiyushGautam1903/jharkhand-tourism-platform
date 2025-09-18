# OpenAI Integration Setup Guide

This guide explains how to set up and configure the OpenAI API for the Jharkhand Tourism Platform chatbot.

## 🚀 Quick Setup

### 1. Get OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Create a new API key
4. Copy the API key (starts with `sk-...`)

### 2. Configure Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` file and replace the placeholder with your actual API key:
   ```env
   OPENAI_API_KEY=sk-your-actual-openai-api-key-here
   ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Test the Integration
1. Run the Django server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to the chatbot (`/chatbot/`)
3. Test with sample messages like:
   - "Hello"
   - "Tell me about places to visit in Jharkhand"
   - "What's the best time to visit Netarhat?"

## 🎯 Features

### Intelligent Chatbot
- **GPT-3.5-turbo** powered responses
- **Tourism-focused context** with comprehensive Jharkhand information
- **Dynamic place integration** from database
- **Error handling** with graceful fallbacks
- **Conversation history** stored in database

### Context Awareness
The AI assistant has detailed knowledge about:
- 🏞️ **Tourism Places**: All 12+ destinations with specific details
- 🎭 **Culture**: Tribal heritage, festivals, art forms
- 🍽️ **Cuisine**: Local dishes and specialties
- 🌤️ **Weather**: Best visiting times and seasonal information
- 🚌 **Transportation**: Airports, railways, road connectivity
- 🛡️ **Safety**: Travel tips and emergency information

### Smart Features
- **Emoji integration** for engaging responses
- **Specific place queries** with detailed information
- **Itinerary suggestions** based on interests
- **Practical travel advice** for tourists
- **Cultural sensitivity** in responses

## 🔧 Configuration Options

### Model Settings (in `main/views.py`)
```python
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",        # AI model to use
    max_tokens=500,               # Maximum response length
    temperature=0.7,              # Creativity level (0-2)
    top_p=1,                      # Nucleus sampling
    frequency_penalty=0,          # Repetition penalty
    presence_penalty=0            # Topic diversity
)
```

### Customizing Tourism Context
Edit `main/tourism_context.py` to:
- Add new tourism information
- Update place details
- Modify response style
- Add seasonal information

## 🛠️ Troubleshooting

### Common Issues

#### 1. "API key not found" Error
- Ensure `.env` file exists in project root
- Check that `OPENAI_API_KEY` is set correctly
- Restart Django server after updating `.env`

#### 2. "Authentication Error"
- Verify your OpenAI API key is valid
- Check if your OpenAI account has credits
- Ensure no extra spaces in the API key

#### 3. "Rate Limit Exceeded"
- You've exceeded OpenAI API limits
- Wait before making more requests
- Consider upgrading your OpenAI plan

#### 4. "Module not found" Error
```bash
pip install openai python-dotenv
```

### Fallback Mode
If OpenAI API is not configured, the chatbot automatically switches to fallback mode with basic responses, ensuring the application continues to function.

## 💰 Cost Management

### Token Usage
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- Average response: 100-300 tokens
- Cost per conversation: ~$0.001

### Optimization Tips
1. **Limit max_tokens** to control response length
2. **Use temperature 0.7** for balanced creativity
3. **Implement conversation limits** per user
4. **Monitor usage** via OpenAI dashboard

## 🔒 Security

### API Key Protection
- ✅ API key stored in environment variables
- ✅ `.env` file in `.gitignore`
- ✅ No hardcoded keys in source code
- ✅ Error handling prevents key exposure

### Best Practices
1. **Never commit** `.env` to version control
2. **Use different keys** for development/production
3. **Rotate keys** regularly
4. **Monitor usage** for unusual activity

## 📊 Monitoring & Analytics

### Usage Tracking
- All conversations saved to `ChatMessage` model
- User message and AI response stored
- Timestamps for analytics
- User association for personalization

### Performance Metrics
Monitor these in production:
- Response time
- Success rate
- Token usage
- User engagement

## 🚀 Advanced Features

### Future Enhancements
- **Multi-language support** (Hindi, tribal languages)
- **Voice integration** with text-to-speech
- **Image understanding** for place photos
- **Real-time weather** API integration
- **Booking integration** for hotels/transport

### Custom Prompts
Modify system prompts for specialized use cases:
- Adventure tourism focus
- Family-friendly recommendations
- Budget travel suggestions
- Cultural tourism emphasis

## 📝 Example Conversations

### Sample Interactions
```
User: "Hello! I'm planning to visit Jharkhand"
AI: "🙏 Welcome to Jharkhand! I'm excited to help you explore the 'Land of Forests'. Are you interested in waterfalls, wildlife, cultural experiences, or spiritual sites?"

User: "Tell me about Hundru Falls"
AI: "🌊 Hundru Falls is absolutely spectacular! It's a 98-meter high waterfall formed by the Subarnarekha River, just 45km from Ranchi..."
```

## 🆘 Support

If you encounter issues:
1. Check this documentation
2. Verify API key setup
3. Test with simple messages first
4. Check Django logs for errors
5. Contact development team

---

**Happy Coding!** 🎉 Your intelligent Jharkhand Tourism Assistant is ready to help visitors discover the beauty of this incredible state!