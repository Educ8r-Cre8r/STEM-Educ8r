#!/usr/bin/env python3
"""
Audio Intelligence Workstation - Interactive Launcher
Easy-to-use menu system for all features
"""

import os
import sys
import subprocess
from pathlib import Path

class InteractiveLauncher:
    def __init__(self):
        self.workstation_script = "audio_intelligence_workstation.py"
        self.demo_script = "demo_guide.py"
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        """Print the main banner"""
        print("\n" + "="*70)
        print("""
    🎙️  AUDIO INTELLIGENCE WORKSTATION
    ═══════════════════════════════════════════════════════════════
    
    Transform audio into actionable intelligence with AI
    Powered by OpenAI Whisper & Claude
        """)
        print("="*70 + "\n")
    
    def print_menu(self):
        """Print the main menu"""
        print("\n📋 MAIN MENU")
        print("─" * 70)
        print()
        print("  1️⃣  Quick Start - Transcribe a single file (recommended)")
        print("  2️⃣  Batch Processing - Transcribe multiple files")
        print("  3️⃣  Custom Options - Advanced settings")
        print()
        print("  📚 Learn & Explore")
        print("  4️⃣  View Interactive Demo Guide")
        print("  5️⃣  Open Visual Workflow (HTML)")
        print("  6️⃣  Read Full Documentation")
        print()
        print("  🔧 Utilities")
        print("  7️⃣  Check System Requirements")
        print("  8️⃣  View Recent Outputs")
        print()
        print("  0️⃣  Exit")
        print()
        print("─" * 70)
    
    def get_choice(self):
        """Get user menu choice"""
        while True:
            choice = input("\n👉 Enter your choice (0-8): ").strip()
            if choice in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                return choice
            print("❌ Invalid choice. Please enter a number between 0-8.")
    
    def get_audio_file(self):
        """Get audio file path from user"""
        print("\n📁 Audio File Selection")
        print("─" * 70)
        print("\nEnter the path to your audio file:")
        print("  • You can drag and drop the file here")
        print("  • Or type the full path")
        print("  • Supported: .m4a, .mp3, .wav, .flac, .ogg, .mp4, etc.")
        print()
        
        while True:
            file_path = input("File path: ").strip().strip('"').strip("'")
            
            if not file_path:
                print("❌ No file path provided. Please try again.")
                continue
            
            path = Path(file_path)
            if path.exists():
                return str(path)
            else:
                print(f"❌ File not found: {file_path}")
                retry = input("Try again? (y/n): ").strip().lower()
                if retry != 'y':
                    return None
    
    def get_multiple_files(self):
        """Get multiple audio file paths"""
        print("\n📁 Multiple File Selection")
        print("─" * 70)
        print("\nEnter audio file paths (one per line)")
        print("  • Press Enter after each file path")
        print("  • Type 'done' when finished")
        print("  • Type 'cancel' to go back")
        print()
        
        files = []
        while True:
            file_path = input(f"File {len(files) + 1} (or 'done'/'cancel'): ").strip().strip('"').strip("'")
            
            if file_path.lower() == 'done':
                if files:
                    return files
                else:
                    print("❌ No files added. Please add at least one file.")
                    continue
            
            if file_path.lower() == 'cancel':
                return None
            
            path = Path(file_path)
            if path.exists():
                files.append(str(path))
                print(f"  ✅ Added: {path.name}")
            else:
                print(f"  ❌ File not found: {file_path}")
    
    def select_model(self):
        """Let user select transcription model"""
        print("\n🎯 Model Selection")
        print("─" * 70)
        print()
        print("  1. tiny   - ⚡⚡⚡⚡⚡ Fastest (good for long files >1hr)")
        print("  2. base   - ⚡⚡⚡⚡   Balanced (DEFAULT, recommended)")
        print("  3. small  - ⚡⚡⚡     High accuracy (important content)")
        print("  4. medium - ⚡⚡      Higher accuracy (professional)")
        print("  5. large  - ⚡       Highest accuracy (critical content)")
        print()
        
        models = {
            '1': 'tiny',
            '2': 'base',
            '3': 'small',
            '4': 'medium',
            '5': 'large'
        }
        
        choice = input("Select model (1-5, default=2): ").strip()
        return models.get(choice, 'base')
    
    def get_output_dir(self):
        """Get custom output directory"""
        print("\n📂 Output Directory")
        print("─" * 70)
        print()
        default_dir = "/mnt/user-data/outputs"
        print(f"Default: {default_dir}")
        print()
        custom = input("Enter custom directory (or press Enter for default): ").strip()
        return custom if custom else default_dir
    
    def run_transcription(self, files, model='base', output_dir=None):
        """Run the transcription workstation"""
        cmd = ['python3', self.workstation_script] + files + ['-m', model]
        
        if output_dir:
            cmd.extend(['-o', output_dir])
        
        print("\n" + "="*70)
        print("🚀 STARTING TRANSCRIPTION")
        print("="*70)
        print(f"\nCommand: {' '.join(cmd)}\n")
        
        try:
            subprocess.run(cmd, check=True)
            print("\n✅ Transcription completed successfully!")
            input("\nPress Enter to continue...")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error during transcription: {e}")
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\n\n⚠️  Transcription cancelled by user.")
            input("\nPress Enter to continue...")
    
    def quick_start(self):
        """Quick start workflow"""
        self.clear_screen()
        self.print_banner()
        print("\n🚀 QUICK START")
        print("="*70)
        
        file_path = self.get_audio_file()
        if not file_path:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
            return
        
        print(f"\n✅ Selected file: {Path(file_path).name}")
        print("📊 Using default model: base (fast and accurate)")
        print("📁 Using default output directory")
        
        confirm = input("\nProceed with transcription? (y/n): ").strip().lower()
        if confirm == 'y':
            self.run_transcription([file_path])
        else:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
    
    def batch_processing(self):
        """Batch processing workflow"""
        self.clear_screen()
        self.print_banner()
        print("\n📦 BATCH PROCESSING")
        print("="*70)
        
        files = self.get_multiple_files()
        if not files:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
            return
        
        print(f"\n✅ Selected {len(files)} file(s):")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {Path(f).name}")
        
        model = self.select_model()
        print(f"\n✅ Using model: {model}")
        
        confirm = input("\nProceed with batch transcription? (y/n): ").strip().lower()
        if confirm == 'y':
            self.run_transcription(files, model=model)
        else:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
    
    def custom_options(self):
        """Custom options workflow"""
        self.clear_screen()
        self.print_banner()
        print("\n⚙️  CUSTOM OPTIONS")
        print("="*70)
        
        files = self.get_multiple_files()
        if not files:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
            return
        
        model = self.select_model()
        output_dir = self.get_output_dir()
        
        print("\n📋 Summary:")
        print("─" * 70)
        print(f"Files: {len(files)}")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {Path(f).name}")
        print(f"Model: {model}")
        print(f"Output: {output_dir}")
        
        confirm = input("\nProceed with transcription? (y/n): ").strip().lower()
        if confirm == 'y':
            self.run_transcription(files, model=model, output_dir=output_dir)
        else:
            print("\n❌ Cancelled.")
            input("\nPress Enter to return to menu...")
    
    def view_demo(self):
        """View the demo guide"""
        self.clear_screen()
        print("\n📚 Loading Interactive Demo Guide...\n")
        try:
            subprocess.run(['python3', self.demo_script])
        except Exception as e:
            print(f"❌ Error loading demo: {e}")
        input("\nPress Enter to return to menu...")
    
    def open_workflow_viz(self):
        """Open the workflow visualization"""
        self.clear_screen()
        print("\n🌐 Opening Visual Workflow...\n")
        
        html_file = Path("workflow_visualization.html")
        if html_file.exists():
            print(f"📊 Workflow visualization: {html_file.absolute()}")
            print("\nOpen this file in your web browser to see the interactive workflow.")
            print(f"\nFile location: {html_file.absolute()}")
        else:
            print("❌ Workflow visualization file not found.")
        
        input("\nPress Enter to return to menu...")
    
    def view_documentation(self):
        """View the full documentation"""
        self.clear_screen()
        print("\n📖 Loading Documentation...\n")
        
        readme_file = Path("AUDIO_INTELLIGENCE_README.md")
        if readme_file.exists():
            try:
                with open(readme_file, 'r') as f:
                    content = f.read()
                print(content)
            except Exception as e:
                print(f"❌ Error reading documentation: {e}")
        else:
            print("❌ Documentation file not found.")
        
        input("\nPress Enter to return to menu...")
    
    def check_requirements(self):
        """Check system requirements"""
        self.clear_screen()
        print("\n🔧 SYSTEM REQUIREMENTS CHECK")
        print("="*70)
        print()
        
        # Check Python
        print("Checking Python version...")
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            print(f"  ✅ {result.stdout.strip()}")
        except:
            print("  ❌ Python 3 not found")
        
        # Check for skill
        skill_path = Path("/mnt/skills/user/audio-transcription/scripts/transcribe.py")
        print("\nChecking audio-transcription skill...")
        if skill_path.exists():
            print(f"  ✅ Skill found at {skill_path.parent.parent}")
        else:
            print("  ❌ audio-transcription skill not found")
        
        # Check for dependencies
        print("\nChecking dependencies...")
        deps = ['openai-whisper', 'python-docx']
        for dep in deps:
            try:
                result = subprocess.run(['pip', 'show', dep], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"  ✅ {dep} installed")
                else:
                    print(f"  ⚠️  {dep} not installed")
            except:
                print(f"  ❌ Cannot check {dep}")
        
        print("\n" + "="*70)
        input("\nPress Enter to return to menu...")
    
    def view_recent_outputs(self):
        """View recent output directories"""
        self.clear_screen()
        print("\n📁 RECENT OUTPUTS")
        print("="*70)
        print()
        
        outputs_dir = Path("/mnt/user-data/outputs")
        if outputs_dir.exists():
            sessions = sorted(
                [d for d in outputs_dir.iterdir() if d.is_dir() and d.name.startswith('audio_session_')],
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )
            
            if sessions:
                print(f"Found {len(sessions)} session(s):\n")
                for i, session in enumerate(sessions[:10], 1):
                    files = list(session.glob('*'))
                    print(f"  {i}. {session.name}")
                    print(f"     📁 {session.absolute()}")
                    print(f"     📄 {len(files)} file(s)")
                    print()
            else:
                print("No session directories found yet.")
        else:
            print("Output directory does not exist yet.")
        
        print("="*70)
        input("\nPress Enter to return to menu...")
    
    def run(self):
        """Run the interactive launcher"""
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            choice = self.get_choice()
            
            if choice == '0':
                self.clear_screen()
                print("\n👋 Thank you for using Audio Intelligence Workstation!")
                print("🎙️  Happy transcribing! ✨\n")
                sys.exit(0)
            elif choice == '1':
                self.quick_start()
            elif choice == '2':
                self.batch_processing()
            elif choice == '3':
                self.custom_options()
            elif choice == '4':
                self.view_demo()
            elif choice == '5':
                self.open_workflow_viz()
            elif choice == '6':
                self.view_documentation()
            elif choice == '7':
                self.check_requirements()
            elif choice == '8':
                self.view_recent_outputs()


def main():
    launcher = InteractiveLauncher()
    try:
        launcher.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
