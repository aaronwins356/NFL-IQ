#!/usr/bin/env python3
"""
Tests for the Choir of Objects system.
"""

from choir_of_objects import ChoirOfObjects, ObjectPersonality, SongSection


def test_create_simple_song():
    """Test creating a simple song."""
    choir = ChoirOfObjects()
    
    objects = [
        ObjectPersonality(
            name="Lamp",
            personality="Gentle and wise, speaks in soft tones."
        )
    ]
    
    sections = [
        SongSection(
            section_name="Verse",
            singer="Lamp",
            lyrics=["I shine for you", "Through darkest night"]
        )
    ]
    
    song = choir.create_song(
        title="Light in the Dark",
        objects=objects,
        sections=sections,
        musical_style="Ambient electronica"
    )
    
    # Verify key components are present
    assert "🎭 Title:" in song
    assert "Light in the Dark" in song
    assert "🎙️ Objects and Personalities:" in song
    assert "Lamp" in song
    assert "🎶 Song Structure:" in song
    assert "🎵 Lyrics:" in song
    assert "I shine for you" in song
    assert "🎧 Musical Style & Arrangement Notes:" in song
    assert "Ambient electronica" in song
    
    print("✓ test_create_simple_song passed")


def test_create_song_with_vocals():
    """Test creating a song with vocal characterizations."""
    choir = ChoirOfObjects()
    
    objects = [
        ObjectPersonality(
            name="Toaster",
            personality="Upbeat and energetic.",
            voice_description="Bright tenor with metallic overtones"
        )
    ]
    
    sections = [
        SongSection(
            section_name="Chorus",
            singer="Toaster",
            lyrics=["Pop! Pop! Here I go!"]
        )
    ]
    
    song = choir.create_song(
        title="Morning Toast",
        objects=objects,
        sections=sections,
        musical_style="Pop rock"
    )
    
    # Verify vocal characterization is included
    assert "🗣️ Vocal Characterization Notes:" in song
    assert "Bright tenor with metallic overtones" in song
    
    print("✓ test_create_song_with_vocals passed")


def test_system_prompt():
    """Test that system prompt is available."""
    prompt = ChoirOfObjects.get_system_prompt()
    
    assert len(prompt) > 0
    assert "inanimate objects" in prompt
    assert "musical personalities" in prompt
    assert "🎭 Title:" in prompt
    
    print("✓ test_system_prompt passed")


def test_example_song():
    """Test that example song generates correctly."""
    song = ChoirOfObjects.create_example_song()
    
    assert "Symphony of Steam and Steel" in song
    assert "Kettle" in song
    assert "Toaster" in song
    assert "Fridge" in song
    assert "Together we rise" in song
    
    print("✓ test_example_song passed")


def test_multiple_objects():
    """Test creating a song with multiple objects."""
    choir = ChoirOfObjects()
    
    objects = [
        ObjectPersonality(name="Lamp", personality="Wise and calm."),
        ObjectPersonality(name="Chair", personality="Sturdy and reliable."),
        ObjectPersonality(name="Book", personality="Thoughtful and verbose.")
    ]
    
    sections = [
        SongSection(
            section_name="Verse 1",
            singer="Lamp",
            lyrics=["I light the page"]
        ),
        SongSection(
            section_name="Verse 2",
            singer="Chair",
            lyrics=["I hold you steady"]
        ),
        SongSection(
            section_name="Verse 3",
            singer="Book",
            lyrics=["I tell the story"]
        ),
        SongSection(
            section_name="Chorus",
            singer="All",
            lyrics=["Together we create", "A perfect reading space"]
        )
    ]
    
    song = choir.create_song(
        title="The Reading Corner",
        objects=objects,
        sections=sections,
        musical_style="Soft acoustic"
    )
    
    assert "Lamp" in song
    assert "Chair" in song
    assert "Book" in song
    assert all(obj.name in song for obj in objects)
    
    print("✓ test_multiple_objects passed")


if __name__ == "__main__":
    print("Running Choir of Objects tests...")
    print()
    
    test_create_simple_song()
    test_create_song_with_vocals()
    test_system_prompt()
    test_example_song()
    test_multiple_objects()
    
    print()
    print("=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
