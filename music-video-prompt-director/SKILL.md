---
name: music-video-prompt-director
description: Turn a song, lyrics, audio analysis, creative brief, performer references, or visual references into a complete AI music-video production plan. Use when an agent needs to analyze a track, divide it into 10–15 second generation clips, design a varied storyboard, create consistent image-keyframe and video prompts, plan selective lip sync, adapt prompts for different image/video models, diagnose repetitive or artificial-looking shots, or prepare a regeneration and assembly workflow without relying on MusVideo.
---

# Music Video Prompt Director

Create production-ready music-video prompts from a song and references. Produce portable artifacts that can be used with any image generator, video generator, editor, or API.

## Operating rules

- Treat the user's creative direction as the highest-priority visual instruction.
- Preserve actual lyric timestamps and musical structure. Never invent timing when audio inspection or supplied timing is available.
- Plan each generated clip as a 10–15 second section by default. Let musical phrases determine boundaries; avoid tiny trailing sections.
- Allocate shot roles across the whole video before writing individual prompts. Do not let every vocal section become the same front-facing singer shot.
- Separate the opening keyframe prompt from the motion/video prompt.
- Use concrete optics, light, color response, surface texture, and motion physics. Do not rely on empty quality tags such as “cinematic, 8K, masterpiece.”
- Preserve identity, wardrobe, props, and location logic when they recur, but do not force the performer into every scene.
- Use lip sync selectively. Reserve direct lip sync for one visible singer, front or three-quarter facing, close or medium-close framing, with an unobstructed mouth.
- Never claim a model supports reference video, audio, multi-shot timing, first/last frames, or native lip sync without checking the model's current capabilities.
- Do not call paid generation APIs or spend credits unless the user asks to generate media.

## Workflow

### 1. Collect or infer the brief

Gather what is available: audio path/URL, duration, lyrics and timestamps, genre, BPM, mood, aspect ratio, performer references, visual references, target models, lip-sync preference, and user direction.

If essential input is missing, continue with explicit assumptions when they do not materially change the concept. Ask only when the missing choice would create a different production.

For audio-led analysis, inspect the audio with available transcription/audio tools. If only text is available, mark BPM, energy, and timing as estimates.

### 2. Analyze the song and segment it

Read [workflow.md](references/workflow.md) for segmentation and coverage logic.

Create contiguous sections covering the full song with no overlaps or gaps. Default to 10–15 seconds per generated clip. Align boundaries to phrase endings, section changes, breaks, drops, or strong energy shifts.

For each section record:

- start/end time and duration;
- musical role and energy;
- exact lyric excerpt or `instrumental`;
- narrative purpose and visual change from the preceding section.

### 3. Establish the global visual contract

Define one coherent visual world with:

- art direction and medium;
- palette and production design;
- lighting logic;
- optical language selected by shot purpose;
- filmic color science with protected highlights and readable shadows;
- believable skin, fabric, material wear, weather, and atmosphere;
- physically weighted camera and subject movement;
- recurrence rules for characters, wardrobe, props, and locations.

Use [realism.md](references/realism.md) when the user asks for cinematic or realistic results, or when existing generations look plastic or synthetic.

### 4. Allocate coverage across the full video

Assign every section one opening role before writing prompts. Rotate among:

- `hero_performance`
- `angled_performance`
- `moving_performance`
- `performance_wide`
- `reaction_closeup`
- `narrative_action`
- `detail_insert`
- `environment_cutaway`
- `symbolic_cutaway`

Ensure adjacent sections differ in subject scale, camera side, foreground/background relationship, movement, and visual action. Use the song's energy arc to decide where to reserve the strongest performance and camera moves.

### 5. Write the opening keyframe prompt

Describe one clean frame, never a storyboard or multi-panel image. Include:

1. subject and singular visible action;
2. environment and production design;
3. framing, orientation, camera angle, and lens behavior;
4. motivated lighting and exposure;
5. material, skin, fabric, weather, and atmospheric detail;
6. continuity anchors and exclusions.

Do not repeat a referenced performer's physical description when the target model receives that reference directly. Otherwise include a concise reusable identity block.

### 6. Write the executable video prompt

Check target-model capabilities and read [model-adapters.md](references/model-adapters.md).

For a multi-shot-capable request, describe 2–3 timed shots inside the 10–15 second clip. Give every shot exactly one framing, one camera behavior, one primary action, and one transition or continuity motivation. Anchor the first shot to the opening keyframe.

For a single-shot request, describe one continuous shot only. Never hide multiple cuts or incompatible camera moves inside prose.

End with only relevant constraints, such as stable identity, natural anatomy, physically plausible motion, no unrequested text, no UI, and no watermark.

### 7. Validate and deliver

Write `music-video-plan.json` using [output-schema.md](references/output-schema.md). Then run:

```bash
python3 scripts/validate_plan.py music-video-plan.json
```

Also provide `music-video-plan.md` as the human-readable shot list when the user wants a reviewable deliverable.

Report assumptions, model capability caveats, and which sections are best candidates for lip sync. Do not generate media unless requested.

## Revision workflow

When reviewing weak results, diagnose the failure at the smallest useful scope:

- identity drift → strengthen reference/continuity anchors;
- repetitive coverage → reallocate roles globally, not just rewrite adjectives;
- plastic look → replace generic quality tags with the realism contract;
- weightless motion → simplify camera behavior and specify inertia/parallax;
- poor lip sync → reserve a stable close performance shot and remove competing motion;
- incoherent multi-shot clip → reduce to two motivated shots or one continuous shot;
- weak musicality → move section boundaries or align motion/cuts to phrase changes;
- one bad clip → regenerate that section without rebuilding the entire project.

Preserve successful sections and maintain a short attempt log containing model, inputs, prompt version, failure, and chosen fix.

## Deliverable quality bar

- Cover the complete song timeline.
- Keep every default generation section within 10–15 seconds unless model constraints require otherwise.
- Make shot variety visible in structure, not merely in wording.
- Keep image and video prompts executable and free of contradictions.
- Distinguish direct lip sync from expressive performance and non-vocal action.
- Avoid unsupported model claims and hidden paid actions.
- Produce valid JSON that passes the bundled validator.
