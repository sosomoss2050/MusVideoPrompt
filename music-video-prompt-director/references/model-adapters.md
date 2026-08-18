# Model adaptation

## Contents

1. Capability check
2. Text-to-video
3. Image-to-video
4. Reference-video generation
5. Lip sync and audio
6. Provider-neutral manifest

## 1. Capability check

Before adapting prompts, verify current official documentation for:

- maximum duration and resolution;
- accepted image, video, and audio references;
- first/last-frame support;
- multi-shot or timed-prompt support;
- native audio and lip sync;
- aspect-ratio and file constraints.

If capability is unknown, use a conservative one-shot image-to-video prompt and state the assumption.

## 2. Text-to-video

Include enough identity, setting, composition, and continuity detail because no opening image anchors the result. Keep the action simple and avoid too many recurring characters.

## 3. Image-to-video

Let the image carry appearance and opening composition. The motion prompt should focus on camera behavior, subject action, environmental response, timing, and continuity. Do not redescribe details that contradict the keyframe.

## 4. Reference-video generation

Use when transferring timing, choreography, camera movement, blocking, or editing structure from an existing video. State which properties should be preserved and which may change. Reference transfer reduces prompt engineering but does not guarantee identity fidelity.

Provider-neutral instruction pattern:

```text
Use Reference Video 1 for shot timing, choreography, camera movement, spatial blocking, cuts, and performance rhythm. Preserve the supplied character and style references where supported. Maintain natural anatomy, stable identity, and physically plausible motion. Do not add text, logos, or watermarks.
```

## 5. Lip sync and audio

If native audio or reference audio is supported, attach the exact section audio and provide the lyric time range. If not, generate a stable performance plate and apply lip sync as a separate step.

Do not combine direct lip sync with complex spins, profile-to-back rotations, face occlusion, dense crowds, or aggressive camera shake.

## 6. Provider-neutral manifest

For every section record:

- target model/provider;
- generation mode;
- duration, resolution, and ratio;
- image/video/audio reference paths or URLs;
- final prompt;
- expected start/end frame behavior;
- lip-sync mode;
- output path;
- attempt number and failure note.

Keep provider-specific request bodies out of the creative plan unless the user asks for executable API integration.
