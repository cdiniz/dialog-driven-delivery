# Feature: Lara - Real-time AI Meeting Assistant

**Date:** November 7, 2025
**Status:** Planning
**Linear Project:** [Lara - Real-time AI Meeting Assistant](https://linear.app/strongheart/project/lara-real-time-ai-meeting-assistant-375e43d0760a)

---

## 1. Feature Overview

### 1.1 Description
Lara is a real-time AI meeting assistant that joins Google Meet sessions as an active participant. Unlike traditional meeting bots that passively record or summarize after the fact, Lara participates in real-time by listening to the conversation, maintaining full meeting context, and providing immediate voice responses when asked questions. Users trigger Lara by saying her name followed by a question, and she responds using LLM knowledge with a professional, natural voice.

This represents a paradigm shift from passive meeting tools to active AI participation, enabling meeting attendees to access AI assistance without leaving the meeting flow or switching contexts.

### 1.2 Business Value
Lara transforms meetings from purely human interactions into AI-augmented collaborative sessions. The key business value includes:

- **Real-time Knowledge Access**: Participants can instantly access AI knowledge without breaking meeting flow or opening external tools
- **Enhanced Decision Making**: Teams can get immediate AI input on questions, suggestions, or alternatives during discussions
- **Improved Meeting Efficiency**: Quick answers reduce the need for follow-up research or additional meetings
- **Natural Integration**: Voice-based interaction feels natural in meeting context, requiring no screen switching or typing
- **Competitive Differentiation**: First-to-market advantage in real-time AI meeting participation vs. passive summarization bots

### 1.3 Target Users
**Primary Persona: Meeting Participants**
- Professionals who attend Google Meet meetings
- Team members who need quick access to information or AI insights during discussions
- Users comfortable with voice interaction and AI assistance
- Knowledge workers in collaborative environments (product teams, engineering, strategy, consulting, etc.)

**User Characteristics:**
- Has Google Meet access
- Can install Chrome extensions
- Comfortable speaking in meetings
- Values real-time AI assistance

### 1.4 Success Criteria
* **User Satisfaction**: Positive qualitative feedback from MVP users indicating Lara adds value to meetings
* **Successful Interactions**: Users are able to ask questions and receive relevant, helpful responses
* **Technical Reliability**: Lara successfully joins meetings, maintains audio connection, and responds when triggered
* **Response Quality**: AI responses are accurate, relevant to meeting context, and professionally delivered

---

## 2. User Workflows

### Workflow 1: Adding Lara to a Meeting
**Actors:** Meeting participant with Chrome extension installed
**Trigger:** User wants AI assistance during an active Google Meet

**Steps:**
1. User joins a Google Meet meeting in Chrome browser
2. User clicks the Lara Chrome extension icon in browser toolbar
3. Extension shows "Send Lara to Meeting" button
4. User clicks button to invite Lara
5. System initiates Lara bot to join the Google Meet session
6. Lara joins the meeting as a visible participant with static avatar
7. User sees Lara in the participant list with her avatar
8. Lara begins listening and transcribing the meeting in real-time
9. User can now interact with Lara during the meeting

**Success Outcome:** Lara is successfully present in the meeting and ready to respond
**Error Scenarios:**
- Extension not detecting active Google Meet tab
- Bot fails to join meeting (connection issues)
- Permission denied to join meeting

### Workflow 2: Asking Lara a Question
**Actors:** Meeting participant, Lara (AI assistant)
**Trigger:** User needs information or AI input during meeting discussion

**Steps:**
1. User speaks clearly during the meeting: "Lara, [question]" (e.g., "Lara, what are the best practices for API versioning?")
2. Lara's voice activation detects the trigger word "Lara"
3. System captures the question from speech-to-text
4. System packages full meeting transcript context + question
5. System sends context and question to LLM provider (Anthropic API)
6. System receives LLM response (streaming or complete)
7. System converts text response to speech (TTS provider)
8. Lara speaks the response in the meeting with professional tone
9. All meeting participants hear Lara's voice response
10. User receives answer and can continue meeting discussion

**Success Outcome:** User receives relevant, helpful answer from Lara in natural voice
**Error Scenarios:**
- Audio quality too poor to detect trigger or question
- LLM provider timeout or failure
- TTS conversion fails
- Multiple people say "Lara" simultaneously

### Workflow 3: Lara Responding with "Let Me Think"
**Actors:** Meeting participant, Lara (AI assistant)
**Trigger:** Lara needs to mask processing latency for complex questions

**Steps:**
1. User asks Lara a question (following Workflow 2 steps 1-5)
2. System detects processing will take noticeable time (>2 seconds estimated)
3. Lara immediately responds with verbal acknowledgment: "Let me think..." or "That's a good question..." or similar variation
4. System continues processing LLM request in background
5. System receives LLM response and converts to speech
6. Lara provides the complete answer
7. User perceives continuous engagement rather than awkward silence

**Success Outcome:** Latency is masked with natural verbal acknowledgment, maintaining meeting flow
**Error Scenarios:**
- Acknowledgment becomes repetitive or annoying with frequent questions
- Processing time exceeds reasonable wait (>10 seconds)

### Workflow 4: Meeting Continuation with Lara Present
**Actors:** Meeting participants, Lara (AI assistant)
**Trigger:** Ongoing meeting with Lara already present

**Steps:**
1. Meeting participants have normal discussion
2. Lara continuously listens and transcribes all speech
3. Lara maintains full meeting context in memory
4. Participants ask Lara questions as needed (invoking Workflow 2)
5. Lara's responses reference meeting context when relevant
6. Participants continue meeting with AI assistance available
7. Meeting ends naturally when participants leave
8. Lara disconnects when meeting ends or when manually removed

**Success Outcome:** Seamless meeting experience with AI assistance available on-demand
**Error Scenarios:**
- Lara accidentally triggers on similar-sounding words
- Connection drops and Lara loses context
- Meeting context becomes too large to process efficiently

---

## 3. Functional Requirements

### 3.1 Core Functionality
* **FR1:** Chrome extension must detect active Google Meet sessions and provide UI to send Lara to meeting
* **FR2:** Lara bot must join Google Meet as a real participant visible to all attendees with static avatar image
* **FR3:** Lara must continuously capture and transcribe all meeting audio in real-time using STT provider
* **FR4:** Lara must maintain complete meeting transcript context from join time until meeting end
* **FR5:** Lara must detect trigger phrase "Lara" followed by user question from meeting audio
* **FR6:** Lara must send meeting context + question to LLM provider and receive response
* **FR7:** Lara must convert LLM text response to natural speech using TTS provider
* **FR8:** Lara must play voice response in meeting so all participants can hear
* **FR9:** Lara must use professional tone in all voice responses
* **FR10:** Lara must not respond to interruptions once speaking - completes full response
* **FR11:** System must handle errors gracefully (ignore and continue) without crashing or leaving meeting

### 3.2 Input Requirements
* **Input 1:** Google Meet URL/Session - Valid active Google Meet meeting URL from Chrome extension
* **Input 2:** Voice Trigger - Clear audio containing "Lara [question]" detected from meeting audio stream
* **Input 3:** Meeting Audio Stream - Continuous audio from all meeting participants for transcription
* **Input 4:** User Action - Click on "Send Lara to Meeting" button in Chrome extension

### 3.3 Output Requirements
* **Output 1:** Visual Presence - Static avatar image visible in Google Meet participant grid
* **Output 2:** Voice Response - Natural speech audio output in meeting audio stream, audible to all participants
* **Output 3:** Extension UI - Simple interface showing Lara status (not in meeting, joining, in meeting)

### 3.4 Business Rules
* **BR1:** Lara only responds when explicitly triggered with name "Lara" - does not respond to general conversation
* **BR2:** Lara uses only LLM knowledge - no access to company data, documents, or external systems
* **BR3:** Lara maintains full meeting context from join time - does not have access to conversation before joining
* **BR4:** Lara completes full response without interruption - cannot be stopped mid-response
* **BR5:** One Lara instance per meeting - extension prevents sending multiple Lara bots to same meeting
* **BR6:** Lara provides only LLM-based answers - if question requires external data, states limitation professionally
* **BR7:** Manual invitation only for MVP - no automatic joining or scheduled presence

### 3.5 Validation Rules
* **VR1:** Meeting URL - Must be valid Google Meet URL format (meet.google.com/*), error: "Invalid Google Meet URL"
* **VR2:** Trigger Detection - Must clearly detect "Lara" keyword before question, ignore if unclear
* **VR3:** Audio Quality - If transcription confidence below threshold, ignore rather than misinterpret
* **VR4:** Extension Installation - Must verify Chrome extension installed and active, error: "Please install Lara extension"

### 3.6 Data Requirements
* **DR1:** Meeting Transcript - Complete real-time transcript of all speech from meeting start (when Lara joins) with speaker timestamps
* **DR2:** Avatar Image - Static image file for Lara's visual presence in meeting participant grid
* **DR3:** System Prompt - Predefined prompt context defining Lara's role, behavior, and response style
* **DR4:** LLM API Credentials - Valid API keys for Anthropic (or configured LLM provider)
* **DR5:** STT/TTS API Credentials - Valid credentials for speech-to-text and text-to-speech providers

---

## 4. Non-Functional Requirements

### 4.1 Performance
* Response latency should be minimized - target under 5 seconds from trigger to voice response start
* Transcription should occur in real-time with minimal lag (< 2 seconds behind live audio)
* Voice responses should sound natural without robotic delays or unnatural pauses
* Extension should detect active Google Meet tabs instantly (< 500ms)
* "Let me think" acknowledgment should play within 1 second of trigger detection

### 4.2 Security
* All data processing occurs locally - no persistent storage of meeting content
* API calls to external providers (LLM, STT, TTS) use secure HTTPS connections
* No recording or retention of meeting transcripts after meeting ends
* Chrome extension follows Chrome Web Store security policies
* API credentials stored securely in extension storage (encrypted)
* No user authentication required for MVP (manual invite model)

### 4.3 Accessibility
* Voice trigger "Lara" must work with various accents and speaking styles
* Visual avatar must be clearly visible in participant grid
* Voice output must be clear and audible at normal meeting volume levels
* Extension UI must be simple enough for non-technical users

### 4.4 Usability
* Chrome extension should have minimal, intuitive UI (one-button operation)
* Error states should fail silently from meeting perspective (participants don't hear errors)
* Lara's voice should be distinguishable from human participants
* Professional tone should match corporate meeting environment
* Responses should be concise and relevant to questions asked
* Extension should clearly indicate when Lara is active in a meeting

### 4.5 Scalability
* MVP has no limits on meeting size or duration
* System should handle meetings with 2-50 participants without degradation
* Transcript context should efficiently handle meetings up to 2 hours without performance issues
* Single Lara instance can serve multiple sequential meetings per user

### 4.6 Internationalization (if applicable)
* MVP is English-only for voice trigger detection, transcription, and TTS
* Future: Multi-language support out of scope for MVP

---

## 5. Dependencies & Constraints

### 5.1 Technical Dependencies
* **Chrome Browser**: Users must use Google Chrome to access extension and Google Meet
* **Google Meet Platform**: Requires Google Meet APIs/methods to join as bot participant
* **STT Provider**: Requires third-party speech-to-text service (e.g., Deepgram, AssemblyAI, Google Speech-to-Text)
* **LLM Provider**: Requires Anthropic API (or alternative LLM provider) for question answering
* **TTS Provider**: Requires text-to-speech service (e.g., ElevenLabs, Google TTS, Azure Speech) for voice generation
* **Real-time Audio Access**: Requires ability to capture meeting audio stream and inject audio into meeting

### 5.2 External Dependencies
* **Anthropic Claude API**: For LLM responses (or configured alternative)
* **Speech-to-Text API**: For real-time transcription
* **Text-to-Speech API**: For voice generation
* **Google Meet Infrastructure**: Platform stability and API availability
* **Internet Connectivity**: Stable connection required for all API calls

### 5.3 Technical Constraints
* **Google Meet Bot Participation**: May require Google Workspace Enterprise for bot to join as real participant (noted as uncertainty in meeting)
* **Browser Extension Limitations**: Chrome extension capabilities for accessing Meet audio streams
* **Audio Processing**: Local processing capability for real-time audio capture and playback
* **API Rate Limits**: Subject to rate limits of LLM, STT, and TTS providers
* **Latency**: Total processing latency depends on STT, LLM, and TTS response times

### 5.4 Business Constraints
* **MVP Scope**: Must focus on core functionality only - no additional features beyond voice Q&A
* **Manual Process**: User must manually invite Lara per meeting (no automation)
* **Platform Limitation**: Google Meet only - no Zoom, Teams, or other platforms
* **No Persistence**: No data retention or meeting history features

### 5.5 Compliance Requirements
* **Data Privacy**: Meeting content processed locally only, no storage or retention
* **User Consent**: Meeting participants should be aware Lara is present (visible participant)
* **API Provider Terms**: Must comply with terms of service for LLM, STT, and TTS providers
* **Chrome Web Store Policies**: Extension must meet Chrome Web Store requirements for publication

---

## 6. Scope Boundaries

### 6.1 In Scope
* Chrome extension for Google Meet integration
* Real-time meeting audio transcription
* Voice trigger detection ("Lara" keyword)
* LLM-based question answering using meeting context
* Text-to-speech voice responses
* Professional tone and response style
* Static avatar visual presence in meeting
* "Let me think" latency masking
* Graceful error handling (ignore and continue)
* Local data processing with no retention
* Single Lara instance per meeting

### 6.2 Out of Scope
* **Other Meeting Platforms**: Zoom, Microsoft Teams, Slack Huddles, etc. (Google Meet only)
* **Post-Meeting Features**: Summaries, transcripts, action items, recordings
* **Multi-Language Support**: Non-English languages for trigger, transcription, or responses
* **Company Data Integration**: No access to internal documents, databases, or systems
* **User Configuration**: No settings for voice type, personality, response style, or behavior
* **Scheduling/Automation**: No automatic joining, scheduled presence, or calendar integration
* **Meeting Management**: No ability to mute/unmute Lara, adjust settings during meeting
* **Interruption Handling**: Cannot interrupt or stop Lara mid-response
* **User Authentication**: No login, user accounts, or permission systems
* **Analytics/Tracking**: No usage metrics, logging, or analytics
* **Multiple Bot Instances**: No support for multiple Lara bots in same meeting
* **Pre-Meeting Context**: Lara only knows conversation after joining, not before

### 6.3 Future Considerations
* Support for other video conferencing platforms (Zoom, Teams)
* Post-meeting summaries and action item extraction
* Multi-language support for global teams
* Integration with company knowledge bases and documentation
* User preferences and customization options
* Meeting scheduling and automatic joining
* Advanced features like proactive suggestions, meeting facilitation
* Analytics on Lara usage and effectiveness
* Mobile app support
* API for third-party integrations

---

## 7. Open Questions

Track unresolved questions that need answers before or during implementation:

- [ ] **Q1:** Can we achieve real participant status in Google Meet without Google Workspace Enterprise?
  - **Owner:** Engineering/Tech Lead
  - **Deadline:** Before technical design phase
  - **Note:** Meeting transcript mentioned this might be required - needs verification

- [ ] **Q2:** What specific STT provider should we use for real-time transcription?
  - **Owner:** Engineering/Tech Lead
  - **Deadline:** During technical design
  - **Options:** Deepgram, AssemblyAI, Google Speech-to-Text, others

- [ ] **Q3:** What specific TTS provider should we use for voice generation?
  - **Owner:** Engineering/Tech Lead
  - **Deadline:** During technical design
  - **Options:** ElevenLabs, Google TTS, Azure Speech, others

- [ ] **Q4:** Should we use streaming responses from LLM or wait for complete response?
  - **Owner:** Engineering/Tech Lead
  - **Deadline:** During technical design
  - **Note:** Streaming could reduce latency but adds complexity

- [ ] **Q5:** How do we determine when to use "let me think" vs. silent waiting?
  - **Owner:** Product/Engineering
  - **Deadline:** During implementation
  - **Note:** Need heuristic for expected processing time

- [ ] **Q6:** What variations should we use for "let me think" acknowledgments?
  - **Owner:** Product/UX
  - **Deadline:** Before implementation
  - **Examples:** "Let me think...", "That's a good question...", "Hmm...", etc.

- [ ] **Q7:** How do we handle the static avatar image - user-provided or default?
  - **Owner:** Product/Design
  - **Deadline:** During implementation
  - **Note:** MVP uses static image - what should it look like?

- [ ] **Q8:** Should there be any visual indicator in extension when Lara is processing a question?
  - **Owner:** Product/UX
  - **Deadline:** During implementation

- [ ] **Q9:** How do we handle meeting context that exceeds LLM token limits (very long meetings)?
  - **Owner:** Engineering
  - **Deadline:** During technical design
  - **Options:** Truncate, summarize, sliding window

- [ ] **Q10:** What is the fallback behavior if LLM, STT, or TTS providers are unavailable?
  - **Owner:** Engineering
  - **Deadline:** During technical design
  - **Note:** Requirement is "ignore and continue" but what does user experience?

---

## 8. Risks & Mitigations

### Risk 1: Google Meet Bot Access Requirements
**Probability:** High
**Impact:** High
**Mitigation Strategy:**
- Immediately research Google Meet bot participation requirements
- Identify if Google Workspace Enterprise is mandatory
- If required, determine cost and procurement process
- Have fallback plan for sidecar approach if real participant status not possible
- Prototype bot joining early in development to validate approach

### Risk 2: Latency Too High for Natural Interaction
**Probability:** Medium
**Impact:** High
**Mitigation Strategy:**
- Set clear latency targets (< 5 seconds total)
- Implement streaming responses from LLM to TTS
- Use "let me think" acknowledgments strategically
- Optimize provider selection for speed
- Consider caching common questions or responses
- Test with real meetings early and iterate

### Risk 3: Voice Trigger False Positives/Negatives
**Probability:** Medium
**Impact:** Medium
**Mitigation Strategy:**
- Use high-quality STT with good accuracy
- Test trigger detection with various accents and audio qualities
- Implement confidence threshold for trigger detection
- Consider phonetic variations of "Lara"
- Allow for slight mispronunciations
- Test in real meeting environments with background noise

### Risk 4: API Provider Costs Exceed Budget
**Probability:** Medium
**Impact:** Medium
**Mitigation Strategy:**
- Estimate costs based on expected usage (meeting length, frequency)
- Monitor API usage and costs closely during MVP
- Set rate limits or usage caps if needed
- Evaluate provider pricing models and optimize selection
- Consider cost as factor in provider selection

### Risk 5: Poor Audio Quality Impacts Transcription
**Probability:** Medium
**Impact:** Medium
**Mitigation Strategy:**
- Test with various audio quality scenarios
- Implement confidence-based filtering (ignore unclear audio)
- Select STT provider with good noise handling
- Consider audio preprocessing/enhancement
- Set user expectations about audio quality requirements

### Risk 6: Multiple External Provider Dependencies Create Reliability Issues
**Probability:** Medium
**Impact:** High
**Mitigation Strategy:**
- Implement robust error handling for each provider
- Add retry logic with exponential backoff
- Consider provider redundancy (backup providers)
- Monitor provider uptime and SLAs
- Graceful degradation when services unavailable
- Clear error communication to users

### Risk 7: Meeting Context Becomes Too Large for LLM
**Probability:** Medium
**Impact:** Medium
**Mitigation Strategy:**
- Implement context window management (sliding window or summarization)
- Monitor token usage per request
- Optimize context by removing redundant information
- Consider different strategies for short vs. long meetings
- Test with 2+ hour meetings to validate approach

### Risk 8: Chrome Extension Approval/Distribution
**Probability:** Low
**Impact:** Medium
**Mitigation Strategy:**
- Review Chrome Web Store policies early
- Ensure extension meets all security requirements
- Plan for review time in project timeline
- Have alternative distribution method if needed (enterprise deployment)

---

## 9. References

- **Meeting Transcript:** November 5, 2025, 15:45 WET - Feature planning discussion with Claudio Diniz and Pedro Sousa
- **Linear Project:** [Lara - Real-time AI Meeting Assistant](https://linear.app/strongheart/project/lara-real-time-ai-meeting-assistant-375e43d0760a)

---

## 10. Appendix

### Meeting Notes Summary

**Key Discussion Points from November 5, 2025 Meeting:**

1. **Product Vision**: A bot that joins meetings and participates in real-time, different from passive summarization bots like Otter.ai or Fireflies.ai

2. **Active Participation**: Lara listens with full meeting context and responds with voice when triggered, creating a new paradigm of AI meeting participation

3. **Naming**: Decided on "Lara" (inspired by Lara Croft) as the product name

4. **Trigger Mechanism**: MVP will use explicit trigger - users say "Lara [question]" to invoke response

5. **Technical Approach**:
   - Real-time transcription for meeting context
   - LLM provider (Anthropic API mentioned) for answering questions
   - Text-to-speech for voice responses
   - Streaming considered for reducing latency

6. **Latency Masking**: Innovative "let me think" approach to mask processing delays with natural verbal acknowledgments

7. **Meeting Platform**: Google Meet for MVP, with awareness that bot participant status might require Google Enterprise

8. **Real Participant**: Lara joins as visible participant with avatar, not a sidecar app - participants can see and hear Lara in the meeting

### Assumptions

1. Users have Google Meet access and can create/join meetings
2. Chrome is the primary browser for Google Meet users
3. Users are comfortable with AI assistance and voice interaction
4. Meeting participants consent to Lara's presence (visible participant)
5. Professional tone is appropriate for target user base (knowledge workers)
6. LLM knowledge alone provides sufficient value without company data integration for MVP
7. Manual invitation process is acceptable for MVP validation
8. English-only support is sufficient for initial user base

### Glossary

- **STT**: Speech-to-Text - technology that converts spoken audio to written text
- **TTS**: Text-to-Speech - technology that converts written text to spoken audio
- **LLM**: Large Language Model - AI model capable of understanding and generating natural language (e.g., Claude, GPT)
- **MVP**: Minimum Viable Product - initial version with core features for user validation
- **Real-time Transcription**: Converting speech to text with minimal delay as conversation happens
- **Streaming Response**: Receiving LLM output progressively as it's generated rather than waiting for complete response
- **Trigger Word**: Specific word or phrase that activates voice assistant ("Lara" in this case)
- **Meeting Context**: Complete transcript and understanding of conversation flow in the meeting
- **Sidecar App**: Application that runs alongside another app but doesn't participate directly (contrast with Lara's real participant approach)
- **Latency Masking**: Technique of using acknowledgments or sounds to make processing delays feel more natural
- **Avatar**: Visual representation of Lara in the meeting participant grid
