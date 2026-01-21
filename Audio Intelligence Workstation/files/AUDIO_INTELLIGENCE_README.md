# 🎙️ Audio Intelligence Workstation

A comprehensive, AI-powered audio transcription and analysis system that transforms your audio files into actionable insights.

## ✨ Features

### 🎯 Core Capabilities
- **Batch Transcription** - Process multiple audio files simultaneously
- **Multiple Output Formats** - Get plain text (.txt) and formatted Word documents (.docx)
- **AI-Powered Analysis** - Automatic extraction of insights from transcriptions
- **Beautiful HTML Reports** - Professional, interactive reports with full analytics
- **Meeting Notes Generation** - Structured meeting notes with action items and questions
- **Flexible Model Selection** - Choose between speed and accuracy

### 📊 Intelligence Features
- **Action Item Detection** - Automatically finds tasks and to-dos
- **Question Extraction** - Identifies all questions raised
- **Summary Generation** - Creates concise previews of content
- **Statistics Dashboard** - Word counts, duration estimates, sentence analysis
- **Visual Analytics** - Color-coded, interactive HTML reports

## 🚀 Quick Start

### Basic Usage

Transcribe a single file:
```bash
python3 audio_intelligence_workstation.py meeting.m4a
```

### Batch Processing

Transcribe multiple files:
```bash
python3 audio_intelligence_workstation.py meeting1.m4a interview.mp3 lecture.wav
```

Or use wildcards:
```bash
python3 audio_intelligence_workstation.py *.m4a
```

### Advanced Options

Higher accuracy with the 'small' model:
```bash
python3 audio_intelligence_workstation.py meeting.m4a -m small
```

Custom output directory:
```bash
python3 audio_intelligence_workstation.py meeting.m4a -o /path/to/output
```

Fast processing with 'tiny' model:
```bash
python3 audio_intelligence_workstation.py long_lecture.m4a -m tiny
```

## 📁 Output Files

For each audio file processed, you'll get:

1. **`filename_transcription.txt`** - Plain text transcription
2. **`filename_transcription.docx`** - Formatted Word document with timestamps
3. **`filename_meeting_notes.md`** - Structured meeting notes with:
   - Summary preview
   - Action items list
   - Questions raised
   - Full transcription
4. **`audio_intelligence_report.html`** - Beautiful comprehensive report with:
   - Overall statistics dashboard
   - Per-file detailed analysis
   - Interactive, color-coded interface
   - Exportable format

## 🎨 HTML Report Features

The generated HTML report includes:

- **📊 Statistics Dashboard**
  - Total files processed
  - Total word count across all files
  - Total audio duration
  - Total action items detected

- **🎙️ Per-File Analysis Cards**
  - File metadata (words, sentences, duration, model used)
  - Summary preview
  - Action items list
  - Questions raised

- **✨ Beautiful Design**
  - Responsive layout
  - Gradient backgrounds
  - Hover effects
  - Professional typography
  - Print-friendly format

## 🔧 Model Selection Guide

| Model  | Speed      | Accuracy | Best For |
|--------|------------|----------|----------|
| tiny   | Fastest    | Good     | Long files (>1hr), quick drafts |
| base   | Fast       | Better   | **Default** - balanced performance |
| small  | Moderate   | High     | Important meetings, interviews |
| medium | Slow       | Higher   | Professional recordings |
| large  | Slowest    | Highest  | Critical accuracy needed |

💡 **Tip**: Start with `base` - it's fast and accurate for most use cases.

## 📋 Command-Line Options

```
usage: audio_intelligence_workstation.py [-h] [-m {tiny,base,small,medium,large}] 
                                          [-o OUTPUT_DIR] 
                                          audio_files [audio_files ...]

Arguments:
  audio_files              Audio file(s) to process (.m4a, .mp3, .wav, etc.)

Options:
  -h, --help              Show this help message
  -m, --model MODEL       Whisper model: tiny, base, small, medium, large
                          (default: base)
  -o, --output-dir DIR    Output directory (default: /mnt/user-data/outputs)
```

## 🎯 Use Cases

### 📞 Meeting Recording
```bash
python3 audio_intelligence_workstation.py team_meeting.m4a
```
Get transcription + automatically extracted action items + meeting notes

