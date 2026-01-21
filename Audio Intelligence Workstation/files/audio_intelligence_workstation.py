#!/usr/bin/env python3
"""
Audio Intelligence Workstation
A comprehensive tool for transcribing and analyzing audio files with AI-powered insights
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
import argparse

class AudioIntelligenceWorkstation:
    def __init__(self, output_dir="/mnt/user-data/outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session_dir = self.output_dir / f"audio_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self.transcriptions = []
        
    def transcribe_audio(self, audio_file, model="base"):
        """Transcribe a single audio file"""
        audio_path = Path(audio_file)
        if not audio_path.exists():
            print(f"❌ Error: File not found: {audio_file}")
            return None
            
        print(f"\n🎙️  Transcribing: {audio_path.name}")
        print(f"📍 Using model: {model}")
        
        # Run the transcription
        cmd = [
            "python3", "/mnt/skills/user/audio-transcription/scripts/transcribe.py",
            str(audio_path),
            "-o", str(self.session_dir),
            "-f", "both",
            "-m", model
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Transcription complete!")
            
            # Find the generated files
            base_name = audio_path.stem
            txt_file = self.session_dir / f"{base_name}_transcription.txt"
            docx_file = self.session_dir / f"{base_name}_transcription.docx"
            
            transcription_data = {
                "audio_file": audio_path.name,
                "txt_file": txt_file,
                "docx_file": docx_file,
                "model": model,
                "timestamp": datetime.now().isoformat()
            }
            
            # Read the transcription text
            if txt_file.exists():
                with open(txt_file, 'r', encoding='utf-8') as f:
                    transcription_data["text"] = f.read()
            
            self.transcriptions.append(transcription_data)
            return transcription_data
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Transcription failed: {e}")
            print(f"Error output: {e.stderr}")
            return None
    
    def batch_transcribe(self, audio_files, model="base"):
        """Transcribe multiple audio files"""
        print(f"\n{'='*60}")
        print(f"🚀 BATCH TRANSCRIPTION STARTED")
        print(f"{'='*60}")
        print(f"📁 Processing {len(audio_files)} file(s)")
        print(f"💾 Output directory: {self.session_dir}")
        
        results = []
        for i, audio_file in enumerate(audio_files, 1):
            print(f"\n[{i}/{len(audio_files)}]", end=" ")
            result = self.transcribe_audio(audio_file, model)
            if result:
                results.append(result)
        
        print(f"\n{'='*60}")
        print(f"✅ Batch transcription complete: {len(results)}/{len(audio_files)} successful")
        print(f"{'='*60}\n")
        
        return results
    
    def analyze_transcription(self, transcription_data):
        """Analyze a transcription to extract insights"""
        text = transcription_data.get("text", "")
        if not text:
            return None
        
        # Simple analysis (could be enhanced with NLP libraries)
        words = text.split()
        sentences = [s.strip() for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
        
        # Extract potential action items (sentences with key words)
        action_keywords = ['will', 'should', 'need to', 'must', 'todo', 'action', 'task']
        action_items = [s for s in sentences if any(keyword in s.lower() for keyword in action_keywords)]
        
        # Extract questions
        questions = [s + '?' for s in text.split('?')[:-1] if s.strip()]
        
        analysis = {
            "audio_file": transcription_data["audio_file"],
            "word_count": len(words),
            "sentence_count": len(sentences),
            "estimated_duration_minutes": len(words) / 150,  # Average speaking rate
            "action_items": action_items[:10],  # Top 10
            "questions": questions[:10],  # Top 10
            "summary_preview": ' '.join(sentences[:3]) if sentences else "",
        }
        
        return analysis
    
    def generate_meeting_notes(self, transcription_data, analysis):
        """Generate structured meeting notes"""
        text = transcription_data.get("text", "")
        
        notes = f"""# Meeting Notes: {transcription_data['audio_file']}

