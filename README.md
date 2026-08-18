# Music Video Prompt Director

An agent skill for turning a song, lyrics, creative direction, and visual references into a complete AI music-video production plan.

It packages the reusable prompt-engineering and directing workflow behind MusVideo into a provider-neutral format that can be used from Codex, Claude Code, WorkBuddy, or another skill-aware coding agent. It does not require a MusVideo account and does not call paid generation APIs unless the user explicitly asks an agent to generate media.

## What it creates

- Song analysis and a continuous 10–15 second scene structure
- A global visual and cinematic-realism contract
- Varied shot coverage across the complete music video
- Separate image-keyframe and video-motion prompts
- Selective lip-sync planning
- Provider-neutral model adaptation guidance
- A machine-readable `music-video-plan.json`
- A human-readable storyboard and shot list
- A validation workflow for catching timing and prompt-structure errors

## Install

The skill is located at:

```text
music-video-prompt-director/
```

### Codex

Copy or symlink the skill folder into your Codex skills directory:

```bash
cp -R music-video-prompt-director ~/.codex/skills/
```

Then invoke it explicitly:

```text
Use $music-video-prompt-director to turn this song into a cinematic music-video storyboard with image and video prompts.
```

### Claude Code

Copy the skill into a Claude skills location supported by your setup, or point Claude Code at `music-video-prompt-director/SKILL.md` and ask it to follow the workflow. The skill uses plain Markdown, JSON, and Python with no platform-specific runtime dependency.

### WorkBuddy and other agents

Import the `music-video-prompt-director` folder as a custom skill, or provide `SKILL.md` as the primary instruction file. Keep its `references/` and `scripts/` directories beside it so the agent can load the detailed directing guidance and run validation.

## Example requests

```text
Use $music-video-prompt-director to analyze song.wav and create a 16:9 cinematic music-video plan. Use singer.jpg as the performer reference and reserve lip sync for chorus close-ups.
```

```text
Use $music-video-prompt-director to rewrite this repetitive storyboard. Keep every generated section between 10 and 15 seconds, increase camera and shot-role variety, and make the image and video prompts feel more physically realistic.
```

```text
Use $music-video-prompt-director to adapt music-video-plan.json for my selected image and video models without generating or spending credits.
```

## Output validation

Validate the generated plan before sending prompts to image or video models:

```bash
python3 music-video-prompt-director/scripts/validate_plan.py music-video-plan.json
```

The validator checks the full timeline, scene and internal-shot timing, the default 10–15 second duration contract, prompt completeness, selective lip-sync eligibility, adjacent shot variety, and unique output paths.

## About MusVideo.ai

[MusVideo.ai](https://musvideo.ai/) is an AI music-video production platform designed to turn a complete song into a structured visual workflow. It helps creators analyze music, develop a storyboard, generate scene keyframes and video clips, apply lip sync where appropriate, regenerate individual weak scenes, and assemble the selected clips with the original track.

This repository exposes the creative planning ideas as an independent agent skill for creators who prefer to operate their own models, APIs, scripts, and editing pipeline. MusVideo.ai remains the integrated option for users who want those production stages managed in one web workflow.

## Design principles

- Plan the complete visual arc before writing individual prompts.
- Use 10–15 second generation sections by default.
- Create variation through shot purpose and coverage, not adjective changes.
- Keep opening keyframes separate from executable motion prompts.
- Describe optics, exposure, materials, and motion physics concretely.
- Preserve recurring identity without forcing the performer into every scene.
- Regenerate failed scenes instead of restarting successful work.
- Verify model capabilities before using reference video, audio, multi-shot, or lip-sync features.

## Repository layout

```text
music-video-prompt-director/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── model-adapters.md
│   ├── output-schema.md
│   ├── realism.md
│   └── workflow.md
└── scripts/
    └── validate_plan.py
```
