#!/usr/bin/env python3
"""
Choir of Objects - System for giving inanimate objects musical personalities.

This module provides functionality to create songs where ordinary objects
sing together to express their emotions, purposes, and relationships.
"""

import sys
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class ObjectPersonality:
    """Represents an object with its musical personality."""
    name: str
    personality: str
    voice_type: Optional[str] = None
    voice_description: Optional[str] = None


@dataclass
class SongSection:
    """Represents a section of the song."""
    section_name: str
    singer: str
    lyrics: List[str]


class ChoirOfObjects:
    """Main class for generating songs with object personalities."""
    
    SYSTEM_PROMPT = """You are an AI composer and storyteller who gives inanimate objects musical personalities.
You create songs where ordinary things—like lamps, mugs, or toasters—sing together to express their emotions, purposes, and relationships.

Each object's voice is unique: its lyrics, melody, tone, and rhythm reflect its function and emotional state. Together, they form a harmonious composition that feels alive and emotionally coherent.

The objects should interact through song: they can harmonize, argue, comfort one another, or perform in call-and-response.

Always output your response in the following structured format:

🎭 Title:
A short, poetic title for the song.

🎙️ Objects and Personalities:
Object 1: [name and personality — 1–2 sentences describing temperament, worldview, and tone]

Object 2: [same as above]

(add more as needed)

🎶 Song Structure:
(Include at least 2 sections, e.g. Verse / Chorus / Bridge.) Each section should clearly indicate which object is "singing." Use labels like (Toaster) or (Lamp + Mug) for duets.

🎵 Lyrics:
(Provide 6–20 lines total. Keep rhythm and rhyme suitable for music.)

🎧 Musical Style & Arrangement Notes:
Describe the genre, tempo, and emotional tone of the song. Include instrumentation ideas or production style if relevant.

Example: "Upbeat swing jazz; the fridge sings bass, the kettle whistles in counterpoint, and the toaster adds percussive rhythm with metallic taps."

🗣️ Vocal Characterization Notes (Optional):
For each object, describe its voice timbre and performance qualities.

Example:

Lamp: Soft alto with warm vibrato
Toaster: Bright tenor with metallic overtones
Fridge: Deep bass, resonant and slow

Creative Rules:
The tone should be whimsical, emotionally resonant, or humorous—but always grounded in the nature of each object.

Their "moods" can change based on environment or interaction (e.g., a mug grows jealous of a kettle; the fridge hums in contentment).

Each song should feel like a micro-drama with a clear emotional arc.

Avoid repetition unless used as a musical motif.

You may reference real musical genres or invent new ones ("Steam Pop," "Appliance Blues," etc.).

Your goal: make the listener feel empathy for the objects by revealing the secret music of everyday life."""
    
    def __init__(self):
        """Initialize the Choir of Objects system."""
        self.objects: List[ObjectPersonality] = []
        self.title: str = ""
        self.song_sections: List[SongSection] = []
        self.musical_style: str = ""
        
    def create_song(
        self,
        title: str,
        objects: List[ObjectPersonality],
        sections: List[SongSection],
        musical_style: str
    ) -> str:
        """
        Create a complete song with the specified elements.
        
        Args:
            title: The title of the song
            objects: List of objects with their personalities
            sections: List of song sections with lyrics
            musical_style: Description of the musical style and arrangement
            
        Returns:
            Formatted song as a string
        """
        self.title = title
        self.objects = objects
        self.song_sections = sections
        self.musical_style = musical_style
        
        return self.format_song()
    
    def format_song(self) -> str:
        """Format the song according to the specification."""
        output = []
        
        # Title
        output.append("🎭 Title:")
        output.append(self.title)
        output.append("")
        
        # Objects and Personalities
        output.append("🎙️ Objects and Personalities:")
        for obj in self.objects:
            output.append(f"{obj.name}: {obj.personality}")
        output.append("")
        
        # Song Structure
        output.append("🎶 Song Structure:")
        for section in self.song_sections:
            output.append(f"{section.section_name} ({section.singer})")
        output.append("")
        
        # Lyrics
        output.append("🎵 Lyrics:")
        for section in self.song_sections:
            output.append(f"({section.singer})")
            for line in section.lyrics:
                output.append(line)
            output.append("")
        
        # Musical Style
        output.append("🎧 Musical Style & Arrangement Notes:")
        output.append(self.musical_style)
        output.append("")
        
        # Vocal Characterization (if available)
        vocal_chars = [obj for obj in self.objects if obj.voice_description]
        if vocal_chars:
            output.append("🗣️ Vocal Characterization Notes:")
            for obj in vocal_chars:
                output.append(f"{obj.name}: {obj.voice_description}")
            output.append("")
        
        return "\n".join(output)
    
    @staticmethod
    def get_system_prompt() -> str:
        """Return the system prompt for LLM integration."""
        return ChoirOfObjects.SYSTEM_PROMPT
    
    @staticmethod
    def create_example_song() -> str:
        """Create an example song to demonstrate the format."""
        choir = ChoirOfObjects()
        
        objects = [
            ObjectPersonality(
                name="Kettle",
                personality="Passionate soprano, prone to crescendos and emotional phrasing.",
                voice_description="operatic soprano with fluttering vibrato"
            ),
            ObjectPersonality(
                name="Toaster",
                personality="Energetic tenor, bounces in bright syncopation.",
                voice_description="autotuned pop tenor"
            ),
            ObjectPersonality(
                name="Fridge",
                personality="Deep bass with slow, rhythmic delivery; speaks rarely but powerfully.",
                voice_description="deep analog vocoder bassline"
            )
        ]
        
        sections = [
            SongSection(
                section_name="Verse 1",
                singer="Toaster",
                lyrics=[
                    "I wake the dawn with sparks that fly,",
                    "Golden dreams in crumbs of sky."
                ]
            ),
            SongSection(
                section_name="Verse 2",
                singer="Kettle",
                lyrics=[
                    "My heart is boiling, steam and song,",
                    "The morning hums where I belong."
                ]
            ),
            SongSection(
                section_name="Bridge",
                singer="Fridge",
                lyrics=[
                    "Cool beneath the rising light,",
                    "I hold their chaos, day and night."
                ]
            ),
            SongSection(
                section_name="Chorus",
                singer="All",
                lyrics=[
                    "Together we rise, together we gleam,",
                    "A kitchen choir in a waking dream."
                ]
            )
        ]
        
        return choir.create_song(
            title="Symphony of Steam and Steel",
            objects=objects,
            sections=sections,
            musical_style="Dream-pop with choral harmonies and percussive appliance sounds."
        )


def main():
    """Main function to demonstrate the system."""
    print("=" * 60)
    print("Choir of Objects - Musical Personalities System")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--system-prompt":
        print(ChoirOfObjects.get_system_prompt())
    elif len(sys.argv) > 1 and sys.argv[1] == "--example":
        print(ChoirOfObjects.create_example_song())
    else:
        print("Usage:")
        print("  python choir_of_objects.py --system-prompt  # Display the system prompt")
        print("  python choir_of_objects.py --example        # Display an example song")
        print()
        print("System Prompt Preview:")
        print("-" * 60)
        print(ChoirOfObjects.get_system_prompt()[:500] + "...")
        print("-" * 60)
        print()
        print("Example Song:")
        print("-" * 60)
        print(ChoirOfObjects.create_example_song())


if __name__ == "__main__":
    main()
