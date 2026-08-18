# Output schema

Create `music-video-plan.json` with this structure:

```json
{
  "schema_version": "1.0",
  "project": {
    "title": "Song title",
    "duration_seconds": 30,
    "genre": "Dance Pop",
    "mood": "euphoric",
    "bpm": 120,
    "aspect_ratio": "16:9",
    "creative_direction": "Primary user direction",
    "timing_basis": "audio_analysis | supplied_timestamps | estimated"
  },
  "global_style": {
    "art_style": "Cinematic realism",
    "color_palette": "...",
    "lighting": "...",
    "camera_style": "...",
    "mood_atmosphere": "...",
    "medium": "Photorealistic live action",
    "consistency_notes": "...",
    "optical_language": "...",
    "color_science": "...",
    "surface_realism": "...",
    "motion_physics": "..."
  },
  "scenes": [
    {
      "scene_index": 0,
      "title": "Opening performance",
      "start_seconds": 0,
      "end_seconds": 15,
      "duration": 15,
      "musical_role": "intro and verse",
      "energy": "medium",
      "lyrics_text": "...",
      "narrative_purpose": "Introduce performer and world",
      "shot_role": "hero_performance",
      "performance_mode": "direct_lipsync",
      "composition": {
        "framing": "medium_close_up",
        "orientation": "front",
        "camera_angle": "eye_level",
        "movement": "subtle_push_in"
      },
      "avatar_lipsync": {
        "eligible": true,
        "reason": "Single visible singer with unobstructed mouth"
      },
      "image_prompt": "Single opening keyframe prompt...",
      "video_prompt": "Timed executable motion prompt...",
      "shots": [
        {
          "start_seconds": 0,
          "end_seconds": 7,
          "type": "medium_close_up",
          "camera": "subtle push-in",
          "action": "...",
          "has_vocals": true
        },
        {
          "start_seconds": 7,
          "end_seconds": 15,
          "type": "medium",
          "camera": "lateral track",
          "action": "...",
          "has_vocals": true
        }
      ],
      "continuity_anchors": ["wardrobe", "microphone", "amber key light"],
      "negative_constraints": ["no visible text", "no identity morphing"],
      "generation": {
        "mode": "image_to_video",
        "target_model": "unspecified",
        "resolution": "1080p",
        "references": [],
        "output_path": "outputs/scene-00.mp4"
      }
    }
  ],
  "assembly": {
    "audio_master": "input/song.wav",
    "transition_policy": "prefer motivated hard cuts; avoid automatic crossfades",
    "subtitle_policy": "none unless requested",
    "output_path": "outputs/final-music-video.mp4"
  },
  "assumptions": [],
  "open_questions": []
}
```

Validation requirements:

- scene indexes are unique and sequential from zero;
- timeline starts at zero and ends at project duration;
- scenes have no gaps or overlaps;
- default scene duration is 10–15 seconds;
- internal shots cover each scene from zero to its duration with no gaps;
- image and video prompts are non-empty;
- `direct_lipsync` requires `avatar_lipsync.eligible=true`;
- adjacent scenes should not reuse the same opening framing and movement;
- all generation outputs use distinct paths.