**Date:** {datetime.fromisoformat(transcription_data['timestamp']).strftime('%B %d, %Y at %I:%M %p')}
**Duration:** ~{analysis['estimated_duration_minutes']:.1f} minutes
**Words:** {analysis['word_count']:,}

## Summary Preview
{analysis['summary_preview']}

## Action Items
"""
        if analysis['action_items']:
            for i, item in enumerate(analysis['action_items'], 1):
                notes += f"{i}. {item}\n"
        else:
            notes += "_No action items detected_\n"
        
        notes += "\n## Questions Raised\n"
        if analysis['questions']:
            for i, q in enumerate(analysis['questions'], 1):
                notes += f"{i}. {q}\n"
        else:
            notes += "_No questions detected_\n"
        
        notes += f"""
## Full Transcription
{text}

---
_Generated by Audio Intelligence Workstation_
"""
        
        # Save meeting notes
        notes_file = self.session_dir / f"{Path(transcription_data['audio_file']).stem}_meeting_notes.md"
        with open(notes_file, 'w', encoding='utf-8') as f:
            f.write(notes)
        
        return notes_file
    
    def generate_html_report(self):
        """Generate a beautiful HTML report with all analyses"""
        if not self.transcriptions:
            print("⚠️  No transcriptions to report")
            return None
        
        # Analyze all transcriptions
        analyses = []
        for trans in self.transcriptions:
            analysis = self.analyze_transcription(trans)
            if analysis:
                analyses.append(analysis)
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audio Intelligence Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        
        .header h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-card .number {{
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
            display: block;
        }}
        
        .stat-card .label {{
            color: #666;
            font-size: 0.9em;
            margin-top: 10px;
        }}
        
        .transcription-card {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .transcription-card h2 {{
            color: #667eea;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .transcription-card h2::before {{
            content: "🎙️";
            font-size: 1.2em;
        }}
        
        .meta-info {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }}
        
        .meta-item {{
            display: flex;
            flex-direction: column;
        }}
        
        .meta-label {{
            color: #666;
            font-size: 0.85em;
            margin-bottom: 5px;
        }}
        
        .meta-value {{
            color: #333;
            font-weight: 600;
        }}
        
        .section {{
            margin-bottom: 25px;
        }}
        
        .section h3 {{
            color: #555;
            margin-bottom: 15px;
            font-size: 1.1em;
        }}
        
        .action-items, .questions {{
            list-style: none;
        }}
        
        .action-items li, .questions li {{
            background: #f8f9fa;
            padding: 12px 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .summary-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
        }}
        
        .badge {{
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Audio Intelligence Report</h1>
            <p class="subtitle">Comprehensive transcription and analysis • Generated {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <span class="number">{len(self.transcriptions)}</span>
                <span class="label">Files Processed</span>
            </div>
            <div class="stat-card">
                <span class="number">{sum(a['word_count'] for a in analyses):,}</span>
                <span class="label">Total Words</span>
            </div>
            <div class="stat-card">
                <span class="number">{sum(a['estimated_duration_minutes'] for a in analyses):.0f}</span>
                <span class="label">Minutes of Audio</span>
            </div>
            <div class="stat-card">
                <span class="number">{sum(len(a['action_items']) for a in analyses)}</span>
                <span class="label">Action Items</span>
            </div>
        </div>
"""
        
        # Add each transcription analysis
        for i, (trans, analysis) in enumerate(zip(self.transcriptions, analyses), 1):
            html += f"""
        <div class="transcription-card">
            <h2>{analysis['audio_file']}<span class="badge">File {i}</span></h2>
            
            <div class="meta-info">
                <div class="meta-item">
                    <span class="meta-label">Words</span>
                    <span class="meta-value">{analysis['word_count']:,}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Sentences</span>
                    <span class="meta-value">{analysis['sentence_count']}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Est. Duration</span>
                    <span class="meta-value">{analysis['estimated_duration_minutes']:.1f} min</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Model</span>
                    <span class="meta-value">{trans['model']}</span>
                </div>
            </div>
            
            <div class="summary-box">
                <h3 style="color: white; margin-bottom: 10px;">✨ Summary Preview</h3>
                <p>{analysis['summary_preview']}</p>
            </div>
            
            <div class="section">
                <h3>📋 Action Items ({len(analysis['action_items'])})</h3>
"""
            if analysis['action_items']:
                html += "<ul class='action-items'>\n"
                for item in analysis['action_items']:
                    html += f"<li>{item}</li>\n"
                html += "</ul>\n"
            else:
                html += "<p style='color: #999;'>No action items detected</p>\n"
            
            html += "</div>\n<div class='section'>\n<h3>❓ Questions Raised ({len(analysis['questions'])})</h3>\n"
            
            if analysis['questions']:
                html += "<ul class='questions'>\n"
                for q in analysis['questions']:
                    html += f"<li>{q}</li>\n"
                html += "</ul>\n"
            else:
                html += "<p style='color: #999;'>No questions detected</p>\n"
            
            html += "</div>\n</div>\n"
        
        html += """
        <div class="footer">
            <p>🤖 Generated by Audio Intelligence Workstation</p>
            <p style="margin-top: 10px; opacity: 0.8;">Powered by OpenAI Whisper & Claude</p>
        </div>
    </div>
</body>
</html>
"""
        
        # Save the report
        report_file = self.session_dir / "audio_intelligence_report.html"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n📊 HTML Report generated: {report_file}")
        return report_file
    
    def run_full_analysis(self, audio_files, model="base"):
        """Complete workflow: transcribe, analyze, and generate reports"""
        print("\n" + "="*60)
        print("🎯 AUDIO INTELLIGENCE WORKSTATION")
        print("="*60)
        
        # Step 1: Batch transcribe
        self.batch_transcribe(audio_files, model)
        
        if not self.transcriptions:
            print("❌ No successful transcriptions. Exiting.")
            return
        
        # Step 2: Generate meeting notes for each
        print("\n📝 Generating meeting notes...")
        for trans in self.transcriptions:
            analysis = self.analyze_transcription(trans)
            if analysis:
                notes_file = self.generate_meeting_notes(trans, analysis)
                print(f"  ✅ {notes_file.name}")
        
        # Step 3: Generate comprehensive HTML report
        print("\n📊 Generating comprehensive HTML report...")
        report_file = self.generate_html_report()
        
        # Step 4: Summary
        print("\n" + "="*60)
        print("✅ ANALYSIS COMPLETE!")
        print("="*60)
        print(f"\n📁 All files saved to: {self.session_dir}")
        print(f"\n📄 Generated files:")
        for trans in self.transcriptions:
            print(f"  • {Path(trans['audio_file']).stem}_transcription.txt")
            print(f"  • {Path(trans['audio_file']).stem}_transcription.docx")
            print(f"  • {Path(trans['audio_file']).stem}_meeting_notes.md")
        print(f"  • audio_intelligence_report.html")
        print(f"\n🌐 Open the HTML report in your browser for a beautiful overview!")
        print("="*60 + "\n")
        
        return self.session_dir


def main():
    parser = argparse.ArgumentParser(
        description="Audio Intelligence Workstation - Transcribe and analyze audio files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s meeting.m4a
  %(prog)s interview.mp3 presentation.m4a -m small
  %(prog)s *.m4a -o ./my_output
        """
    )
    
    parser.add_argument('audio_files', nargs='+', help='Audio file(s) to process')
    parser.add_argument('-m', '--model', default='base',
                       choices=['tiny', 'base', 'small', 'medium', 'large'],
                       help='Whisper model size (default: base)')
    parser.add_argument('-o', '--output-dir', default='/mnt/user-data/outputs',
                       help='Output directory (default: /mnt/user-data/outputs)')
    
    args = parser.parse_args()
    
    # Create workstation
    workstation = AudioIntelligenceWorkstation(output_dir=args.output_dir)
    
    # Run full analysis
    workstation.run_full_analysis(args.audio_files, model=args.model)


if __name__ == "__main__":
    main()