### 🎓 Lecture Notes
```bash
python3 audio_intelligence_workstation.py lecture.m4a -m small
```
High-accuracy transcription for academic content

### 🎤 Interview Analysis
```bash
python3 audio_intelligence_workstation.py interview1.m4a interview2.m4a interview3.m4a
```
Batch process multiple interviews with comprehensive report

### 📱 Voice Memo Processing
```bash
python3 audio_intelligence_workstation.py voice_*.m4a -m tiny
```
Quickly process multiple voice memos

## 💡 Pro Tips

1. **For clear speech (meetings, podcasts)**: Use `base` or `small` model
2. **For long files (>1 hour)**: Use `tiny` or `base` to save time
3. **For poor audio quality**: Try `small` or `medium` model
4. **For multiple files**: Batch process them together - you'll get a combined report
5. **Timestamps needed**: Check the Word document (.docx) - it has timestamped segments
6. **Want summaries**: Look at the meeting notes (.md) or HTML report

## 🎬 Example Workflow

1. Record your meeting/interview/lecture
2. Run the workstation:
   ```bash
   python3 audio_intelligence_workstation.py my_audio.m4a
   ```
3. Get notified when complete
4. Open the HTML report in your browser
5. Review action items and questions
6. Share the Word document with your team
7. Keep meeting notes for reference

## 📊 What You Get

```
📁 audio_session_20250119_143022/
├── 📄 meeting_transcription.txt          # Plain text
├── 📄 meeting_transcription.docx         # Formatted Word doc
├── 📄 meeting_meeting_notes.md           # Structured notes
├── 📊 audio_intelligence_report.html     # Beautiful report
└── [additional files for each input audio file]
```

## 🌟 Example Output

The HTML report will show something like:

```
📊 Audio Intelligence Report
════════════════════════════════════════

[Statistics Dashboard]
3 Files     2,847 Words     19 Minutes     12 Action Items

[File: team_meeting.m4a]
Words: 1,234 | Sentences: 87 | Duration: 8.2 min
✨ Summary: Discussion about Q1 goals and new project timeline...

📋 Action Items (4)
1. John will prepare the budget proposal by Friday
2. Team should review the design mockups before Monday
3. Need to schedule follow-up meeting with stakeholders
4. Marketing needs to draft social media campaign

❓ Questions Raised (2)
1. What's the deadline for the final deliverable?
2. Do we have budget approval for additional resources?
```

## 🔍 Supported Audio Formats

- **Audio**: MP3, M4A, WAV, FLAC, OGG, OPUS
- **Video** (audio extraction): MP4, AVI, MKV, MOV

## ⚙️ Requirements

The workstation uses your existing `audio-transcription` skill, which requires:
- Python 3.7+
- openai-whisper
- python-docx
- ffmpeg

These should already be installed with your skill. If not, run:
```bash
bash /mnt/skills/user/audio-transcription/scripts/setup.sh
```

## 🎓 Learning Resources

- First time using? Try with a single short file first
- Check the meeting notes (.md) to see the structure
- Open the HTML report in your browser - it's interactive!
- The Word document has timestamped segments for easy reference

## 🚀 Advanced Features

### Programmatic Usage

You can also use the workstation as a Python library:

```python
from audio_intelligence_workstation import AudioIntelligenceWorkstation

# Create workstation
workstation = AudioIntelligenceWorkstation(output_dir="./my_output")

# Run full analysis
workstation.run_full_analysis(
    audio_files=["meeting.m4a", "interview.mp3"],
    model="small"
)
```

### Individual Components

```python
# Just transcribe
workstation.transcribe_audio("meeting.m4a", model="base")

# Just analyze
analysis = workstation.analyze_transcription(transcription_data)

# Just generate report
workstation.generate_html_report()
```

## 📝 Notes

- Models download on first use (requires internet)
- Processing time depends on file length and model size
- Output files are saved to a timestamped session directory
- All files are kept together for easy access and sharing

## 🎉 Enjoy Your Audio Intelligence!

Transform your audio files into organized, actionable insights with just one command!

---
**Powered by OpenAI Whisper & Claude • Built with ❤️ for productivity**
